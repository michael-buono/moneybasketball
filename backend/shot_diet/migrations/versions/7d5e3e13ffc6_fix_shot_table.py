"""Fix shot table

Revision ID: 7d5e3e13ffc6
Revises: d107a11af626
Create Date: 2023-06-30 11:11:59.191089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5e3e13ffc6'
down_revision = 'd107a11af626'
branch_labels = None
depends_on = None

tmp_table_name = "tmp_shot"


def upgrade():
    # Create the temporary table
    op.create_table(
        tmp_table_name,
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
        sa.Column("player_shot_team_year_id", sa.Integer(), nullable=True),
        sa.Column("season_year", sa.String(length=100), nullable=True),
        sa.Column("shot_value", sa.Integer(), nullable=True),
        sa.Column("shot_result", sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['TEAM_ID'], ['team.team_id'], name='fk_shot_team_id'),
        sa.ForeignKeyConstraint(['PLAYER_ID'], ['player.PLAYER_ID'], name='fk_shot_player_id'),
        sa.ForeignKeyConstraint(['player_shot_team_year_id'], ['player_shot_team_year.id'], name='fk_shot_player_shot_team_year_id'),
        sa.PrimaryKeyConstraint("id"),
    )

    # Copy data from the original shot table to the temporary table
    op.execute(f"INSERT INTO {tmp_table_name} SELECT * FROM shot")
    
    # Drop the original table
    op.drop_table('shot')

    # Rename the temporary table to the original table name
    op.rename_table(tmp_table_name, 'shot')

    
def downgrade():
    op.create_table(
        tmp_table_name,
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("GRID_TYPE", sa.String(length=100), nullable=True),
        sa.Column("GAME_ID", sa.Integer(), nullable=True),
        sa.Column("GAME_EVENT_ID", sa.Integer(), nullable=True),
        sa.Column("PLAYER_ID", sa.Integer(), nullable=True),
        sa.Column("PLAYER_NAME", sa.String(length=100), nullable=True),
        sa.Column("TEAM_ID", sa.Integer(), nullable=True),
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
        sa.Column("player_shot_team_year_id", sa.Integer(), nullable=True),
        sa.Column("season_year", sa.String(length=100), nullable=True),
        sa.Column("shot_value", sa.Integer(), nullable=True),
        sa.Column("shot_result", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    # Copy data from the original shot table to the temporary table
    op.execute(f"INSERT INTO {tmp_table_name} SELECT * FROM shot")
    # Drop the original table
    op.drop_table('shot')

    # Rename the temporary table to the original table name
    op.rename_table(tmp_table_name, 'shot')
