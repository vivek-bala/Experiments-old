__author__ = 'vivek'

import sys
import time
import bigjobasync
import random
import os


# Number of tasks to run
N = 16
Nfiles = 5
filesize = 1048576  #bytes
itime = 0.0
avgtime = []

# ----------------------------------------------------------------------------
#
def resource_cb(origin, old_state, new_state):
    msg = " * Resource '%s' state changed from '%s' to '%s'.\n" % \
        (str(origin), old_state, new_state)
    sys.stderr.write(msg)

    if new_state == bigjobasync.FAILED:
        # Print the log and exit if big job has failed
        for entry in origin.log:
            print "   * LOG: %s" % entry
        sys.stderr.write("   * EXITING.\n")
        sys.exit(-1)

# ----------------------------------------------------------------------------
#
def task_cb(origin, old_state, new_state):
    """Task callback function: writes task state changes to STDERR
    """
    msg = " * Task %s state changed from '%s' to '%s'.\n" % \
        (str(origin), old_state, new_state)
    sys.stderr.write(msg)

    if new_state == bigjobasync.FAILED:
        # Print the log entry if task has failed to run
        for entry in origin.log:
            print "     LOG: %s" % entry

# ----------------------------------------------------------------------------
#
if __name__ == "__main__":

    for i in range(0,Nfiles):
        f1 = open('ifiles_%s.txt'%i,'w')
        for l in range(0,filesize):
            f1.write(str(random.randint(0,9)))
        f1.close()


    #itime = 0.0
    #for i in range(0,5):
    print('No of tasks : %s'%N)
    print('No of files : %s'%Nfiles)
    stampede = bigjobasync.Resource(
            name       = "sierra",
            resource   = bigjobasync.RESOURCES['FUTUREGRID.SIERRA'],
            username   = 'vivek91',
            runtime    = 10,
            cores      = 8,
            workdir    = "/N/u/vivek91/tryout/",
            project_id = "TG-MCB090174"
        )

    stampede.register_callbacks(resource_cb)
    stampede.allocate(terminate_on_empty_queue=True)

    # Define tasks and their input and output files
    all_tasks = []
    inputfiles = []

    for f in range(0,Nfiles):
        temp = {
            "mode":bigjobasync.COPY,
            "origin":bigjobasync.LOCAL,
            "origin_path":os.getcwd()+'/ifiles_%s.txt'%f,
        }
        inputfiles.append(temp)

    for i in range(0, N):

        sleep_task = bigjobasync.Task(
            name        = "sleep-task-%s" % i,
            cores       = 1,
            environment = {},
            executable  = "/bin/sleep 1",
            arguments   = [],
            input = inputfiles,
            output = []
        )
        sleep_task.register_callbacks(task_cb)
        all_tasks.append(sleep_task)

    # Submit all tasks to stampede
    t1=time.time()
    stampede.schedule_tasks(all_tasks)
    # Wait for the Resource allocation to finish, i.e., run out of wall time
    stampede.wait()
    t3=time.time()
    #itime=itime+(t3-t1)
    print ('itime is %s'%(t3-t1))
    avgtime.append(t3-t1)

    print(avgtime)
    sys.exit(0)

