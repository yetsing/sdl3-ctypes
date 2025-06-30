"""
SDL_error.h
Error Handling
Document: https://wiki.libsdl.org/SDL3/CategoryError
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_InvalidParamError(param)    SDL_SetError("Parameter '%s' is invalid", (param))
# #define SDL_Unsupported()               SDL_SetError("That operation is not supported")


# bool SDL_ClearError(void);
SDL_ClearError = libsdl3.SDL_ClearError
SDL_ClearError.argtypes = []
SDL_ClearError.restype = ctypes.c_bool


# const char * SDL_GetError(void);
SDL_GetError = libsdl3.SDL_GetError
SDL_GetError.argtypes = []
SDL_GetError.restype = ctypes.c_char_p


# bool SDL_OutOfMemory(void);
SDL_OutOfMemory = libsdl3.SDL_OutOfMemory
SDL_OutOfMemory.argtypes = []
SDL_OutOfMemory.restype = ctypes.c_bool

# bool SDL_SetError(const char *fmt, ...);
# bool SDL_SetErrorV(const char *fmt, va_list ap);
