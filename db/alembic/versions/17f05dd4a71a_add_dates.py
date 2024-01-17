"""add dates

Revision ID: 17f05dd4a71a
Revises: 7d38dae95adf
Create Date: 2024-01-17 15:44:19.743616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17f05dd4a71a'
down_revision: Union[str, None] = '7d38dae95adf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grades', 'description')
    # ### end Alembic commands ###