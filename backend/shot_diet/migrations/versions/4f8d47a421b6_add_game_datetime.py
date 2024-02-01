"""Add game_datetime

Revision ID: 4f8d47a421b6
Revises: ab5a81292fd7
Create Date: 2023-06-30 19:25:31.470678

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4f8d47a421b6"
down_revision = "ab5a81292fd7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("game", schema=None) as batch_op:
        batch_op.add_column(sa.Column("game_datetime", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("game", schema=None) as batch_op:
        batch_op.drop_column("game_datetime")

    # ### end Alembic commands ###
