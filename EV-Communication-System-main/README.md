# EV-Communication-System
# IoT based Electric Vehicle Communication System
The purpose is to design lane detection ADAS (Advanced Driver Assistance Systems) feature for electric vehicle and communicate the parameters or factors with the user located at long distance using MQTT protocol.
The lane detection code is mostly dependent on Computer Vision(CV2) library of Python.
The project shows how we can share the EV data using MQTT protocol easily.

MQTT is a communication protocol based on pub/sub model. The broker used to communicate data is EMQX. 

Execution procedure:
1) Install all the necessary libraries.
2) Run Lane Detection Publish Data.py file, the data will start getting published on the terminal and demo video will be played where lanes are detected. 
3) Run Subscribe Data.py file on another terminal window.
 
Lane Detection Publish Data.py output:
![pub](https://user-images.githubusercontent.com/73383343/126430604-15ae0de7-748f-40c1-8a5d-618cd0a5ce83.JPG)

Subscribe Data.py output:

Now the published data will be received on the terminal window where the Subscribe Data.py file was executed.

![sub](https://user-images.githubusercontent.com/73383343/126430654-e76524d3-e1e0-4401-8d61-fcc7eb3170cc.JPG)


There are various data transmission parameters like throughput, data packets captured, packet drop ratio which can be analyzed using network analyzer tools like wireshark.

Throughput for QoS 0:
![LD Throughput QOS 0](https://user-images.githubusercontent.com/73383343/126430797-a0b27e8f-bce8-4ab7-8c1d-c9c53937be87.png)
Data Packets captured for QoS 0:
![Packet Lengths QOS 0](https://user-images.githubusercontent.com/73383343/126430814-b342bf4d-9a4a-41a5-a41f-a1ac51431c70.PNG)
Flow Graph for QoS 0: We can see some TCP errors in the flow graph because some of the data is lost in QoS 0 and because of that no acknowledgement is received from the receiver.
![Flow Graph QOS 0](https://user-images.githubusercontent.com/73383343/126430957-45bf97c4-d79b-46ef-b1cd-d60eeb1025eb.png)


QoS: Quality of Service is decided while publishing and subscribing data. There are 3 QoS in MQTT protocol. 

QoS 0: There is no acknowldgement whether data is received by subscriber or not. Data might be lost in this case.

QoS 1: Data is sent at least once i.e. when there is no acknowledgement from subscriber, publisher keeps on sending data until acknowledgement is received. 

QoS 2: Data is sent at most once i.e. The next data packet is not sent by publisher until acknowledgement is received from subscriber. This QoS uses more system power and it is useful where data plays critical role and data loss is not recommended eg. banks, automation.

For this particular project we are going to use QoS 1 as it is compatible with our project and we want to use system power as low as possible.   
