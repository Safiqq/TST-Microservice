"""create foreign key

Revision ID: 9736ea8801a6
Revises: f4e2fc5bd9ff
Create Date: 2023-11-13 22:01:46.708252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9736ea8801a6'
down_revision: Union[str, None] = 'f4e2fc5bd9ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        'fk_ducks_farm_id_farms',
        'ducks', 'farms',
        ['farm_id'], ['id'],
    )

def downgrade() -> None:
    op.drop_constraint('fk_ducks_farm_id_farms', 'ducks', type_='foreignkey')
