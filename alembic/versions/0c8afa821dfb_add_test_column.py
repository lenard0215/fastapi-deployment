"""add test column

Revision ID: 0c8afa821dfb
Revises: 8919945854e6
Create Date: 2025-05-29 08:13:49.161707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c8afa821dfb'
down_revision: Union[str, None] = '8919945854e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('test', sa.String(50), nullable=False))
    pass

def downgrade():
    op.drop_column('users', 'test')
    pass
