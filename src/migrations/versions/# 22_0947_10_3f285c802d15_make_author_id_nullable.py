"""make author_id nullable

Revision ID: 3f285c802d15
Revises: 58d99cb6628c
Create Date: 2026-03-22 09:47:10.097922

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f285c802d15'
down_revision: Union[str, Sequence[str], None] = '58d99cb6628c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('books', 'author_id', existing_type=sa.INTEGER(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('books', 'author_id', existing_type=sa.INTEGER(), nullable=False)
