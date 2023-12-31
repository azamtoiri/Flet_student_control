"""initain revision

Revision ID: 7f77b79e761b
Revises: 
Create Date: 2023-12-27 10:03:41.007270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f77b79e761b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('middle_name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('course', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grades',
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('grade_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('user_roles')
    op.drop_table('subjects')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
