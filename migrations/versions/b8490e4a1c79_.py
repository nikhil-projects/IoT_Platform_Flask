"""empty message

Revision ID: b8490e4a1c79
Revises: 9ae1efd2f20c
Create Date: 2019-07-19 19:10:10.285784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8490e4a1c79'
down_revision = '9ae1efd2f20c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_timestamp')
    # ### end Alembic commands ###
