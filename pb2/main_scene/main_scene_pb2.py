# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main_scene.proto

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
  name='main_scene.proto',
  package='main_scene',
  serialized_pb='\n\x10main_scene.proto\x12\nmain_scene\x1a\x16universal/public.proto\x1a\x14universal/base.proto\"/\n\x0fregisterRoleMsg\x12\x0c\n\x04\x65pId\x18\x01 \x02(\x03\x12\x0e\n\x06roleId\x18\x02 \x02(\x03\"\x8a\x01\n\nentityInfo\x12\x0e\n\x06iEttId\x18\x01 \x02(\x03\x12\x10\n\x08iEttType\x18\x02 \x01(\x05\x12\x10\n\x08iSceneId\x18\x03 \x01(\x05\x12\t\n\x01x\x18\x04 \x01(\x05\x12\t\n\x01y\x18\x05 \x01(\x05\x12\t\n\x01\x64\x18\x06 \x01(\x05\x12\x17\n\x0fsBaseSerialized\x18\x07 \x01(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x08 \x01(\x05\"b\n\rmodEntityInfo\x12\x0e\n\x06iEttId\x18\x01 \x02(\x03\x12\x17\n\x0fsBaseSerialized\x18\x02 \x02(\x0c\x12\x15\n\rsChangePacket\x18\x03 \x01(\x0c\x12\x11\n\tuIgnoreId\x18\x05 \x03(\x03\"A\n\x08moveInfo\x12\x0e\n\x06iEttId\x18\x01 \x02(\x03\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x0f\n\x07sceneId\x18\x04 \x01(\x05\"d\n\x0fswitchSceneInfo\x12\x10\n\x08iSceneId\x18\x01 \x02(\x05\x12\x0e\n\x06iEttId\x18\x02 \x02(\x03\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x12\x19\n\x11sSwitchSerialized\x18\x05 \x01(\x0c\"d\n\tsceneInfo\x12\x10\n\x08iSceneId\x18\x01 \x02(\x05\x12\x0e\n\x06iWidth\x18\x02 \x02(\x05\x12\x0f\n\x07iHeight\x18\x03 \x02(\x05\x12\x0c\n\x04iRes\x18\x04 \x02(\x05\x12\x16\n\x0eiBroadcastRole\x18\x05 \x01(\x05\"0\n\x0cremoveEntity\x12\x10\n\x08iSceneId\x18\x01 \x02(\x05\x12\x0e\n\x06iEttId\x18\x02 \x02(\x03\"8\n\x12removeEntityByType\x12\x10\n\x08iSceneId\x18\x01 \x02(\x05\x12\x10\n\x08iEttType\x18\x02 \x01(\x05\"_\n\x11\x62roadCastByXYInfo\x12\x10\n\x08iSceneId\x18\x01 \x02(\x05\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x0f\n\x07sPacket\x18\x04 \x02(\x0c\x12\x11\n\tuIgnoreId\x18\x05 \x03(\x03\"K\n\x15\x62roadCastByEntityInfo\x12\x0e\n\x06iEttId\x18\x01 \x02(\x03\x12\x0f\n\x07sPacket\x18\x02 \x02(\x0c\x12\x11\n\tuIgnoreId\x18\x03 \x03(\x03\"i\n\x0bmodTeamInfo\x12\x0e\n\x06teamId\x18\x01 \x01(\x05\x12\x0e\n\x06leader\x18\x02 \x01(\x03\x12\x12\n\nmemberList\x18\x03 \x03(\x03\x12\x11\n\tleaveList\x18\x04 \x03(\x03\x12\x13\n\x0bofflineList\x18\x05 \x03(\x03\"\x1d\n\x0breleaseTeam\x12\x0e\n\x06teamId\x18\x01 \x01(\x05\"1\n\npacketInfo\x12\x0e\n\x06roleId\x18\x01 \x02(\x03\x12\x13\n\x0bsSerialized\x18\x02 \x02(\x0c\x32\xc3\x08\n\nmain2scene\x12\x33\n\rrpcSSRoleMove\x12\x14.main_scene.moveInfo\x1a\x0c.public.fake\x12\x35\n\x0frpcSSEntityMove\x12\x14.main_scene.moveInfo\x1a\x0c.public.fake\x12<\n\x0frpcRegisterRole\x12\x1b.main_scene.registerRoleMsg\x1a\x0c.public.fake\x12/\n\x11rpcUnRegisterRole\x12\x0c.base.int64_\x1a\x0c.public.fake\x12\x37\n\x0frpcCreateEntity\x12\x16.main_scene.entityInfo\x1a\x0c.public.fake\x12-\n\x0frpcDeleteEntity\x12\x0c.base.int64_\x1a\x0c.public.fake\x12;\n\x10rpcModEntityInfo\x12\x19.main_scene.modEntityInfo\x1a\x0c.public.fake\x12\x39\n\x0frpcRemoveEntity\x12\x18.main_scene.removeEntity\x1a\x0c.public.fake\x12\x45\n\x15rpcRemoveEntityByType\x12\x1e.main_scene.removeEntityByType\x1a\x0c.public.fake\x12\x30\n\x12rpcRemoveAllEntity\x12\x0c.base.int64_\x1a\x0c.public.fake\x12\x35\n\x0erpcCreateScene\x12\x15.main_scene.sceneInfo\x1a\x0c.public.fake\x12,\n\x0erpcRemoveScene\x12\x0c.base.int32_\x1a\x0c.public.fake\x12?\n\x10rpcBroadcastByXY\x12\x1d.main_scene.broadCastByXYInfo\x1a\x0c.public.fake\x12G\n\x14rpcBroadcastByEntity\x12!.main_scene.broadCastByEntityInfo\x1a\x0c.public.fake\x12;\n\x0erpcSwitchScene\x12\x1b.main_scene.switchSceneInfo\x1a\x0c.public.fake\x12\x39\n\x10rpcModSSTeamInfo\x12\x17.main_scene.modTeamInfo\x1a\x0c.public.fake\x12\x35\n\x0crpcDelSSTeam\x12\x17.main_scene.releaseTeam\x1a\x0c.public.fake\x12\x37\n\x0frpcSendToClient\x12\x16.main_scene.packetInfo\x1a\x0c.public.fake\x12*\n\x0crpcHotUpdate\x12\x0c.base.bytes_\x1a\x0c.public.fake2t\n\nscene2main\x12\x32\n\x15rpcHelloMain_iAmScene\x12\x0c.public.fake\x1a\x0b.base.bool_\x12\x32\n\x0crpcRoleNewXY\x12\x14.main_scene.moveInfo\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_REGISTERROLEMSG = _descriptor.Descriptor(
  name='registerRoleMsg',
  full_name='main_scene.registerRoleMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epId', full_name='main_scene.registerRoleMsg.epId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleId', full_name='main_scene.registerRoleMsg.roleId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=78,
  serialized_end=125,
)


