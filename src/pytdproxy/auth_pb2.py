# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pytdproxy/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pytdproxy/auth.proto\x12\x06protos\"\x82\x01\n\tAuthToken\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x05\x12\x12\n\ntoken_type\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x14\n\x0clast_fetched\x18\x06 \x01(\t\"J\n\x13\x41\x64\x64\x41uthTokenRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.protos.AuthToken\"T\n\x14\x41\x64\x64\x41uthTokenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_error_message\"c\n\x10StartAuthRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61llback_url\x18\x02 \x01(\t\x12\x17\n\nlaunch_url\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\r\n\x0b_launch_url\"\\\n\x11StartAuthResponse\x12\x19\n\x11\x63ontinue_auth_url\x18\x01 \x01(\t\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_error_message\"L\n\x13\x43ompleteAuthRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61llback_url\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\"T\n\x14\x43ompleteAuthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_error_message2\xed\x01\n\x0b\x41uthService\x12K\n\x0c\x41\x64\x64\x41uthToken\x12\x1b.protos.AddAuthTokenRequest\x1a\x1c.protos.AddAuthTokenResponse\"\x00\x12\x43\n\nStartLogin\x12\x18.protos.StartAuthRequest\x1a\x19.protos.StartAuthResponse\"\x00\x12L\n\rCompleteLogin\x12\x1b.protos.CompleteAuthRequest\x1a\x1c.protos.CompleteAuthResponse\"\x00\x42\x10Z\x0etdproxy/protosb\x06proto3')



_AUTHTOKEN = DESCRIPTOR.message_types_by_name['AuthToken']
_ADDAUTHTOKENREQUEST = DESCRIPTOR.message_types_by_name['AddAuthTokenRequest']
_ADDAUTHTOKENRESPONSE = DESCRIPTOR.message_types_by_name['AddAuthTokenResponse']
_STARTAUTHREQUEST = DESCRIPTOR.message_types_by_name['StartAuthRequest']
_STARTAUTHRESPONSE = DESCRIPTOR.message_types_by_name['StartAuthResponse']
_COMPLETEAUTHREQUEST = DESCRIPTOR.message_types_by_name['CompleteAuthRequest']
_COMPLETEAUTHRESPONSE = DESCRIPTOR.message_types_by_name['CompleteAuthResponse']
AuthToken = _reflection.GeneratedProtocolMessageType('AuthToken', (_message.Message,), {
  'DESCRIPTOR' : _AUTHTOKEN,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.AuthToken)
  })
_sym_db.RegisterMessage(AuthToken)

AddAuthTokenRequest = _reflection.GeneratedProtocolMessageType('AddAuthTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDAUTHTOKENREQUEST,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.AddAuthTokenRequest)
  })
_sym_db.RegisterMessage(AddAuthTokenRequest)

AddAuthTokenResponse = _reflection.GeneratedProtocolMessageType('AddAuthTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDAUTHTOKENRESPONSE,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.AddAuthTokenResponse)
  })
_sym_db.RegisterMessage(AddAuthTokenResponse)

StartAuthRequest = _reflection.GeneratedProtocolMessageType('StartAuthRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTAUTHREQUEST,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.StartAuthRequest)
  })
_sym_db.RegisterMessage(StartAuthRequest)

StartAuthResponse = _reflection.GeneratedProtocolMessageType('StartAuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTAUTHRESPONSE,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.StartAuthResponse)
  })
_sym_db.RegisterMessage(StartAuthResponse)

CompleteAuthRequest = _reflection.GeneratedProtocolMessageType('CompleteAuthRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETEAUTHREQUEST,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.CompleteAuthRequest)
  })
_sym_db.RegisterMessage(CompleteAuthRequest)

CompleteAuthResponse = _reflection.GeneratedProtocolMessageType('CompleteAuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETEAUTHRESPONSE,
  '__module__' : 'pytdproxy.auth_pb2'
  # @@protoc_insertion_point(class_scope:protos.CompleteAuthResponse)
  })
_sym_db.RegisterMessage(CompleteAuthResponse)

_AUTHSERVICE = DESCRIPTOR.services_by_name['AuthService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\016tdproxy/protos'
  _AUTHTOKEN._serialized_start=33
  _AUTHTOKEN._serialized_end=163
  _ADDAUTHTOKENREQUEST._serialized_start=165
  _ADDAUTHTOKENREQUEST._serialized_end=239
  _ADDAUTHTOKENRESPONSE._serialized_start=241
  _ADDAUTHTOKENRESPONSE._serialized_end=325
  _STARTAUTHREQUEST._serialized_start=327
  _STARTAUTHREQUEST._serialized_end=426
  _STARTAUTHRESPONSE._serialized_start=428
  _STARTAUTHRESPONSE._serialized_end=520
  _COMPLETEAUTHREQUEST._serialized_start=522
  _COMPLETEAUTHREQUEST._serialized_end=598
  _COMPLETEAUTHRESPONSE._serialized_start=600
  _COMPLETEAUTHRESPONSE._serialized_end=684
  _AUTHSERVICE._serialized_start=687
  _AUTHSERVICE._serialized_end=924
# @@protoc_insertion_point(module_scope)
