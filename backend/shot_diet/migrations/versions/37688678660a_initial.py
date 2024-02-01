"""initial

Revision ID: 37688678660a
Revises: 
Create Date: 2023-06-25 22:31:15.674443

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "37688678660a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "player",
        sa.Column("id", sa.Integer(), nullable=False),
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
        sa.Column("PLAYER_ID", sa.Integer(), nullable=True),
        sa.Column("HOW_ACQUIRED", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "shot",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("grid_type", sa.String(length=100), nullable=True),
        sa.Column("game_id", sa.Integer(), nullable=True),
        sa.Column("game_event_id", sa.Integer(), nullable=True),
        sa.Column("player_id", sa.Integer(), nullable=True),
        sa.Column("player_name", sa.String(length=100), nullable=True),
        sa.Column("team_id", sa.Integer(), nullable=True),
        sa.Column("team_name", sa.String(length=100), nullable=True),
        sa.Column("period", sa.Integer(), nullable=True),
        sa.Column("minutes_remaining", sa.Integer(), nullable=True),
        sa.Column("seconds_remaining", sa.Integer(), nullable=True),
        sa.Column("event_type", sa.String(length=100), nullable=True),
        sa.Column("action_type", sa.String(length=100), nullable=True),
        sa.Column("shot_type", sa.String(length=100), nullable=True),
        sa.Column("shot_zone_basic", sa.String(length=100), nullable=True),
        sa.Column("shot_zone_area", sa.String(length=100), nullable=True),
        sa.Column("shot_zone_range", sa.String(length=100), nullable=True),
        sa.Column("shot_distance", sa.Integer(), nullable=True),
        sa.Column("loc_x", sa.Integer(), nullable=True),
        sa.Column("loc_y", sa.Integer(), nullable=True),
        sa.Column("shot_attempted_flag", sa.Integer(), nullable=True),
        sa.Column("shot_made_flag", sa.Integer(), nullable=True),
        sa.Column("game_date", sa.String(length=100), nullable=True),
        sa.Column("htm", sa.String(length=100), nullable=True),
        sa.Column("vtm", sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["player.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shot")
    op.drop_table("player")
    # ### end Alembic commands ###
