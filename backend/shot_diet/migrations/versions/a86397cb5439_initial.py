"""Initial

Revision ID: a86397cb5439
Revises: 
Create Date: 2024-02-08 18:13:59.690815

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a86397cb5439"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "game",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("GAME_ID", sa.Integer(), nullable=False),
        sa.Column("HTM", sa.String(length=100), nullable=True),
        sa.Column("VTM", sa.String(length=100), nullable=True),
        sa.Column("GAME_DATE", sa.String(length=100), nullable=True),
        sa.Column("game_datetime", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("game", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_game_GAME_ID"), ["GAME_ID"], unique=False)

    op.create_table(
        "lineup",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("GROUP_ID", sa.String(length=100), nullable=False),
        sa.Column("GROUP_NAME", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("lineup", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_lineup_GROUP_ID"), ["GROUP_ID"], unique=True
        )

    op.create_table(
        "player",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("PLAYER_ID", sa.Integer(), nullable=False),
        sa.Column("TeamID", sa.String(length=255), nullable=True),
        sa.Column("SEASON", sa.String(length=255), nullable=True),
        sa.Column("LeagueID", sa.String(length=255), nullable=True),
        sa.Column("PLAYER", sa.String(length=255), nullable=True),
        sa.Column("NICKNAME", sa.String(length=255), nullable=True),
        sa.Column("PLAYER_SLUG", sa.String(length=255), nullable=True),
        sa.Column("NUM", sa.String(length=255), nullable=True),
        sa.Column("POSITION", sa.String(length=255), nullable=True),
        sa.Column("HEIGHT", sa.String(length=255), nullable=True),
        sa.Column("WEIGHT", sa.String(length=255), nullable=True),
        sa.Column("BIRTH_DATE", sa.String(length=255), nullable=True),
        sa.Column("AGE", sa.Integer(), nullable=True),
        sa.Column("EXP", sa.Integer(), nullable=True),
        sa.Column("SCHOOL", sa.String(length=255), nullable=True),
        sa.Column("HOW_ACQUIRED", sa.String(length=255), nullable=True),
        sa.Column("random_color", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("player", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_player_PLAYER_ID"), ["PLAYER_ID"], unique=False
        )

    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=True),
        sa.Column("abbreviation", sa.String(length=255), nullable=True),
        sa.Column("nickname", sa.String(length=255), nullable=True),
        sa.Column("city", sa.String(length=255), nullable=True),
        sa.Column("state", sa.String(length=255), nullable=True),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("team", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_team_team_id"), ["team_id"], unique=False)

    op.create_table(
        "lineup_player_association",
        sa.Column("lineup_id", sa.Integer(), nullable=True),
        sa.Column("player_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["lineup_id"],
            ["lineup.id"],
        ),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["player.PLAYER_ID"],
        ),
    )
    op.create_table(
        "lineup_team_year",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("lineup_id", sa.String(length=255), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("season_year", sa.String(length=255), nullable=False),
        sa.Column("is_current_season", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lineup_id"],
            ["lineup.GROUP_ID"],
        ),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["team.team_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("lineup_team_year", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_lineup_team_year_lineup_id"), ["lineup_id"], unique=False
        )

    op.create_table(
        "player_shot_career",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["player.PLAYER_ID"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "player_shot_team_year",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("season_year", sa.String(length=255), nullable=False),
        sa.Column("is_current_season", sa.Boolean(), nullable=False),
        sa.Column("player_shot_career_id", sa.Integer(), nullable=True),
        sa.Column("empty", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["player.PLAYER_ID"],
        ),
        sa.ForeignKeyConstraint(
            ["player_shot_career_id"],
            ["player_shot_career.id"],
        ),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["team.team_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "shot",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("GRID_TYPE", sa.String(length=100), nullable=True),
        sa.Column("GAME_ID", sa.Integer(), nullable=True),
        sa.Column("GAME_EVENT_ID", sa.Integer(), nullable=True),
        sa.Column("PLAYER_ID", sa.Integer(), nullable=False),
        sa.Column("PLAYER_NAME", sa.String(length=100), nullable=True),
        sa.Column("TEAM_ID", sa.Integer(), nullable=False),
        sa.Column("TEAM_NAME", sa.String(length=100), nullable=True),
        sa.Column("PERIOD", sa.Integer(), nullable=True),
        sa.Column("MINUTES_REMAINING", sa.Integer(), nullable=True),
        sa.Column("SECONDS_REMAINING", sa.Integer(), nullable=True),
        sa.Column("EVENT_TYPE", sa.String(length=100), nullable=True),
        sa.Column("ACTION_TYPE", sa.String(length=100), nullable=True),
        sa.Column("SHOT_TYPE", sa.String(length=100), nullable=True),
        sa.Column("SHOT_ZONE_BASIC", sa.String(length=100), nullable=True),
        sa.Column("SHOT_ZONE_AREA", sa.String(length=100), nullable=True),
        sa.Column("SHOT_ZONE_RANGE", sa.String(length=100), nullable=True),
        sa.Column("SHOT_DISTANCE", sa.Integer(), nullable=True),
        sa.Column("LOC_X", sa.Integer(), nullable=True),
        sa.Column("LOC_Y", sa.Integer(), nullable=True),
        sa.Column("SHOT_ATTEMPTED_FLAG", sa.Integer(), nullable=True),
        sa.Column("SHOT_MADE_FLAG", sa.Integer(), nullable=True),
        sa.Column("GAME_DATE", sa.String(length=100), nullable=True),
        sa.Column("HTM", sa.String(length=100), nullable=True),
        sa.Column("VTM", sa.String(length=100), nullable=True),
        sa.Column("GROUP_ID", sa.String(length=100), nullable=True),
        sa.Column("GROUP_NAME", sa.String(length=100), nullable=True),
        sa.Column("season_year", sa.String(length=100), nullable=True),
        sa.Column("shot_value", sa.Integer(), nullable=True),
        sa.Column("shot_result", sa.Integer(), nullable=True),
        sa.Column("player_shot_team_year_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["GAME_ID"],
            ["game.GAME_ID"],
        ),
        sa.ForeignKeyConstraint(
            ["GROUP_ID"],
            ["lineup.GROUP_ID"],
        ),
        sa.ForeignKeyConstraint(
            ["PLAYER_ID"],
            ["player.PLAYER_ID"],
        ),
        sa.ForeignKeyConstraint(
            ["TEAM_ID"],
            ["team.team_id"],
        ),
        sa.ForeignKeyConstraint(
            ["player_shot_team_year_id"],
            ["player_shot_team_year.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("shot", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_shot_GROUP_ID"), ["GROUP_ID"], unique=False
        )
        batch_op.create_index(
            batch_op.f("ix_shot_PLAYER_ID"), ["PLAYER_ID"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_shot_TEAM_ID"), ["TEAM_ID"], unique=False)
        batch_op.create_index(
            batch_op.f("ix_shot_season_year"), ["season_year"], unique=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("shot", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_shot_season_year"))
        batch_op.drop_index(batch_op.f("ix_shot_TEAM_ID"))
        batch_op.drop_index(batch_op.f("ix_shot_PLAYER_ID"))
        batch_op.drop_index(batch_op.f("ix_shot_GROUP_ID"))

    op.drop_table("shot")
    op.drop_table("player_shot_team_year")
    op.drop_table("player_shot_career")
    with op.batch_alter_table("lineup_team_year", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_lineup_team_year_lineup_id"))

    op.drop_table("lineup_team_year")
    op.drop_table("lineup_player_association")
    with op.batch_alter_table("team", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_team_team_id"))

    op.drop_table("team")
    with op.batch_alter_table("player", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_player_PLAYER_ID"))

    op.drop_table("player")
    with op.batch_alter_table("lineup", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_lineup_GROUP_ID"))

    op.drop_table("lineup")
    with op.batch_alter_table("game", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_game_GAME_ID"))

    op.drop_table("game")
    # ### end Alembic commands ###
