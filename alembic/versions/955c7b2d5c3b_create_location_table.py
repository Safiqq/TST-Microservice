"""create location table

Revision ID: 955c7b2d5c3b
Revises: 
Create Date: 2023-12-05 01:06:35.816799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '955c7b2d5c3b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'location',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('type', sa.Enum("farm", "market", "warehouse", name="type"), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('address', sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('location')
    op.execute("""DROP TYPE type""")
