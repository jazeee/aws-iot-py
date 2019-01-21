import datetime
import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

myShadowClient = AWSIoTMQTTShadowClient("Switch8266-v1")
myShadowClient.configureEndpoint("a2arj82jdj67sr.iot.us-west-2.amazonaws.com", 8883)
myShadowClient.configureCredentials("./certs/aws/rootCA.pem", "./certs/aws/850d42b0ff-private.pem.key", "./certs/aws/850d42b0ff-certificate.pem.crt")

myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec


myShadowClient.connect()

def customCallback(result ,r2, r3):
  print("Result=%r, %r, %r"%(result,r2, r3))

deviceShadow = myShadowClient.createShadowHandlerWithName("Switch8266-v1", True)
deviceShadow.shadowGet(customCallback, 5)

deviceShadow.shadowRegisterDeltaCallback(customCallback)

while 1:
  print("%r Sleeping" % (datetime.datetime.now()))
  time.sleep(10)

myDeviceShadow.shadowUnregisterDeltaCallback()
myShadowClient.disconnect()

