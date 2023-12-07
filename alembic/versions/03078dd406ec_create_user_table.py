"""create user table

Revision ID: 03078dd406ec
Revises: b8ff454dc972
Create Date: 2023-12-05 01:06:40.992806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03078dd406ec'
down_revision: Union[str, None] = 'b8ff454dc972'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(25), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('admin', sa.Boolean, server_default=sa.false(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')
