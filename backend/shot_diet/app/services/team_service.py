from nba_api.stats.static import teams
from shot_diet.app.models.team import Team
from shot_diet.database import db


def get_or_fetch_teams():
    # Check if we have 30 teams in the database
    if Team.query.count() < 30:
        # Fetch teams from the API
        fetch_teams()
    return [{"team_id": t.team_id, "full_name": t.full_name} for t in Team.query.all()]


def fetch_teams():
    for t in teams.get_teams():
        team = Team.query.filter_by(team_id=t["id"]).first()
        if team:
            team.team_id = t["id"]
            team.full_name = t["full_name"]
            team.abbreviation = t["abbreviation"]
            team.nickname = t["nickname"]
            team.city = t["city"]
            team.state = t["state"]
        else:
            team = Team(
                team_id=t["id"],
                full_name=t["full_name"],
                abbreviation=t["abbreviation"],
                nickname=t["nickname"],
                city=t["city"],
                state=t["state"],
            )
        db.session.add(team)
    db.session.commit()
