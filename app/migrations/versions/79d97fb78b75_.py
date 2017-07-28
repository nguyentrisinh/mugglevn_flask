"""empty message

Revision ID: 79d97fb78b75
Revises: 3a8874111523
Create Date: 2017-07-26 10:39:01.824867

"""

# revision identifiers, used by Alembic.
revision = '79d97fb78b75'
down_revision = '3a8874111523'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('companies', 'overview')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('overview', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
