"""Add cascade delete in table Authors

Revision ID: bf7a5ca12de4
Revises: 4aed03e8cdc0
Create Date: 2025-01-19 23:35:43.975750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf7a5ca12de4'
down_revision: Union[str, None] = '4aed03e8cdc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
