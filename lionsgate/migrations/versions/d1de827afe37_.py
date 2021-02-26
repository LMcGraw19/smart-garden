"""empty message

Revision ID: d1de827afe37
Revises: e42be0195e6a
Create Date: 2020-01-17 03:02:40.348707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1de827afe37'
down_revision = 'e42be0195e6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_sensor_id'), 'data', ['sensor_id'], unique=False)
    op.create_index(op.f('ix_data_timestamp'), 'data', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_timestamp'), table_name='data')
    op.drop_index(op.f('ix_data_sensor_id'), table_name='data')
    op.drop_table('data')
    # ### end Alembic commands ###
