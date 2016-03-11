#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.perfectomobile.httpclient import Credentials, ParameterValue
from com.perfectomobile.httpclient.device import DevicesHttpClient


credentials = Credentials(perfectomobileServer['username'], perfectomobileServer['password'])
client = DevicesHttpClient(perfectomobileServer['url'], credentials)
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
    devices[device.getResponseValue("deviceId")] = "%s | %s" % (device.getResponseValue("model"), device.getResponseValue("available"))