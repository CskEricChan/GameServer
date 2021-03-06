# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: act_teamRace.proto

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
  name='act_teamRace.proto',
  package='act_teamRace',
  serialized_pb='\n\x12\x61\x63t_teamRace.proto\x12\x0c\x61\x63t_teamRace\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\"*\n\x08\x65nterMsg\x12\x0f\n\x07timeout\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\"B\n\x07infoMsg\x12\x10\n\x08\x63ountWin\x18\x01 \x01(\x05\x12\x12\n\ncountFight\x18\x02 \x01(\x05\x12\x11\n\tracePoint\x18\x03 \x01(\x03\"8\n\tfightInfo\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\r\n\x05times\x18\x02 \x01(\x05\x12\x0e\n\x06result\x18\x03 \x01(\x0c\"`\n\x07rankMsg\x12\x0e\n\x06rankNo\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\x0c\x12\x12\n\nschoolName\x18\x03 \x02(\x0c\x12\x15\n\rteamRacePoint\x18\x04 \x02(\x05\x12\x0c\n\x04iUid\x18\x05 \x01(\x04\"\\\n\nrankAllMsg\x12\'\n\x08rankList\x18\x01 \x03(\x0b\x32\x15.act_teamRace.rankMsg\x12%\n\x06rankMy\x18\x02 \x01(\x0b\x32\x15.act_teamRace.rankMsg\":\n\rfightInfoList\x12)\n\x08infoList\x18\x01 \x03(\x0b\x32\x17.act_teamRace.fightInfo\"j\n\x08roleInfo\x12\x0e\n\x06roleId\x18\x01 \x02(\x03\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\r\n\x05shape\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0e\n\x06school\x18\x05 \x01(\x05\x12\x12\n\nfightPower\x18\x06 \x01(\x05\"M\n\topenMatch\x12\x10\n\x08\x63oolTime\x18\x01 \x01(\x05\x12.\n\x0emyTeamRoleInfo\x18\x02 \x03(\x0b\x32\x16.act_teamRace.roleInfo\"9\n\tmatchInfo\x12,\n\x0croleInfoList\x18\x01 \x03(\x0b\x32\x16.act_teamRace.roleInfo2r\n\rterminal2main\x12\x32\n\x12rpcTeamRaceRankGet\x12\x0e.common.int32_\x1a\x0c.public.fake\x12-\n\x0frpcTeamRaceQuit\x12\x0c.public.fake\x1a\x0c.public.fake2\x9e\x05\n\rmain2terminal\x12=\n\x13rpcTeamRaceRankSend\x12\x18.act_teamRace.rankAllMsg\x1a\x0c.public.fake\x12\x38\n\x10rpcTeamRaceEnter\x12\x16.act_teamRace.enterMsg\x1a\x0c.public.fake\x12\x36\n\x0frpcTeamRaceInfo\x12\x15.act_teamRace.infoMsg\x1a\x0c.public.fake\x12<\n\x15rpcTeamRaceInfoChange\x12\x15.act_teamRace.infoMsg\x1a\x0c.public.fake\x12,\n\x0erpcTeamRaceEnd\x12\x0c.public.fake\x1a\x0c.public.fake\x12\x45\n\x18rpcTeamRaceFightInfoList\x12\x1b.act_teamRace.fightInfoList\x1a\x0c.public.fake\x12@\n\x17rpcTeamRaceFightInfoAdd\x12\x17.act_teamRace.fightInfo\x1a\x0c.public.fake\x12=\n\x14rpcTeamRaceOpenMatch\x12\x17.act_teamRace.openMatch\x1a\x0c.public.fake\x12\x33\n\x15rpcTeamRaceCloseMatch\x12\x0c.public.fake\x1a\x0c.public.fake\x12=\n\x14rpcTeamRaceMatchInfo\x12\x17.act_teamRace.matchInfo\x1a\x0c.public.fake\x12\x34\n\x14rpcTeamRaceTeamCount\x12\x0e.common.int32_\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_ENTERMSG = _descriptor.Descriptor(
  name='enterMsg',
  full_name='act_teamRace.enterMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='act_teamRace.enterMsg.timeout', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='act_teamRace.enterMsg.state', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=74,
  serialized_end=116,
)


_INFOMSG = _descriptor.Descriptor(
  name='infoMsg',
  full_name='act_teamRace.infoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='countWin', full_name='act_teamRace.infoMsg.countWin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='countFight', full_name='act_teamRace.infoMsg.countFight', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='racePoint', full_name='act_teamRace.infoMsg.racePoint', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=118,
  serialized_end=184,
)


_FIGHTINFO = _descriptor.Descriptor(
  name='fightInfo',
  full_name='act_teamRace.fightInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='act_teamRace.fightInfo.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='act_teamRace.fightInfo.times', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='act_teamRace.fightInfo.result', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=186,
  serialized_end=242,
)


_RANKMSG = _descriptor.Descriptor(
  name='rankMsg',
  full_name='act_teamRace.rankMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rankNo', full_name='act_teamRace.rankMsg.rankNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='act_teamRace.rankMsg.name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schoolName', full_name='act_teamRace.rankMsg.schoolName', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teamRacePoint', full_name='act_teamRace.rankMsg.teamRacePoint', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iUid', full_name='act_teamRace.rankMsg.iUid', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=244,
  serialized_end=340,
)


_RANKALLMSG = _descriptor.Descriptor(
  name='rankAllMsg',
  full_name='act_teamRace.rankAllMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rankList', full_name='act_teamRace.rankAllMsg.rankList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rankMy', full_name='act_teamRace.rankAllMsg.rankMy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=342,
  serialized_end=434,
)


