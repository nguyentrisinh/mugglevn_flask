"""empty message

Revision ID: edf68f8922f3
Revises: 22b7f02cbf27
Create Date: 2017-07-26 14:09:47.661660

"""

# revision identifiers, used by Alembic.
revision = 'edf68f8922f3'
down_revision = '22b7f02cbf27'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'title')
    # ### end Alembic commands ###
