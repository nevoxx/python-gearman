import gearman

client_name = 'python3-worker'
hosts = ['localhost:4730']
task = "testing"


def task_listener_reverse(gearman_worker, gearman_job):
    print("\nReceived new Job")
    print("Workload: %s" % gearman_job.data)
    return gearman_job.data

gm_worker = gearman.GearmanWorker(hosts)
gm_worker.set_client_id(client_name)
gm_worker.register_task(task, task_listener_reverse)

print("starting work queue...")
gm_worker.work()
