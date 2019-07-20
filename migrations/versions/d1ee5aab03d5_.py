"""empty message

Revision ID: d1ee5aab03d5
Revises: cafd6ca3db04
Create Date: 2019-07-19 20:19:18.565333

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd1ee5aab03d5'
down_revision = 'cafd6ca3db04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boards', sa.Column('name', sa.String(length=48), nullable=True))
    op.create_index(op.f('ix_boards_name'), 'boards', ['name'], unique=False)
    op.drop_index('ix_boards_type_', table_name='boards')
    op.drop_column('boards', 'type_')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boards', sa.Column('type_', mysql.VARCHAR(length=48), nullable=True))
    op.create_index('ix_boards_type_', 'boards', ['type_'], unique=False)
    op.drop_index(op.f('ix_boards_name'), table_name='boards')
    op.drop_column('boards', 'name')
    # ### end Alembic commands ###