_FIGHTINFOLIST = _descriptor.Descriptor(
  name='fightInfoList',
  full_name='act_teamRace.fightInfoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infoList', full_name='act_teamRace.fightInfoList.infoList', index=0,
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
  serialized_start=436,
  serialized_end=494,
)


_ROLEINFO = _descriptor.Descriptor(
  name='roleInfo',
  full_name='act_teamRace.roleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleId', full_name='act_teamRace.roleInfo.roleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='act_teamRace.roleInfo.name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='act_teamRace.roleInfo.shape', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='act_teamRace.roleInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='school', full_name='act_teamRace.roleInfo.school', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fightPower', full_name='act_teamRace.roleInfo.fightPower', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=496,
  serialized_end=602,
)


_OPENMATCH = _descriptor.Descriptor(
  name='openMatch',
  full_name='act_teamRace.openMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coolTime', full_name='act_teamRace.openMatch.coolTime', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='myTeamRoleInfo', full_name='act_teamRace.openMatch.myTeamRoleInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=604,
  serialized_end=681,
)


_MATCHINFO = _descriptor.Descriptor(
  name='matchInfo',
  full_name='act_teamRace.matchInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleInfoList', full_name='act_teamRace.matchInfo.roleInfoList', index=0,
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
  serialized_start=683,
  serialized_end=740,
)

_RANKALLMSG.fields_by_name['rankList'].message_type = _RANKMSG
_RANKALLMSG.fields_by_name['rankMy'].message_type = _RANKMSG
_FIGHTINFOLIST.fields_by_name['infoList'].message_type = _FIGHTINFO
_OPENMATCH.fields_by_name['myTeamRoleInfo'].message_type = _ROLEINFO
_MATCHINFO.fields_by_name['roleInfoList'].message_type = _ROLEINFO
DESCRIPTOR.message_types_by_name['enterMsg'] = _ENTERMSG
DESCRIPTOR.message_types_by_name['infoMsg'] = _INFOMSG
DESCRIPTOR.message_types_by_name['fightInfo'] = _FIGHTINFO
DESCRIPTOR.message_types_by_name['rankMsg'] = _RANKMSG
DESCRIPTOR.message_types_by_name['rankAllMsg'] = _RANKALLMSG
DESCRIPTOR.message_types_by_name['fightInfoList'] = _FIGHTINFOLIST
DESCRIPTOR.message_types_by_name['roleInfo'] = _ROLEINFO
DESCRIPTOR.message_types_by_name['openMatch'] = _OPENMATCH
DESCRIPTOR.message_types_by_name['matchInfo'] = _MATCHINFO

class enterMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERMSG

  # @@protoc_insertion_point(class_scope:act_teamRace.enterMsg)

class infoMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INFOMSG

  # @@protoc_insertion_point(class_scope:act_teamRace.infoMsg)

class fightInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTINFO

  # @@protoc_insertion_point(class_scope:act_teamRace.fightInfo)

class rankMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANKMSG

  # @@protoc_insertion_point(class_scope:act_teamRace.rankMsg)

class rankAllMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANKALLMSG

  # @@protoc_insertion_point(class_scope:act_teamRace.rankAllMsg)

class fightInfoList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTINFOLIST

  # @@protoc_insertion_point(class_scope:act_teamRace.fightInfoList)

class roleInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO

  # @@protoc_insertion_point(class_scope:act_teamRace.roleInfo)

class openMatch(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENMATCH

  # @@protoc_insertion_point(class_scope:act_teamRace.openMatch)

class matchInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATCHINFO

  # @@protoc_insertion_point(class_scope:act_teamRace.matchInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='act_teamRace.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=742,
  serialized_end=856,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceRankGet',
    full_name='act_teamRace.terminal2main.rpcTeamRaceRankGet',
    index=0,
    containing_service=None,
    input_type=common_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceQuit',
    full_name='act_teamRace.terminal2main.rpcTeamRaceQuit',
    index=1,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
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
  full_name='act_teamRace.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=859,
  serialized_end=1529,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceRankSend',
    full_name='act_teamRace.main2terminal.rpcTeamRaceRankSend',
    index=0,
    containing_service=None,
    input_type=_RANKALLMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceEnter',
    full_name='act_teamRace.main2terminal.rpcTeamRaceEnter',
    index=1,
    containing_service=None,
    input_type=_ENTERMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceInfo',
    full_name='act_teamRace.main2terminal.rpcTeamRaceInfo',
    index=2,
    containing_service=None,
    input_type=_INFOMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceInfoChange',
    full_name='act_teamRace.main2terminal.rpcTeamRaceInfoChange',
    index=3,
    containing_service=None,
    input_type=_INFOMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceEnd',
    full_name='act_teamRace.main2terminal.rpcTeamRaceEnd',
    index=4,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceFightInfoList',
    full_name='act_teamRace.main2terminal.rpcTeamRaceFightInfoList',
    index=5,
    containing_service=None,
    input_type=_FIGHTINFOLIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceFightInfoAdd',
    full_name='act_teamRace.main2terminal.rpcTeamRaceFightInfoAdd',
    index=6,
    containing_service=None,
    input_type=_FIGHTINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceOpenMatch',
    full_name='act_teamRace.main2terminal.rpcTeamRaceOpenMatch',
    index=7,
    containing_service=None,
    input_type=_OPENMATCH,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceCloseMatch',
    full_name='act_teamRace.main2terminal.rpcTeamRaceCloseMatch',
    index=8,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceMatchInfo',
    full_name='act_teamRace.main2terminal.rpcTeamRaceMatchInfo',
    index=9,
    containing_service=None,
    input_type=_MATCHINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTeamRaceTeamCount',
    full_name='act_teamRace.main2terminal.rpcTeamRaceTeamCount',
    index=10,
    containing_service=None,
    input_type=common_pb2._INT32_,
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
