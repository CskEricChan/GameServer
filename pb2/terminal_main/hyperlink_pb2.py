# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hyperlink.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import common_pb2
import props_pb2
import pet_pb2
import task_pb2
import team_pb2
import lineup_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hyperlink.proto',
  package='hyperlink',
  serialized_pb='\n\x0fhyperlink.proto\x12\thyperlink\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\x1a\x0bprops.proto\x1a\tpet.proto\x1a\ntask.proto\x1a\nteam.proto\x1a\x0clineup.proto\"y\n\x08roleInfo\x12\x0e\n\x06roleId\x18\x01 \x02(\x03\x12\r\n\x05shape\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\x0c\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0e\n\x06teamId\x18\x06 \x01(\x05\x12\x11\n\tguildName\x18\x07 \x01(\x0c\x12\x0e\n\x06school\x18\x08 \x01(\x05\"W\n\rhyperlinkInfo\x12\x0f\n\x07iRoleId\x18\x01 \x02(\x03\x12\r\n\x05iType\x18\x02 \x01(\x05\x12\x11\n\tiTargetNo\x18\x03 \x01(\x05\x12\x13\n\x0bsSerialized\x18\x04 \x01(\x0c\x32G\n\rterminal2main\x12\x36\n\x0crpcHyperlink\x12\x18.hyperlink.hyperlinkInfo\x1a\x0c.public.fake2\xbc\x02\n\rmain2terminal\x12\x31\n\x11rpcPropsHyperlink\x12\x0e.props.itemMsg\x1a\x0c.public.fake\x12-\n\x0frpcPetHyperlink\x12\x0c.pet.petData\x1a\x0c.public.fake\x12/\n\x10rpcTaskHyperlink\x12\r.task.taskMsg\x1a\x0c.public.fake\x12\x30\n\x10rpcTeamHyperlink\x12\x0e.team.teamInfo\x1a\x0c.public.fake\x12\x35\n\x10rpcRoleHyperlink\x12\x13.hyperlink.roleInfo\x1a\x0c.public.fake\x12/\n\x0frpcEyeHyperlink\x12\x0e.lineup.eyeMsg\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_ROLEINFO = _descriptor.Descriptor(
  name='roleInfo',
  full_name='hyperlink.roleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleId', full_name='hyperlink.roleInfo.roleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='hyperlink.roleInfo.shape', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='hyperlink.roleInfo.name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='hyperlink.roleInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teamId', full_name='hyperlink.roleInfo.teamId', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guildName', full_name='hyperlink.roleInfo.guildName', index=5,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='school', full_name='hyperlink.roleInfo.school', index=6,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=130,
  serialized_end=251,
)


_HYPERLINKINFO = _descriptor.Descriptor(
  name='hyperlinkInfo',
  full_name='hyperlink.hyperlinkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='hyperlink.hyperlinkInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iType', full_name='hyperlink.hyperlinkInfo.iType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iTargetNo', full_name='hyperlink.hyperlinkInfo.iTargetNo', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sSerialized', full_name='hyperlink.hyperlinkInfo.sSerialized', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=253,
  serialized_end=340,
)

DESCRIPTOR.message_types_by_name['roleInfo'] = _ROLEINFO
DESCRIPTOR.message_types_by_name['hyperlinkInfo'] = _HYPERLINKINFO

class roleInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO

  # @@protoc_insertion_point(class_scope:hyperlink.roleInfo)

class hyperlinkInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HYPERLINKINFO

  # @@protoc_insertion_point(class_scope:hyperlink.hyperlinkInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='hyperlink.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=342,
  serialized_end=413,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcHyperlink',
    full_name='hyperlink.terminal2main.rpcHyperlink',
    index=0,
    containing_service=None,
    input_type=_HYPERLINKINFO,
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
  full_name='hyperlink.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=416,
  serialized_end=732,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcPropsHyperlink',
    full_name='hyperlink.main2terminal.rpcPropsHyperlink',
    index=0,
    containing_service=None,
    input_type=props_pb2._ITEMMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcPetHyperlink',
    full_name='hyperlink.main2terminal.rpcPetHyperlink',
    index=1,
    containing_service=None,
    input_type=pet_pb2._PETDATA,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTaskHyperlink',
    full_name='hyperlink.main2terminal.rpcTaskHyperlink',
    index=2,
    containing_service=None,
    input_type=task_pb2._TASKMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamHyperlink',
    full_name='hyperlink.main2terminal.rpcTeamHyperlink',
    index=3,
    containing_service=None,
    input_type=team_pb2._TEAMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRoleHyperlink',
    full_name='hyperlink.main2terminal.rpcRoleHyperlink',
    index=4,
    containing_service=None,
    input_type=_ROLEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEyeHyperlink',
    full_name='hyperlink.main2terminal.rpcEyeHyperlink',
    index=5,
    containing_service=None,
    input_type=lineup_pb2._EYEMSG,
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
