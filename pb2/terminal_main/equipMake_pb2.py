# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipMake.proto

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
  name='equipMake.proto',
  package='equipMake',
  serialized_pb='\n\x0f\x65quipMake.proto\x12\tequipMake\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\"\xda\x02\n\tequipInfo\x12\x10\n\x08iPropsId\x18\x01 \x02(\x04\x12\x0b\n\x03iNo\x18\x02 \x01(\r\x12\x0b\n\x03\x63on\x18\x03 \x01(\x05\x12\x0b\n\x03mag\x18\x04 \x01(\x05\x12\x0b\n\x03str\x18\x05 \x01(\x05\x12\x0b\n\x03res\x18\x06 \x01(\x05\x12\x0b\n\x03spi\x18\x07 \x01(\x05\x12\x0b\n\x03\x64\x65x\x18\x08 \x01(\x05\x12\x0e\n\x06phyDam\x18\t \x01(\x05\x12\x0e\n\x06magDam\x18\n \x01(\x05\x12\x0c\n\x04\x63ure\x18\x0b \x01(\x05\x12\r\n\x05hpMax\x18\x0c \x01(\x05\x12\r\n\x05mpMax\x18\r \x01(\x05\x12\x0b\n\x03spe\x18\x0e \x01(\x05\x12\x0e\n\x06phyDef\x18\x0f \x01(\x05\x12\x0e\n\x06magDef\x18\x10 \x01(\x05\x12\x10\n\x08\x66iveAttr\x18\x11 \x01(\x05\x12\x10\n\x08spEffect\x18\x12 \x01(\x05\x12\x0f\n\x07spSkill\x18\x13 \x01(\x05\x12\x0f\n\x07sealHit\x18\x14 \x01(\x05\x12\x11\n\treSealHit\x18\x15 \x01(\x05\x12\x0e\n\x06isRare\x18\x16 \x01(\x05\"N\n\x0cmaterialInfo\x12\x0b\n\x03iNo\x18\x01 \x02(\r\x12\x0f\n\x07iAmount\x18\x02 \x01(\r\x12\x11\n\tiCashType\x18\x03 \x01(\r\x12\r\n\x05iCash\x18\x04 \x01(\r\"Y\n\x08makeInfo\x12\x0f\n\x07\x65quipNo\x18\x01 \x02(\x05\x12\x10\n\x08makeType\x18\x02 \x01(\x05\x12*\n\tmaterials\x18\x03 \x03(\x0b\x32\x17.equipMake.materialInfo\"0\n\x07gemInfo\x12%\n\x04gems\x18\x01 \x03(\x0b\x32\x17.equipMake.materialInfo\"?\n\naddGemInfo\x12\x10\n\x08iEquipId\x18\x01 \x02(\x03\x12\x0f\n\x07iHoleNo\x18\x02 \x02(\x05\x12\x0e\n\x06iGemNo\x18\x03 \x02(\x05\"2\n\rremoveGemInfo\x12\x10\n\x08iEquipId\x18\x01 \x02(\x03\x12\x0f\n\x07iHoleNo\x18\x02 \x02(\x05\"!\n\x0erecastAttrInfo\x12\x0f\n\x07propsId\x18\x01 \x02(\x04\"/\n\nrecastInfo\x12\x0f\n\x07propsId\x18\x01 \x02(\x04\x12\x10\n\x08shortcut\x18\x02 \x01(\x05\"Y\n\x0crecastResult\x12\x10\n\x08\x63oolTime\x18\x01 \x02(\x05\x12(\n\nrecastAttr\x18\x02 \x01(\x0b\x32\x14.equipMake.equipInfo\x12\r\n\x05iType\x18\x03 \x01(\x05\"/\n\x0crepairedInfo\x12\r\n\x05iType\x18\x01 \x02(\x05\x12\x10\n\x08iEquipId\x18\x02 \x01(\x03\" \n\x0crepairedList\x12\x10\n\x08iEquipId\x18\x01 \x03(\x03\x32\x85\x04\n\rterminal2main\x12\x38\n\x13rpcEquipMakeInfoReq\x12\x13.equipMake.makeInfo\x1a\x0c.public.fake\x12\x34\n\x0frpcEquipMakeReq\x12\x13.equipMake.makeInfo\x1a\x0c.public.fake\x12+\n\rrpcGemInfoReq\x12\x0c.public.fake\x1a\x0c.public.fake\x12\x30\n\trpcAddGem\x12\x15.equipMake.addGemInfo\x1a\x0c.public.fake\x12\x36\n\x0crpcRemoveGem\x12\x18.equipMake.removeGemInfo\x1a\x0c.public.fake\x12\x39\n\x10rpcEquipRepaired\x12\x17.equipMake.repairedInfo\x1a\x0c.public.fake\x12=\n\x12rpcEquipRecastAttr\x12\x19.equipMake.recastAttrInfo\x1a\x0c.public.fake\x12\x35\n\x0erpcEquipRecast\x12\x15.equipMake.recastInfo\x1a\x0c.public.fake\x12<\n\x15rpcEquipRecastReplace\x12\x15.equipMake.recastInfo\x1a\x0c.public.fake2\xc5\x02\n\rmain2terminal\x12=\n\x18rpcEquipMakeInfoResponse\x12\x13.equipMake.makeInfo\x1a\x0c.public.fake\x12:\n\x14rpcEquipMakeResponse\x12\x14.equipMake.equipInfo\x1a\x0c.public.fake\x12\x36\n\x12rpcGemInfoResponse\x12\x12.equipMake.gemInfo\x1a\x0c.public.fake\x12@\n\x17rpcEquipRepairedSuccess\x12\x17.equipMake.repairedList\x1a\x0c.public.fake\x12?\n\x16rpcEquipRecastResponse\x12\x17.equipMake.recastResult\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_EQUIPINFO = _descriptor.Descriptor(
  name='equipInfo',
  full_name='equipMake.equipInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iPropsId', full_name='equipMake.equipInfo.iPropsId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iNo', full_name='equipMake.equipInfo.iNo', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='con', full_name='equipMake.equipInfo.con', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mag', full_name='equipMake.equipInfo.mag', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str', full_name='equipMake.equipInfo.str', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='equipMake.equipInfo.res', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spi', full_name='equipMake.equipInfo.spi', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dex', full_name='equipMake.equipInfo.dex', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phyDam', full_name='equipMake.equipInfo.phyDam', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magDam', full_name='equipMake.equipInfo.magDam', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cure', full_name='equipMake.equipInfo.cure', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hpMax', full_name='equipMake.equipInfo.hpMax', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mpMax', full_name='equipMake.equipInfo.mpMax', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spe', full_name='equipMake.equipInfo.spe', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phyDef', full_name='equipMake.equipInfo.phyDef', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magDef', full_name='equipMake.equipInfo.magDef', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fiveAttr', full_name='equipMake.equipInfo.fiveAttr', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spEffect', full_name='equipMake.equipInfo.spEffect', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spSkill', full_name='equipMake.equipInfo.spSkill', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sealHit', full_name='equipMake.equipInfo.sealHit', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reSealHit', full_name='equipMake.equipInfo.reSealHit', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isRare', full_name='equipMake.equipInfo.isRare', index=21,
      number=22, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=415,
)


