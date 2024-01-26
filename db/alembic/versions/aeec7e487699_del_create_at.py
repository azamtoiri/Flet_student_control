"""del create at

Revision ID: aeec7e487699
Revises: a079652c4376
Create Date: 2024-01-26 22:04:18.911006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'aeec7e487699'
down_revision: Union[str, None] = 'a079652c4376'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enrollments', 'enrollment_date')
    op.drop_column('grades', 'grade_date')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('grades', sa.Column('grade_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('enrollments', sa.Column('enrollment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
