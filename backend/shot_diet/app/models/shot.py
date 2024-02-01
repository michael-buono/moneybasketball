import pandas as pd

from shot_diet.app import db


#
# Sample pandas.Series:
# ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME',
# 'TEAM_ID', 'TEAM_NAME', 'PERIOD', 'MINUTES_REMAINING',
# 'SECONDS_REMAINING', 'EVENT_TYPE', 'ACTION_TYPE', 'SHOT_TYPE',
# 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE',
# 'LOC_X', 'LOC_Y', 'SHOT_ATTEMPTED_FLAG', 'SHOT_MADE_FLAG', 'GAME_DATE',
# 'HTM', 'VTM']
#
class Shot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    GRID_TYPE = db.Column(db.String(100))
    GAME_ID = db.Column(db.Integer, db.ForeignKey("game.GAME_ID"))
    GAME_EVENT_ID = db.Column(db.Integer)
    PLAYER_ID = db.Column(
        db.Integer, db.ForeignKey("player.PLAYER_ID"), nullable=False, index=True
    )
    PLAYER_NAME = db.Column(db.String(100))
    TEAM_ID = db.Column(
        db.Integer, db.ForeignKey("team.team_id"), nullable=False, index=True
    )
    TEAM_NAME = db.Column(db.String(100))
    PERIOD = db.Column(db.Integer)
    MINUTES_REMAINING = db.Column(db.Integer)
    SECONDS_REMAINING = db.Column(db.Integer)
    EVENT_TYPE = db.Column(db.String(100))
    ACTION_TYPE = db.Column(db.String(100))
    SHOT_TYPE = db.Column(db.String(100))
    SHOT_ZONE_BASIC = db.Column(db.String(100))
    SHOT_ZONE_AREA = db.Column(db.String(100))
    SHOT_ZONE_RANGE = db.Column(db.String(100))
    SHOT_DISTANCE = db.Column(db.Integer)
    LOC_X = db.Column(db.Integer)
    LOC_Y = db.Column(db.Integer)
    SHOT_ATTEMPTED_FLAG = db.Column(db.Integer)
    SHOT_MADE_FLAG = db.Column(db.Integer)
    GAME_DATE = db.Column(db.String(100))
    HTM = db.Column(db.String(100))
    VTM = db.Column(db.String(100))
    GROUP_ID = db.Column(db.String(100), db.ForeignKey("lineup.GROUP_ID"), index=True)
    GROUP_NAME = db.Column(db.String(100))

    # Homemade
    season_year = db.Column(db.String(100), index=True)
    shot_value = db.Column(db.Integer)
    shot_result = db.Column(db.Integer)

    player_shot_team_year_id = db.Column(
        db.Integer, db.ForeignKey("player_shot_team_year.id")
    )

    lineup = db.relationship("Lineup", backref="shots", lazy=True)

    player_obj = db.relationship("Player", backref="shots", lazy=True)
    team = db.relationship("Team", backref="shots", lazy=True)
    player_shot_team_year = db.relationship(
        "PlayerShotTeamYear", backref="shots", lazy=True
    )

    def get_data_frames(self):
        # Convert the shot instance to a dictionary
        shot_dict = self.__dict__

        # Remove SQLAlchemy internal keys from the shot dictionary
        shot_dict.pop("_sa_instance_state", None)

        # Create a data frame from the shot dictionary
        df = pd.DataFrame.from_records([shot_dict])

        return df

    def game_date(self):
        return self.game.game_datetime

    def get_data(self):
        # Convert the shot instance to a dictionary
        shot_dict = self.__dict__.copy()

        # Remove SQLAlchemy internal keys from the shot dictionary
        shot_dict.pop("_sa_instance_state", None)
        return shot_dict

    @classmethod
    def combine_to_dataframe(cls, shots):
        if not shots:
            print("No shots to combine to dataframe, returning None")
            return None

        shot_data = [
            shot.get_data() for shot in shots
        ]  # Modify to return a dictionary of shot data
        combined_df = pd.DataFrame(shot_data)
        return combined_df

    @classmethod
    def expected_ts_df(cls, shots, season, team_id=None):
        df = Shot.combine_to_dataframe(shots)
        all_shots = pd.DataFrame()

        groupby_cols = [
            "PLAYER_ID",
            "ACTION_TYPE",
            "SHOT_TYPE",
            "shot_value",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_RANGE",
            "SHOT_ZONE_AREA",
        ]
        player_ids = df["PLAYER_ID"].unique()
        for player in player_ids:
            player_shot_data = df[df.PLAYER_ID == player]
            if team_id:
                season_player = player_shot_data[
                    player_shot_data["season_year"] == season
                ]
                season_player = season_player[season_player["TEAM_ID"] == team_id]
            else:
                season_player = player_shot_data[
                    player_shot_data["season_year"] == season
                ]

            past_shots = Shot.query.filter(
                Shot.PLAYER_ID == int(player), Shot.season_year < str(season)
            ).all()
            if not past_shots:
                continue

            # Now we know we have some shots
            training_data = Shot.combine_to_dataframe(past_shots)
            if training_data is None:
                return None

            all_at_once = (
                training_data.groupby(groupby_cols)["SHOT_MADE_FLAG"]
                .agg(["mean", "sum", "count"])
                .reset_index()
                .rename(
                    columns={
                        "mean": "EXPECTED_FG_PCT",
                        "sum": "TOTAL_FEATURE_MATCHES_MADE",
                        "count": "NUM_FEATURE_MATCHES",
                    }
                )
            )
            all_at_once["EXPECTED_TS"] = (
                all_at_once["EXPECTED_FG_PCT"] * all_at_once["shot_value"]
            )

            group_keys = groupby_cols

            # now we merge into the dataset for the one season
            merged_df = pd.merge(season_player, all_at_once, on=group_keys, how="left")
            all_shots = pd.concat([all_shots, merged_df])
        return all_shots

    def __repr__(self):
        return f"<Shot id={self.id} player_id={self.PLAYER_ID} player_name={self.PLAYER_NAME} game_date={self.GAME_DATE}>"
