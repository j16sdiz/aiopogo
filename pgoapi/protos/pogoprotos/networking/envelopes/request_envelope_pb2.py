# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/envelopes/request_envelope.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests import request_pb2 as pogoprotos_dot_networking_dot_requests_dot_request__pb2
from pogoprotos.networking.envelopes import auth_ticket_pb2 as pogoprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2
from pogoprotos.networking.platform import platform_request_type_pb2 as pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/envelopes/request_envelope.proto',
  package='pogoprotos.networking.envelopes',
  syntax='proto3',
  serialized_pb=_b('\n6pogoprotos/networking/envelopes/request_envelope.proto\x12\x1fpogoprotos.networking.envelopes\x1a,pogoprotos/networking/requests/request.proto\x1a\x31pogoprotos/networking/envelopes/auth_ticket.proto\x1a:pogoprotos/networking/platform/platform_request_type.proto\"\xc3\x05\n\x0fRequestEnvelope\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12\x39\n\x08requests\x18\x04 \x03(\x0b\x32\'.pogoprotos.networking.requests.Request\x12[\n\x11platform_requests\x18\x06 \x03(\x0b\x32@.pogoprotos.networking.envelopes.RequestEnvelope.PlatformRequest\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\t \x01(\x01\x12L\n\tauth_info\x18\n \x01(\x0b\x32\x39.pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo\x12@\n\x0b\x61uth_ticket\x18\x0b \x01(\x0b\x32+.pogoprotos.networking.envelopes.AuthTicket\x12!\n\x19ms_since_last_locationfix\x18\x0c \x01(\x03\x1a\x95\x01\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12L\n\x05token\x18\x02 \x01(\x0b\x32=.pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT\x1a)\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x05\x1am\n\x0fPlatformRequest\x12\x41\n\x04type\x18\x01 \x01(\x0e\x32\x33.pogoprotos.networking.platform.PlatformRequestType\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_request__pb2.DESCRIPTOR,pogoprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2.DESCRIPTOR,pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTENVELOPE_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT.unknown2', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=845,
)

_REQUESTENVELOPE_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=845,
)

_REQUESTENVELOPE_PLATFORMREQUEST = _descriptor.Descriptor(
  name='PlatformRequest',
  full_name='pogoprotos.networking.envelopes.RequestEnvelope.PlatformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.networking.envelopes.RequestEnvelope.PlatformRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.envelopes.RequestEnvelope.PlatformRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=956,
)

_REQUESTENVELOPE = _descriptor.Descriptor(
  name='RequestEnvelope',
  full_name='pogoprotos.networking.envelopes.RequestEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='pogoprotos.networking.envelopes.RequestEnvelope.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='pogoprotos.networking.envelopes.RequestEnvelope.request_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='pogoprotos.networking.envelopes.RequestEnvelope.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_requests', full_name='pogoprotos.networking.envelopes.RequestEnvelope.platform_requests', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.envelopes.RequestEnvelope.latitude', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.envelopes.RequestEnvelope.longitude', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='pogoprotos.networking.envelopes.RequestEnvelope.altitude', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='pogoprotos.networking.envelopes.RequestEnvelope.auth_info', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='pogoprotos.networking.envelopes.RequestEnvelope.auth_ticket', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ms_since_last_locationfix', full_name='pogoprotos.networking.envelopes.RequestEnvelope.ms_since_last_locationfix', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO, _REQUESTENVELOPE_PLATFORMREQUEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=956,
)

_REQUESTENVELOPE_AUTHINFO_JWT.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOPE_AUTHINFO_JWT
_REQUESTENVELOPE_AUTHINFO.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE_PLATFORMREQUEST.fields_by_name['type'].enum_type = pogoprotos_dot_networking_dot_platform_dot_platform__request__type__pb2._PLATFORMREQUESTTYPE
_REQUESTENVELOPE_PLATFORMREQUEST.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE.fields_by_name['requests'].message_type = pogoprotos_dot_networking_dot_requests_dot_request__pb2._REQUEST
_REQUESTENVELOPE.fields_by_name['platform_requests'].message_type = _REQUESTENVELOPE_PLATFORMREQUEST
_REQUESTENVELOPE.fields_by_name['auth_info'].message_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE.fields_by_name['auth_ticket'].message_type = pogoprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2._AUTHTICKET
DESCRIPTOR.message_types_by_name['RequestEnvelope'] = _REQUESTENVELOPE

RequestEnvelope = _reflection.GeneratedProtocolMessageType('RequestEnvelope', (_message.Message,), dict(

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_JWT,
      __module__ = 'pogoprotos.networking.envelopes.request_envelope_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO,
    __module__ = 'pogoprotos.networking.envelopes.request_envelope_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.envelopes.RequestEnvelope.AuthInfo)
    ))
  ,

  PlatformRequest = _reflection.GeneratedProtocolMessageType('PlatformRequest', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPE_PLATFORMREQUEST,
    __module__ = 'pogoprotos.networking.envelopes.request_envelope_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.envelopes.RequestEnvelope.PlatformRequest)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOPE,
  __module__ = 'pogoprotos.networking.envelopes.request_envelope_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.envelopes.RequestEnvelope)
  ))
_sym_db.RegisterMessage(RequestEnvelope)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.JWT)
_sym_db.RegisterMessage(RequestEnvelope.PlatformRequest)


# @@protoc_insertion_point(module_scope)
