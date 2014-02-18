import time
import sys
import os
import saga
from pilot import PilotComputeService, ComputeDataService, State
class simple:
	#Input values from user - Number of jobs, Pilot Description, Redis Server Coordination URL
	def __init__(self,no_jobs,pilot,COORD_url=None):
		self.no_jobs = no_jobs
		self.pilot = pilot
		if(COORD_url == None):
			self.COORD = "redis://ILikeBigJob_wITH-REdIS@gw68.quarry.iu.teragrid.org:6379"
		else:
			self.COORD = COORD_url
		#Time variable to analyse timing responses
		self.pilot_setup_time = 0
		self.total_cu_time = 0
		self.cu_sub_time = 0
		self.cu_wait_time = 0
			
	def startpilot(self):
		#API currently supports single pilot applications
		print 'Start pilot service'
		p1=time.time()
		self.pilot_compute_service = PilotComputeService(self.COORD)
		#Mandatory service url,number_of_processes of the Pilot
		self.pilot_compute_description = { 
						"service_url" : self.pilot["service_url"],
						"number_of_processes" : self.pilot["number_of_processes"]
						}
		#Check for possible keys for Working Directory,
		#Queue, Walltime. Take default values if not mentioned.
		if self.pilot.has_key("working_directory"):
			self.pilot_compute_description["working_directory"] = self.pilot["working_directory"]
		if self.pilot.has_key("queue"):
			self.pilot_compute_description["queue"] = self.pilot["queue"]
		if self.pilot.has_key("walltime"):
			self.pilot_compute_description["walltime"] = self.pilot["walltime"]
		self.pilotjob = self.pilot_compute_service.create_pilot(pilot_compute_description=self.pilot_compute_description)
		p2=time.time()
		self.pilot_setup_time = p2 - p1
		print 'Pilot successfully started'
	
	def startCU(self):
		print 'Starting Compute Unit submissions'
		#p1,p2,p3,p4,p5 - Probes for time calculations
		p1 = time.time()
		self.compute_data_service = ComputeDataService()
		self.compute_data_service.add_pilot_compute_service(self.pilot_compute_service)
		for i in range(self.no_jobs):
			print 'Submitting job %s on %s'%(i+1,self.pilot["service_url"])
			p2 = time.time()
			self.compute_unit_description = {
							"executable":"/bin/sleep 4",
							#"arguments" : ["$MYOUTPUT"],
							#"environment" : {'MYOUTPUT':'"Hello from Simple API"'},
							"number_of_processes" : 1,
							"output" : "stdout.txt",
							"error" : "stderr.txt"
							}
			self.compute_unit = self.compute_data_service.submit_compute_unit(self.compute_unit_description)
			p3 = time.time()
			self.cu_sub_time = self.cu_sub_time + (p3-p2)
		print 'All Compute Units Submitted. Waiting for completion'
		p4 = time.time()
		self.compute_data_service.wait()
		p5 = time.time()
		self.total_cu_time = p5 - p1
		self.cu_wait_time = p5 - p4
		print 'All CU executions completed'
		
	def terminate(self):
		#Terminate all CUs and pilot, Display all timing responses
		print 'Terminating pilot'
		self.compute_data_service.cancel()
		self.pilot_compute_service.cancel()
		print 'No of jobs : ',self.no_jobs
		print 'Pilot setup time : ',self.pilot_setup_time
		print 'CU submission time : ',self.cu_sub_time
		print 'CU wait time : ',self.cu_wait_time
		print 'Total CU time : ',self.total_cu_time
							

