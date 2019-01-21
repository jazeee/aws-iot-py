from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
myMQTTClient = AWSIoTMQTTClient("Switch8266-v1")
# myMQTTClient = AWSIoTMQTTClient("Switch8266-v1", useWebsocket=True)
myMQTTClient.configureEndpoint("a2arj82jdj67sr.iot.us-west-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./certs/aws/rootCA.pem", "./certs/aws/850d42b0ff-private.pem.key", "./certs/aws/850d42b0ff-certificate.pem.crt")
# myMQTTClient.configureCredentials("./aws/rootCA.pem")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myMQTTClient.connect()


