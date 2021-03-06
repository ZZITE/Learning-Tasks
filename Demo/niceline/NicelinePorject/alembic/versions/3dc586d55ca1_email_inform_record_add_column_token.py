"""email_inform_record add column token

Revision ID: 3dc586d55ca1
Revises: 40f8cc9bdfd8
Create Date: 2017-12-22 10:15:47.977528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dc586d55ca1'
down_revision = '40f8cc9bdfd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_inform_record', sa.Column('token', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email_inform_record', 'token')
    # ### end Alembic commands ###
