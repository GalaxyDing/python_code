"""empty message

Revision ID: c1dc79843587
Revises: a20633bb361c
Create Date: 2019-12-19 22:43:14.601894

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c1dc79843587'
down_revision = 'a20633bb361c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('chinese', mysql.FLOAT(), nullable=True),
    sa.Column('math', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'student', ['name'], unique=True)
    # ### end Alembic commands ###
