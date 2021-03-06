# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='map.proto',
  package='surge.map.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmap.proto\x12\x0esurge.map.grpc\"8\n\x11\x43oordinateRequest\x12\x10\n\x08latitude\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\t\"C\n\x10\x44istrictResponse\x12\x10\n\x08\x64istrict\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t2a\n\x03Map\x12Z\n\x11GetServerResponse\x12!.surge.map.grpc.CoordinateRequest\x1a .surge.map.grpc.DistrictResponse\"\x00\x62\x06proto3'
)




_COORDINATEREQUEST = _descriptor.Descriptor(
  name='CoordinateRequest',
  full_name='surge.map.grpc.CoordinateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='surge.map.grpc.CoordinateRequest.latitude', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='surge.map.grpc.CoordinateRequest.longitude', index=1,
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
  serialized_start=29,
  serialized_end=85,
)


_DISTRICTRESPONSE = _descriptor.Descriptor(
  name='DistrictResponse',
  full_name='surge.map.grpc.DistrictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='district', full_name='surge.map.grpc.DistrictResponse.district', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='surge.map.grpc.DistrictResponse.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='surge.map.grpc.DistrictResponse.country', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=87,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['CoordinateRequest'] = _COORDINATEREQUEST
DESCRIPTOR.message_types_by_name['DistrictResponse'] = _DISTRICTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoordinateRequest = _reflection.GeneratedProtocolMessageType('CoordinateRequest', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATEREQUEST,
  '__module__' : 'map_pb2'
  # @@protoc_insertion_point(class_scope:surge.map.grpc.CoordinateRequest)
  })
_sym_db.RegisterMessage(CoordinateRequest)

DistrictResponse = _reflection.GeneratedProtocolMessageType('DistrictResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISTRICTRESPONSE,
  '__module__' : 'map_pb2'
  # @@protoc_insertion_point(class_scope:surge.map.grpc.DistrictResponse)
  })
_sym_db.RegisterMessage(DistrictResponse)



_MAP = _descriptor.ServiceDescriptor(
  name='Map',
  full_name='surge.map.grpc.Map',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=156,
  serialized_end=253,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='surge.map.grpc.Map.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_COORDINATEREQUEST,
    output_type=_DISTRICTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAP)

DESCRIPTOR.services_by_name['Map'] = _MAP

# @@protoc_insertion_point(module_scope)
