"""add user table

Revision ID: 7209aa9e2088
Revises: d58ddcda12de
Create Date: 2022-08-01 14:43:03.215077

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7209aa9e2088'
down_revision = 'd58ddcda12de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
