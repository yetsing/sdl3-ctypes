"""
SDL_locale.h
Locale Info
Document: https://wiki.libsdl.org/SDL3/CategoryLocale
"""

import ctypes

from sdl3_ctypes.lib import libsdl3


# typedef struct SDL_Locale
# {
#     const char *language;  /**< A language name, like "en" for English. */
#     const char *country;  /**< A country, like "US" for America. Can be NULL. */
# } SDL_Locale;
class SDL_Locale(ctypes.Structure):
    _fields_ = [("language", ctypes.c_char_p), ("country", ctypes.c_char_p)]


# SDL_Locale ** SDL_GetPreferredLocales(int *count);
SDL_GetPreferredLocales = libsdl3.SDL_GetPreferredLocales
SDL_GetPreferredLocales.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetPreferredLocales.restype = ctypes.POINTER(ctypes.POINTER(SDL_Locale))
