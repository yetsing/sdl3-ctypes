"""
SDL_storage.h
Storage Abstraction
Document: https://wiki.libsdl.org/SDL3/CategoryStorage
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_filesystem import SDL_EnumerateDirectoryCallback, SDL_PathInfo


# typedef struct SDL_StorageInterface
# {
#     /* The version of this interface */
#     Uint32 version;
#     /* Called when the storage is closed */
#     bool (SDLCALL *close)(void *userdata);
#     /* Optional, returns whether the storage is currently ready for access */
#     bool (SDLCALL *ready)(void *userdata);
#     /* Enumerate a directory, optional for write-only storage */
#     bool (SDLCALL *enumerate)(void *userdata, const char *path, SDL_EnumerateDirectoryCallback callback, void *callback_userdata);
#     /* Get path information, optional for write-only storage */
#     bool (SDLCALL *info)(void *userdata, const char *path, SDL_PathInfo *info);
#     /* Read a file from storage, optional for write-only storage */
#     bool (SDLCALL *read_file)(void *userdata, const char *path, void *destination, Uint64 length);
#     /* Write a file to storage, optional for read-only storage */
#     bool (SDLCALL *write_file)(void *userdata, const char *path, const void *source, Uint64 length);
#     /* Create a directory, optional for read-only storage */
#     bool (SDLCALL *mkdir)(void *userdata, const char *path);
#     /* Remove a file or empty directory, optional for read-only storage */
#     bool (SDLCALL *remove)(void *userdata, const char *path);
#     /* Rename a path, optional for read-only storage */
#     bool (SDLCALL *rename)(void *userdata, const char *oldpath, const char *newpath);
#     /* Copy a file, optional for read-only storage */
#     bool (SDLCALL *copy)(void *userdata, const char *oldpath, const char *newpath);
#     /* Get the space remaining, optional for read-only storage */
#     Uint64 (SDLCALL *space_remaining)(void *userdata);
# } SDL_StorageInterface;
class SDL_StorageInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        ("ready", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        (
            "enumerate",
            ctypes.CFUNCTYPE(
                ctypes.c_bool,
                ctypes.c_void_p,
                ctypes.c_char_p,
                SDL_EnumerateDirectoryCallback,
                ctypes.c_void_p,
            ),
        ),
        (
            "info",
            ctypes.CFUNCTYPE(
                ctypes.c_bool,
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.POINTER(SDL_PathInfo),
            ),
        ),
        (
            "read_file",
            ctypes.CFUNCTYPE(
                ctypes.c_bool,
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_void_p,
                ctypes.c_uint64,
            ),
        ),
        (
            "write_file",
            ctypes.CFUNCTYPE(
                ctypes.c_bool,
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_void_p,
                ctypes.c_uint64,
            ),
        ),
        ("mkdir", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        ("remove", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        (
            "rename",
            ctypes.CFUNCTYPE(
                ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p
            ),
        ),
        (
            "copy",
            ctypes.CFUNCTYPE(
                ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p
            ),
        ),
        ("space_remaining", ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_void_p)),
    ]


# typedef struct SDL_Storage SDL_Storage;


# bool SDL_CloseStorage(SDL_Storage *storage);
SDL_CloseStorage = libsdl3.SDL_CloseStorage
SDL_CloseStorage.argtypes = [ctypes.c_void_p]
SDL_CloseStorage.restype = ctypes.c_bool


# bool SDL_CopyStorageFile(SDL_Storage *storage, const char *oldpath, const char *newpath);
SDL_CopyStorageFile = libsdl3.SDL_CopyStorageFile
SDL_CopyStorageFile.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
SDL_CopyStorageFile.restype = ctypes.c_bool


# bool SDL_CreateStorageDirectory(SDL_Storage *storage, const char *path);
SDL_CreateStorageDirectory = libsdl3.SDL_CreateStorageDirectory
SDL_CreateStorageDirectory.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_CreateStorageDirectory.restype = ctypes.c_bool


# bool SDL_EnumerateStorageDirectory(SDL_Storage *storage, const char *path, SDL_EnumerateDirectoryCallback callback, void *userdata);
SDL_EnumerateStorageDirectory = libsdl3.SDL_EnumerateStorageDirectory
SDL_EnumerateStorageDirectory.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    SDL_EnumerateDirectoryCallback,
    ctypes.c_void_p,
]
SDL_EnumerateStorageDirectory.restype = ctypes.c_bool


# bool SDL_GetStorageFileSize(SDL_Storage *storage, const char *path, Uint64 *length);
SDL_GetStorageFileSize = libsdl3.SDL_GetStorageFileSize
SDL_GetStorageFileSize.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_uint64),
]
SDL_GetStorageFileSize.restype = ctypes.c_bool


# bool SDL_GetStoragePathInfo(SDL_Storage *storage, const char *path, SDL_PathInfo *info);
SDL_GetStoragePathInfo = libsdl3.SDL_GetStoragePathInfo
SDL_GetStoragePathInfo.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.POINTER(SDL_PathInfo),
]
SDL_GetStoragePathInfo.restype = ctypes.c_bool


# Uint64 SDL_GetStorageSpaceRemaining(SDL_Storage *storage);
SDL_GetStorageSpaceRemaining = libsdl3.SDL_GetStorageSpaceRemaining
SDL_GetStorageSpaceRemaining.argtypes = [ctypes.c_void_p]
SDL_GetStorageSpaceRemaining.restype = ctypes.c_uint64


# char ** SDL_GlobStorageDirectory(SDL_Storage *storage, const char *path, const char *pattern, SDL_GlobFlags flags, int *count);
SDL_GlobStorageDirectory = libsdl3.SDL_GlobStorageDirectory
SDL_GlobStorageDirectory.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_int),
]
SDL_GlobStorageDirectory.restype = ctypes.POINTER(ctypes.c_char_p)


# SDL_Storage * SDL_OpenFileStorage(const char *path);
SDL_OpenFileStorage = libsdl3.SDL_OpenFileStorage
SDL_OpenFileStorage.argtypes = [ctypes.c_char_p]
SDL_OpenFileStorage.restype = ctypes.c_void_p


# SDL_Storage * SDL_OpenStorage(const SDL_StorageInterface *iface, void *userdata);
SDL_OpenStorage = libsdl3.SDL_OpenStorage
SDL_OpenStorage.argtypes = [ctypes.POINTER(SDL_StorageInterface), ctypes.c_void_p]
SDL_OpenStorage.restype = ctypes.c_void_p


# SDL_Storage * SDL_OpenTitleStorage(const char *override, SDL_PropertiesID props);
SDL_OpenTitleStorage = libsdl3.SDL_OpenTitleStorage
SDL_OpenTitleStorage.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
SDL_OpenTitleStorage.restype = ctypes.c_void_p


# SDL_Storage * SDL_OpenUserStorage(const char *org, const char *app, SDL_PropertiesID props);
SDL_OpenUserStorage = libsdl3.SDL_OpenUserStorage
SDL_OpenUserStorage.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32]
SDL_OpenUserStorage.restype = ctypes.c_void_p


# bool SDL_ReadStorageFile(SDL_Storage *storage, const char *path, void *destination, Uint64 length);
SDL_ReadStorageFile = libsdl3.SDL_ReadStorageFile
SDL_ReadStorageFile.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_void_p,
    ctypes.c_uint64,
]
SDL_ReadStorageFile.restype = ctypes.c_bool


# bool SDL_RemoveStoragePath(SDL_Storage *storage, const char *path);
SDL_RemoveStoragePath = libsdl3.SDL_RemoveStoragePath
SDL_RemoveStoragePath.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_RemoveStoragePath.restype = ctypes.c_bool


# bool SDL_RenameStoragePath(SDL_Storage *storage, const char *oldpath, const char *newpath);
SDL_RenameStoragePath = libsdl3.SDL_RenameStoragePath
SDL_RenameStoragePath.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
SDL_RenameStoragePath.restype = ctypes.c_bool


# bool SDL_StorageReady(SDL_Storage *storage);
SDL_StorageReady = libsdl3.SDL_StorageReady
SDL_StorageReady.argtypes = [ctypes.c_void_p]
SDL_StorageReady.restype = ctypes.c_bool


# bool SDL_WriteStorageFile(SDL_Storage *storage, const char *path, const void *source, Uint64 length);
SDL_WriteStorageFile = libsdl3.SDL_WriteStorageFile
SDL_WriteStorageFile.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_void_p,
    ctypes.c_uint64,
]
SDL_WriteStorageFile.restype = ctypes.c_bool
