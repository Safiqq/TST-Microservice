"""create users table

Revision ID: f4e2fc5bd9ff
Revises: 30454610cd24
Create Date: 2023-11-12 15:57:40.057361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4e2fc5bd9ff'
down_revision: Union[str, None] = '30454610cd24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), unique=True, nullable=False),
        sa.Column('username', sa.String(25), unique=True, nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
