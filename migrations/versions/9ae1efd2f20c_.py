"""empty message

Revision ID: 9ae1efd2f20c
Revises: dd8a3ce6410d
Create Date: 2019-07-19 18:46:00.552569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ae1efd2f20c'
down_revision = 'dd8a3ce6410d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', mysql.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###
