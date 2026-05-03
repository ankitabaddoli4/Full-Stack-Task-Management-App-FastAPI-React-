"""create users table

Revision ID: 1a2b3c
Revises: 
Create Date: 2026-05-03
"""

from alembic import op
import sqlalchemy as sa

revision = "1a2b3c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(100), unique=True, nullable=False),
        sa.Column("password", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("users")
