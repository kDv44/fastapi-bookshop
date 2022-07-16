"""test2

Revision ID: c4d026292bda
Revises: 7bd6b8be5d2e
Create Date: 2022-07-16 16:48:05.454388

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c4d026292bda'
down_revision = '7bd6b8be5d2e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Books',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('book_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.Column('number_pages', sa.Integer(), nullable=True),
    sa.Column('number_amount', sa.Integer(), nullable=True),
    sa.Column('is_sale', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Books_id'), 'Books', ['id'], unique=False)
    op.create_table('Users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('is_adminer', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Users_id'), table_name='Users')
    op.drop_table('Users')
    op.drop_index(op.f('ix_Books_id'), table_name='Books')
    op.drop_table('Books')
    # ### end Alembic commands ###