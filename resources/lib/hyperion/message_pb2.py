# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='proto',
  serialized_pb='\n\rmessage.proto\x12\x05proto\"\x82\x01\n\x0fHyperionRequest\x12/\n\x07\x63ommand\x18\x01 \x02(\x0e\x32\x1e.proto.HyperionRequest.Command\"8\n\x07\x43ommand\x12\t\n\x05\x43OLOR\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\t\n\x05\x43LEAR\x10\x03\x12\x0c\n\x08\x43LEARALL\x10\x04*\x04\x08\n\x10\x65\"\x87\x01\n\x0c\x43olorRequest\x12\x10\n\x08priority\x18\x01 \x02(\x05\x12\x10\n\x08RgbColor\x18\x02 \x02(\x05\x12\x10\n\x08\x64uration\x18\x03 \x01(\x05\x32\x41\n\x0c\x63olorRequest\x12\x16.proto.HyperionRequest\x18\n \x01(\x0b\x32\x13.proto.ColorRequest\"\xb1\x01\n\x0cImageRequest\x12\x10\n\x08priority\x18\x01 \x02(\x05\x12\x12\n\nimagewidth\x18\x02 \x02(\x05\x12\x13\n\x0bimageheight\x18\x03 \x02(\x05\x12\x11\n\timagedata\x18\x04 \x02(\x0c\x12\x10\n\x08\x64uration\x18\x05 \x01(\x05\x32\x41\n\x0cimageRequest\x12\x16.proto.HyperionRequest\x18\x0b \x01(\x0b\x32\x13.proto.ImageRequest\"c\n\x0c\x43learRequest\x12\x10\n\x08priority\x18\x01 \x02(\x05\x32\x41\n\x0c\x63learRequest\x12\x16.proto.HyperionRequest\x18\x0c \x01(\x0b\x32\x13.proto.ClearRequest\"\xa5\x01\n\rHyperionReply\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.proto.HyperionReply.Type\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x10\n\x08grabbing\x18\x04 \x01(\x05\x12\r\n\x05video\x18\x05 \x01(\x05\"*\n\x04Type\x12\t\n\x05REPLY\x10\x01\x12\x0c\n\x08GRABBING\x10\x02\x12\t\n\x05VIDEO\x10\x03')



_HYPERIONREQUEST_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='proto.HyperionRequest.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEARALL', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=93,
  serialized_end=149,
)

_HYPERIONREPLY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='proto.HyperionReply.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REPLY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRABBING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=700,
  serialized_end=742,
)


_HYPERIONREQUEST = _descriptor.Descriptor(
  name='HyperionRequest',
  full_name='proto.HyperionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='proto.HyperionRequest.command', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERIONREQUEST_COMMAND,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10, 101), ],
  serialized_start=25,
  serialized_end=155,
)


_COLORREQUEST = _descriptor.Descriptor(
  name='ColorRequest',
  full_name='proto.ColorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='proto.ColorRequest.priority', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RgbColor', full_name='proto.ColorRequest.RgbColor', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='proto.ColorRequest.duration', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='colorRequest', full_name='proto.ColorRequest.colorRequest', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=158,
  serialized_end=293,
)


_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='proto.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='proto.ImageRequest.priority', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imagewidth', full_name='proto.ImageRequest.imagewidth', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageheight', full_name='proto.ImageRequest.imageheight', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imagedata', full_name='proto.ImageRequest.imagedata', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='proto.ImageRequest.duration', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='imageRequest', full_name='proto.ImageRequest.imageRequest', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=296,
  serialized_end=473,
)


_CLEARREQUEST = _descriptor.Descriptor(
  name='ClearRequest',
  full_name='proto.ClearRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='proto.ClearRequest.priority', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='clearRequest', full_name='proto.ClearRequest.clearRequest', index=0,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=475,
  serialized_end=574,
)


_HYPERIONREPLY = _descriptor.Descriptor(
  name='HyperionReply',
  full_name='proto.HyperionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.HyperionReply.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='proto.HyperionReply.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.HyperionReply.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grabbing', full_name='proto.HyperionReply.grabbing', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video', full_name='proto.HyperionReply.video', index=4,
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
    _HYPERIONREPLY_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=577,
  serialized_end=742,
)

_HYPERIONREQUEST.fields_by_name['command'].enum_type = _HYPERIONREQUEST_COMMAND
_HYPERIONREQUEST_COMMAND.containing_type = _HYPERIONREQUEST;
_HYPERIONREPLY.fields_by_name['type'].enum_type = _HYPERIONREPLY_TYPE
_HYPERIONREPLY_TYPE.containing_type = _HYPERIONREPLY;
DESCRIPTOR.message_types_by_name['HyperionRequest'] = _HYPERIONREQUEST
DESCRIPTOR.message_types_by_name['ColorRequest'] = _COLORREQUEST
DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['ClearRequest'] = _CLEARREQUEST
DESCRIPTOR.message_types_by_name['HyperionReply'] = _HYPERIONREPLY

class HyperionRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HYPERIONREQUEST

  # @@protoc_insertion_point(class_scope:proto.HyperionRequest)

class ColorRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COLORREQUEST

  # @@protoc_insertion_point(class_scope:proto.ColorRequest)

class ImageRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IMAGEREQUEST

  # @@protoc_insertion_point(class_scope:proto.ImageRequest)

class ClearRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLEARREQUEST

  # @@protoc_insertion_point(class_scope:proto.ClearRequest)

class HyperionReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HYPERIONREPLY

  # @@protoc_insertion_point(class_scope:proto.HyperionReply)

_COLORREQUEST.extensions_by_name['colorRequest'].message_type = _COLORREQUEST
HyperionRequest.RegisterExtension(_COLORREQUEST.extensions_by_name['colorRequest'])
_IMAGEREQUEST.extensions_by_name['imageRequest'].message_type = _IMAGEREQUEST
HyperionRequest.RegisterExtension(_IMAGEREQUEST.extensions_by_name['imageRequest'])
_CLEARREQUEST.extensions_by_name['clearRequest'].message_type = _CLEARREQUEST
HyperionRequest.RegisterExtension(_CLEARREQUEST.extensions_by_name['clearRequest'])

# @@protoc_insertion_point(module_scope)
