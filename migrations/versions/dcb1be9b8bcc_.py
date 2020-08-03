"""empty message

Revision ID: dcb1be9b8bcc
Revises: 
Create Date: 2020-08-02 14:59:29.227831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcb1be9b8bcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('filename', sa.String(length=100), nullable=True),
    sa.Column('hosting', sa.String(length=100), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('source', sa.String(length=100), nullable=True),
    sa.Column('last_served', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_record')
    # ### end Alembic commands ###
