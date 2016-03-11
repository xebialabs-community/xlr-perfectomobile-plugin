#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#


from com.perfectomobile.selenium import MobileDriver

driver = MobileDriver(perfectomobileServer['url'],perfectomobileServer['username'],perfectomobileServer['password'])
try:
    for key in deviceIds:
        device=driver.getDevice(key)
        device.resetApplications()
finally:
    driver.quit()