# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entity.proto',
  package='entity',
  serialized_pb='\n\x0c\x65ntity.proto\x12\x06\x65ntity\x1a\x16universal/public.proto\"4\n\x08\x62ombInfo\x12\x12\n\niCountdown\x18\x01 \x01(\x05\x12\x14\n\x0ciTriggerType\x18\x02 \x01(\x05\"c\n\x08lkfpInfo\x12\x13\n\x08iNumberX\x18\x01 \x01(\x05:\x01\x31\x12\x13\n\x08iNumberY\x18\x02 \x01(\x05:\x01\x31\x12\x12\n\niCountdown\x18\x03 \x01(\x05\x12\x0b\n\x03iHp\x18\x04 \x01(\x05\x12\x0c\n\x04iDef\x18\x05 \x01(\x05\"g\n\ntricksInfo\x12\x0b\n\x03iId\x18\x01 \x02(\x05\x12\r\n\x05iType\x18\x02 \x02(\x05\x12\x0f\n\x07iDemage\x18\x03 \x02(\x05\x12\x16\n\x0biAppearType\x18\x04 \x01(\x05:\x01\x31\x12\x14\n\x0ctrickEttInfo\x18\x05 \x02(\x0c\"\xe1\x01\n\x0bpetSkillMsg\x12\x10\n\x08iSkillNo\x18\x01 \x01(\x05\x12\x14\n\x0c\x66SkillFactor\x18\x02 \x01(\x02\x12\x16\n\x0eiSkillDuration\x18\x03 \x01(\x05\x12\x15\n\rfSkillBaseNum\x18\x04 \x01(\x02\x12\x15\n\rsSkillActDesc\x18\x05 \x01(\x0c\x12\x12\n\niTriggType\x18\x06 \x01(\x05\x12\x13\n\x0b\x66TriggValue\x18\x07 \x01(\x02\x12\x11\n\tfLvFactor\x18\x08 \x01(\x02\x12\x10\n\x08iActAvLv\x18\t \x01(\x05\x12\x16\n\x0e\x66SkillEftValue\x18\n \x01(\x02\"d\n\x06petMsg\x12\x0e\n\x06iPetNo\x18\x01 \x02(\x05\x12\x0e\n\x06iPetLv\x18\x02 \x01(\x05\x12\x13\n\x0biStrengthLv\x18\x03 \x01(\x05\x12%\n\x08petSkill\x18\x04 \x03(\x0b\x32\x13.entity.petSkillMsg\"\xa9\x01\n\taiAttrMsg\x12\x14\n\x0ciWeaponShape\x18\x01 \x01(\x05\x12\x15\n\riWeaponEffect\x18\x02 \x01(\x05\x12\x11\n\tiWearFDId\x18\x03 \x01(\x05\x12\x13\n\x0biAttaEffect\x18\x04 \x01(\x05\x12\x16\n\x0eiAttaEffectAdd\x18\x05 \x01(\x05\x12\x0e\n\x06\x62\x41wark\x18\x06 \x01(\x08\x12\x1f\n\x07petList\x18\x07 \x03(\x0b\x32\x0e.entity.petMsg*|\n\ntricksType\x12\x10\n\x0c\x42OMB_TRIGGER\x10\x01\x12\x10\n\x0c\x42OMB_TIMEING\x10\x02\x12\x0e\n\nKNIFT_RAIN\x10\x03\x12\n\n\x06LUCKER\x10\x04\x12\x0e\n\nBOMB_ROUND\x10\x05\x12\x0c\n\x08\x45RUPTION\x10\x06\x12\x10\n\x0cPOISON_CLOUD\x10\x63')

_TRICKSTYPE = _descriptor.EnumDescriptor(
  name='tricksType',
  full_name='entity.tricksType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOMB_TRIGGER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOMB_TIMEING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KNIFT_RAIN', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUCKER', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOMB_ROUND', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERUPTION', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POISON_CLOUD', index=6, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=810,
  serialized_end=934,
)

tricksType = enum_type_wrapper.EnumTypeWrapper(_TRICKSTYPE)
BOMB_TRIGGER = 1
BOMB_TIMEING = 2
KNIFT_RAIN = 3
LUCKER = 4
BOMB_ROUND = 5
ERUPTION = 6
POISON_CLOUD = 99



_BOMBINFO = _descriptor.Descriptor(
  name='bombInfo',
  full_name='entity.bombInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iCountdown', full_name='entity.bombInfo.iCountdown', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iTriggerType', full_name='entity.bombInfo.iTriggerType', index=1,
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
  serialized_start=48,
  serialized_end=100,
)


