from datetime import datetime
from shot_diet.app import db

class PlayerShotCareer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.PLAYER_ID'), nullable=False)

    player_shot_team_years = db.relationship('PlayerShotTeamYear', backref='player_shot_career')

    def __repr__(self):
        return f"<PlayerShotCareer id={self.id} player_id={self.player_id}>"