"""add content column to posts table

Revision ID: d58ddcda12de
Revises: 2ddebdd0205e
Create Date: 2022-08-01 14:30:47.288341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd58ddcda12de'
down_revision = '2ddebdd0205e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