_LKFPINFO = _descriptor.Descriptor(
  name='lkfpInfo',
  full_name='entity.lkfpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iNumberX', full_name='entity.lkfpInfo.iNumberX', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iNumberY', full_name='entity.lkfpInfo.iNumberY', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iCountdown', full_name='entity.lkfpInfo.iCountdown', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iHp', full_name='entity.lkfpInfo.iHp', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iDef', full_name='entity.lkfpInfo.iDef', index=4,
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
  serialized_start=102,
  serialized_end=201,
)


_TRICKSINFO = _descriptor.Descriptor(
  name='tricksInfo',
  full_name='entity.tricksInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iId', full_name='entity.tricksInfo.iId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iType', full_name='entity.tricksInfo.iType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iDemage', full_name='entity.tricksInfo.iDemage', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAppearType', full_name='entity.tricksInfo.iAppearType', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trickEttInfo', full_name='entity.tricksInfo.trickEttInfo', index=4,
      number=5, type=12, cpp_type=9, label=2,
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
  serialized_start=203,
  serialized_end=306,
)


_PETSKILLMSG = _descriptor.Descriptor(
  name='petSkillMsg',
  full_name='entity.petSkillMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iSkillNo', full_name='entity.petSkillMsg.iSkillNo', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fSkillFactor', full_name='entity.petSkillMsg.fSkillFactor', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSkillDuration', full_name='entity.petSkillMsg.iSkillDuration', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fSkillBaseNum', full_name='entity.petSkillMsg.fSkillBaseNum', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sSkillActDesc', full_name='entity.petSkillMsg.sSkillActDesc', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iTriggType', full_name='entity.petSkillMsg.iTriggType', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fTriggValue', full_name='entity.petSkillMsg.fTriggValue', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fLvFactor', full_name='entity.petSkillMsg.fLvFactor', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iActAvLv', full_name='entity.petSkillMsg.iActAvLv', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fSkillEftValue', full_name='entity.petSkillMsg.fSkillEftValue', index=9,
      number=10, type=2, cpp_type=6, label=1,
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
  serialized_start=309,
  serialized_end=534,
)


_PETMSG = _descriptor.Descriptor(
  name='petMsg',
  full_name='entity.petMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iPetNo', full_name='entity.petMsg.iPetNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iPetLv', full_name='entity.petMsg.iPetLv', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iStrengthLv', full_name='entity.petMsg.iStrengthLv', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='petSkill', full_name='entity.petMsg.petSkill', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=536,
  serialized_end=636,
)


_AIATTRMSG = _descriptor.Descriptor(
  name='aiAttrMsg',
  full_name='entity.aiAttrMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iWeaponShape', full_name='entity.aiAttrMsg.iWeaponShape', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iWeaponEffect', full_name='entity.aiAttrMsg.iWeaponEffect', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iWearFDId', full_name='entity.aiAttrMsg.iWearFDId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAttaEffect', full_name='entity.aiAttrMsg.iAttaEffect', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAttaEffectAdd', full_name='entity.aiAttrMsg.iAttaEffectAdd', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bAwark', full_name='entity.aiAttrMsg.bAwark', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='petList', full_name='entity.aiAttrMsg.petList', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=639,
  serialized_end=808,
)

_PETMSG.fields_by_name['petSkill'].message_type = _PETSKILLMSG
_AIATTRMSG.fields_by_name['petList'].message_type = _PETMSG
DESCRIPTOR.message_types_by_name['bombInfo'] = _BOMBINFO
DESCRIPTOR.message_types_by_name['lkfpInfo'] = _LKFPINFO
DESCRIPTOR.message_types_by_name['tricksInfo'] = _TRICKSINFO
DESCRIPTOR.message_types_by_name['petSkillMsg'] = _PETSKILLMSG
DESCRIPTOR.message_types_by_name['petMsg'] = _PETMSG
DESCRIPTOR.message_types_by_name['aiAttrMsg'] = _AIATTRMSG

class bombInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOMBINFO

  # @@protoc_insertion_point(class_scope:entity.bombInfo)

class lkfpInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LKFPINFO

  # @@protoc_insertion_point(class_scope:entity.lkfpInfo)

class tricksInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRICKSINFO

  # @@protoc_insertion_point(class_scope:entity.tricksInfo)

class petSkillMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PETSKILLMSG

  # @@protoc_insertion_point(class_scope:entity.petSkillMsg)

class petMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PETMSG

  # @@protoc_insertion_point(class_scope:entity.petMsg)

class aiAttrMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AIATTRMSG

  # @@protoc_insertion_point(class_scope:entity.aiAttrMsg)


# @@protoc_insertion_point(module_scope)
