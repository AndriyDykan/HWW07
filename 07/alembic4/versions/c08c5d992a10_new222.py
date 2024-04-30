"""new222

Revision ID: c08c5d992a10
Revises: 3e13b9b0c8e6
Create Date: 2024-04-30 13:48:14.132608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c08c5d992a10'
down_revision: Union[str, None] = '3e13b9b0c8e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
