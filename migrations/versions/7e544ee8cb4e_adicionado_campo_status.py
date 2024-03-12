"""adicionado campo status

Revision ID: 7e544ee8cb4e
Revises: 0e851ae96926
Create Date: 2024-03-12 04:50:04.954088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e544ee8cb4e'
down_revision = '0e851ae96926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('approved_card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))

    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.drop_column('status')

    with op.batch_alter_table('approved_card', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###