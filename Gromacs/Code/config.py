#!/usr/bin/env python

# ----------------------------------------------------------------------------
# MAIN DESCRIPTION

RESOURCE = {
        #Resource related inputs	--MANDATORY
        'remote_host' : 'XSEDE.STAMPEDE',
        'remote_directory' : '/home1/02734/vivek91/output/',
        'username' : 'vivek91',
        'number_of_cores' : 4,
        'resource_name' : "sierra:12cores",
        'project_id' : "TG-MCB090174",
        'walltime' : 20
    }

TASK = {
        #Task related inputs		--MANDATORY

        #Paths/Directories involved
        'source_directory' : '/home/vivek/Research/github_tests/EnsembleAPI-PYP_tests/gromacs_input_PYP/',
        'output_directory' : "",

        #kernel/wrapper names
        'kernel_type' : 'python',       #/bin/bash or python
        'app_kernel' : 'gromacs_run.py',

        #Resource requirement and number of tasks
        'cores_per_task' : 1,
        'number_of_tasks' : 4,

    }

