"""new

Revision ID: ff651795fd45
Revises: 6dd6cc43c064
Create Date: 2024-04-30 13:30:56.424726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff651795fd45'
down_revision: Union[str, None] = '6dd6cc43c064'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
