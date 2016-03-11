#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.io import File
from java.net import URL

from org.apache.commons.io import FileUtils

from com.perfectomobile.selenium import MobileDriver

driver = MobileDriver(perfectomobileServer['url'], perfectomobileServer['username'], perfectomobileServer['password'])

try:
    file = File.createTempFile("application","maf")
    FileUtils.copyURLToFile(URL(applicationUrl), file, 300000, 300000)

    driver.uploadMedia(repositoryKey, file)
    for key in deviceIds:
        device = driver.getDevice(key)
        device.installApplication(repositoryKey)

finally:
    driver.quit()