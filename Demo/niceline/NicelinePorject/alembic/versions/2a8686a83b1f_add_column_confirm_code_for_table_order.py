"""add column 'confirm_code' for table 'order'

Revision ID: 2a8686a83b1f
Revises: 8f6790743d91
Create Date: 2017-12-27 20:10:16.175036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a8686a83b1f'
down_revision = '8f6790743d91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('confirm_code', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'confirm_code')
    # ### end Alembic commands ###