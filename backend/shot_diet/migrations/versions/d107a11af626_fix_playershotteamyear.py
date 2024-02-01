"""empty message

Revision ID: d107a11af626
Revises: 2e52bae88b49
Create Date: 2023-06-30 10:49:35.302274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd107a11af626'
down_revision = '2e52bae88b49'
branch_labels = None
depends_on = None

def upgrade():
    # Create a temporary table without the foreign key constraint
    op.create_table('player_shot_team_year_tmp',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('player_id', sa.Integer(), nullable=False),
        sa.Column('team_id', sa.Integer(), nullable=False),
        sa.Column('season_year', sa.String(length=255), nullable=False),
        sa.Column('is_current_season', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('player_shot_career_id', sa.Integer(), nullable=True),
        sa.Column('empty', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['team_id'], ['team.team_id'], name='fk_player_shot_team_year_team_id'),
        sa.ForeignKeyConstraint(['player_id'], ['player.PLAYER_ID'], name='fk_player_shot_team_year_player_id'),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the original table to the temporary table
    op.execute('INSERT INTO player_shot_team_year_tmp SELECT id, player_id, team_id, season_year, is_current_season, created_at, updated_at, player_shot_career_id, empty FROM player_shot_team_year')

    # Drop the original table
    op.drop_table('player_shot_team_year')

    # Rename the temporary table to the original table name
    op.rename_table('player_shot_team_year_tmp', 'player_shot_team_year')

def downgrade():
    # Create a temporary table with the foreign key constraint
    op.create_table('player_shot_team_year_tmp',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('player_id', sa.Integer(), nullable=False),
        sa.Column('team_id', sa.Integer(), nullable=False),
        sa.Column('season_year', sa.String(length=255), nullable=False),
        sa.Column('is_current_season', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('player_shot_career_id', sa.Integer(), nullable=True),
        sa.Column('empty', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the original table to the temporary table
    op.execute('INSERT INTO player_shot_team_year_tmp SELECT id, player_id, team_id, season_year, is_current_season, created_at, updated_at, player_shot_career_id, empty FROM player_shot_team_year')

    # Drop the original table
    op.drop_table('player_shot_team_year')

    # Rename the temporary table to the original table name
    op.rename_table('player_shot_team_year_tmp', 'player_shot_team_year')