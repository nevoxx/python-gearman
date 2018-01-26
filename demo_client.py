import gearman
import gearman.constants


workload = "Hello World!"
hosts = ['localhost:4730']
task = "testing"


def check_request_status(job_request):
    if job_request.complete:
        print("Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result))
    elif job_request.timed_out:
        print("Job %s timed out!" % job_request.unique)
    elif job_request.state == gearman.constants.JOB_UNKNOWN:
        print("Job %s connection failed!" % job_request.unique)

gm_client = gearman.GearmanClient(hosts)
gm_client.submit_job(task, workload, background=True)
