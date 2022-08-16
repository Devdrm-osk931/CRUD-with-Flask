"""empty message

Revision ID: db8b0e31c34c
Revises: cca5f5bb4ec5
Create Date: 2022-01-14 02:00:37.675759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db8b0e31c34c'
down_revision = 'cca5f5bb4ec5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###