"""
SDL_dialog.h
File Dialogs
Document: https://wiki.libsdl.org/SDL3/CategoryDialog
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_FileDialogType
# {
#     SDL_FILEDIALOG_OPENFILE,
#     SDL_FILEDIALOG_SAVEFILE,
#     SDL_FILEDIALOG_OPENFOLDER
# } SDL_FileDialogType;
SDL_FILEDIALOG_OPENFILE = 0
SDL_FILEDIALOG_SAVEFILE = 1
SDL_FILEDIALOG_OPENFOLDER = 2


# typedef struct SDL_DialogFileFilter
# {
#     const char *name;
#     const char *pattern;
# } SDL_DialogFileFilter;
class SDL_DialogFileFilter(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p), ("pattern", ctypes.c_char_p)]


# typedef void (SDLCALL *SDL_DialogFileCallback)(void *userdata, const char * const *filelist, int filter);
SDL_DialogFileCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)), ctypes.c_int
)


# void SDL_ShowFileDialogWithProperties(SDL_FileDialogType type, SDL_DialogFileCallback callback, void *userdata, SDL_PropertiesID props);
SDL_ShowFileDialogWithProperties = libsdl3.SDL_ShowFileDialogWithProperties
SDL_ShowFileDialogWithProperties.argtypes = [
    ctypes.c_int,
    SDL_DialogFileCallback,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_ShowFileDialogWithProperties.restype = None


# void SDL_ShowOpenFileDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const SDL_DialogFileFilter *filters, int nfilters, const char *default_location, bool allow_many);
SDL_ShowOpenFileDialog = libsdl3.SDL_ShowOpenFileDialog
SDL_ShowOpenFileDialog.argtypes = [
    SDL_DialogFileCallback,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.POINTER(SDL_DialogFileFilter),
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_bool,
]
SDL_ShowOpenFileDialog.restype = None


# void SDL_ShowOpenFolderDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const char *default_location, bool allow_many);
SDL_ShowOpenFolderDialog = libsdl3.SDL_ShowOpenFolderDialog
SDL_ShowOpenFolderDialog.argtypes = [
    SDL_DialogFileCallback,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_bool,
]
SDL_ShowOpenFolderDialog.restype = None


# void SDL_ShowSaveFileDialog(SDL_DialogFileCallback callback, void *userdata, SDL_Window *window, const SDL_DialogFileFilter *filters, int nfilters, const char *default_location);
SDL_ShowSaveFileDialog = libsdl3.SDL_ShowSaveFileDialog
SDL_ShowSaveFileDialog.argtypes = [
    SDL_DialogFileCallback,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.POINTER(SDL_DialogFileFilter),
    ctypes.c_int,
    ctypes.c_char_p,
]
SDL_ShowSaveFileDialog.restype = None
