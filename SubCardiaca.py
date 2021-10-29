# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:10:18 2021

@author: Ramon Silva
"""

#import ssl
import sys
import paho.mqtt.client

from DatabaseController import updateTableCardiaca

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='cardiaca', qos=2)

def on_message(client, userdata, message):
    print('------------------------------')
    #print('topic: %s' % message.topic)
    data = message.payload.decode('utf-8')
    print('%s' % data)
    updateTableCardiaca(data)
    print('qos: %d' % message.qos)

def main():
	client = paho.mqtt.client.Client('cardiaca')
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()

sys.exit(0)