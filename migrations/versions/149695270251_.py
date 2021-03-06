"""empty message

Revision ID: 149695270251
Revises: fb3114b70f3c
Create Date: 2016-08-06 14:41:12.450088

"""

# revision identifiers, used by Alembic.
revision = '149695270251'
down_revision = 'fb3114b70f3c'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('description_toggle', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'description_toggle')
    ### end Alembic commands ###
