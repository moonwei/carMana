"""Add new columns to carmra model

Revision ID: 42b7b62d817a
Revises: 
Create Date: 2024-10-21 21:04:49.254399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b7b62d817a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('camera', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('ip_address', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('password', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('camera', schema=None) as batch_op:
        batch_op.drop_column('password')
        batch_op.drop_column('username')
        batch_op.drop_column('ip_address')
        batch_op.drop_column('location')

    # ### end Alembic commands ###