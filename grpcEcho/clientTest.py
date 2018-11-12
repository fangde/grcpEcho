import grpc
import rpcEcho_pb2
import rpcEcho_pb2_grpc

import time

channel=grpc.insecure_channel('localhost:50051')
stub=rpcEcho_pb2_grpc.EchoImageServiceStub(channel)

for i in range(1000):
    t1=time.time()
    echoImage=rpcEcho_pb2.EchoImage()

    response=stub.ProcessImage(echoImage)
    t2=time.time()
    print t2-t1 
    print response
