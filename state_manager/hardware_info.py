import psutil
import time


class HardwareInfo:
	def __init__(self, pid, job_queue_ref):
		self.last_time = -1
		self.last_num_jobs = -1
		self.pid = pid
		self.job_queue_ref = job_queue_ref


	def hardware_info():
		ret = {}
		#need to compute speed
		if self.last_time == -1:
			self.last_time = time.time()
		else:
			time_elapsed = time.time() - self.last_time
			self.last_time = time.time()
			print("time is " + str(time_elapsed))

		ret["time"] = time_elapsed

		qlen = self.job_queue_ref.qsize()
		if self.last_num_jobs == -1:
			self.last_num_jobs = qlen
		elif qlen == 0:
			res["status"] = "Done"
		else: 
			jobs_done = qlen - self.last_num_jobs
			self.last_num_jobs = qlen
			res["status"] = "Runnning"
		
		proc = psutil.Process(self.pid)
		ret["my_cpu"] = proc.get_cpu_percent(0.1)
		ret["free_cpu"] = 100 - psutil.cpu_percent(interval=0.1)
		ret["num"] = qlen
		with open('throttling.config', 'r') as config:
			throttling_val = int(config.read())
		ret["throttling"] = throttling_val
		ret["type"] = "bibi"

		print(ret)
		return ret
