#
# Ignore the imported but not used errors from eslint,
# as we want to be able to test these models via `flask shell`
#
from shot_diet.app import db  # noqa: F401
from .game import Game  # noqa: F401
from .lineup import Lineup  # noqa: F401
from .lineup_team_year import LineupTeamYear  # noqa: F401
from .player import Player  # noqa: F401
from .player_shot_career import PlayerShotCareer  # noqa: F401
from .player_shot_team_year import PlayerShotTeamYear  # noqa: F401
from .shot import Shot  # noqa: F401
from .team import Team  # noqa: F401
