"""
SDL_metal.h
Metal Support
Document: https://wiki.libsdl.org/SDL3/CategoryMetal
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef void *SDL_MetalView;


# SDL_MetalView SDL_Metal_CreateView(SDL_Window *window);
SDL_Metal_CreateView = libsdl3.SDL_Metal_CreateView
SDL_Metal_CreateView.argtypes = [ctypes.c_void_p]
SDL_Metal_CreateView.restype = ctypes.c_void_p


# void SDL_Metal_DestroyView(SDL_MetalView view);
SDL_Metal_DestroyView = libsdl3.SDL_Metal_DestroyView
SDL_Metal_DestroyView.argtypes = [ctypes.c_void_p]
SDL_Metal_DestroyView.restype = None


# void * SDL_Metal_GetLayer(SDL_MetalView view);
SDL_Metal_GetLayer = libsdl3.SDL_Metal_GetLayer
SDL_Metal_GetLayer.argtypes = [ctypes.c_void_p]
SDL_Metal_GetLayer.restype = ctypes.c_void_p
