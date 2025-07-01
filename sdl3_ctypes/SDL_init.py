"""
SDL_init.h
Initialization and Shutdown
Document: https://wiki.libsdl.org/SDL3/CategoryInit
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_events import SDL_Event

# typedef enum SDL_AppResult
# {
#     SDL_APP_CONTINUE,   /**< Value that requests that the app continue from the main callbacks. */
#     SDL_APP_SUCCESS,    /**< Value that requests termination with success from the main callbacks. */
#     SDL_APP_FAILURE     /**< Value that requests termination with error from the main callbacks. */
# } SDL_AppResult;
SDL_APP_CONTINUE = 0
SDL_APP_SUCCESS = 1
SDL_APP_FAILURE = 2


# typedef SDL_AppResult (SDLCALL *SDL_AppEvent_func)(void *appstate, SDL_Event *event);
SDL_AppEvent_func = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(SDL_Event)
)


# typedef SDL_AppResult (SDLCALL *SDL_AppInit_func)(void **appstate, int argc, char *argv[]);
SDL_AppInit_func = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_char_p),
)


# typedef SDL_AppResult (SDLCALL *SDL_AppIterate_func)(void *appstate);
SDL_AppIterate_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)


# typedef void (SDLCALL *SDL_AppQuit_func)(void *appstate, SDL_AppResult result);
SDL_AppQuit_func = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)

# typedef Uint32 SDL_InitFlags;
# #define SDL_INIT_AUDIO      0x00000010u /**< `SDL_INIT_AUDIO` implies `SDL_INIT_EVENTS` */
# #define SDL_INIT_VIDEO      0x00000020u /**< `SDL_INIT_VIDEO` implies `SDL_INIT_EVENTS`, should be initialized on the main thread */
# #define SDL_INIT_JOYSTICK   0x00000200u /**< `SDL_INIT_JOYSTICK` implies `SDL_INIT_EVENTS` */
# #define SDL_INIT_HAPTIC     0x00001000u
# #define SDL_INIT_GAMEPAD    0x00002000u /**< `SDL_INIT_GAMEPAD` implies `SDL_INIT_JOYSTICK` */
# #define SDL_INIT_EVENTS     0x00004000u
# #define SDL_INIT_SENSOR     0x00008000u /**< `SDL_INIT_SENSOR` implies `SDL_INIT_EVENTS` */
# #define SDL_INIT_CAMERA     0x00010000u /**< `SDL_INIT_CAMERA` implies `SDL_INIT_EVENTS` */
SDL_INIT_AUDIO = 0x10
SDL_INIT_VIDEO = 0x20
SDL_INIT_JOYSTICK = 0x200
SDL_INIT_HAPTIC = 0x1000
SDL_INIT_GAMEPAD = 0x2000
SDL_INIT_EVENTS = 0x4000
SDL_INIT_SENSOR = 0x8000
SDL_INIT_CAMERA = 0x10000

# typedef void (SDLCALL *SDL_MainThreadCallback)(void *userdata);
SDL_MainThreadCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)


# const char * SDL_GetAppMetadataProperty(const char *name);
SDL_GetAppMetadataProperty = libsdl3.SDL_GetAppMetadataProperty
SDL_GetAppMetadataProperty.argtypes = [ctypes.c_char_p]
SDL_GetAppMetadataProperty.restype = ctypes.c_char_p


# bool SDL_Init(SDL_InitFlags flags);
SDL_Init = libsdl3.SDL_Init
SDL_Init.argtypes = [ctypes.c_uint32]
SDL_Init.restype = ctypes.c_bool


# bool SDL_InitSubSystem(SDL_InitFlags flags);
SDL_InitSubSystem = libsdl3.SDL_InitSubSystem
SDL_InitSubSystem.argtypes = [ctypes.c_uint32]
SDL_InitSubSystem.restype = ctypes.c_bool


# bool SDL_IsMainThread(void);
SDL_IsMainThread = libsdl3.SDL_IsMainThread
SDL_IsMainThread.argtypes = []
SDL_IsMainThread.restype = ctypes.c_bool


# void SDL_Quit(void);
SDL_Quit = libsdl3.SDL_Quit
SDL_Quit.argtypes = []
SDL_Quit.restype = None


# void SDL_QuitSubSystem(SDL_InitFlags flags);
SDL_QuitSubSystem = libsdl3.SDL_QuitSubSystem
SDL_QuitSubSystem.argtypes = [ctypes.c_uint32]
SDL_QuitSubSystem.restype = None


# bool SDL_RunOnMainThread(SDL_MainThreadCallback callback, void *userdata, bool wait_complete);
SDL_RunOnMainThread = libsdl3.SDL_RunOnMainThread
SDL_RunOnMainThread.argtypes = [SDL_MainThreadCallback, ctypes.c_void_p, ctypes.c_bool]
SDL_RunOnMainThread.restype = ctypes.c_bool


# bool SDL_SetAppMetadata(const char *appname, const char *appversion, const char *appidentifier);
SDL_SetAppMetadata = libsdl3.SDL_SetAppMetadata
SDL_SetAppMetadata.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
SDL_SetAppMetadata.restype = ctypes.c_bool


# bool SDL_SetAppMetadataProperty(const char *name, const char *value);
SDL_SetAppMetadataProperty = libsdl3.SDL_SetAppMetadataProperty
SDL_SetAppMetadataProperty.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_SetAppMetadataProperty.restype = ctypes.c_bool


# SDL_InitFlags SDL_WasInit(SDL_InitFlags flags);
SDL_WasInit = libsdl3.SDL_WasInit
SDL_WasInit.argtypes = [ctypes.c_uint32]
SDL_WasInit.restype = ctypes.c_uint32
