from shot_diet.app import db
import pandas as pd
from datetime import datetime

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # We use all caps to indicate a field that is named by the NBA's dataset,
    # lowercase for the fields we are generating ourselves.
    GAME_ID = db.Column(db.Integer, nullable=False)
    HTM = db.Column(db.String(100))
    VTM = db.Column(db.String(100))
    GAME_DATE = db.Column(db.String(100))

    game_datetime = db.Column(db.DateTime)
    shots = db.relationship('Shot', backref='game', lazy=True)  # Relationship to Shot model

    def convert_game_date_to_datetime(self):
        date_format = '%Y%m%d'
        self.game_datetime = datetime.strptime(self.GAME_DATE, date_format)
    
    def __repr__(self):
        return f"<Game id={self.id} GAME_ID={self.GAME_ID} HTM={self.HTM} VTM={self.VTM} GAME_DATE={self.game_datetime}>"