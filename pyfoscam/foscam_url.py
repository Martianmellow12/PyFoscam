# Foscam Command URLs
#
# List Compiled By Martianmellow12

### Camera Control Variables ###
MOVE_STOP = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=1'
MOVE_LEFT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=6'
MOVE_RIGHT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=4'
MOVE_UP = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=0'
MOVE_DOWN = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=2'
MOVE_UPLEFT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=91'
MOVE_UPRIGHT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=90'
MOVE_DOWNLEFT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=93'
MOVE_DOWNRIGHT = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=92'
MOVE_CENTER = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=25' # FYI, it gets real twisty to find the center, so expect it to take 15-30 seconds

PATROL_VERTICAL_START = 'http://%s:%d/decoder_control.cgi?command=26&user=%s&pwd=%s'
PATROL_VERTICAL_STOP = 'http://%s:%d/decoder_control.cgi?command=27&user=%s&pwd=%s'
PATROL_HORIZONTAL_START = 'http://%s:%d/decoder_control.cgi?command=28&user=%s&pwd=%s'
PATROL_HORIZONTAL_STOP = 'http://%s:%d/decoder_control.cgi?command=29&user=%s&pwd=%s'

SET_RES_320X240 = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=0&value=8'
SET_RES_640X480 = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=0&value=32'
SET_FLIP_ON = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=5&value=1'
SET_FLIP_OFF = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=5&value=0'
SET_MIRROR_ON = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=5&value=2'
SET_MIRROR_OFF = 'http://%s:%d/camera_control.cgi?user=%s&pwd=%s&param=5&value=0'
SET_IR_ON = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=95'
SET_IR_OFF = 'http://%s:%d/decoder_control.cgi?user=%s&pwd=%s&command=94'

GET_SNAPSHOT = 'http://%s:%d/snapshot.cgi?user=%s&pwd=%s'
DO_REBOOT = 'http://%s:%d/reboot.cgi?user=%s&pwd=%s'
################################

### Preset Variables ###
SET_PRESET_1 = 'http://%s:%d/decoder_control.cgi?command=30&user=%s&pwd=%s'

GO_PRESET_1 = 'http://%s:%d/decoder_control.cgi?command=31&user=%s&pwd=%s'
########################

### Login Variables ###
LOGIN_CHECK = 'http://%s:%d/check_user2.cgi?user=%s&pwd=%s'
LOGIN_SUCCESS = 'var pri=3;'
LOGIN_FAIL = 'var pri=0;'
#######################

### Info Variables ###
GET_STATUS = 'http://%s:%d/get_status.cgi?user=%s&pwd=%s'
GET_PARAMS = 'http://%s:%d/get_params.cgi?user=%s&pwd=%s'
GET_MISC = 'http://%s:%d/get_misc.cgi?user=%s&pwd=%s'
GET_FACTORY_DDNS = 'http://%s:%d/get_factory_ddns.cgi?user=%s&pwd=%s'
######################

### Wifi Scan Variables ###
WIFI_SCAN = 'http://%s:%d/wifi_scan.cgi?user=%s&pwd=%s'
GET_WIFI_SCAN = 'http://%s:%d/get_wifi_scan_result.cgi?user=%s&pwd=%s'
###########################
