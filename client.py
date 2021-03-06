import os
import hey_how_pb2
import hey_how_pb2_grpc
import time
import grpc

def run():
	counter = 0
	pid = os.getpid()
	with grpc.insecure_channel("localhost:9999") as channel:
		stub = hey_how_pb2_grpc.HeyHowServiceStub(channel)
		while True:
			try:
				start = time.time()
				response = stub.heyhow(hey_how_pb2.HeyHow(count=counter, msg="HeyHow"))
				counter = response.count
				if counter % 1000 == 0:
					print(response.msg)
					print("%4f : resp=%s " % (time.time() - start, response.count))
			except KeyboardInterrupt:
				print("KeyboardInterrupt")
				channel.unsubscribe(close)
				exit()
				
def close(channel):
	channel.close()

if __name__ == "__main__":
	run()
