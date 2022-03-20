# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pytdproxy/chains.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16pytdproxy/chains.proto\x12\x06protos\x1a\x1cgoogle/protobuf/struct.proto\"{\n\x06Option\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61te_string\x18\x02 \x01(\t\x12\x14\n\x0cprice_string\x18\x03 \x01(\t\x12\x0f\n\x07is_call\x18\x04 \x01(\x08\x12%\n\x04info\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"r\n\x05\x43hain\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07is_call\x18\x03 \x01(\x08\x12\x19\n\x11last_refreshed_at\x18\x04 \x01(\t\x12\x1f\n\x07options\x18\x05 \x03(\x0b\x32\x0e.protos.Option\"Q\n\x13GetChainInfoRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x19\n\x0crefresh_type\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x0f\n\r_refresh_type\"P\n\x14GetChainInfoResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05\x64\x61tes\x18\x02 \x03(\t\x12\x19\n\x11last_refreshed_at\x18\x03 \x01(\t\"l\n\x0fGetChainRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07is_call\x18\x03 \x01(\x08\x12\x19\n\x0crefresh_type\x18\x04 \x01(\x05H\x00\x88\x01\x01\x42\x0f\n\r_refresh_type\"^\n\x10GetChainResponse\x12\x1a\n\rerror_message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x05\x63hain\x18\x02 \x01(\x0b\x32\r.protos.ChainB\x10\n\x0e_error_message2\x9c\x01\n\x0c\x43hainService\x12K\n\x0cGetChainInfo\x12\x1b.protos.GetChainInfoRequest\x1a\x1c.protos.GetChainInfoResponse\"\x00\x12?\n\x08GetChain\x12\x17.protos.GetChainRequest\x1a\x18.protos.GetChainResponse\"\x00\x42\x10Z\x0etdproxy/protosb\x06proto3')



_OPTION = DESCRIPTOR.message_types_by_name['Option']
_CHAIN = DESCRIPTOR.message_types_by_name['Chain']
_GETCHAININFOREQUEST = DESCRIPTOR.message_types_by_name['GetChainInfoRequest']
_GETCHAININFORESPONSE = DESCRIPTOR.message_types_by_name['GetChainInfoResponse']
_GETCHAINREQUEST = DESCRIPTOR.message_types_by_name['GetChainRequest']
_GETCHAINRESPONSE = DESCRIPTOR.message_types_by_name['GetChainResponse']
Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), {
  'DESCRIPTOR' : _OPTION,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.Option)
  })
_sym_db.RegisterMessage(Option)

Chain = _reflection.GeneratedProtocolMessageType('Chain', (_message.Message,), {
  'DESCRIPTOR' : _CHAIN,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.Chain)
  })
_sym_db.RegisterMessage(Chain)

GetChainInfoRequest = _reflection.GeneratedProtocolMessageType('GetChainInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHAININFOREQUEST,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetChainInfoRequest)
  })
_sym_db.RegisterMessage(GetChainInfoRequest)

GetChainInfoResponse = _reflection.GeneratedProtocolMessageType('GetChainInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHAININFORESPONSE,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetChainInfoResponse)
  })
_sym_db.RegisterMessage(GetChainInfoResponse)

GetChainRequest = _reflection.GeneratedProtocolMessageType('GetChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCHAINREQUEST,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetChainRequest)
  })
_sym_db.RegisterMessage(GetChainRequest)

GetChainResponse = _reflection.GeneratedProtocolMessageType('GetChainResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCHAINRESPONSE,
  '__module__' : 'pytdproxy.chains_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetChainResponse)
  })
_sym_db.RegisterMessage(GetChainResponse)

_CHAINSERVICE = DESCRIPTOR.services_by_name['ChainService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\016tdproxy/protos'
  _OPTION._serialized_start=64
  _OPTION._serialized_end=187
  _CHAIN._serialized_start=189
  _CHAIN._serialized_end=303
  _GETCHAININFOREQUEST._serialized_start=305
  _GETCHAININFOREQUEST._serialized_end=386
  _GETCHAININFORESPONSE._serialized_start=388
  _GETCHAININFORESPONSE._serialized_end=468
  _GETCHAINREQUEST._serialized_start=470
  _GETCHAINREQUEST._serialized_end=578
  _GETCHAINRESPONSE._serialized_start=580
  _GETCHAINRESPONSE._serialized_end=674
  _CHAINSERVICE._serialized_start=677
  _CHAINSERVICE._serialized_end=833
# @@protoc_insertion_point(module_scope)
