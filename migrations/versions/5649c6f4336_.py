"""empty message

Revision ID: 5649c6f4336
Revises: None
Create Date: 2015-03-01 22:40:43.592318

"""

# revision identifiers, used by Alembic.
revision = '5649c6f4336'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search')
    ### end Alembic commands ###