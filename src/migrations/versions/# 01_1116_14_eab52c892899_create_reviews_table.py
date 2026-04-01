"""create reviews table

Revision ID: eab52c892899
Revises: 00f2f043a43c
Create Date: 2026-04-01 11:16:14.929423

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eab52c892899'
down_revision: Union[str, Sequence[str], None] = '00f2f043a43c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('author_id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.SMALLINT(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ['author_id'],
            ['users.id'],
        ),
        sa.ForeignKeyConstraint(
            ['book_id'],
            ['books.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('author_id', 'book_id', name='uq_author_book'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('reviews')
