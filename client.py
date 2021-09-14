import os
import hey_how_pb2
import hey_how_pb2_grpc
import time
import grpc

def run():
	counter = 0
	pid = os.getpid()
	with grpc.insecure_channel("localhost:666") as channel:
		stub = hey_how_pb2_grpc.HeyHowServiceStub(channel)
		while True:
			try:
				start = time.time()
				response = stub.heyhow(hey_how_pb2.HeyHow(count=counter))
				counter = response.count
				if counter % 1000 == 0:
					print("%4f : resp=%s : procid=%i" % (time.time() - start, response.count, pid))
			except KeyboardInterrupt:
				print("KeyboardInterrupt")
				channel.unsubscribe(close)
				exit()
				
def close(channel):
	channel.close()

if __name__ == "__main__":
	run()
