"""
SDL_main.h
Application entry points
Document: https://wiki.libsdl.org/SDL3/CategoryMain
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_init import (
    SDL_AppEvent_func,
    SDL_AppInit_func,
    SDL_AppIterate_func,
    SDL_AppQuit_func,
)

# #define SDL_MAIN_HANDLED 1
SDL_MAIN_HANDLED = 1
# #define SDL_MAIN_USE_CALLBACKS 1
SDL_MAIN_USE_CALLBACKS = 1


# typedef int (SDLCALL *SDL_main_func)(int argc, char *argv[]);
SDL_main_func = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)
)


# int SDL_EnterAppMainCallbacks(int argc, char *argv[], SDL_AppInit_func appinit, SDL_AppIterate_func appiter, SDL_AppEvent_func appevent, SDL_AppQuit_func appquit);
SDL_EnterAppMainCallbacks = libsdl3.SDL_EnterAppMainCallbacks
SDL_EnterAppMainCallbacks.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_char_p),
    SDL_AppInit_func,
    SDL_AppIterate_func,
    SDL_AppEvent_func,
    SDL_AppQuit_func,
]
SDL_EnterAppMainCallbacks.restype = ctypes.c_int

# void SDL_GDKSuspendComplete(void);
SDL_GDKSuspendComplete = libsdl3.SDL_GDKSuspendComplete
SDL_GDKSuspendComplete.argtypes = []
SDL_GDKSuspendComplete.restype = None

# bool SDL_RegisterApp(const char *name, Uint32 style, void *hInst);
SDL_RegisterApp = libsdl3.SDL_RegisterApp
SDL_RegisterApp.argtypes = [ctypes.c_char_p, ctypes.c_uint32, ctypes.c_void_p]
SDL_RegisterApp.restype = ctypes.c_bool

# int SDL_RunApp(int argc, char *argv[], SDL_main_func mainFunction, void *reserved);
SDL_RunApp = libsdl3.SDL_RunApp
SDL_RunApp.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_char_p),
    SDL_main_func,
    ctypes.c_void_p,
]
SDL_RunApp.restype = ctypes.c_int

# void SDL_SetMainReady(void);
SDL_SetMainReady = libsdl3.SDL_SetMainReady
SDL_SetMainReady.argtypes = []
SDL_SetMainReady.restype = None

# void SDL_UnregisterApp(void);
SDL_UnregisterApp = libsdl3.SDL_UnregisterApp
SDL_UnregisterApp.argtypes = []
SDL_UnregisterApp.restype = None
