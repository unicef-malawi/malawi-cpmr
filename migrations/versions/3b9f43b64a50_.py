"""empty message

Revision ID: 3b9f43b64a50
Revises: 83eb91938dbe
Create Date: 2019-07-24 21:06:20.815928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b9f43b64a50'
down_revision = '83eb91938dbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flow_data', sa.Column('year', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_flow_data_year'), 'flow_data', ['year'], unique=False)
    # op.drop_index('flow_data_idx1', table_name='flow_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('flow_data_idx1', 'flow_data', ['values'], unique=False)
    op.drop_index(op.f('ix_flow_data_year'), table_name='flow_data')
    op.drop_column('flow_data', 'year')
    # ### end Alembic commands ###