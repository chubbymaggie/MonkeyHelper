#
# Copyright 2014 Mingyuan Xia (http://mxia.me) and others
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Contributor(s):
#   Mingyuan Xia
#   Xinye Lin
#

""" This script tests all agents, hosted by monkeyrunner
"""

import os, sys, inspect


def module_path():
    ''' returns the module path without the use of __file__.
    from http://stackoverflow.com/questions/729583/getting-file-path-of-imported-module'''
    return os.path.abspath(os.path.dirname(inspect.getsourcefile(module_path)))


sys.path.append(module_path())
sys.path.append(os.path.join(module_path(), '..', 'src'))

from Agents import CellularAgent, ScreenAgent, SystemStatusAgent, WifiAgent
from MonkeyHelper import EMonkeyDevice
from time import sleep

device = EMonkeyDevice()
test = CellularAgent(device)
print 'current cellular data status', test.getCellularDataStatus()
print 'toggle cellular data status', test.toggleCellularDataStatus()
sleep(5)
print 'turn off cellular data status', test.turnOffCellularData()
sleep(5)
print 'turn on cellular data status', test.turnOnCellularData()

#print device.shell('uiautomator runtest /sdcard/ChangeOrientationTest.jar -c edu.mcgill.lynxiayel.changeorientationtest.ChangeOrientationTest#testChangeRightDown').encode('utf-8')
#print os.system('adb shell uiautomator runtest /sdcard/ChangeOrientationTest.jar -c edu.mcgill.lynxiayel.changeorientationtest.ChangeOrientationTest#testChangeRightDown')
test = ScreenAgent(device)
print 'current screen rotation status', test.getScreenRotationStatus()
print 'current orientation', test.getOrientation()
print test.changeOrientation()
print test.changeLeftDown()
print test.changeRightDown()

test = SystemStatusAgent(device)
print 'current WIFI status', test.getWifiStatus()
print 'current battery level', test.getBatteryLevel()
print test.hasFile('')
print test.hasFile('test.jar')
print test.pushFile('test.jar')

test = WifiAgent(device)
print 'current WIFI status', test.getWiFiStatus()
print 'toggle WIFI status', test.changeWifiStatus()
sleep(5)
print'turn off cellular data status',  test.turnOffWifi()
sleep(5)
print 'turn on cellular data status', test.turnOnWifi()

