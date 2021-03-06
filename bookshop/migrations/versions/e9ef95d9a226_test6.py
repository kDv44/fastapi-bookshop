"""test6

Revision ID: e9ef95d9a226
Revises: 7b5d63927046
Create Date: 2022-07-18 20:56:25.867462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e9ef95d9a226'
down_revision = '7b5d63927046'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.Column('number_pages', sa.Integer(), nullable=True),
    sa.Column('number_amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('is_adminer', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_index('ix_Users_id', table_name='Users')
    op.drop_table('Users')
    op.drop_index('ix_Books_id', table_name='Books')
    op.drop_table('Books')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Books',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('author', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('genre', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('number_pages', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('number_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Books_pkey')
    )
    op.create_index('ix_Books_id', 'Books', ['id'], unique=False)
    op.create_table('Users',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('is_adminer', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Users_pkey')
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###
