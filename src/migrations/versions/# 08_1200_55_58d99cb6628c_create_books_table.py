"""create books table

Revision ID: 58d99cb6628c
Revises: 06cdb5b8f4a4
Create Date: 2026-03-08 12:00:55.427475

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58d99cb6628c"
down_revision: Union[str, Sequence[str], None] = "06cdb5b8f4a4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=90), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("volume", sa.Integer(), nullable=False),
        sa.Column("rating", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("books")
