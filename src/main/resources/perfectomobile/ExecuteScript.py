#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.perfectomobile.httpclient import Credentials
from com.perfectomobile.httpclient.execution import ExecutionsHttpClient


credentials = Credentials(perfectomobileServer['username'], perfectomobileServer['password'])
client = ExecutionsHttpClient(perfectomobileServer['url'], credentials)

executionIds = {}
executionStatuses = {}
try:
    for key in deviceIds:
        scrip_execution_result = client.executeScript(key, scriptKey)
        executionIds[key] = scrip_execution_result.getExecutionId()
    if waitForExecutionFinish:
        for key, value in executionIds.iteritems():
            response = client.waitForExecution(value)
            executionStatuses[value] = response.get("status")
except:
    print "Failed to Execute script.\n"
    raise


