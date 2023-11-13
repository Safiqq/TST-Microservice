"""create farms table

Revision ID: 30454610cd24
Revises: 88414ffae138
Create Date: 2023-11-12 15:57:31.314397

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision: str = '30454610cd24'
down_revision: Union[str, None] = '88414ffae138'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'farms',
        Column('id', Integer, primary_key=True),
        Column('farm_name', String(50), nullable=False),
        Column('farm_location', String(50), nullable=False),
        Column('number_of_barns', Integer, nullable=False),
        Column('total_capacity', Integer, nullable=False),
        Column('owner_name', String(50), nullable=False),
        Column('phone_number', String(16), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('farms')
