"""create ducks table

Revision ID: 88414ffae138
Revises: 
Create Date: 2023-11-12 15:57:27.098793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88414ffae138'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ducks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('duck_name', sa.String(50), nullable=False),
        sa.Column('duck_type', sa.String(50), nullable=False),
        sa.Column('birthplace', sa.String(50), nullable=False),
        sa.Column('birthdate', sa.DateTime, nullable=False),
        sa.Column('gender', sa.String(6), nullable=False),
        sa.Column('health_status', sa.String(5), nullable=False),
        sa.Column('farm_id', sa.Integer, nullable=False),
    )
    # op.create_foreign_key(
    #     'fk_ducks_farm_id_farms',
    #     'ducks', 'farms',
    #     ['farm_id'], ['id'],
    # )


def downgrade() -> None:
    op.drop_table('ducks')