_ENTITYINFO = _descriptor.Descriptor(
  name='entityInfo',
  full_name='main_scene.entityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.entityInfo.iEttId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iEttType', full_name='main_scene.entityInfo.iEttType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.entityInfo.iSceneId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='main_scene.entityInfo.x', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='main_scene.entityInfo.y', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='d', full_name='main_scene.entityInfo.d', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sBaseSerialized', full_name='main_scene.entityInfo.sBaseSerialized', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='main_scene.entityInfo.action', index=7,
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
  serialized_start=128,
  serialized_end=266,
)


_MODENTITYINFO = _descriptor.Descriptor(
  name='modEntityInfo',
  full_name='main_scene.modEntityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.modEntityInfo.iEttId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sBaseSerialized', full_name='main_scene.modEntityInfo.sBaseSerialized', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sChangePacket', full_name='main_scene.modEntityInfo.sChangePacket', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uIgnoreId', full_name='main_scene.modEntityInfo.uIgnoreId', index=3,
      number=5, type=3, cpp_type=2, label=3,
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
  serialized_start=268,
  serialized_end=366,
)


_MOVEINFO = _descriptor.Descriptor(
  name='moveInfo',
  full_name='main_scene.moveInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.moveInfo.iEttId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='main_scene.moveInfo.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='main_scene.moveInfo.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='main_scene.moveInfo.sceneId', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=368,
  serialized_end=433,
)


_SWITCHSCENEINFO = _descriptor.Descriptor(
  name='switchSceneInfo',
  full_name='main_scene.switchSceneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.switchSceneInfo.iSceneId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.switchSceneInfo.iEttId', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='main_scene.switchSceneInfo.x', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='main_scene.switchSceneInfo.y', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sSwitchSerialized', full_name='main_scene.switchSceneInfo.sSwitchSerialized', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=435,
  serialized_end=535,
)


_SCENEINFO = _descriptor.Descriptor(
  name='sceneInfo',
  full_name='main_scene.sceneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.sceneInfo.iSceneId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iWidth', full_name='main_scene.sceneInfo.iWidth', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iHeight', full_name='main_scene.sceneInfo.iHeight', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRes', full_name='main_scene.sceneInfo.iRes', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iBroadcastRole', full_name='main_scene.sceneInfo.iBroadcastRole', index=4,
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
  serialized_start=537,
  serialized_end=637,
)


_REMOVEENTITY = _descriptor.Descriptor(
  name='removeEntity',
  full_name='main_scene.removeEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.removeEntity.iSceneId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.removeEntity.iEttId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=639,
  serialized_end=687,
)


