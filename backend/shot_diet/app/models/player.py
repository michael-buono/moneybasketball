import pandas as pd

from shot_diet.app import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PLAYER_ID = db.Column(db.Integer, nullable=False, index=True)
    TeamID = db.Column(db.String(255))
    SEASON = db.Column(db.String(255))
    LeagueID = db.Column(db.String(255))
    PLAYER = db.Column(db.String(255))
    NICKNAME = db.Column(db.String(255))
    PLAYER_SLUG = db.Column(db.String(255))
    NUM = db.Column(db.String(255))
    POSITION = db.Column(db.String(255))
    HEIGHT = db.Column(db.String(255))
    WEIGHT = db.Column(db.String(255))
    BIRTH_DATE = db.Column(db.String(255))
    AGE = db.Column(db.Integer)
    EXP = db.Column(db.Integer)
    SCHOOL = db.Column(db.String(255))
    HOW_ACQUIRED = db.Column(db.String(255))
    random_color = db.Column(db.String(255))

    player_shot_career = db.relationship(
        "PlayerShotCareer", backref="player_obj", uselist=False
    )
    lineups = db.relationship(
        "Lineup", secondary="lineup_player_association", back_populates="players"
    )

    def get_data_frames(self):
        # Convert the shot instance to a dictionary
        d = self.__dict__

        # Remove SQLAlchemy internal keys from the shot dictionary
        d.pop("_sa_instance_state", None)

        # Create a data frame from the shot dictionary
        df = pd.DataFrame.from_records([d])

        return df

    def __repr__(self):
        return f"<Player id={self.id} player_id={self.PLAYER_ID} PLAYER={self.PLAYER}>"
