"""test8

Revision ID: 0c0dfd9f42d0
Revises: 34409d9ce0c8
Create Date: 2022-07-20 13:30:36.822305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c0dfd9f42d0'
down_revision = '34409d9ce0c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hash_password', sa.String(length=1000), nullable=True))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('users', 'hash_password')
    # ### end Alembic commands ###