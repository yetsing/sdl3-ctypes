"""
SDL_bits.h
Bit Manipulation
Document: https://wiki.libsdl.org/SDL3/CategoryBits
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# SDL_FORCE_INLINE bool SDL_HasExactlyOneBitSet32(Uint32 x);
SDL_HasExactlyOneBitSet32 = libsdl3.SDL_HasExactlyOneBitSet32
SDL_HasExactlyOneBitSet32.argtypes = [ctypes.c_uint32]
SDL_HasExactlyOneBitSet32.restype = ctypes.c_bool


# SDL_FORCE_INLINE int SDL_MostSignificantBitIndex32(Uint32 x);
SDL_MostSignificantBitIndex32 = libsdl3.SDL_MostSignificantBitIndex32
SDL_MostSignificantBitIndex32.argtypes = [ctypes.c_uint32]
SDL_MostSignificantBitIndex32.restype = ctypes.c_int
