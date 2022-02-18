"""add user columns

Revision ID: 1419931d73bc
Revises: f168dead9938
Create Date: 2022-02-17 12:59:24.432722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1419931d73bc'
down_revision = 'f168dead9938'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False
                                     , server_default="True"),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False
                                     , server_default=sa.text("now()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
