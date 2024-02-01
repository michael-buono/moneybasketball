"""Add LineupTeamYear

Revision ID: 77e14d478773
Revises: bf2f91b4a34d
Create Date: 2023-07-05 15:58:02.192757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77e14d478773'
down_revision = 'bf2f91b4a34d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lineup_team_year',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lineup_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('season_year', sa.String(length=255), nullable=False),
    sa.Column('is_current_season', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['lineup_id'], ['lineup.GROUP_ID'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.team_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lineup_team_year')
    # ### end Alembic commands ###