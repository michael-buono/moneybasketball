"""Add PlayerShotTeamYear

Revision ID: 86be55a040b0
Revises: 055da0e71af9
Create Date: 2023-06-25 22:40:44.489900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86be55a040b0'
down_revision = '37688678660a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('abbreviation', sa.String(length=255), nullable=True),
    sa.Column('nickname', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_shot_team_year',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('season_year', sa.Integer(), nullable=False),
    sa.Column('is_current_season', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_shot_career',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.PLAYER_ID'], name='fk_player_shot_career_player_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_shot_team_year')
    op.drop_table('player_shot_career')
    op.drop_table('team')
    # ### end Alembic commands ###