"""empty message

Revision ID: 5024b3cfcf33
Revises: c3d38863a5f2
Create Date: 2018-08-06 22:35:50.758386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5024b3cfcf33'
down_revision = 'c3d38863a5f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('binding', sa.String(length=20), nullable=True),
    sa.Column('publisher', sa.String(length=50), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('pubdate', sa.String(length=20), nullable=True),
    sa.Column('isbn', sa.String(length=20), nullable=False),
    sa.Column('summary', sa.String(length=2000), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###