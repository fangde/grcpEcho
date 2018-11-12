import grpc
from concurrent import futures
import rpcEcho_pb2
import rpcEcho_pb2_grpc
import time

class EchoImageService(rpcEcho_pb2_grpc.EchoImageServiceServicer):
    def ProcessImage(self,request,context):
        response=rpcEcho_pb2.Empty()
        print 'received', request
        return response


def Serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpcEcho_pb2_grpc.add_EchoImageServiceServicer_to_server(EchoImageService(),server)
  
    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    while True:
        time.sleep(3600)

if __name__=="__main__":
    Serve()
   