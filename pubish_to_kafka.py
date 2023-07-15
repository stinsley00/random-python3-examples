#
#  This is an example def used in pushing messages to kafka for python based micro services
#  
#

def publish_message(kafka_instance, topic, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        kafka_instance.send(topic, key=key_bytes, value=value_bytes)
        kafka_instance.flush()
        print('Message published.')

    except Exception as ex:
        print(f'Exception in publishing message: {ex}')
