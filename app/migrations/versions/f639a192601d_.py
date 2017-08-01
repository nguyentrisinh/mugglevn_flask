"""empty message

Revision ID: f639a192601d
Revises: 1a1b376257f2
Create Date: 2017-08-01 10:54:40.194979

"""

# revision identifiers, used by Alembic.
revision = 'f639a192601d'
down_revision = '1a1b376257f2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('test', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'test')
    # ### end Alembic commands ###
