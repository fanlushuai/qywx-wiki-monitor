from apscheduler.schedulers.blocking import BlockingScheduler

from main import *

sched = BlockingScheduler()


@sched.scheduled_job('cron', id='my_job_id', day='*/1', hour=10, minute=1)
def job_function():
    date = dateUtil.today()
    print(date + "Job Start" + date)
    run()
    print(date + "Job End" + dateUtil.today())


sched.start()
