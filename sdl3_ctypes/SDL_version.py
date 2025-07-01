"""
SDL_version.h
Querying SDL Version
Document: https://wiki.libsdl.org/SDL3/CategoryVersion
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_MAJOR_VERSION   3
SDL_MAJOR_VERSION = 3
# #define SDL_MICRO_VERSION   0
SDL_MICRO_VERSION = 0
# #define SDL_MINOR_VERSION   3
SDL_MINOR_VERSION = 3
# #define SDL_REVISION "Some arbitrary string decided at SDL build time"
SDL_REVISION = "Some arbitrary string decided at SDL build time"
# #define SDL_VERSION \
#     SDL_VERSIONNUM(SDL_MAJOR_VERSION, SDL_MINOR_VERSION, SDL_MICRO_VERSION)
SDL_VERSION = SDL_MAJOR_VERSION * 1000000 + SDL_MINOR_VERSION * 1000 + SDL_MICRO_VERSION
# #define SDL_VERSION_ATLEAST(X, Y, Z) \
#     (SDL_VERSION >= SDL_VERSIONNUM(X, Y, Z))
# #define SDL_VERSIONNUM(major, minor, patch) \
#     ((major) * 1000000 + (minor) * 1000 + (patch))
# #define SDL_VERSIONNUM_MAJOR(version) ((version) / 1000000)
# #define SDL_VERSIONNUM_MICRO(version) ((version) % 1000)
# #define SDL_VERSIONNUM_MINOR(version) (((version) / 1000) % 1000)


# const char * SDL_GetRevision(void);
SDL_GetRevision = libsdl3.SDL_GetRevision
SDL_GetRevision.argtypes = []
SDL_GetRevision.restype = ctypes.c_char_p


# int SDL_GetVersion(void);
SDL_GetVersion = libsdl3.SDL_GetVersion
SDL_GetVersion.argtypes = []
SDL_GetVersion.restype = ctypes.c_int
