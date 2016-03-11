#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.perfectomobile.httpclient import Credentials
from com.perfectomobile.httpclient.execution import ExecutionsHttpClient


credentials = Credentials(perfectomobileServer['username'], perfectomobileServer['password'])
client = ExecutionsHttpClient(perfectomobileServer['url'], credentials)
try:
    for key in deviceIds:
        scrip_execution_result = client.executeScript(key, scriptKey)
        executionId[key] = scrip_execution_result.getExecutionId()
except:
    print "Failed to Execute script.\n"
    raise


