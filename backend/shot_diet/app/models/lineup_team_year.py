from shot_diet.app import db


class LineupTeamYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lineup_id = db.Column(
        db.Integer, db.ForeignKey("lineup.GROUP_ID"), nullable=False, index=True
    )
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)
    season_year = db.Column(db.String(255), nullable=False)
    is_current_season = db.Column(db.Boolean, nullable=False, default=False)

    lineup = db.relationship("Lineup", backref="lineup_team_years", lazy=True)

    def __repr__(self):
        return f"<LineupTeamYear id={self.id} lineup_id={self.lineup_id} team_id={self.team_id} season_year={self.season_year} >"
