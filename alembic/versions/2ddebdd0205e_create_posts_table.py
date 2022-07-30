"""create posts table

Revision ID: 2ddebdd0205e
Revises: 
Create Date: 2022-07-30 12:35:08.816899

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2ddebdd0205e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
