from shot_diet.app import db


class Lineup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    GROUP_ID = db.Column(db.String(100), nullable=False, unique=True, index=True)
    GROUP_NAME = db.Column(db.String(100), nullable=False, unique=False)

    players = db.relationship(
        "Player", secondary="lineup_player_association", back_populates="lineups"
    )
    lineup_player_association = db.Table(
        "lineup_player_association",
        db.Column("lineup_id", db.Integer, db.ForeignKey("lineup.id")),
        db.Column("player_id", db.Integer, db.ForeignKey("player.PLAYER_ID")),
    )

    def save(self):
        db.session.add(self)
        db.session.commit()
        self.setup_player_relationships()

    def setup_player_relationships(self):
        player_ids = [
            int(player_id)
            for player_id in self.GROUP_ID.split("-")[1:-1]
            if player_id != ""
        ]
        players = Player.query.filter(Player.PLAYER_ID.in_(player_ids)).all()
        self.players.extend(players)

    def __repr__(self):
        return f"<Lineup id={self.id} GROUP_ID={self.GROUP_ID} GROUP_NAME={self.GROUP_NAME}>"
