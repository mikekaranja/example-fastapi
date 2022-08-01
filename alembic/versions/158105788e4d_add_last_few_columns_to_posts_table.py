"""add last few columns to posts table

Revision ID: 158105788e4d
Revises: 79248e3c617c
Create Date: 2022-08-01 15:12:46.268945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158105788e4d'
down_revision = '79248e3c617c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
