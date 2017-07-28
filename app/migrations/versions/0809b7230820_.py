"""empty message

Revision ID: 0809b7230820
Revises: c0ed9f294c20
Create Date: 2017-07-25 16:30:13.617850

"""

# revision identifiers, used by Alembic.
revision = '0809b7230820'
down_revision = 'c0ed9f294c20'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    # ### end Alembic commands ###
