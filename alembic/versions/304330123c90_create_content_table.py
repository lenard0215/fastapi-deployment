"""create content table

Revision ID: 304330123c90
Revises: 838de3b2bc70
Create Date: 2025-03-17 10:39:48.224107

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import JSON
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '304330123c90'
down_revision: Union[str, None] = '838de3b2bc70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('contents',
    sa.Column('content_id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('content_username', sa.String(50), nullable=True),
    sa.Column('content_user_picture', sa.String(50), nullable= True),
    sa.Column('media_type', sa.String(50), nullable=False),
    sa.Column('content_description', sa.String(250), nullable= True),
    sa.Column('image_title', sa.String(50), nullable=False),
    sa.Column('video_title', sa.String(50), nullable=False),
    sa.Column('video_url', sa.String(100), nullable=True),
    sa.Column('image_url', sa.String(100), nullable=True),    
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.Column('images', sa.ARRAY(sa.JSON), nullable=True),
    sa.Column('videos', sa.ARRAY(sa.JSON), nullable=True),
    sa.Column('slider_images', sa.ARRAY(sa.JSON), nullable=True),
    sa.Column('slider2_images', sa.ARRAY(sa.JSON), nullable=True),
    sa.Column('slider2_videos', sa.ARRAY(sa.JSON), nullable=True)),
    pass


def downgrade():
    op.drop_table('contents')
    pass
