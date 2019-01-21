import datetime
import time
import json
import requests

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient


# Custom Shadow callback
def customShadowCallback_Delta(payload, responseStatus, token):
    # payload is a JSON string ready to be parsed using json.loads(...)
    # in both Py2.x and Py3.x
    print(responseStatus)
    payloadDict = json.loads(payload)
    states = payloadDict["state"]["states"]
    print("++++++++DELTA++++++++++")
    print("property: " + str(states))
    print("version: " + str(payloadDict["version"]))
    print("+++++++++++++++++++++++\n\n")
    for state in states:
        switchId = state["switchId"]
        relayState = state["relayState"]
        print("%r -> %r" % (switchId, relayState))
        URL="http://10.2.1.%d/toggle-relay" % (switchId,)
        response = requests.post(URL, data = {})
        print(response)

myShadowClient = AWSIoTMQTTShadowClient("Switch8266-v1", useWebsocket=True)
myShadowClient.configureEndpoint("a2arj82jdj67sr.iot.us-west-2.amazonaws.com", 443)
myShadowClient.configureCredentials("./certs/aws/rootCA.pem")#, "./certs/aws/850d42b0ff-private.pem.key", "./certs/aws/850d42b0ff-certificate.pem.crt")

myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec


myShadowClient.connect()

def customCallback(state ,r2, r3):
  print("Result=%r, %r, %r"%(state,r2, r3))


deviceShadow = myShadowClient.createShadowHandlerWithName("Switch8266-v1", True)
# deviceShadow.shadowGet(customCallback, 5)

deviceShadow.shadowRegisterDeltaCallback(customShadowCallback_Delta)

while 1:
  time.sleep(1)

myDeviceShadow.shadowUnregisterDeltaCallback()
myShadowClient.disconnect()
