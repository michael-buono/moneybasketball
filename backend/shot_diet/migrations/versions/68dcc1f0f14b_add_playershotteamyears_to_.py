"""Add PlayerShotTeamYears to PlayerShotCareer

Revision ID: 68dcc1f0f14b
Revises: 06a89e457c6f
Create Date: 2023-06-27 00:36:46.528181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68dcc1f0f14b'
down_revision = '06a89e457c6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player_shot_team_year', schema=None) as batch_op:
        batch_op.add_column(sa.Column('player_shot_career_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key("oh wont you constraint with me", 'player_shot_career', ['player_shot_career_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player_shot_team_year', schema=None) as batch_op:
        batch_op.drop_constraint("oh wont you constraint with me", type_='foreignkey')
        batch_op.drop_column('player_shot_career_id')

    # ### end Alembic commands ###