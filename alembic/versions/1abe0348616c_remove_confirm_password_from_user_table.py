"""remove confirm_password from user table

Revision ID: 1abe0348616c
Revises: ab296f56cdbf
Create Date: 2026-07-19 00:12:05.853616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1abe0348616c'
down_revision: Union[str, Sequence[str], None] = 'ab296f56cdbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('users', 'confirm_password')

def downgrade():
    op.add_column('users', sa.Column('confirm_password', sa.String(), nullable=False))