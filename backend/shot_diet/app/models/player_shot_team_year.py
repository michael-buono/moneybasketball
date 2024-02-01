from datetime import datetime
from shot_diet.app import db

class PlayerShotTeamYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.PLAYER_ID'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    season_year = db.Column(db.String(255), nullable=False)
    is_current_season = db.Column(db.Boolean, nullable=False, default=False)
    player_shot_career_id = db.Column(db.Integer, db.ForeignKey('player_shot_career.id'))
    empty = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    player_obj = db.relationship('Player', backref='player_shot_team_years', lazy=True)

    def __repr__(self):
        return f"<PlayerShotTeamYear id={self.id} player_id={self.player_id} team_id={self.team_id} season_year={self.season_year} >"