"""second

Revision ID: 09c43bcca39e
Revises: b5a03710416a
Create Date: 2023-06-11 00:47:07.799239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c43bcca39e'
down_revision = 'b5a03710416a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('students_amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groups', 'students_amount')
    # ### end Alembic commands ###