_REMOVEENTITYBYTYPE = _descriptor.Descriptor(
  name='removeEntityByType',
  full_name='main_scene.removeEntityByType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.removeEntityByType.iSceneId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iEttType', full_name='main_scene.removeEntityByType.iEttType', index=1,
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
  serialized_start=689,
  serialized_end=745,
)


_BROADCASTBYXYINFO = _descriptor.Descriptor(
  name='broadCastByXYInfo',
  full_name='main_scene.broadCastByXYInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSceneId', full_name='main_scene.broadCastByXYInfo.iSceneId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='main_scene.broadCastByXYInfo.x', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='main_scene.broadCastByXYInfo.y', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPacket', full_name='main_scene.broadCastByXYInfo.sPacket', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uIgnoreId', full_name='main_scene.broadCastByXYInfo.uIgnoreId', index=4,
      number=5, type=3, cpp_type=2, label=3,
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
  serialized_start=747,
  serialized_end=842,
)


_BROADCASTBYENTITYINFO = _descriptor.Descriptor(
  name='broadCastByEntityInfo',
  full_name='main_scene.broadCastByEntityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEttId', full_name='main_scene.broadCastByEntityInfo.iEttId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPacket', full_name='main_scene.broadCastByEntityInfo.sPacket', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uIgnoreId', full_name='main_scene.broadCastByEntityInfo.uIgnoreId', index=2,
      number=3, type=3, cpp_type=2, label=3,
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
  serialized_start=844,
  serialized_end=919,
)


_MODTEAMINFO = _descriptor.Descriptor(
  name='modTeamInfo',
  full_name='main_scene.modTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamId', full_name='main_scene.modTeamInfo.teamId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leader', full_name='main_scene.modTeamInfo.leader', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memberList', full_name='main_scene.modTeamInfo.memberList', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leaveList', full_name='main_scene.modTeamInfo.leaveList', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offlineList', full_name='main_scene.modTeamInfo.offlineList', index=4,
      number=5, type=3, cpp_type=2, label=3,
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
  serialized_start=921,
  serialized_end=1026,
)


_RELEASETEAM = _descriptor.Descriptor(
  name='releaseTeam',
  full_name='main_scene.releaseTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamId', full_name='main_scene.releaseTeam.teamId', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1028,
  serialized_end=1057,
)


_PACKETINFO = _descriptor.Descriptor(
  name='packetInfo',
  full_name='main_scene.packetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleId', full_name='main_scene.packetInfo.roleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sSerialized', full_name='main_scene.packetInfo.sSerialized', index=1,
      number=2, type=12, cpp_type=9, label=2,
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
  serialized_start=1059,
  serialized_end=1108,
)

DESCRIPTOR.message_types_by_name['registerRoleMsg'] = _REGISTERROLEMSG
DESCRIPTOR.message_types_by_name['entityInfo'] = _ENTITYINFO
DESCRIPTOR.message_types_by_name['modEntityInfo'] = _MODENTITYINFO
DESCRIPTOR.message_types_by_name['moveInfo'] = _MOVEINFO
DESCRIPTOR.message_types_by_name['switchSceneInfo'] = _SWITCHSCENEINFO
DESCRIPTOR.message_types_by_name['sceneInfo'] = _SCENEINFO
DESCRIPTOR.message_types_by_name['removeEntity'] = _REMOVEENTITY
DESCRIPTOR.message_types_by_name['removeEntityByType'] = _REMOVEENTITYBYTYPE
DESCRIPTOR.message_types_by_name['broadCastByXYInfo'] = _BROADCASTBYXYINFO
DESCRIPTOR.message_types_by_name['broadCastByEntityInfo'] = _BROADCASTBYENTITYINFO
DESCRIPTOR.message_types_by_name['modTeamInfo'] = _MODTEAMINFO
DESCRIPTOR.message_types_by_name['releaseTeam'] = _RELEASETEAM
DESCRIPTOR.message_types_by_name['packetInfo'] = _PACKETINFO

class registerRoleMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERROLEMSG

  # @@protoc_insertion_point(class_scope:main_scene.registerRoleMsg)

class entityInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTITYINFO

  # @@protoc_insertion_point(class_scope:main_scene.entityInfo)

class modEntityInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODENTITYINFO

  # @@protoc_insertion_point(class_scope:main_scene.modEntityInfo)

class moveInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOVEINFO

  # @@protoc_insertion_point(class_scope:main_scene.moveInfo)

class switchSceneInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SWITCHSCENEINFO

  # @@protoc_insertion_point(class_scope:main_scene.switchSceneInfo)

class sceneInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCENEINFO

  # @@protoc_insertion_point(class_scope:main_scene.sceneInfo)

