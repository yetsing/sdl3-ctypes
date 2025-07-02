"""
SDL_thread.h
Thread Management
Document: https://wiki.libsdl.org/SDL3/CategoryThread
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_ThreadPriority {
#     SDL_THREAD_PRIORITY_LOW,
#     SDL_THREAD_PRIORITY_NORMAL,
#     SDL_THREAD_PRIORITY_HIGH,
#     SDL_THREAD_PRIORITY_TIME_CRITICAL
# } SDL_ThreadPriority;
SDL_THREAD_PRIORITY_LOW = 0
SDL_THREAD_PRIORITY_NORMAL = 1
SDL_THREAD_PRIORITY_HIGH = 2
SDL_THREAD_PRIORITY_TIME_CRITICAL = 3
# typedef enum SDL_ThreadState
# {
#     SDL_THREAD_UNKNOWN,     /**< The thread is not valid */
#     SDL_THREAD_ALIVE,       /**< The thread is currently running */
#     SDL_THREAD_DETACHED,    /**< The thread is detached and can't be waited on */
#     SDL_THREAD_COMPLETE     /**< The thread has finished and should be cleaned up with SDL_WaitThread() */
# } SDL_ThreadState;
SDL_THREAD_UNKNOWN = 0
SDL_THREAD_ALIVE = 1
SDL_THREAD_DETACHED = 2
SDL_THREAD_COMPLETE = 3


# typedef struct SDL_Thread SDL_Thread;

# typedef int (SDLCALL *SDL_ThreadFunction) (void *data);
SDL_ThreadFunction = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

# typedef Uint64 SDL_ThreadID;

# typedef void (SDLCALL *SDL_TLSDestructorCallback)(void *value);
SDL_TLSDestructorCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

# typedef SDL_AtomicInt SDL_TLSID;


# void SDL_CleanupTLS(void);
SDL_CleanupTLS = libsdl3.SDL_CleanupTLS
SDL_CleanupTLS.argtypes = []
SDL_CleanupTLS.restype = None


# SDL_Thread * SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);
SDL_CreateThread = libsdl3.SDL_CreateThread
SDL_CreateThread.argtypes = [SDL_ThreadFunction, ctypes.c_char_p, ctypes.c_void_p]
SDL_CreateThread.restype = ctypes.c_void_p


# SDL_Thread * SDL_CreateThreadWithProperties(SDL_PropertiesID props);
SDL_CreateThreadWithProperties = libsdl3.SDL_CreateThreadWithProperties
SDL_CreateThreadWithProperties.argtypes = [ctypes.c_uint32]
SDL_CreateThreadWithProperties.restype = ctypes.c_void_p


# void SDL_DetachThread(SDL_Thread *thread);
SDL_DetachThread = libsdl3.SDL_DetachThread
SDL_DetachThread.argtypes = [ctypes.c_void_p]
SDL_DetachThread.restype = None


# SDL_ThreadID SDL_GetCurrentThreadID(void);
SDL_GetCurrentThreadID = libsdl3.SDL_GetCurrentThreadID
SDL_GetCurrentThreadID.argtypes = []
SDL_GetCurrentThreadID.restype = ctypes.c_uint64


# SDL_ThreadID SDL_GetThreadID(SDL_Thread *thread);
SDL_GetThreadID = libsdl3.SDL_GetThreadID
SDL_GetThreadID.argtypes = [ctypes.c_void_p]
SDL_GetThreadID.restype = ctypes.c_uint64


# const char * SDL_GetThreadName(SDL_Thread *thread);
SDL_GetThreadName = libsdl3.SDL_GetThreadName
SDL_GetThreadName.argtypes = [ctypes.c_void_p]
SDL_GetThreadName.restype = ctypes.c_char_p


# SDL_ThreadState SDL_GetThreadState(SDL_Thread *thread);
SDL_GetThreadState = libsdl3.SDL_GetThreadState
SDL_GetThreadState.argtypes = [ctypes.c_void_p]
SDL_GetThreadState.restype = ctypes.c_int


# void * SDL_GetTLS(SDL_TLSID *id);
SDL_GetTLS = libsdl3.SDL_GetTLS
SDL_GetTLS.argtypes = [ctypes.c_void_p]
SDL_GetTLS.restype = ctypes.c_void_p


# bool SDL_SetCurrentThreadPriority(SDL_ThreadPriority priority);
SDL_SetCurrentThreadPriority = libsdl3.SDL_SetCurrentThreadPriority
SDL_SetCurrentThreadPriority.argtypes = [ctypes.c_int]
SDL_SetCurrentThreadPriority.restype = ctypes.c_bool


# bool SDL_SetTLS(SDL_TLSID *id, const void *value, SDL_TLSDestructorCallback destructor);
SDL_SetTLS = libsdl3.SDL_SetTLS
SDL_SetTLS.argtypes = [ctypes.c_void_p, ctypes.c_void_p, SDL_TLSDestructorCallback]
SDL_SetTLS.restype = ctypes.c_bool


# void SDL_WaitThread(SDL_Thread *thread, int *status);
SDL_WaitThread = libsdl3.SDL_WaitThread
SDL_WaitThread.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_WaitThread.restype = None
