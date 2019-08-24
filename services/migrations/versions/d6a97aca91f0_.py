"""empty message

Revision ID: d6a97aca91f0
Revises: 1492da312f6d
Create Date: 2019-08-23 23:14:45.444592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6a97aca91f0'
down_revision = '1492da312f6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estado_planificacion', sa.Column('nombre_estado2', sa.String(length=60), nullable=True))
    op.create_unique_constraint(None, 'estado_planificacion', ['nombre_estado2'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'estado_planificacion', type_='unique')
    op.drop_column('estado_planificacion', 'nombre_estado2')
    # ### end Alembic commands ###
