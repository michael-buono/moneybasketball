"""Add indexes

Revision ID: c00a6c1668a9
Revises: 2e52b67b663c
Create Date: 2023-07-05 22:56:36.654415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c00a6c1668a9'
down_revision = '2e52b67b663c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_PLAYER_ID'), ['PLAYER_ID'], unique=False)

    with op.batch_alter_table('shot', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_shot_GROUP_ID'), ['GROUP_ID'], unique=False)
        batch_op.create_index(batch_op.f('ix_shot_PLAYER_ID'), ['PLAYER_ID'], unique=False)
        batch_op.create_index(batch_op.f('ix_shot_TEAM_ID'), ['TEAM_ID'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shot', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_shot_TEAM_ID'))
        batch_op.drop_index(batch_op.f('ix_shot_PLAYER_ID'))
        batch_op.drop_index(batch_op.f('ix_shot_GROUP_ID'))

    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_PLAYER_ID'))

    # ### end Alembic commands ###
