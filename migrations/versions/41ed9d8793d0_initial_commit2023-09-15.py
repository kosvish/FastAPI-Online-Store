"""initial commit

Revision ID: 41ed9d8793d0
Revises: 
Create Date: 2023-09-15 13:47:03.365744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '41ed9d8793d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('category', sa.String(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('brand', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('order',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('status', sa.String(), nullable=False),
                    sa.Column('total_price', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('product')
    op.drop_table('user')
    # ### end Alembic commands ###
