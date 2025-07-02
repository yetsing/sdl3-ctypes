"""
SDL_timer.h
Timer Support
Document: https://wiki.libsdl.org/SDL3/CategoryTimer
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_MS_PER_SECOND   1000
SDL_MS_PER_SECOND = 0x3E8
# #define SDL_MS_TO_NS(MS)        (((Uint64)(MS)) * SDL_NS_PER_MS)
# #define SDL_NS_PER_MS       1000000
SDL_NS_PER_MS = 0xF4240
# #define SDL_NS_PER_SECOND   1000000000LL
SDL_NS_PER_SECOND = 0x3B9ACA00
# #define SDL_NS_PER_US       1000
SDL_NS_PER_US = 0x3E8
# #define SDL_NS_TO_MS(NS)        ((NS) / SDL_NS_PER_MS)
# #define SDL_NS_TO_SECONDS(NS)   ((NS) / SDL_NS_PER_SECOND)
# #define SDL_NS_TO_US(NS)        ((NS) / SDL_NS_PER_US)
# #define SDL_SECONDS_TO_NS(S)    (((Uint64)(S)) * SDL_NS_PER_SECOND)
# #define SDL_US_PER_SECOND   1000000
SDL_US_PER_SECOND = 0xF4240
# #define SDL_US_TO_NS(US)        (((Uint64)(US)) * SDL_NS_PER_US)


# typedef Uint64 (SDLCALL *SDL_NSTimerCallback)(void *userdata, SDL_TimerID timerID, Uint64 interval);
SDL_NSTimerCallback = ctypes.CFUNCTYPE(
    ctypes.c_uint64, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint64
)


# typedef Uint32 (SDLCALL *SDL_TimerCallback)(void *userdata, SDL_TimerID timerID, Uint32 interval);
SDL_TimerCallback = ctypes.CFUNCTYPE(
    ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32
)

# typedef Uint32 SDL_TimerID;


# SDL_TimerID SDL_AddTimer(Uint32 interval, SDL_TimerCallback callback, void *userdata);
SDL_AddTimer = libsdl3.SDL_AddTimer
SDL_AddTimer.argtypes = [ctypes.c_uint32, SDL_TimerCallback, ctypes.c_void_p]
SDL_AddTimer.restype = ctypes.c_uint32


# SDL_TimerID SDL_AddTimerNS(Uint64 interval, SDL_NSTimerCallback callback, void *userdata);
SDL_AddTimerNS = libsdl3.SDL_AddTimerNS
SDL_AddTimerNS.argtypes = [ctypes.c_uint64, SDL_NSTimerCallback, ctypes.c_void_p]
SDL_AddTimerNS.restype = ctypes.c_uint32


# void SDL_Delay(Uint32 ms);
SDL_Delay = libsdl3.SDL_Delay
SDL_Delay.argtypes = [ctypes.c_uint32]
SDL_Delay.restype = None


# void SDL_DelayNS(Uint64 ns);
SDL_DelayNS = libsdl3.SDL_DelayNS
SDL_DelayNS.argtypes = [ctypes.c_uint64]
SDL_DelayNS.restype = None


# void SDL_DelayPrecise(Uint64 ns);
SDL_DelayPrecise = libsdl3.SDL_DelayPrecise
SDL_DelayPrecise.argtypes = [ctypes.c_uint64]
SDL_DelayPrecise.restype = None


# Uint64 SDL_GetPerformanceCounter(void);
SDL_GetPerformanceCounter = libsdl3.SDL_GetPerformanceCounter
SDL_GetPerformanceCounter.argtypes = []
SDL_GetPerformanceCounter.restype = ctypes.c_uint64


# Uint64 SDL_GetPerformanceFrequency(void);
SDL_GetPerformanceFrequency = libsdl3.SDL_GetPerformanceFrequency
SDL_GetPerformanceFrequency.argtypes = []
SDL_GetPerformanceFrequency.restype = ctypes.c_uint64


# Uint64 SDL_GetTicks(void);
SDL_GetTicks = libsdl3.SDL_GetTicks
SDL_GetTicks.argtypes = []
SDL_GetTicks.restype = ctypes.c_uint64


# Uint64 SDL_GetTicksNS(void);
SDL_GetTicksNS = libsdl3.SDL_GetTicksNS
SDL_GetTicksNS.argtypes = []
SDL_GetTicksNS.restype = ctypes.c_uint64


# bool SDL_RemoveTimer(SDL_TimerID id);
SDL_RemoveTimer = libsdl3.SDL_RemoveTimer
SDL_RemoveTimer.argtypes = [ctypes.c_uint32]
SDL_RemoveTimer.restype = ctypes.c_bool