_MATERIALINFO = _descriptor.Descriptor(
  name='materialInfo',
  full_name='equipMake.materialInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iNo', full_name='equipMake.materialInfo.iNo', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAmount', full_name='equipMake.materialInfo.iAmount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iCashType', full_name='equipMake.materialInfo.iCashType', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iCash', full_name='equipMake.materialInfo.iCash', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=417,
  serialized_end=495,
)


_MAKEINFO = _descriptor.Descriptor(
  name='makeInfo',
  full_name='equipMake.makeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipNo', full_name='equipMake.makeInfo.equipNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='makeType', full_name='equipMake.makeInfo.makeType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='materials', full_name='equipMake.makeInfo.materials', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=497,
  serialized_end=586,
)


_GEMINFO = _descriptor.Descriptor(
  name='gemInfo',
  full_name='equipMake.gemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gems', full_name='equipMake.gemInfo.gems', index=0,
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
  serialized_start=588,
  serialized_end=636,
)


_ADDGEMINFO = _descriptor.Descriptor(
  name='addGemInfo',
  full_name='equipMake.addGemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEquipId', full_name='equipMake.addGemInfo.iEquipId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iHoleNo', full_name='equipMake.addGemInfo.iHoleNo', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iGemNo', full_name='equipMake.addGemInfo.iGemNo', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=638,
  serialized_end=701,
)


_REMOVEGEMINFO = _descriptor.Descriptor(
  name='removeGemInfo',
  full_name='equipMake.removeGemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEquipId', full_name='equipMake.removeGemInfo.iEquipId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iHoleNo', full_name='equipMake.removeGemInfo.iHoleNo', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=703,
  serialized_end=753,
)


_RECASTATTRINFO = _descriptor.Descriptor(
  name='recastAttrInfo',
  full_name='equipMake.recastAttrInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propsId', full_name='equipMake.recastAttrInfo.propsId', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=755,
  serialized_end=788,
)


_RECASTINFO = _descriptor.Descriptor(
  name='recastInfo',
  full_name='equipMake.recastInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propsId', full_name='equipMake.recastInfo.propsId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shortcut', full_name='equipMake.recastInfo.shortcut', index=1,
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
  serialized_start=790,
  serialized_end=837,
)


_RECASTRESULT = _descriptor.Descriptor(
  name='recastResult',
  full_name='equipMake.recastResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coolTime', full_name='equipMake.recastResult.coolTime', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recastAttr', full_name='equipMake.recastResult.recastAttr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iType', full_name='equipMake.recastResult.iType', index=2,
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
  serialized_start=839,
  serialized_end=928,
)


_REPAIREDINFO = _descriptor.Descriptor(
  name='repairedInfo',
  full_name='equipMake.repairedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iType', full_name='equipMake.repairedInfo.iType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iEquipId', full_name='equipMake.repairedInfo.iEquipId', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=930,
  serialized_end=977,
)


