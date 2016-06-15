"""empty message

Revision ID: ffb21f7a6e61
Revises: 7a110ca7061b
Create Date: 2016-06-15 09:12:17.437332

"""

# revision identifiers, used by Alembic.
revision = 'ffb21f7a6e61'
down_revision = '7a110ca7061b'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('format')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('format',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('label_en', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'format_pkey')
    )
    ### end Alembic commands ###
