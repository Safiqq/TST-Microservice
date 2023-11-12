"""create farms table

Revision ID: 30454610cd24
Revises: 88414ffae138
Create Date: 2023-11-12 15:57:31.314397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30454610cd24'
down_revision: Union[str, None] = '88414ffae138'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'farms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('farm_name', sa.String(50), nullable=False),
        sa.Column('farm_location', sa.String(50), nullable=False),
        sa.Column('number_of_barns', sa.Integer, nullable=False),
        sa.Column('total_capacity', sa.Integer, nullable=False),
        sa.Column('owner_name', sa.String(50), nullable=False),
        sa.Column('phone_number', sa.String(16), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('farms')
