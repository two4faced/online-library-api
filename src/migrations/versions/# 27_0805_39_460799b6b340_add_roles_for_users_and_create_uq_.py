"""add roles for users and create uq constraint for book and chapters numbers

Revision ID: 460799b6b340
Revises: 50a6816102c8
Create Date: 2026-03-27 08:05:39.332595

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '460799b6b340'
down_revision: Union[str, Sequence[str], None] = '50a6816102c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

user_roles = sa.Enum('READER', 'AUTHOR', 'ADMIN', name='userrole')


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        'uq_book_id_chapter_number', 'book_chapters', ['book_id', 'chapter_number']
    )
    user_roles.create(op.get_bind())
    op.add_column(
        'users',
        sa.Column(
            'role',
            sa.Enum('READER', 'AUTHOR', 'ADMIN', name='userrole'),
            nullable=False,
            server_default='READER',
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'role')
    op.drop_constraint('uq_book_id_chapter_number', 'book_chapters', type_='unique')