class removeEntity(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEENTITY

  # @@protoc_insertion_point(class_scope:main_scene.removeEntity)

class removeEntityByType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEENTITYBYTYPE

  # @@protoc_insertion_point(class_scope:main_scene.removeEntityByType)

class broadCastByXYInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BROADCASTBYXYINFO

  # @@protoc_insertion_point(class_scope:main_scene.broadCastByXYInfo)

class broadCastByEntityInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BROADCASTBYENTITYINFO

  # @@protoc_insertion_point(class_scope:main_scene.broadCastByEntityInfo)

class modTeamInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODTEAMINFO

  # @@protoc_insertion_point(class_scope:main_scene.modTeamInfo)

class releaseTeam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RELEASETEAM

  # @@protoc_insertion_point(class_scope:main_scene.releaseTeam)

class packetInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PACKETINFO

  # @@protoc_insertion_point(class_scope:main_scene.packetInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_MAIN2SCENE = _descriptor.ServiceDescriptor(
  name='main2scene',
  full_name='main_scene.main2scene',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1111,
  serialized_end=2202,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcSSRoleMove',
    full_name='main_scene.main2scene.rpcSSRoleMove',
    index=0,
    containing_service=None,
    input_type=_MOVEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcSSEntityMove',
    full_name='main_scene.main2scene.rpcSSEntityMove',
    index=1,
    containing_service=None,
    input_type=_MOVEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRegisterRole',
    full_name='main_scene.main2scene.rpcRegisterRole',
    index=2,
    containing_service=None,
    input_type=_REGISTERROLEMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcUnRegisterRole',
    full_name='main_scene.main2scene.rpcUnRegisterRole',
    index=3,
    containing_service=None,
    input_type=universal.base_pb2._INT64_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcCreateEntity',
    full_name='main_scene.main2scene.rpcCreateEntity',
    index=4,
    containing_service=None,
    input_type=_ENTITYINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcDeleteEntity',
    full_name='main_scene.main2scene.rpcDeleteEntity',
    index=5,
    containing_service=None,
    input_type=universal.base_pb2._INT64_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcModEntityInfo',
    full_name='main_scene.main2scene.rpcModEntityInfo',
    index=6,
    containing_service=None,
    input_type=_MODENTITYINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRemoveEntity',
    full_name='main_scene.main2scene.rpcRemoveEntity',
    index=7,
    containing_service=None,
    input_type=_REMOVEENTITY,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRemoveEntityByType',
    full_name='main_scene.main2scene.rpcRemoveEntityByType',
    index=8,
    containing_service=None,
    input_type=_REMOVEENTITYBYTYPE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRemoveAllEntity',
    full_name='main_scene.main2scene.rpcRemoveAllEntity',
    index=9,
    containing_service=None,
    input_type=universal.base_pb2._INT64_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcCreateScene',
    full_name='main_scene.main2scene.rpcCreateScene',
    index=10,
    containing_service=None,
    input_type=_SCENEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRemoveScene',
    full_name='main_scene.main2scene.rpcRemoveScene',
    index=11,
    containing_service=None,
    input_type=universal.base_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcBroadcastByXY',
    full_name='main_scene.main2scene.rpcBroadcastByXY',
    index=12,
    containing_service=None,
    input_type=_BROADCASTBYXYINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcBroadcastByEntity',
    full_name='main_scene.main2scene.rpcBroadcastByEntity',
    index=13,
    containing_service=None,
    input_type=_BROADCASTBYENTITYINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcSwitchScene',
    full_name='main_scene.main2scene.rpcSwitchScene',
    index=14,
    containing_service=None,
    input_type=_SWITCHSCENEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcModSSTeamInfo',
    full_name='main_scene.main2scene.rpcModSSTeamInfo',
    index=15,
    containing_service=None,
    input_type=_MODTEAMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcDelSSTeam',
    full_name='main_scene.main2scene.rpcDelSSTeam',
    index=16,
    containing_service=None,
    input_type=_RELEASETEAM,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcSendToClient',
    full_name='main_scene.main2scene.rpcSendToClient',
    index=17,
    containing_service=None,
    input_type=_PACKETINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcHotUpdate',
    full_name='main_scene.main2scene.rpcHotUpdate',
    index=18,
    containing_service=None,
    input_type=universal.base_pb2._BYTES_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class main2scene(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _MAIN2SCENE
class main2scene_Stub(main2scene):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _MAIN2SCENE


_SCENE2MAIN = _descriptor.ServiceDescriptor(
  name='scene2main',
  full_name='main_scene.scene2main',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=2204,
  serialized_end=2320,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcHelloMain_iAmScene',
    full_name='main_scene.scene2main.rpcHelloMain_iAmScene',
    index=0,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.base_pb2._BOOL_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRoleNewXY',
    full_name='main_scene.scene2main.rpcRoleNewXY',
    index=1,
    containing_service=None,
    input_type=_MOVEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class scene2main(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _SCENE2MAIN
class scene2main_Stub(scene2main):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _SCENE2MAIN

# @@protoc_insertion_point(module_scope)