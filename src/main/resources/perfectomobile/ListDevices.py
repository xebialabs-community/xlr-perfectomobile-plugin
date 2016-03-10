from com.perfectomobile.httpclient import Credentials, ParameterValue
from com.perfectomobile.httpclient.device import DevicesHttpClient


credentials = Credentials(perfectomobileServer.username, perfectomobileServer.passwor)
client = DevicesHttpClient(perfectomobileServer.url, credentials)
inputParameters = []
param = ParameterValue("availableTo", availableTo)
inputParameters.append(param)
perfecto_devices = None
try:
    perfecto_devices = client.listDevices(inputParameters, False)
except:
    print "Failed to fetch device list"
    raise Exception("Failed to fetch device list")


devices = {}
for device in perfecto_devices:
    devices[device.getResponseValue("deviceId")] = device.getResponseValue("available")