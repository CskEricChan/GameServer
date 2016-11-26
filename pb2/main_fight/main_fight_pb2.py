# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main_fight.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import universal.base_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='main_fight.proto',
  package='',
  serialized_pb='\n\x10main_fight.proto\x1a\x16universal/public.proto\x1a\x14universal/base.proto2l\n\nmain2fight\x12\x32\n\x15rpcHelloFight_iAmMain\x12\x0c.public.fake\x1a\x0b.base.bool_\x12*\n\x0crpcHotUpdate\x12\x0c.base.bytes_\x1a\x0c.public.fake2@\n\nfight2main\x12\x32\n\x15rpcHelloMain_iAmFight\x12\x0c.base.int32_\x1a\x0b.base.bool_B\x03\x90\x01\x01')





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_MAIN2FIGHT = _descriptor.ServiceDescriptor(
  name='main2fight',
  full_name='main2fight',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=66,
  serialized_end=174,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcHelloFight_iAmMain',
    full_name='main2fight.rpcHelloFight_iAmMain',
    index=0,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.base_pb2._BOOL_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcHotUpdate',
    full_name='main2fight.rpcHotUpdate',
    index=1,
    containing_service=None,
    input_type=universal.base_pb2._BYTES_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class main2fight(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _MAIN2FIGHT
class main2fight_Stub(main2fight):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _MAIN2FIGHT


_FIGHT2MAIN = _descriptor.ServiceDescriptor(
  name='fight2main',
  full_name='fight2main',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=176,
  serialized_end=240,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcHelloMain_iAmFight',
    full_name='fight2main.rpcHelloMain_iAmFight',
    index=0,
    containing_service=None,
    input_type=universal.base_pb2._INT32_,
    output_type=universal.base_pb2._BOOL_,
    options=None,
  ),
])

class fight2main(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _FIGHT2MAIN
class fight2main_Stub(fight2main):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _FIGHT2MAIN

# @@protoc_insertion_point(module_scope)