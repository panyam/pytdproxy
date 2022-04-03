# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pytdproxy import chains_pb2 as pytdproxy_dot_chains__pb2


class ChainServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetChainInfo = channel.unary_stream(
                '/protos.ChainService/GetChainInfo',
                request_serializer=pytdproxy_dot_chains__pb2.GetChainInfoRequest.SerializeToString,
                response_deserializer=pytdproxy_dot_chains__pb2.GetChainInfoResponse.FromString,
                )
        self.GetChain = channel.unary_unary(
                '/protos.ChainService/GetChain',
                request_serializer=pytdproxy_dot_chains__pb2.GetChainRequest.SerializeToString,
                response_deserializer=pytdproxy_dot_chains__pb2.GetChainResponse.FromString,
                )


class ChainServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetChainInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetChainInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.GetChainInfo,
                    request_deserializer=pytdproxy_dot_chains__pb2.GetChainInfoRequest.FromString,
                    response_serializer=pytdproxy_dot_chains__pb2.GetChainInfoResponse.SerializeToString,
            ),
            'GetChain': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChain,
                    request_deserializer=pytdproxy_dot_chains__pb2.GetChainRequest.FromString,
                    response_serializer=pytdproxy_dot_chains__pb2.GetChainResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.ChainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChainService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetChainInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/protos.ChainService/GetChainInfo',
            pytdproxy_dot_chains__pb2.GetChainInfoRequest.SerializeToString,
            pytdproxy_dot_chains__pb2.GetChainInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.ChainService/GetChain',
            pytdproxy_dot_chains__pb2.GetChainRequest.SerializeToString,
            pytdproxy_dot_chains__pb2.GetChainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
