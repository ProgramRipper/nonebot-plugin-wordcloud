"""init_db

Revision ID: ee2869aa7c5a
Revises:
Create Date: 2023-01-18 20:35:39.707472

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "ee2869aa7c5a"
down_revision = None
branch_labels = None
depends_on = None


def _has_table(name: str) -> bool:
    from sqlalchemy import inspect

    insp = inspect(op.get_bind())
    return name in insp.get_table_names()


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if _has_table("wordcloud_schedule"):
        op.rename_table("wordcloud_schedule", "nonebot_plugin_wordcloud_schedule")
        with op.batch_alter_table(
            "nonebot_plugin_wordcloud_schedule", schema=None
        ) as batch_op:
            batch_op.create_unique_constraint("unique_schedule", ["bot_id", "group_id"])
    else:
        op.create_table(
            "nonebot_plugin_wordcloud_schedule",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("bot_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("group_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("time", sa.Time(), nullable=True),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("bot_id", "group_id", name="unique_schedule"),
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_wordcloud_schedule")
    # ### end Alembic commands ###
