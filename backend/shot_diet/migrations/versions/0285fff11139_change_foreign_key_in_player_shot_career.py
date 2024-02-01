"""Change foreign key in player_shot_career

Revision ID: 0285fff11139
Revises: 4d4c745190b7
Create Date: 2023-06-30 11:48:33.696724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0285fff11139'
down_revision = '4d4c745190b7'
branch_labels = None
depends_on = None

tmp_table_name = "tmp_player_shot_career"

def upgrade():
    # Create a temporary table without the foreign key constraint
    op.create_table(tmp_table_name,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('player_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['player_id'], ['player.PLAYER_ID'], name='fk_player_shot_career_player_id'),
        sa.PrimaryKeyConstraint('id')
    )

     # Copy data from the original shot table to the temporary table
    op.execute(f"INSERT INTO {tmp_table_name} SELECT * FROM player_shot_career")
    
    # Drop the original table
    op.drop_table('player_shot_career')

    # Rename the temporary table to the original table name
    op.rename_table(tmp_table_name, 'player_shot_career')

def downgrade():
    # Create a temporary table without the foreign key constraint
    op.create_table(tmp_table_name,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('player_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

     # Copy data from the original shot table to the temporary table
    op.execute(f"INSERT INTO {tmp_table_name} SELECT * FROM player_shot_career")
    
    # Drop the original table
    op.drop_table('player_shot_career')

    # Rename the temporary table to the original table name
    op.rename_table(tmp_table_name, 'player_shot_career')