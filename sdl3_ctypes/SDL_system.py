"""
SDL_system.h
Platform-specific Functionality
Document: https://wiki.libsdl.org/SDL3/CategorySystem
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_ANDROID_EXTERNAL_STORAGE_READ   0x01
SDL_ANDROID_EXTERNAL_STORAGE_READ = 1
# #define SDL_ANDROID_EXTERNAL_STORAGE_WRITE  0x02
SDL_ANDROID_EXTERNAL_STORAGE_WRITE = 2


# typedef enum SDL_Sandbox
# {
#     SDL_SANDBOX_NONE = 0,
#     SDL_SANDBOX_UNKNOWN_CONTAINER,
#     SDL_SANDBOX_FLATPAK,
#     SDL_SANDBOX_SNAP,
#     SDL_SANDBOX_MACOS
# } SDL_Sandbox;
SDL_SANDBOX_NONE = 0
SDL_SANDBOX_UNKNOWN_CONTAINER = 1
SDL_SANDBOX_FLATPAK = 2
SDL_SANDBOX_SNAP = 3
SDL_SANDBOX_MACOS = 4


# typedef void (SDLCALL *SDL_iOSAnimationCallback)(void *userdata);
SDL_iOSAnimationCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)


# typedef void (SDLCALL *SDL_RequestAndroidPermissionCallback)(void *userdata, const char *permission, bool granted);
SDL_RequestAndroidPermissionCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool
)


# typedef bool (SDLCALL *SDL_WindowsMessageHook)(void *userdata, MSG *msg);
SDL_WindowsMessageHook = ctypes.CFUNCTYPE(
    ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p
)


# typedef bool (SDLCALL *SDL_X11EventHook)(void *userdata, XEvent *xevent);
SDL_X11EventHook = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)


# void * SDL_GetAndroidActivity(void);
SDL_GetAndroidActivity = libsdl3.SDL_GetAndroidActivity
SDL_GetAndroidActivity.argtypes = []
SDL_GetAndroidActivity.restype = ctypes.c_void_p


# const char * SDL_GetAndroidCachePath(void);
SDL_GetAndroidCachePath = libsdl3.SDL_GetAndroidCachePath
SDL_GetAndroidCachePath.argtypes = []
SDL_GetAndroidCachePath.restype = ctypes.c_char_p


# const char * SDL_GetAndroidExternalStoragePath(void);
SDL_GetAndroidExternalStoragePath = libsdl3.SDL_GetAndroidExternalStoragePath
SDL_GetAndroidExternalStoragePath.argtypes = []
SDL_GetAndroidExternalStoragePath.restype = ctypes.c_char_p


# Uint32 SDL_GetAndroidExternalStorageState(void);
SDL_GetAndroidExternalStorageState = libsdl3.SDL_GetAndroidExternalStorageState
SDL_GetAndroidExternalStorageState.argtypes = []
SDL_GetAndroidExternalStorageState.restype = ctypes.c_uint32


# const char * SDL_GetAndroidInternalStoragePath(void);
SDL_GetAndroidInternalStoragePath = libsdl3.SDL_GetAndroidInternalStoragePath
SDL_GetAndroidInternalStoragePath.argtypes = []
SDL_GetAndroidInternalStoragePath.restype = ctypes.c_char_p


# void * SDL_GetAndroidJNIEnv(void);
SDL_GetAndroidJNIEnv = libsdl3.SDL_GetAndroidJNIEnv
SDL_GetAndroidJNIEnv.argtypes = []
SDL_GetAndroidJNIEnv.restype = ctypes.c_void_p


# int SDL_GetAndroidSDKVersion(void);
SDL_GetAndroidSDKVersion = libsdl3.SDL_GetAndroidSDKVersion
SDL_GetAndroidSDKVersion.argtypes = []
SDL_GetAndroidSDKVersion.restype = ctypes.c_int


# int SDL_GetDirect3D9AdapterIndex(SDL_DisplayID displayID);
SDL_GetDirect3D9AdapterIndex = libsdl3.SDL_GetDirect3D9AdapterIndex
SDL_GetDirect3D9AdapterIndex.argtypes = [ctypes.c_uint32]
SDL_GetDirect3D9AdapterIndex.restype = ctypes.c_int


# bool SDL_GetDXGIOutputInfo(SDL_DisplayID displayID, int *adapterIndex, int *outputIndex);
SDL_GetDXGIOutputInfo = libsdl3.SDL_GetDXGIOutputInfo
SDL_GetDXGIOutputInfo.argtypes = [
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetDXGIOutputInfo.restype = ctypes.c_bool


# bool SDL_GetGDKDefaultUser(XUserHandle *outUserHandle);
SDL_GetGDKDefaultUser = libsdl3.SDL_GetGDKDefaultUser
SDL_GetGDKDefaultUser.argtypes = [ctypes.c_void_p]
SDL_GetGDKDefaultUser.restype = ctypes.c_bool


# bool SDL_GetGDKTaskQueue(XTaskQueueHandle *outTaskQueue);
SDL_GetGDKTaskQueue = libsdl3.SDL_GetGDKTaskQueue
SDL_GetGDKTaskQueue.argtypes = [ctypes.c_void_p]
SDL_GetGDKTaskQueue.restype = ctypes.c_bool


# SDL_Sandbox SDL_GetSandbox(void);
SDL_GetSandbox = libsdl3.SDL_GetSandbox
SDL_GetSandbox.argtypes = []
SDL_GetSandbox.restype = ctypes.c_int


# bool SDL_IsChromebook(void);
SDL_IsChromebook = libsdl3.SDL_IsChromebook
SDL_IsChromebook.argtypes = []
SDL_IsChromebook.restype = ctypes.c_bool


# bool SDL_IsDeXMode(void);
SDL_IsDeXMode = libsdl3.SDL_IsDeXMode
SDL_IsDeXMode.argtypes = []
SDL_IsDeXMode.restype = ctypes.c_bool


# bool SDL_IsTablet(void);
SDL_IsTablet = libsdl3.SDL_IsTablet
SDL_IsTablet.argtypes = []
SDL_IsTablet.restype = ctypes.c_bool


# bool SDL_IsTV(void);
SDL_IsTV = libsdl3.SDL_IsTV
SDL_IsTV.argtypes = []
SDL_IsTV.restype = ctypes.c_bool


# void SDL_OnApplicationDidChangeStatusBarOrientation(void);
SDL_OnApplicationDidChangeStatusBarOrientation = (
    libsdl3.SDL_OnApplicationDidChangeStatusBarOrientation
)
SDL_OnApplicationDidChangeStatusBarOrientation.argtypes = []
SDL_OnApplicationDidChangeStatusBarOrientation.restype = None


# void SDL_OnApplicationDidEnterBackground(void);
SDL_OnApplicationDidEnterBackground = libsdl3.SDL_OnApplicationDidEnterBackground
SDL_OnApplicationDidEnterBackground.argtypes = []
SDL_OnApplicationDidEnterBackground.restype = None


# void SDL_OnApplicationDidEnterForeground(void);
SDL_OnApplicationDidEnterForeground = libsdl3.SDL_OnApplicationDidEnterForeground
SDL_OnApplicationDidEnterForeground.argtypes = []
SDL_OnApplicationDidEnterForeground.restype = None


# void SDL_OnApplicationDidReceiveMemoryWarning(void);
SDL_OnApplicationDidReceiveMemoryWarning = (
    libsdl3.SDL_OnApplicationDidReceiveMemoryWarning
)
SDL_OnApplicationDidReceiveMemoryWarning.argtypes = []
SDL_OnApplicationDidReceiveMemoryWarning.restype = None


# void SDL_OnApplicationWillEnterBackground(void);
SDL_OnApplicationWillEnterBackground = libsdl3.SDL_OnApplicationWillEnterBackground
SDL_OnApplicationWillEnterBackground.argtypes = []
SDL_OnApplicationWillEnterBackground.restype = None


# void SDL_OnApplicationWillEnterForeground(void);
SDL_OnApplicationWillEnterForeground = libsdl3.SDL_OnApplicationWillEnterForeground
SDL_OnApplicationWillEnterForeground.argtypes = []
SDL_OnApplicationWillEnterForeground.restype = None


# void SDL_OnApplicationWillTerminate(void);
SDL_OnApplicationWillTerminate = libsdl3.SDL_OnApplicationWillTerminate
SDL_OnApplicationWillTerminate.argtypes = []
SDL_OnApplicationWillTerminate.restype = None


# bool SDL_RequestAndroidPermission(const char *permission, SDL_RequestAndroidPermissionCallback cb, void *userdata);
SDL_RequestAndroidPermission = libsdl3.SDL_RequestAndroidPermission
SDL_RequestAndroidPermission.argtypes = [
    ctypes.c_char_p,
    SDL_RequestAndroidPermissionCallback,
    ctypes.c_void_p,
]
SDL_RequestAndroidPermission.restype = ctypes.c_bool


# void SDL_SendAndroidBackButton(void);
SDL_SendAndroidBackButton = libsdl3.SDL_SendAndroidBackButton
SDL_SendAndroidBackButton.argtypes = []
SDL_SendAndroidBackButton.restype = None


# bool SDL_SendAndroidMessage(Uint32 command, int param);
SDL_SendAndroidMessage = libsdl3.SDL_SendAndroidMessage
SDL_SendAndroidMessage.argtypes = [ctypes.c_uint32, ctypes.c_int]
SDL_SendAndroidMessage.restype = ctypes.c_bool


# bool SDL_SetiOSAnimationCallback(SDL_Window *window, int interval, SDL_iOSAnimationCallback callback, void *callbackParam);
SDL_SetiOSAnimationCallback = libsdl3.SDL_SetiOSAnimationCallback
SDL_SetiOSAnimationCallback.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    SDL_iOSAnimationCallback,
    ctypes.c_void_p,
]
SDL_SetiOSAnimationCallback.restype = ctypes.c_bool


# void SDL_SetiOSEventPump(bool enabled);
SDL_SetiOSEventPump = libsdl3.SDL_SetiOSEventPump
SDL_SetiOSEventPump.argtypes = [ctypes.c_bool]
SDL_SetiOSEventPump.restype = None


# bool SDL_SetLinuxThreadPriority(Sint64 threadID, int priority);
SDL_SetLinuxThreadPriority = libsdl3.SDL_SetLinuxThreadPriority
SDL_SetLinuxThreadPriority.argtypes = [ctypes.c_int64, ctypes.c_int]
SDL_SetLinuxThreadPriority.restype = ctypes.c_bool


# bool SDL_SetLinuxThreadPriorityAndPolicy(Sint64 threadID, int sdlPriority, int schedPolicy);
SDL_SetLinuxThreadPriorityAndPolicy = libsdl3.SDL_SetLinuxThreadPriorityAndPolicy
SDL_SetLinuxThreadPriorityAndPolicy.argtypes = [
    ctypes.c_int64,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_SetLinuxThreadPriorityAndPolicy.restype = ctypes.c_bool


# void SDL_SetWindowsMessageHook(SDL_WindowsMessageHook callback, void *userdata);
SDL_SetWindowsMessageHook = libsdl3.SDL_SetWindowsMessageHook
SDL_SetWindowsMessageHook.argtypes = [SDL_WindowsMessageHook, ctypes.c_void_p]
SDL_SetWindowsMessageHook.restype = None


# void SDL_SetX11EventHook(SDL_X11EventHook callback, void *userdata);
SDL_SetX11EventHook = libsdl3.SDL_SetX11EventHook
SDL_SetX11EventHook.argtypes = [SDL_X11EventHook, ctypes.c_void_p]
SDL_SetX11EventHook.restype = None


# bool SDL_ShowAndroidToast(const char *message, int duration, int gravity, int xoffset, int yoffset);
SDL_ShowAndroidToast = libsdl3.SDL_ShowAndroidToast
SDL_ShowAndroidToast.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_ShowAndroidToast.restype = ctypes.c_bool
