from background_task import background

import ho.pisa as pisa
import sys
from datetime import datetime
sys.path.append("../")

from competition.models import School, ResponsibleTeacher

# It seems that this file needs to be in the uctMaths folder and not competition. 
# Finding a workaround would make the code cleaner.

# All processes which could cause the server to hang due to run-time or volume should
# be background tasks

@background(queue="report-email-queue")
def bg_email_results(school_id):
    print("Emailing results for school with ID: " + str(school_id))
    from competition.compadmin import printer_school_report
    from competition.reports import send_confirmation

    school = School.objects.filter(id=school_id)[0]
    rteacher = ResponsibleTeacher.objects.filter(school=school)[0]
    
    result = printer_school_report(None, [school])
    send_confirmation(school, result, True)
    print("Finished sending report email for:", school.name)

# Ideally this function would be in competition/compadmin.py
@background(queue="AS-generation-queue")
def bg_generate_school_answer_sheets(school_id):
    print("Emailing answer sheets for school with ID: " + str(school_id))
    from competition.compadmin import printer_answer_sheet
    from competition.reports import send_answer_sheets

    school = School.objects.filter(id=school_id)[0]
    
    if not school.assigned_to:
        print("Cannot send an email to a school with no assigned responsible teacher!")
        return
    pdf = printer_answer_sheet(None, school)
    if not pdf:
        print("Unable to get answer sheets!")
        return
    
    send_answer_sheets(school, pdf, True)
    school.answer_sheets_emailed = datetime.now()
    school.save()
    print("Finished sending answer sheet email for school:", school.name)