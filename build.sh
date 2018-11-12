#!/bin/bash
python -m grpc_tools.protoc   -I ./protos --python_out=./grpcEcho --grpc_python_out=./grpcEcho ./protos/rpcEcho.proto
