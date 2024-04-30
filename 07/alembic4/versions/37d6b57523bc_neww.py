"""neww

Revision ID: 37d6b57523bc
Revises: c08c5d992a10
Create Date: 2024-04-30 13:49:34.028501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37d6b57523bc'
down_revision: Union[str, None] = 'c08c5d992a10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
