# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hey_how.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hey_how.proto',
  package='hey_how',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rhey_how.proto\x12\x07hey_how\"$\n\x06HeyHow\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"$\n\x06LetsGo\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t2=\n\rHeyHowService\x12,\n\x06heyhow\x12\x0f.hey_how.HeyHow\x1a\x0f.hey_how.LetsGo\"\x00\x62\x06proto3'
)




_HEYHOW = _descriptor.Descriptor(
  name='HeyHow',
  full_name='hey_how.HeyHow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='hey_how.HeyHow.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='hey_how.HeyHow.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=62,
)


_LETSGO = _descriptor.Descriptor(
  name='LetsGo',
  full_name='hey_how.LetsGo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='hey_how.LetsGo.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='hey_how.LetsGo.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['HeyHow'] = _HEYHOW
DESCRIPTOR.message_types_by_name['LetsGo'] = _LETSGO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeyHow = _reflection.GeneratedProtocolMessageType('HeyHow', (_message.Message,), {
  'DESCRIPTOR' : _HEYHOW,
  '__module__' : 'hey_how_pb2'
  # @@protoc_insertion_point(class_scope:hey_how.HeyHow)
  })
_sym_db.RegisterMessage(HeyHow)

LetsGo = _reflection.GeneratedProtocolMessageType('LetsGo', (_message.Message,), {
  'DESCRIPTOR' : _LETSGO,
  '__module__' : 'hey_how_pb2'
  # @@protoc_insertion_point(class_scope:hey_how.LetsGo)
  })
_sym_db.RegisterMessage(LetsGo)



_HEYHOWSERVICE = _descriptor.ServiceDescriptor(
  name='HeyHowService',
  full_name='hey_how.HeyHowService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=163,
  methods=[
  _descriptor.MethodDescriptor(
    name='heyhow',
    full_name='hey_how.HeyHowService.heyhow',
    index=0,
    containing_service=None,
    input_type=_HEYHOW,
    output_type=_LETSGO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEYHOWSERVICE)

DESCRIPTOR.services_by_name['HeyHowService'] = _HEYHOWSERVICE

# @@protoc_insertion_point(module_scope)
