"""create users table

Revision ID: 838de3b2bc70
Revises: 
Create Date: 2025-02-27 08:18:05.328829

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '838de3b2bc70'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(): 
    op.create_table(
    'users', sa.Column('id', sa.Integer, primary_key=True, nullable=False),
     sa.Column('first_name',sa.String, nullable=False),
     sa.Column('last_name', sa.String, nullable=False),
     sa.Column('user_name', sa.String, nullable=False),
     sa.Column('email',sa.String, nullable=False, unique=True),
     sa.Column('password', sa.String, nullable=False),
    sa.Column('bio',sa.String, nullable=True),
    sa.Column('profile_picture', sa.String, nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    #sa.PrimaryKeyConstraint('id'),
    #sa.UniqueConstraint('email')
    pass

def downgrade():
    op.drop_table('users')
    pass
