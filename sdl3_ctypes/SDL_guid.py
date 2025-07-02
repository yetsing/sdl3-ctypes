"""
SDL_guid.h
GUIDs
Document: https://wiki.libsdl.org/SDL3/CategoryGUID
"""

import ctypes

from sdl3_ctypes.lib import libsdl3


# typedef struct SDL_GUID {
#     Uint8 data[16];
# } SDL_GUID;
class SDL_GUID(ctypes.Structure):
    _fields_ = [("data", ctypes.c_uint8 * 16)]


# void SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);
SDL_GUIDToString = libsdl3.SDL_GUIDToString
SDL_GUIDToString.argtypes = [SDL_GUID, ctypes.c_char_p, ctypes.c_int]
SDL_GUIDToString.restype = None


# SDL_GUID SDL_StringToGUID(const char *pchGUID);
SDL_StringToGUID = libsdl3.SDL_StringToGUID
SDL_StringToGUID.argtypes = [ctypes.c_char_p]
SDL_StringToGUID.restype = SDL_GUID
