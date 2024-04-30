"""new

Revision ID: c8881abe1bf8
Revises: ff651795fd45
Create Date: 2024-04-30 13:34:45.074678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8881abe1bf8'
down_revision: Union[str, None] = 'ff651795fd45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass