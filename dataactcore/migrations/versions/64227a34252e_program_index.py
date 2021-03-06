"""program_index

Revision ID: 64227a34252e
Revises: c1728858aaff
Create Date: 2016-06-07 13:20:12.649000

"""

# revision identifiers, used by Alembic.
revision = '64227a34252e'
down_revision = 'c1728858aaff'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_pa_tas_pa', 'program_activity', ['budget_year', 'agency_id', 'allocation_transfer_id', 'account_number', 'program_activity_code', 'program_activity_name'], unique=True)
    ### end Alembic commands ###


def downgrade_validation():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pa_tas_pa', table_name='program_activity')
    ### end Alembic commands ###


def upgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_staging():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###

