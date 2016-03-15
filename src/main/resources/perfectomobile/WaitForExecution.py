#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from com.perfectomobile.httpclient import Credentials
from com.perfectomobile.httpclient.execution import ExecutionsHttpClient


credentials = Credentials(perfectomobileServer['username'], perfectomobileServer['password'])
client = ExecutionsHttpClient(perfectomobileServer['url'], credentials)

executionStatuses = {}
try:
    for key, value in executionIds.iteritems():
        response = client.waitForExecution(value)
        executionStatuses[value] = response.get("status")
except:
    print "Failed to get execution statuses.\n"
    raise


