"""Make transaction code unique and alter date column type

Revision ID: ac017bebd0d9
Revises: 938272616394
Create Date: 2024-10-23

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ac017bebd0d9"
down_revision = "938272616394"
branch_labels = None
depends_on = None


def upgrade():
    # Añadir la columna 'code' a la tabla de transacciones
    op.add_column("transactions", sa.Column("code", sa.String(), nullable=False))

    # Crear constraint para que el código sea único
    op.create_unique_constraint("uq_transactions_code", "transactions", ["code"])

    # Alterar la columna 'date' y cambiar su tipo de VARCHAR a TIMESTAMP WITH TIME ZONE
    op.alter_column(
        "transactions",
        "date",
        type_=sa.TIMESTAMP(timezone=True),
        postgresql_using="date::timestamp with time zone",
    )


def downgrade():
    # Revertir cambios
    op.alter_column(
        "transactions", "date", type_=sa.String(), postgresql_using="date::varchar"
    )
    op.drop_constraint("uq_transactions_code", "transactions", type_="unique")
    op.drop_column("transactions", "code")
