"""add a content column

Revision ID: 0ba318ab7e60
Revises: 44e0ea0d4886
Create Date: 2022-02-17 12:22:36.708802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba318ab7e60'
down_revision = '44e0ea0d4886'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
