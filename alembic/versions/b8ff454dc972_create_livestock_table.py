"""create livestock table

Revision ID: b8ff454dc972
Revises: 955c7b2d5c3b
Create Date: 2023-12-05 01:06:37.260825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8ff454dc972'
down_revision: Union[str, None] = '955c7b2d5c3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'livestock',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('breed', sa.String(50), nullable=False),
        sa.Column('species', sa.String(50), nullable=False),
        sa.Column('birthplace_id', sa.Integer, sa.ForeignKey('location.id'), nullable=False),
        sa.Column('birthdate', sa.DateTime, nullable=False),
        sa.Column('gender', sa.Enum("male", "female", name="gender"), nullable=False),
        sa.Column('location_id', sa.Integer, sa.ForeignKey('location.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('livestock')
    op.execute("""DROP TYPE gender""")