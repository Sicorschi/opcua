# opcua_server1.py - Create an OPC UA server and simulate 2 tags
#
import opcua
import random
import time
  
s = opcua.Server()
s.set_server_name("OpcUa Test Server")
s.set_endpoint("opc.tcp://192.168.0.17:4840")
   
# Register the OPC-UA namespace
idx = s.register_namespace("http://192.168.0.17:4840")
# start the OPC UA server (no tags at this point)  
s.start() 
   
objects = s.get_objects_node()
# Define a Weather Station object with some tags
myobject = objects.add_object(idx, "Station")
   
# Add a Temperature tag with a value and range
myvar1 = myobject.add_variable(idx, "Temperature", 25)
myvar1.set_writable(writable=True)
   
# Add a Windspeed tag with a value and range
myvar2 = myobject.add_variable(idx, "Windspeed", 11)
myvar2.set_writable(writable=True)
  
# Create some simulated data
while True:
    myvar1.set_value(random.randrange(25, 29))
    myvar2.set_value(random.randrange(10, 20))
    time.sleep(5)