"""
SDL_clipboard.h
Clipboard Handling
Document: https://wiki.libsdl.org/SDL3/CategoryClipboard
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef void (SDLCALL *SDL_ClipboardCleanupCallback)(void *userdata);
SDL_ClipboardCleanupCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)


# typedef const void *(SDLCALL *SDL_ClipboardDataCallback)(void *userdata, const char *mime_type, size_t *size);
SDL_ClipboardDataCallback = ctypes.CFUNCTYPE(
    ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)
)


# bool SDL_ClearClipboardData(void);
SDL_ClearClipboardData = libsdl3.SDL_ClearClipboardData
SDL_ClearClipboardData.argtypes = []
SDL_ClearClipboardData.restype = ctypes.c_bool


# void * SDL_GetClipboardData(const char *mime_type, size_t *size);
SDL_GetClipboardData = libsdl3.SDL_GetClipboardData
SDL_GetClipboardData.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)]
SDL_GetClipboardData.restype = ctypes.c_void_p


# char ** SDL_GetClipboardMimeTypes(size_t *num_mime_types);
SDL_GetClipboardMimeTypes = libsdl3.SDL_GetClipboardMimeTypes
SDL_GetClipboardMimeTypes.argtypes = [ctypes.POINTER(ctypes.c_size_t)]
SDL_GetClipboardMimeTypes.restype = ctypes.POINTER(ctypes.c_char_p)


# char * SDL_GetClipboardText(void);
SDL_GetClipboardText = libsdl3.SDL_GetClipboardText
SDL_GetClipboardText.argtypes = []
SDL_GetClipboardText.restype = ctypes.c_char_p


# char * SDL_GetPrimarySelectionText(void);
SDL_GetPrimarySelectionText = libsdl3.SDL_GetPrimarySelectionText
SDL_GetPrimarySelectionText.argtypes = []
SDL_GetPrimarySelectionText.restype = ctypes.c_char_p


# bool SDL_HasClipboardData(const char *mime_type);
SDL_HasClipboardData = libsdl3.SDL_HasClipboardData
SDL_HasClipboardData.argtypes = [ctypes.c_char_p]
SDL_HasClipboardData.restype = ctypes.c_bool


# bool SDL_HasClipboardText(void);
SDL_HasClipboardText = libsdl3.SDL_HasClipboardText
SDL_HasClipboardText.argtypes = []
SDL_HasClipboardText.restype = ctypes.c_bool


# bool SDL_HasPrimarySelectionText(void);
SDL_HasPrimarySelectionText = libsdl3.SDL_HasPrimarySelectionText
SDL_HasPrimarySelectionText.argtypes = []
SDL_HasPrimarySelectionText.restype = ctypes.c_bool


# bool SDL_SetClipboardData(SDL_ClipboardDataCallback callback, SDL_ClipboardCleanupCallback cleanup, void *userdata, const char **mime_types, size_t num_mime_types);
SDL_SetClipboardData = libsdl3.SDL_SetClipboardData
SDL_SetClipboardData.argtypes = [
    SDL_ClipboardDataCallback,
    SDL_ClipboardCleanupCallback,
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.c_size_t,
]
SDL_SetClipboardData.restype = ctypes.c_bool


# bool SDL_SetClipboardText(const char *text);
SDL_SetClipboardText = libsdl3.SDL_SetClipboardText
SDL_SetClipboardText.argtypes = [ctypes.c_char_p]
SDL_SetClipboardText.restype = ctypes.c_bool


# bool SDL_SetPrimarySelectionText(const char *text);
SDL_SetPrimarySelectionText = libsdl3.SDL_SetPrimarySelectionText
SDL_SetPrimarySelectionText.argtypes = [ctypes.c_char_p]
SDL_SetPrimarySelectionText.restype = ctypes.c_bool
