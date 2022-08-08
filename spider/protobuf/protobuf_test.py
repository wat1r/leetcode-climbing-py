# import blackboxprotobuf
#
# a = "ï²®†Ë²®† ·Äô".encode()
# deserialize_data, message_type = blackboxprotobuf.protobuf_to_json(a)
# print(deserialize_data)  # 非序列化的原始数据
# print(message_type)  # 消息类型结构


import blackboxprotobuf
content = b'\x08\x9f\x19\x10\xbc)\x18\xa9) \x9f\x19(\x86#0\xc7(8\xa1"@\xfeBH\xd2:P\xcd\x03'
print(blackboxprotobuf.protobuf_to_json(content))
