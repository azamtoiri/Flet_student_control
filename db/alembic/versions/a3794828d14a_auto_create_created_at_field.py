"""auto create 'created_at' field

Revision ID: a3794828d14a
Revises: 27b403a113ae
Create Date: 2024-01-17 21:35:28.009545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3794828d14a'
down_revision: Union[str, None] = '27b403a113ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=sa.DATE(),
               type_=sa.TIMESTAMP(timezone=True),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=sa.TIMESTAMP(timezone=True),
               type_=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###
