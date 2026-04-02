"""add date when posted for reviews

Revision ID: 097e94eec41c
Revises: eab52c892899
Create Date: 2026-04-02 10:51:53.506372

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '097e94eec41c'
down_revision: Union[str, Sequence[str], None] = 'eab52c892899'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('reviews', sa.Column('posted', sa.Date(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('reviews', 'posted')
