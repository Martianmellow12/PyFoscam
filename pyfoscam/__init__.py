# PyFoscam Library
#
# Written By Martianmellow12
import urllib2
import time
import foscam_url

#
#
#
#
#
# FoscamException
class FoscamException(Exception):
    pass
#
#
#
#
#
# Foscam Class
class Foscam(object):

    def __init__(self, ip, port, username, password):
        self.login = (ip, port, username, password)
        if not self.checkLogin():
            raise FoscamException('Invalid login information')

    def checkLogin(self):
        response = urllib2.urlopen(foscam_url.LOGIN_CHECK % self.login).read()
        if response == foscam_url.LOGIN_SUCCESS:
            return True
        elif response == foscam_url.LOGIN_FAIL:
            return False
        else:
            raise FoscamException('Unrecognized login check response: <%s>' % response)

    # Info Functions
    #
    # Return device information
    def getStatus(self):
        status_dict = {}
        status_data = urllib2.urlopen(foscam_url.GET_STATUS % self.login).read()
        status_list = status_data.split(';\n')
        for i in range(0, len(status_list)):
            if status_list[i] == '':
                continue
            status_list[i] = status_list[i].replace('var ', '')
            status_item = status_list[i].split('=')
            status_dict[status_item[0]] = status_item[1].strip("'")
        return status_dict

    def getParams(self):
        params_dict = {}
        params_data = urllib2.urlopen(foscam_url.GET_PARAMS % self.login).read()
        params_list = params_data.split(';\n')
        for i in range(0, len(params_list)):
            if params_list[i] == '':
                continue
            params_list[i] = params_list[i].replace('var ', '')
            params_item = params_list[i].split('=')
            params_dict[params_item[0]] = params_item[1].strip("'")
        return params_dict

    def getMisc(self):
        misc_dict = {}
        misc_data = urllib2.urlopen(foscam_url.GET_MISC % self.login).read()
        misc_list = misc_data.split(';\n')
        for i in range(0, len(misc_list)):
            if misc_list[i] == '':
                continue
            misc_list[i] = misc_list[i].replace('var ', '')
            misc_item = misc_list[i].split('=')
            misc_dict[misc_item[0]] = misc_item[1].strip("'")
        return misc_dict
        
    # Movement Functions
    #
    # Note that it will keep moving until stopped
    def moveStop(self):
        resp = urllib2.urlopen(foscam_url.MOVE_STOP % self.login).read()
        return resp
    
    def moveUp(self):
        resp = urllib2.urlopen(foscam_url.MOVE_UP % self.login).read()
        return resp

    def moveDown(self):
        resp = urllib2.urlopen(foscam_url.MOVE_DOWN % self.login).read()
        return resp

    def moveLeft(self):
        resp = urllib2.urlopen(foscam_url.MOVE_LEFT % self.login).read()
        return resp

    def moveRight(self):
        resp = urllib2.urlopen(foscam_url.MOVE_RIGHT % self.login).read()
        return resp

    def moveCenter(self):
        resp = urllib2.urlopen(foscam_url.MOVE_CENTER % self.login).read()
        return resp

    def patrolVerticalConfig(self, active):
        if active:
            resp = urllib2.urlopen(foscam_url.PATROL_VERTICAL_START % self.login).read()
        else:
            resp = urllib2.urlopen(foscam_url.PATROL_VERTICAL_STOP % self.login).read()
        return resp

    def patrolHorizontalConfig(self, active):
        if active:
            resp = urllib2.urlopen(foscam_url.PATROL_HORIZONTAL_START % self.login).read()
        else:
            resp = urllib2.urlopen(foscam_url.PATROL_HORIZONTAL_STOP % self.login).read()
        return resp

    def setPreset1(self):
        resp = urllib2.urlopen(foscam_url.SET_PRESET_1 % self.login).read()
        return resp

    def goPreset1(self):
        resp = urllib2.urlopen(foscam_url.GO_PRESET_1 % self.login).read()
        return resp
    
    # IR Control Functions
    #
    # Used to control night vision
    def irConfig(self, active):
        if active:
            resp = urllib2.urlopen(foscam_url.SET_IR_ON % self.login).read()
        else:
            resp = urllib2.urlopen(foscam_url.SET_IR_OFF % self.login).read()
        return resp

    # Image Configuration Functions
    #
    # Used to configure how the camera sees
    def setRes320x240(self):
        resp = urllib2.urlopen(foscam_url.SET_RES_320X240 % self.login).read()
        return resp

    def setRes640x480(self):
        resp = urllib2.urlopen(foscam_url.SET_RES_640X480 % self.login).read()
        return resp

    def flipConfig(self, active):
        if active:
            resp = urllib2.urlopen(foscam_url.SET_FLIP_ON % self.login).read()
        else:
            resp = urllib2.urlopen(foscam_url.SET_FLIP_OFF % self.login).read()
        return resp

    def mirrorConfig(self, active):
        if active:
            resp = urllib2.urlopen(foscam_url.SET_MIRROR_ON % self.login).read()
        else:
            resp = urllib2.urlopen(foscam_url.SET_MIRROR_OFF % self.login).read()
        return resp

    # Get Snapshot Function
    #
    # Get what the camera is currently seeing as a jpeg image
    def getSnapshot(self, image_file='image.jpg'):
        image_data = urllib2.urlopen(foscam_url.GET_SNAPSHOT % self.login).read()
        fileout = open(image_file, 'wb')
        fileout.write(image_data)
        fileout.close()
        return True

    # Misc. Functions
    #
    # Functions that didn't really fit into any categories
    def wifiScan(self):
        resp = urllib2.urlopen(foscam_url.WIFI_SCAN % self.login).read()
        wifi_scan_data = urllib2.urlopen(foscam_url.GET_WIFI_SCAN % self.login).read()
        return wifi_scan_data

    def reboot(self, delay=30, retries=3):
        resp = urllib2.urlopen(foscam_url.DO_REBOOT % self.login).read()
        time.sleep(delay)

        for i in range(0, retries):
            try:
                result = self.checkLogin()
            except urllib2.URLError:
                pass
            else:
                return result
        return False