_REPAIREDLIST = _descriptor.Descriptor(
  name='repairedList',
  full_name='equipMake.repairedList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iEquipId', full_name='equipMake.repairedList.iEquipId', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  serialized_start=979,
  serialized_end=1011,
)

_MAKEINFO.fields_by_name['materials'].message_type = _MATERIALINFO
_GEMINFO.fields_by_name['gems'].message_type = _MATERIALINFO
_RECASTRESULT.fields_by_name['recastAttr'].message_type = _EQUIPINFO
DESCRIPTOR.message_types_by_name['equipInfo'] = _EQUIPINFO
DESCRIPTOR.message_types_by_name['materialInfo'] = _MATERIALINFO
DESCRIPTOR.message_types_by_name['makeInfo'] = _MAKEINFO
DESCRIPTOR.message_types_by_name['gemInfo'] = _GEMINFO
DESCRIPTOR.message_types_by_name['addGemInfo'] = _ADDGEMINFO
DESCRIPTOR.message_types_by_name['removeGemInfo'] = _REMOVEGEMINFO
DESCRIPTOR.message_types_by_name['recastAttrInfo'] = _RECASTATTRINFO
DESCRIPTOR.message_types_by_name['recastInfo'] = _RECASTINFO
DESCRIPTOR.message_types_by_name['recastResult'] = _RECASTRESULT
DESCRIPTOR.message_types_by_name['repairedInfo'] = _REPAIREDINFO
DESCRIPTOR.message_types_by_name['repairedList'] = _REPAIREDLIST

class equipInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EQUIPINFO

  # @@protoc_insertion_point(class_scope:equipMake.equipInfo)

class materialInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATERIALINFO

  # @@protoc_insertion_point(class_scope:equipMake.materialInfo)

class makeInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAKEINFO

  # @@protoc_insertion_point(class_scope:equipMake.makeInfo)

class gemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GEMINFO

  # @@protoc_insertion_point(class_scope:equipMake.gemInfo)

class addGemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDGEMINFO

  # @@protoc_insertion_point(class_scope:equipMake.addGemInfo)

class removeGemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMOVEGEMINFO

  # @@protoc_insertion_point(class_scope:equipMake.removeGemInfo)

class recastAttrInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECASTATTRINFO

  # @@protoc_insertion_point(class_scope:equipMake.recastAttrInfo)

class recastInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECASTINFO

  # @@protoc_insertion_point(class_scope:equipMake.recastInfo)

class recastResult(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECASTRESULT

  # @@protoc_insertion_point(class_scope:equipMake.recastResult)

class repairedInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REPAIREDINFO

  # @@protoc_insertion_point(class_scope:equipMake.repairedInfo)

class repairedList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REPAIREDLIST

  # @@protoc_insertion_point(class_scope:equipMake.repairedList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='equipMake.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1014,
  serialized_end=1531,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcEquipMakeInfoReq',
    full_name='equipMake.terminal2main.rpcEquipMakeInfoReq',
    index=0,
    containing_service=None,
    input_type=_MAKEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipMakeReq',
    full_name='equipMake.terminal2main.rpcEquipMakeReq',
    index=1,
    containing_service=None,
    input_type=_MAKEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGemInfoReq',
    full_name='equipMake.terminal2main.rpcGemInfoReq',
    index=2,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcAddGem',
    full_name='equipMake.terminal2main.rpcAddGem',
    index=3,
    containing_service=None,
    input_type=_ADDGEMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcRemoveGem',
    full_name='equipMake.terminal2main.rpcRemoveGem',
    index=4,
    containing_service=None,
    input_type=_REMOVEGEMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRepaired',
    full_name='equipMake.terminal2main.rpcEquipRepaired',
    index=5,
    containing_service=None,
    input_type=_REPAIREDINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRecastAttr',
    full_name='equipMake.terminal2main.rpcEquipRecastAttr',
    index=6,
    containing_service=None,
    input_type=_RECASTATTRINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRecast',
    full_name='equipMake.terminal2main.rpcEquipRecast',
    index=7,
    containing_service=None,
    input_type=_RECASTINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRecastReplace',
    full_name='equipMake.terminal2main.rpcEquipRecastReplace',
    index=8,
    containing_service=None,
    input_type=_RECASTINFO,
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
  full_name='equipMake.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1534,
  serialized_end=1859,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcEquipMakeInfoResponse',
    full_name='equipMake.main2terminal.rpcEquipMakeInfoResponse',
    index=0,
    containing_service=None,
    input_type=_MAKEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipMakeResponse',
    full_name='equipMake.main2terminal.rpcEquipMakeResponse',
    index=1,
    containing_service=None,
    input_type=_EQUIPINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGemInfoResponse',
    full_name='equipMake.main2terminal.rpcGemInfoResponse',
    index=2,
    containing_service=None,
    input_type=_GEMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRepairedSuccess',
    full_name='equipMake.main2terminal.rpcEquipRepairedSuccess',
    index=3,
    containing_service=None,
    input_type=_REPAIREDLIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcEquipRecastResponse',
    full_name='equipMake.main2terminal.rpcEquipRecastResponse',
    index=4,
    containing_service=None,
    input_type=_RECASTRESULT,
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
