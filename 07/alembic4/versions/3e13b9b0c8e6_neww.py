"""neww

Revision ID: 3e13b9b0c8e6
Revises: c8881abe1bf8
Create Date: 2024-04-30 13:39:48.601218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e13b9b0c8e6'
down_revision: Union[str, None] = 'c8881abe1bf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
