import saga
import simpleAPI
import traceback
import os,time,sys,random

HOSTNAME_sierra = "vivek91@sierra.futuregrid.org"
WORKDIR_sierra = "/N/u/vivek91/tryout/"

NUMBER_JOBS = 16

if __name__ == "__main__":

    #workdir = saga.filesystem.Directory("sftp://%s/%s" %(HOSTNAME_sierra,WORKDIR_sierra),saga.filesystem.CREATE_PARENTS)
    #mbpy = saga.filesystem.File("file://localhost/%s/searcher.py"%os.getcwd())
    #mbpy.copy(workdir.get_url())
    
    pilot = {
   		"service_url":"pbs+ssh://%s" %HOSTNAME_sierra,
   		"number_of_processes" : 8,
   		"working_directory" : WORKDIR_sierra,
   		"walltime" : 10
   		}	
    
    obj1=simpleAPI.simple(NUMBER_JOBS,pilot)
    obj1.startpilot()
    obj1.startCU()
    obj1.terminate()
