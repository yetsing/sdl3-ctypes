"""
SDL_touch.h
Touch Support
Document: https://wiki.libsdl.org/SDL3/CategoryTouch
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_MOUSE_TOUCHID ((SDL_TouchID)-1)
# #define SDL_TOUCH_MOUSEID ((SDL_MouseID)-1)


# typedef enum SDL_TouchDeviceType
# {
#     SDL_TOUCH_DEVICE_INVALID = -1,
#     SDL_TOUCH_DEVICE_DIRECT,            /**< touch screen with window-relative coordinates */
#     SDL_TOUCH_DEVICE_INDIRECT_ABSOLUTE, /**< trackpad with absolute device coordinates */
#     SDL_TOUCH_DEVICE_INDIRECT_RELATIVE  /**< trackpad with screen cursor-relative coordinates */
# } SDL_TouchDeviceType;
SDL_TOUCH_DEVICE_INVALID = -1
SDL_TOUCH_DEVICE_DIRECT = 0
SDL_TOUCH_DEVICE_INDIRECT_ABSOLUTE = 1
SDL_TOUCH_DEVICE_INDIRECT_RELATIVE = 2


# typedef struct SDL_Finger
# {
#     SDL_FingerID id;  /**< the finger ID */
#     float x;  /**< the x-axis location of the touch event, normalized (0...1) */
#     float y;  /**< the y-axis location of the touch event, normalized (0...1) */
#     float pressure; /**< the quantity of pressure applied, normalized (0...1) */
# } SDL_Finger;
class SDL_Finger(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint64),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("pressure", ctypes.c_float),
    ]


# typedef Uint64 SDL_FingerID;
# typedef Uint64 SDL_TouchID;


# const char * SDL_GetTouchDeviceName(SDL_TouchID touchID);
SDL_GetTouchDeviceName = libsdl3.SDL_GetTouchDeviceName
SDL_GetTouchDeviceName.argtypes = [ctypes.c_uint64]
SDL_GetTouchDeviceName.restype = ctypes.c_char_p


# SDL_TouchID * SDL_GetTouchDevices(int *count);
SDL_GetTouchDevices = libsdl3.SDL_GetTouchDevices
SDL_GetTouchDevices.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetTouchDevices.restype = ctypes.POINTER(ctypes.c_uint64)


# SDL_TouchDeviceType SDL_GetTouchDeviceType(SDL_TouchID touchID);
SDL_GetTouchDeviceType = libsdl3.SDL_GetTouchDeviceType
SDL_GetTouchDeviceType.argtypes = [ctypes.c_uint64]
SDL_GetTouchDeviceType.restype = ctypes.c_int


# SDL_Finger ** SDL_GetTouchFingers(SDL_TouchID touchID, int *count);
SDL_GetTouchFingers = libsdl3.SDL_GetTouchFingers
SDL_GetTouchFingers.argtypes = [ctypes.c_uint64, ctypes.POINTER(ctypes.c_int)]
SDL_GetTouchFingers.restype = ctypes.POINTER(ctypes.POINTER(SDL_Finger))
