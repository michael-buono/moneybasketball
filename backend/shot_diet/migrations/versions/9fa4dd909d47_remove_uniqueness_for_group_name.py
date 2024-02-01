"""Remove uniqueness for group_name

Revision ID: 9fa4dd909d47
Revises: 77e14d478773
Create Date: 2023-07-05 16:20:05.608997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fa4dd909d47'
down_revision = '77e14d478773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lineup', schema=None) as batch_op:
        batch_op.drop_constraint('group_name_uniq', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lineup', schema=None) as batch_op:
        batch_op.create_unique_constraint('group_name_uniq', ['GROUP_NAME'])

    # ### end Alembic commands ###