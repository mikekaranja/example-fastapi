"""add foreign-key to posts table

Revision ID: 79248e3c617c
Revises: 7209aa9e2088
Create Date: 2022-08-01 14:49:42.534832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79248e3c617c'
down_revision = '7209aa9e2088'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
