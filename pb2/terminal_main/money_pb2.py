# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: money.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='money.proto',
  package='money',
  serialized_pb='\n\x0bmoney.proto\x12\x05money\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto2\x0f\n\rterminal2main2\xa7\x01\n\rmain2terminal\x12\x30\n\x0erpcCashLackBox\x12\x0e.common.int64_\x1a\x0e.common.int32_\x12\x35\n\x13rpcTradeCashLackBox\x12\x0e.common.int64_\x1a\x0e.common.int32_\x12-\n\x0frpcOpenRecharge\x12\x0c.public.fake\x1a\x0c.public.fakeB\x03\x90\x01\x01')





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='money.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=60,
  serialized_end=75,
  methods=[
])

class terminal2main(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _TERMINAL2MAIN
class terminal2main_Stub(terminal2main):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _TERMINAL2MAIN


_MAIN2TERMINAL = _descriptor.ServiceDescriptor(
  name='main2terminal',
  full_name='money.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=78,
  serialized_end=245,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcCashLackBox',
    full_name='money.main2terminal.rpcCashLackBox',
    index=0,
    containing_service=None,
    input_type=common_pb2._INT64_,
    output_type=common_pb2._INT32_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTradeCashLackBox',
    full_name='money.main2terminal.rpcTradeCashLackBox',
    index=1,
    containing_service=None,
    input_type=common_pb2._INT64_,
    output_type=common_pb2._INT32_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcOpenRecharge',
    full_name='money.main2terminal.rpcOpenRecharge',
    index=2,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class main2terminal(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _MAIN2TERMINAL
class main2terminal_Stub(main2terminal):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _MAIN2TERMINAL

# @@protoc_insertion_point(module_scope)
