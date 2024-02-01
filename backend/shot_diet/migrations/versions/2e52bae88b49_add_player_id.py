"""Add player_id

Revision ID: 2e52bae88b49
Revises: eb75375fa54d
Create Date: 2023-06-29 23:23:14.135088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e52bae88b49'
down_revision = 'eb75375fa54d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shot', schema=None) as batch_op:
        batch_op.alter_column('PLAYER_ID',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('shot_result',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=True)

    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('team_id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_column('team_id')

    with op.batch_alter_table('shot', schema=None) as batch_op:
        batch_op.alter_column('shot_result',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('PLAYER_ID',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_column('PLAYER_ID')

    # ### end Alembic commands ###
