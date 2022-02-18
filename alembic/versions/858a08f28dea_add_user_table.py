"""add user table

Revision ID: 858a08f28dea
Revises: 0ba318ab7e60
Create Date: 2022-02-17 12:31:00.413087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '858a08f28dea'
down_revision = '0ba318ab7e60'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users"
                    , sa.Column("id", sa.Integer(), nullable=False)
                    , sa.Column("email", sa.String(), nullable=False)
                    , sa.Column("password", sa.String(), nullable=False)
                    , sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False)
                    , sa.PrimaryKeyConstraint("id")
                    , sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
