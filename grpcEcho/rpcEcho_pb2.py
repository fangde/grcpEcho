# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpcEcho.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpcEcho.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rrpcEcho.proto\"r\n\tEchoImage\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06\x63hanel\x18\x03 \x01(\r\x12\r\n\x05image\x18\x04 \x01(\x0c\x12\n\n\x02sx\x18\x05 \x01(\x02\x12\n\n\x02sy\x18\x06 \x01(\x02\x12\x0f\n\x07ijk2ras\x18\x07 \x01(\x02\"\x10\n\x0e\x45\x63hoImageReply2E\n\x10\x45\x63hoImageService\x12\x31\n\x10\x45\x63hoImageMethods\x12\n.EchoImage\x1a\x0f.EchoImageReply\"\x00\x62\x06proto3')
)




_ECHOIMAGE = _descriptor.Descriptor(
  name='EchoImage',
  full_name='EchoImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='EchoImage.height', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='EchoImage.width', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chanel', full_name='EchoImage.chanel', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='EchoImage.image', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sx', full_name='EchoImage.sx', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sy', full_name='EchoImage.sy', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ijk2ras', full_name='EchoImage.ijk2ras', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=131,
)


_ECHOIMAGEREPLY = _descriptor.Descriptor(
  name='EchoImageReply',
  full_name='EchoImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['EchoImage'] = _ECHOIMAGE
DESCRIPTOR.message_types_by_name['EchoImageReply'] = _ECHOIMAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoImage = _reflection.GeneratedProtocolMessageType('EchoImage', (_message.Message,), dict(
  DESCRIPTOR = _ECHOIMAGE,
  __module__ = 'rpcEcho_pb2'
  # @@protoc_insertion_point(class_scope:EchoImage)
  ))
_sym_db.RegisterMessage(EchoImage)

EchoImageReply = _reflection.GeneratedProtocolMessageType('EchoImageReply', (_message.Message,), dict(
  DESCRIPTOR = _ECHOIMAGEREPLY,
  __module__ = 'rpcEcho_pb2'
  # @@protoc_insertion_point(class_scope:EchoImageReply)
  ))
_sym_db.RegisterMessage(EchoImageReply)



_ECHOIMAGESERVICE = _descriptor.ServiceDescriptor(
  name='EchoImageService',
  full_name='EchoImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=151,
  serialized_end=220,
  methods=[
  _descriptor.MethodDescriptor(
    name='EchoImageMethods',
    full_name='EchoImageService.EchoImageMethods',
    index=0,
    containing_service=None,
    input_type=_ECHOIMAGE,
    output_type=_ECHOIMAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOIMAGESERVICE)

DESCRIPTOR.services_by_name['EchoImageService'] = _ECHOIMAGESERVICE

# @@protoc_insertion_point(module_scope)
