"""create book chapters table

Revision ID: 50a6816102c8
Revises: 3f285c802d15
Create Date: 2026-03-25 10:49:53.093952

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50a6816102c8'
down_revision: Union[str, Sequence[str], None] = '3f285c802d15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'book_chapters',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('chapter_number', sa.Integer(), nullable=False),
        sa.Column('chapter_name', sa.String(length=150), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ['book_id'],
            ['books.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('book_chapters')
