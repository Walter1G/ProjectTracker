"""initial migration and create project db

Revision ID: 77a67ca2d704
Revises: 
Create Date: 2025-01-02 16:14:49.609397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77a67ca2d704'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('budget', sa.Float(), nullable=False),
    sa.Column('amount_paid', sa.Float(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('expected_due', sa.DateTime(), nullable=False),
    sa.Column('actual_due', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###