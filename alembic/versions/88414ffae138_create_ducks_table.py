"""create ducks table

Revision ID: 88414ffae138
Revises: 
Create Date: 2023-11-12 15:57:27.098793

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, DateTime


# revision identifiers, used by Alembic.
revision: str = '88414ffae138'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ducks',
        Column('id', Integer, primary_key=True),
        Column('duck_name', String(50), nullable=False),
        Column('duck_type', String(50), nullable=False),
        Column('birthplace', String(50), nullable=False),
        Column('birthdate', DateTime, nullable=False),
        Column('gender', String(6), nullable=False),
        Column('health_status', String(5), nullable=False),
        Column('farm_id', Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('ducks')
