"""
SDL_loadso.h
Shared Object/DLL Management
Document: https://wiki.libsdl.org/SDL3/CategorySharedObject
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_stdinc import SDL_FunctionPointer

# typedef struct SDL_SharedObject SDL_SharedObject;


# SDL_FunctionPointer SDL_LoadFunction(SDL_SharedObject *handle, const char *name);
SDL_LoadFunction = libsdl3.SDL_LoadFunction
SDL_LoadFunction.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_LoadFunction.restype = SDL_FunctionPointer


# SDL_SharedObject * SDL_LoadObject(const char *sofile);
SDL_LoadObject = libsdl3.SDL_LoadObject
SDL_LoadObject.argtypes = [ctypes.c_char_p]
SDL_LoadObject.restype = ctypes.c_void_p


# void SDL_UnloadObject(SDL_SharedObject *handle);
SDL_UnloadObject = libsdl3.SDL_UnloadObject
SDL_UnloadObject.argtypes = [ctypes.c_void_p]
SDL_UnloadObject.restype = None
