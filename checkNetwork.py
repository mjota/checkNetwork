#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# CheckNetwork - Network reloader for Ubuntu
# Copyright (c) 2012 - Manuel Joaquin Díaz Pol
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
#==============================================================================
#

import urllib2
import time
from gi.repository import Notify
import commands

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.113.99',timeout=5)
        return True
    except urllib2.URLError as err: pass
    return False

if __name__ == '__main__':
    Notify.init("Check Network")
    print "Init checker"
        
    while(1):
        time.sleep(10)
        if(internet_on() == False):
            commandOut = commands.getoutput("service network-manager restart")
            NotPref = Notify.Notification.new("Check Network",commandOut,"dialog-information")
            NotPref.show()
            time.sleep(20)
            
