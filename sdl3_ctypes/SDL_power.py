"""
SDL_power.h
Power Management Status
Document: https://wiki.libsdl.org/SDL3/CategoryPower
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_PowerState
# {
#     SDL_POWERSTATE_ERROR = -1,   /**< error determining power status */
#     SDL_POWERSTATE_UNKNOWN,      /**< cannot determine power status */
#     SDL_POWERSTATE_ON_BATTERY,   /**< Not plugged in, running on the battery */
#     SDL_POWERSTATE_NO_BATTERY,   /**< Plugged in, no battery available */
#     SDL_POWERSTATE_CHARGING,     /**< Plugged in, charging battery */
#     SDL_POWERSTATE_CHARGED       /**< Plugged in, battery charged */
# } SDL_PowerState;
SDL_POWERSTATE_ERROR = -1
SDL_POWERSTATE_UNKNOWN = 0
SDL_POWERSTATE_ON_BATTERY = 1
SDL_POWERSTATE_NO_BATTERY = 2
SDL_POWERSTATE_CHARGING = 3
SDL_POWERSTATE_CHARGED = 4


# SDL_PowerState SDL_GetPowerInfo(int *seconds, int *percent);
SDL_GetPowerInfo = libsdl3.SDL_GetPowerInfo
SDL_GetPowerInfo.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
SDL_GetPowerInfo.restype = ctypes.c_int
