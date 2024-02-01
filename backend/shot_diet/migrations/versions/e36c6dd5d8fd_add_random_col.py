"""Add random col

Revision ID: e36c6dd5d8fd
Revises: 86be55a040b0
Create Date: 2023-06-25 22:51:08.999829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36c6dd5d8fd'
down_revision = '86be55a040b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('random_color', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_column('random_color')

    # ### end Alembic commands ###