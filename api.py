import os, ctypes
from ctypes import *

_API_DIR = '/home/pi/HROS2/HROS1-Framework/Linux/project/api_wrapper2/api_wrapper2'
os.chdir(_API_DIR)

_apiwrapper = CDLL(os.path.join(_API_DIR, 'apiwrapper.so'))

Initialize = _apiwrapper.InitializeJS
Initialize.argtypes = []
Initialize.restype = c_bool
ServoShutdown = _apiwrapper.ServoShutdownJS
ServoShutdown.argtypes = []
ServoShutdown.restype = None
ServoStartup = _apiwrapper.ServoStartupJS
ServoStartup.argtypes = []
ServoStartup.restype = None
PlayAction = _apiwrapper.PlayActionJS
PlayAction.argtypes = [c_int]
PlayAction.restype = c_int
Walk = _apiwrapper.WalkJS
Walk.argtypes = [c_bool]
Walk.restype = None
Walking = _apiwrapper.WalkingJS
Walking.argtypes = [c_int, c_int]
Walking.restype = None
WalkMove = _apiwrapper.WalkMoveJS
WalkMove.argtypes = [c_double]
WalkMove.restype = None
WalkTurn = _apiwrapper.WalkTurnJS
WalkTurn.argtypes = [c_double]
WalkTurn.restype = None
CheckServos = _apiwrapper.CheckServosJS
CheckServos.argtypes = []
CheckServos.restype = c_int
BatteryVoltLevel = _apiwrapper.BatteryVoltLevelJS
BatteryVoltLevel.argtypes = []
BatteryVoltLevel.restype = c_int
SetMotorValue = _apiwrapper.SetMotorValueJS
SetMotorValue.argtypes = [c_int, c_int]
SetMotorValue.restype = None
GetMotorValue = _apiwrapper.GetMotorValueJS
GetMotorValue.argtypes = [c_int]
GetMotorValue.restype = c_int
