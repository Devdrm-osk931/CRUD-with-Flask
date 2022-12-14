"""empty message

Revision ID: 03ae5f6565ac
Revises: 4c8dbdea64b6
Create Date: 2022-01-14 01:17:57.428112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ae5f6565ac'
down_revision = '4c8dbdea64b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
    op.create_foreign_key(op.f('fk_message_user_id_user'), 'message', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    op.create_unique_constraint(op.f('uq_user_username'), 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_username'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    op.drop_constraint(op.f('fk_message_user_id_user'), 'message', type_='foreignkey')
    op.drop_column('message', 'user_id')
    # ### end Alembic commands ###
