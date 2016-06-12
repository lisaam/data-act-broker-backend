from dataactcore.models.stagingModels import Appropriation, ObjectClassProgramActivity, AwardFinancial, AwardFinancialAssistance
from dataactcore.models.stagingInterface import StagingInterface
from mixer.backend.sqlalchemy import Mixer
import random

staging_db = StagingInterface()
SESSION = staging_db.session

mixer = Mixer(session=SESSION, commit=True)
mixer.register(ObjectClassProgramActivity,
    programactivitycode=lambda: str(random.randint(1,9999)).zfill(4),
    objectclass=lambda: random.choice(['999','1252', '101', '2251', '1111', '1410', '000']))
mixer.register(AwardFinancial,
    programactivitycode=lambda: str(random.randint(1, 9999)).zfill(4),
    objectclass=lambda: random.choice(['999', '1252', '101', '2251', '1111', '1410', '000']),
    bydirectreimbursablefundingsource=lambda: random.choice(['D', 'R', None]))

def insert_tas_submission(taslist, submission_id, approp_job_id, ocpa_job_id, af_job_id, afa_job_id):

    approp = mixer.blend(Appropriation,
        allocationtransferagencyidentifier=taslist[0],
        agencyidentifier=taslist[1],
        beginningperiodofavailability=taslist[2],
        endingperiodofavailability=taslist[3],
        availabilitytypecode=taslist[4],
        mainaccountcode=taslist[5],
        subaccountcode=taslist[6],
        tas=taslist[7],
        submission_id=submission_id,
        job_id=approp_job_id)

    # object class program activity
    for i in range(0, random.randint(1, 50)):
        ocpa = mixer.blend(ObjectClassProgramActivity,
        allocationtransferagencyidentifier=taslist[0],
        agencyidentifier=taslist[1],
        beginningperiodofavailability=taslist[2],
        endingperiodofavailability=taslist[3],
        availabilitytypecode=taslist[4],
        mainaccountcode=taslist[5],
        subaccountcode=taslist[6],
        tas=taslist[7],
        submission_id=submission_id,
        job_id=ocpa_job_id)

    # some award financial
    for i in range(0, random.randint(5, 100)):
        af = mixer.blend(AwardFinancial,
        allocationtransferagencyidentifier=taslist[0],
        agencyidentifier=taslist[1],
        beginningperiodofavailability=taslist[2],
        endingperiodofavailability=taslist[3],
        availabilitytypecode=taslist[4],
        mainaccountcode=taslist[5],
        subaccountcode=taslist[6],
        tas=taslist[7],
        ussgl490100_deliveredordersobligationsunpaid_cpe=123456,
        submission_id=submission_id,
        job_id=af_job_id)

    # awards
    for i in range(0, random.randint(10,200)):
        afa = mixer.blend(AwardFinancialAssistance,
        submission_id=submission_id,
        job_id=afa_job_id)

    return submission_id


# fake submisison id
submission_id = random.randint(100, 9999)
approp_job_id = random.randint(1, 5000)
ocpa_job_id = random.randint(1, 5000)
af_job_id = random.randint(1, 5000)
afa_job_id = random.randint(1, 5000)


# some TAS to use
taslist = ['000','028', '0000', '0000', 'X', '406', '000']
taslist.append(''.join(taslist))
insert_tas_submission(
    taslist, submission_id, approp_job_id, ocpa_job_id, af_job_id, afa_job_id)
taslist = ['000', '028', '2015', '2017', ' ', '406', '000']
taslist.append(''.join(taslist))
insert_tas_submission(
    taslist, submission_id, approp_job_id, ocpa_job_id, af_job_id, afa_job_id)
taslist = ['000', '019', '2016', '2016', ' ', '113', '000']
taslist.append(''.join(taslist))
insert_tas_submission(
    taslist, submission_id, approp_job_id, ocpa_job_id, af_job_id, afa_job_id)
