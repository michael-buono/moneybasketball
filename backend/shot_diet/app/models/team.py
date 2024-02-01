from shot_diet.app import db
import pandas as pd

# 
# Sample team hash:
# {'id': 1610612737,
#   'full_name': 'Atlanta Hawks',
#   'abbreviation': 'ATL',
#   'nickname': 'Hawks',
#   'city': 'Atlanta',
#   'state': 'Georgia',
#   'year_founded': 1949
# }
#
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    abbreviation = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    city = db.Column(db.String(255))
    team_id = db.Column(db.Integer, nullable=False)

    player_shot_team_years = db.relationship('PlayerShotTeamYear', backref='team', lazy=True)

    def get_data_frames(self):
        # Convert the shot instance to a dictionary
        d = self.__dict__

        # Remove SQLAlchemy internal keys from the shot dictionary
        d.pop('_sa_instance_state', None)

        # Create a data frame from the shot dictionary
        df = pd.DataFrame.from_records([d])

        return df
    def __repr__(self):
        return f"<Team id={self.id} team_id={self.team_id} full_name={self.full_name}>"