from concurrent import futures
import grpc
import hey_how_pb2
import hey_how_pb2_grpc
import time
import threading

class Listener(hey_how_pb2_grpc.HeyHowServiceServicer):
	def __init__(self, *args, **kwargs):
		self.counter = 0
		self.mgs = "Let's go"
		self.lastPrintTime = time.time()
	
	#same name as in the protofile
	def heyhow(self, request, context):
		self.counter += 1
		if self.counter > 10000 :
			print(request.msg)
			print("10000 calls in %3f seconds" % (time.time() - self.lastPrintTime))
			self.lastPrintTime = time.time()
			self.counter = 0
		#count is also defined in the .proto file
		return hey_how_pb2.LetsGo(count=request.count + 1, msg=self.mgs)
		
def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
	hey_how_pb2_grpc.add_HeyHowServiceServicer_to_server(Listener(), server)
	server.add_insecure_port("[::]:9999")
	server.start()
	try:
		while True:
			print("server on: threads %i" % (threading.active_count()))
			time.sleep(5)
	except KeyboardInterrupt:
		print("Keyboard Interrupt")
		server.stop(0)

if __name__ == "__main__":
	serve()	
	