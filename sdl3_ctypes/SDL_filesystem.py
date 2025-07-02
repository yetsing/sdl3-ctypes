"""
SDL_filesystem.h
Filesystem Access
Document: https://wiki.libsdl.org/SDL3/CategoryFilesystem
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_EnumerationResult
# {
#     SDL_ENUM_CONTINUE,   /**< Value that requests that enumeration continue. */
#     SDL_ENUM_SUCCESS,    /**< Value that requests that enumeration stop, successfully. */
#     SDL_ENUM_FAILURE     /**< Value that requests that enumeration stop, as a failure. */
# } SDL_EnumerationResult;
SDL_ENUM_CONTINUE = 0
SDL_ENUM_SUCCESS = 1
SDL_ENUM_FAILURE = 2
# typedef enum SDL_Folder
# {
#     SDL_FOLDER_HOME,        /**< The folder which contains all of the current user's data, preferences, and documents. It usually contains most of the other folders. If a requested folder does not exist, the home folder can be considered a safe fallback to store a user's documents. */
#     SDL_FOLDER_DESKTOP,     /**< The folder of files that are displayed on the desktop. Note that the existence of a desktop folder does not guarantee that the system does show icons on its desktop; certain GNU/Linux distros with a graphical environment may not have desktop icons. */
#     SDL_FOLDER_DOCUMENTS,   /**< User document files, possibly application-specific. This is a good place to save a user's projects. */
#     SDL_FOLDER_DOWNLOADS,   /**< Standard folder for user files downloaded from the internet. */
#     SDL_FOLDER_MUSIC,       /**< Music files that can be played using a standard music player (mp3, ogg...). */
#     SDL_FOLDER_PICTURES,    /**< Image files that can be displayed using a standard viewer (png, jpg...). */
#     SDL_FOLDER_PUBLICSHARE, /**< Files that are meant to be shared with other users on the same computer. */
#     SDL_FOLDER_SAVEDGAMES,  /**< Save files for games. */
#     SDL_FOLDER_SCREENSHOTS, /**< Application screenshots. */
#     SDL_FOLDER_TEMPLATES,   /**< Template files to be used when the user requests the desktop environment to create a new file in a certain folder, such as "New Text File.txt".  Any file in the Templates folder can be used as a starting point for a new file. */
#     SDL_FOLDER_VIDEOS,      /**< Video files that can be played using a standard video player (mp4, webm...). */
#     SDL_FOLDER_COUNT        /**< Total number of types in this enum, not a folder type by itself. */
# } SDL_Folder;
SDL_FOLDER_HOME = 0
SDL_FOLDER_DESKTOP = 1
SDL_FOLDER_DOCUMENTS = 2
SDL_FOLDER_DOWNLOADS = 3
SDL_FOLDER_MUSIC = 4
SDL_FOLDER_PICTURES = 5
SDL_FOLDER_PUBLICSHARE = 6
SDL_FOLDER_SAVEDGAMES = 7
SDL_FOLDER_SCREENSHOTS = 8
SDL_FOLDER_TEMPLATES = 9
SDL_FOLDER_VIDEOS = 10
SDL_FOLDER_COUNT = 11
# typedef enum SDL_PathType
# {
#     SDL_PATHTYPE_NONE,      /**< path does not exist */
#     SDL_PATHTYPE_FILE,      /**< a normal file */
#     SDL_PATHTYPE_DIRECTORY, /**< a directory */
#     SDL_PATHTYPE_OTHER      /**< something completely different like a device node (not a symlink, those are always followed) */
# } SDL_PathType;
SDL_PATHTYPE_NONE = 0
SDL_PATHTYPE_FILE = 1
SDL_PATHTYPE_DIRECTORY = 2
SDL_PATHTYPE_OTHER = 3


# typedef struct SDL_PathInfo
# {
#     SDL_PathType type;      /**< the path type */
#     Uint64 size;            /**< the file size in bytes */
#     SDL_Time create_time;   /**< the time when the path was created */
#     SDL_Time modify_time;   /**< the last time the path was modified */
#     SDL_Time access_time;   /**< the last time the path was read */
# } SDL_PathInfo;
class SDL_PathInfo(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("size", ctypes.c_uint64),
        ("create_time", ctypes.c_int64),
        ("modify_time", ctypes.c_int64),
        ("access_time", ctypes.c_int64),
    ]


# typedef SDL_EnumerationResult (SDLCALL *SDL_EnumerateDirectoryCallback)(void *userdata, const char *dirname, const char *fname);
SDL_EnumerateDirectoryCallback = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p
)

# typedef Uint32 SDL_GlobFlags;
# #define SDL_GLOB_CASEINSENSITIVE (1u << 0)
SDL_GLOB_CASEINSENSITIVE = 0x1


# bool SDL_CopyFile(const char *oldpath, const char *newpath);
SDL_CopyFile = libsdl3.SDL_CopyFile
SDL_CopyFile.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_CopyFile.restype = ctypes.c_bool


# bool SDL_CreateDirectory(const char *path);
SDL_CreateDirectory = libsdl3.SDL_CreateDirectory
SDL_CreateDirectory.argtypes = [ctypes.c_char_p]
SDL_CreateDirectory.restype = ctypes.c_bool


# bool SDL_EnumerateDirectory(const char *path, SDL_EnumerateDirectoryCallback callback, void *userdata);
SDL_EnumerateDirectory = libsdl3.SDL_EnumerateDirectory
SDL_EnumerateDirectory.argtypes = [
    ctypes.c_char_p,
    SDL_EnumerateDirectoryCallback,
    ctypes.c_void_p,
]
SDL_EnumerateDirectory.restype = ctypes.c_bool


# const char * SDL_GetBasePath(void);
SDL_GetBasePath = libsdl3.SDL_GetBasePath
SDL_GetBasePath.argtypes = []
SDL_GetBasePath.restype = ctypes.c_char_p


# char * SDL_GetCurrentDirectory(void);
SDL_GetCurrentDirectory = libsdl3.SDL_GetCurrentDirectory
SDL_GetCurrentDirectory.argtypes = []
SDL_GetCurrentDirectory.restype = ctypes.c_char_p


# bool SDL_GetPathInfo(const char *path, SDL_PathInfo *info);
SDL_GetPathInfo = libsdl3.SDL_GetPathInfo
SDL_GetPathInfo.argtypes = [ctypes.c_char_p, ctypes.POINTER(SDL_PathInfo)]
SDL_GetPathInfo.restype = ctypes.c_bool


# char * SDL_GetPrefPath(const char *org, const char *app);
SDL_GetPrefPath = libsdl3.SDL_GetPrefPath
SDL_GetPrefPath.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_GetPrefPath.restype = ctypes.c_char_p


# const char * SDL_GetUserFolder(SDL_Folder folder);
SDL_GetUserFolder = libsdl3.SDL_GetUserFolder
SDL_GetUserFolder.argtypes = [ctypes.c_int]
SDL_GetUserFolder.restype = ctypes.c_char_p


# char ** SDL_GlobDirectory(const char *path, const char *pattern, SDL_GlobFlags flags, int *count);
SDL_GlobDirectory = libsdl3.SDL_GlobDirectory
SDL_GlobDirectory.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_int),
]
SDL_GlobDirectory.restype = ctypes.POINTER(ctypes.c_char_p)


# bool SDL_RemovePath(const char *path);
SDL_RemovePath = libsdl3.SDL_RemovePath
SDL_RemovePath.argtypes = [ctypes.c_char_p]
SDL_RemovePath.restype = ctypes.c_bool


# bool SDL_RenamePath(const char *oldpath, const char *newpath);
SDL_RenamePath = libsdl3.SDL_RenamePath
SDL_RenamePath.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_RenamePath.restype = ctypes.c_bool
