import unittest
from django.test import TestCase,Client
import paho.mqtt.client as mqtt
from unittest import TestCase, mock
#from subscribe.mqtt_client import on_message
import time


client = mqtt.Client("test_client2")
mqttBroker = "mqtt.eclipseprojects.io"
# mqtt_client = MyMQTTClient("test_client")

# Create your tests here.
class MyTestCase(TestCase):
    # def test_subscribe(self):
    #     # Define the expected arguments
    #     topic = 'test_topic'
    #     mqtt_client.subscribe(topic)
    #     self.assertEqual(mqtt_client.is_subscribed, True)
    
    # test for publish
    def test_publish(self):
        mqttBroker = "mqtt.eclipseprojects.io"
        client = mqtt.Client("test_client")
        client.connect(mqttBroker)
        client.subscribe("topic")
        (result,mid) = client.publish("topic", "test")
        self.assertEqual(result,0)
       
        
    # def test_unsubscribe(self):
    #     topic = "test_topic"
    #     mqtt_client.subscribe(topic)
    #     mqtt_client.unsubscribe(topic)
    #     self.assertEqual(mqtt_client.is_subscribed, False)
        
    # test for unsubscribe without altering paho method
    def test_unsubscribe2(self):
        mqttBroker = "mqtt.eclipseprojects.io"
        client = mqtt.Client("test_client")
        client.connect(mqttBroker)
        topic = 'test_topic'
        # unsubscribe() returns a tuple (result, mid) where result determines success of connection. 0 for success, 1-4 for errors
        # mid = message id
        (result, mid) = client.unsubscribe(topic)
        assert(result == 0)
    
    # test for subscribe() withouth altering paho method
    def test_subscribe2(self):
        mqttBroker = "mqtt.eclipseprojects.io"
        client = mqtt.Client("test_client")
        client.connect(mqttBroker)
        topic = 'test_topic'
        # subscribe() returns a tuple (result, mid) where result determines success of connection. 0 for success, 1-4 for errors
        # mid = message id
        (result, mid) = client.subscribe(topic)
        assert(result == 0)
        
    def test_on_message(self):
        message = ""
        assert(message=="hello")
        
    def test_sensor_list(self):
        self.client = Client()
        response = self.client.get('/sensorList')
        self.assertEqual(response.status_code, 200)
        
    def test_subscribe_client(self):
        self.client = Client()
        response = self.client.get('/subscribeClient')
        self.assertEqual(response.status_code, 200)
    
    def test_disconnect(self):
        mqttBroker = "mqtt.eclipseprojects.io"
        client = mqtt.Client("test_client")
        client.connect(mqttBroker)
        client.disconnect()
        self.assertEqual(client.is_connected(), False)
        
    def test_connect(self):
        mqttBroker = "mqtt.eclipseprojects.io"
        client = mqtt.Client("test_client")
        client.connect(mqttBroker)
        client.loop_start()  # start the network loop
        time.sleep(1)        # wait for the client to establish a connection
        self.assertTrue(client.is_connected())  # assert that the client is connected
        client.loop_stop()   
          