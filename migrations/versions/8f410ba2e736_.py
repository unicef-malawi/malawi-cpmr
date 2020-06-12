"""empty message

Revision ID: 8f410ba2e736
Revises: 9a194a3e0f65
Create Date: 2020-02-20 10:13:20.081602

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8f410ba2e736'
down_revision = '9a194a3e0f65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('one_stop_centers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_one_stop_centers_name'), 'one_stop_centers', ['name'], unique=False)
    op.add_column('flow_data', sa.Column('one_stop_center', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'flow_data', 'one_stop_centers', ['one_stop_center'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'flow_data', type_='foreignkey')
    op.drop_column('flow_data', 'one_stop_center')
    op.drop_index(op.f('ix_one_stop_centers_name'), table_name='one_stop_centers')
    op.drop_table('one_stop_centers')
    # ### end Alembic commands ###
