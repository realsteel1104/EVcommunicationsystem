import paho.mqtt.client as mqtt
import time
import logging
def on_connect(client, userdata, flags, rc):
    logging.info("Connected flags"+str(flags)+"result code " + str(rc)+ "client1_id")
    client.connected_flag=True
def on_message(client, userdata, message):
    print("Received message: " ,str(message.payload.decode("utf-8")))
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected MQTT disconnection. Will auto-reconnect")
#mqttBroker ="mqtt.eclipse.org"
client = mqtt.Client("Lane Detection")
client.username_pw_set("electric_vehicle", "elec@123")
client.connect("broker.emqx.io", 1883, 60) 
client.subscribe("Lane Detection Parameters",qos=1)
client.on_connect = on_connect
client.on_message=on_message 
client.on_disconnect = on_disconnect
client.loop_forever()
