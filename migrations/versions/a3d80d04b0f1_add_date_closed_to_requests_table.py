"""Add date_closed to Requests table

Revision ID: a3d80d04b0f1
Revises: ebeb3491636e
Create Date: 2018-08-17 15:30:12.488761

"""

# revision identifiers, used by Alembic.
revision = 'a3d80d04b0f1'
down_revision = 'ebeb3491636e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('date_closed', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'date_closed')
    ### end Alembic commands ###