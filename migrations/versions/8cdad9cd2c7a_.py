"""empty message

Revision ID: 8cdad9cd2c7a
Revises: 35b7a3611f4a
Create Date: 2025-01-23 19:38:38.540249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cdad9cd2c7a'
down_revision: Union[str, None] = '35b7a3611f4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
