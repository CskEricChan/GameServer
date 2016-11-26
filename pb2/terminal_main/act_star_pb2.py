# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: act_star.proto

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
  name='act_star.proto',
  package='act_star',
  serialized_pb='\n\x0e\x61\x63t_star.proto\x12\x08\x61\x63t_star\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\"@\n\nselectInfo\x12\x12\n\niMonsterId\x18\x01 \x01(\x05\x12\r\n\x05iTime\x18\x02 \x01(\x05\x12\x0f\n\x07iAmount\x18\x03 \x01(\x05\"[\n\x08roleInfo\x12\x0f\n\x07iRoleId\x18\x01 \x02(\x03\x12\x0e\n\x06iLevel\x18\x02 \x01(\x05\x12\r\n\x05sName\x18\x03 \x01(\x0c\x12\x0f\n\x07iSchool\x18\x04 \x01(\x05\x12\x0e\n\x06iShape\x18\x05 \x01(\x05\"0\n\x08roleList\x12$\n\x08roleList\x18\x01 \x03(\x0b\x32\x12.act_star.roleInfo2J\n\rterminal2main\x12\x39\n\x13rpcStarSelectCancle\x12\x14.act_star.selectInfo\x1a\x0c.public.fake2\xeb\x01\n\rmain2terminal\x12\x37\n\x11rpcStarSelectSend\x12\x14.act_star.selectInfo\x1a\x0c.public.fake\x12\x36\n\x10rpcStarSelectMod\x12\x14.act_star.selectInfo\x1a\x0c.public.fake\x12\x37\n\x13rpcStarSelectResult\x12\x12.act_star.roleList\x1a\x0c.public.fake\x12\x30\n\x12rpcStarSelectClose\x12\x0c.public.fake\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_SELECTINFO = _descriptor.Descriptor(
  name='selectInfo',
  full_name='act_star.selectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iMonsterId', full_name='act_star.selectInfo.iMonsterId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iTime', full_name='act_star.selectInfo.iTime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAmount', full_name='act_star.selectInfo.iAmount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=66,
  serialized_end=130,
)


_ROLEINFO = _descriptor.Descriptor(
  name='roleInfo',
  full_name='act_star.roleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='act_star.roleInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iLevel', full_name='act_star.roleInfo.iLevel', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sName', full_name='act_star.roleInfo.sName', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSchool', full_name='act_star.roleInfo.iSchool', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iShape', full_name='act_star.roleInfo.iShape', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=132,
  serialized_end=223,
)


_ROLELIST = _descriptor.Descriptor(
  name='roleList',
  full_name='act_star.roleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleList', full_name='act_star.roleList.roleList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=225,
  serialized_end=273,
)

_ROLELIST.fields_by_name['roleList'].message_type = _ROLEINFO
DESCRIPTOR.message_types_by_name['selectInfo'] = _SELECTINFO
DESCRIPTOR.message_types_by_name['roleInfo'] = _ROLEINFO
DESCRIPTOR.message_types_by_name['roleList'] = _ROLELIST

class selectInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SELECTINFO

  # @@protoc_insertion_point(class_scope:act_star.selectInfo)

class roleInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO

  # @@protoc_insertion_point(class_scope:act_star.roleInfo)

class roleList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLELIST

  # @@protoc_insertion_point(class_scope:act_star.roleList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='act_star.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=275,
  serialized_end=349,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcStarSelectCancle',
    full_name='act_star.terminal2main.rpcStarSelectCancle',
    index=0,
    containing_service=None,
    input_type=_SELECTINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class terminal2main(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _TERMINAL2MAIN
class terminal2main_Stub(terminal2main):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _TERMINAL2MAIN


_MAIN2TERMINAL = _descriptor.ServiceDescriptor(
  name='main2terminal',
  full_name='act_star.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=352,
  serialized_end=587,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcStarSelectSend',
    full_name='act_star.main2terminal.rpcStarSelectSend',
    index=0,
    containing_service=None,
    input_type=_SELECTINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcStarSelectMod',
    full_name='act_star.main2terminal.rpcStarSelectMod',
    index=1,
    containing_service=None,
    input_type=_SELECTINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcStarSelectResult',
    full_name='act_star.main2terminal.rpcStarSelectResult',
    index=2,
    containing_service=None,
    input_type=_ROLELIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcStarSelectClose',
    full_name='act_star.main2terminal.rpcStarSelectClose',
    index=3,
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