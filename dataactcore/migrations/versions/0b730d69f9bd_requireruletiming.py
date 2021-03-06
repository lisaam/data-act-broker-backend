"""requireRuleTiming

Revision ID: 0b730d69f9bd
Revises: e4d26a4b740e
Create Date: 2016-03-24 14:25:20.913000

"""

# revision identifiers, used by Alembic.
revision = '0b730d69f9bd'
down_revision = 'e4d26a4b740e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rule', 'rule_timing_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rule', 'rule_timing_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###

def upgrade_error_data():
    pass

def downgrade_error_data():
    pass

def upgrade_job_tracker():
    pass

def downgrade_job_tracker():
    pass

def upgrade_user_manager():
    pass

def downgrade_user_manager():
    pass

def upgrade_staging():
    pass

def downgrade_staging():
    pass