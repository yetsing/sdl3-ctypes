"""
SDL_misc.h
Miscellaneous
Document: https://wiki.libsdl.org/SDL3/CategoryMisc
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# bool SDL_OpenURL(const char *url);
SDL_OpenURL = libsdl3.SDL_OpenURL
SDL_OpenURL.argtypes = [ctypes.c_char_p]
SDL_OpenURL.restype = ctypes.c_bool
