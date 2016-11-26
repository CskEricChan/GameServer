# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exchange.proto',
  package='exchange',
  serialized_pb='\n\x0e\x65xchange.proto\x12\x08\x65xchange\"(\n\x05order\x12\x0e\n\x06iPrice\x18\x01 \x02(\x03\x12\x0f\n\x07iAmount\x18\x02 \x02(\x05\":\n\x08gearInfo\x12\r\n\x05iGear\x18\x01 \x02(\x05\x12\x0e\n\x06iPrice\x18\x02 \x02(\x05\x12\x0f\n\x07iAmount\x18\x03 \x02(\x05\"1\n\tquotation\x12$\n\x08gearInfo\x18\x01 \x03(\x0b\x32\x12.exchange.gearInfo\"\x9d\x01\n\x07myOrder\x12\x31\n\torderInfo\x18\x01 \x03(\x0b\x32\x1e.exchange.myOrder.orderInfoTag\x1a_\n\x0corderInfoTag\x12\x10\n\x08iOrderId\x18\x01 \x02(\x05\x12\x0e\n\x06iPrice\x18\x02 \x02(\x05\x12\x0f\n\x07iAmount\x18\x03 \x02(\x05\x12\r\n\x05iType\x18\x04 \x02(\x05\x12\r\n\x05sTime\x18\x05 \x01(\x0c')




_ORDER = _descriptor.Descriptor(
  name='order',
  full_name='exchange.order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iPrice', full_name='exchange.order.iPrice', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAmount', full_name='exchange.order.iAmount', index=1,
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
  serialized_start=28,
  serialized_end=68,
)


_GEARINFO = _descriptor.Descriptor(
  name='gearInfo',
  full_name='exchange.gearInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iGear', full_name='exchange.gearInfo.iGear', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iPrice', full_name='exchange.gearInfo.iPrice', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAmount', full_name='exchange.gearInfo.iAmount', index=2,
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
  serialized_start=70,
  serialized_end=128,
)


_QUOTATION = _descriptor.Descriptor(
  name='quotation',
  full_name='exchange.quotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gearInfo', full_name='exchange.quotation.gearInfo', index=0,
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
  serialized_start=130,
  serialized_end=179,
)


_MYORDER_ORDERINFOTAG = _descriptor.Descriptor(
  name='orderInfoTag',
  full_name='exchange.myOrder.orderInfoTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iOrderId', full_name='exchange.myOrder.orderInfoTag.iOrderId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iPrice', full_name='exchange.myOrder.orderInfoTag.iPrice', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAmount', full_name='exchange.myOrder.orderInfoTag.iAmount', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iType', full_name='exchange.myOrder.orderInfoTag.iType', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sTime', full_name='exchange.myOrder.orderInfoTag.sTime', index=4,
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
  serialized_start=244,
  serialized_end=339,
)

_MYORDER = _descriptor.Descriptor(
  name='myOrder',
  full_name='exchange.myOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderInfo', full_name='exchange.myOrder.orderInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MYORDER_ORDERINFOTAG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=182,
  serialized_end=339,
)

_QUOTATION.fields_by_name['gearInfo'].message_type = _GEARINFO
_MYORDER_ORDERINFOTAG.containing_type = _MYORDER;
_MYORDER.fields_by_name['orderInfo'].message_type = _MYORDER_ORDERINFOTAG
DESCRIPTOR.message_types_by_name['order'] = _ORDER
DESCRIPTOR.message_types_by_name['gearInfo'] = _GEARINFO
DESCRIPTOR.message_types_by_name['quotation'] = _QUOTATION
DESCRIPTOR.message_types_by_name['myOrder'] = _MYORDER

class order(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORDER

  # @@protoc_insertion_point(class_scope:exchange.order)

class gearInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GEARINFO

  # @@protoc_insertion_point(class_scope:exchange.gearInfo)

class quotation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUOTATION

  # @@protoc_insertion_point(class_scope:exchange.quotation)

class myOrder(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class orderInfoTag(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _MYORDER_ORDERINFOTAG

    # @@protoc_insertion_point(class_scope:exchange.myOrder.orderInfoTag)
  DESCRIPTOR = _MYORDER

  # @@protoc_insertion_point(class_scope:exchange.myOrder)


# @@protoc_insertion_point(module_scope)
