"""
SDL_log.h
Log Handling
Document: https://wiki.libsdl.org/SDL3/CategoryLog
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_LogCategory
# {
#     SDL_LOG_CATEGORY_APPLICATION,
#     SDL_LOG_CATEGORY_ERROR,
#     SDL_LOG_CATEGORY_ASSERT,
#     SDL_LOG_CATEGORY_SYSTEM,
#     SDL_LOG_CATEGORY_AUDIO,
#     SDL_LOG_CATEGORY_VIDEO,
#     SDL_LOG_CATEGORY_RENDER,
#     SDL_LOG_CATEGORY_INPUT,
#     SDL_LOG_CATEGORY_TEST,
#     SDL_LOG_CATEGORY_GPU,
#     /* Reserved for future SDL library use */
#     SDL_LOG_CATEGORY_RESERVED2,
#     SDL_LOG_CATEGORY_RESERVED3,
#     SDL_LOG_CATEGORY_RESERVED4,
#     SDL_LOG_CATEGORY_RESERVED5,
#     SDL_LOG_CATEGORY_RESERVED6,
#     SDL_LOG_CATEGORY_RESERVED7,
#     SDL_LOG_CATEGORY_RESERVED8,
#     SDL_LOG_CATEGORY_RESERVED9,
#     SDL_LOG_CATEGORY_RESERVED10,
#     /* Beyond this point is reserved for application use, e.g.
#        enum {
#            MYAPP_CATEGORY_AWESOME1 = SDL_LOG_CATEGORY_CUSTOM,
#            MYAPP_CATEGORY_AWESOME2,
#            MYAPP_CATEGORY_AWESOME3,
#            ...
#        };
#      */
#     SDL_LOG_CATEGORY_CUSTOM
# } SDL_LogCategory;
SDL_LOG_CATEGORY_APPLICATION = 0
SDL_LOG_CATEGORY_ERROR = 1
SDL_LOG_CATEGORY_ASSERT = 2
SDL_LOG_CATEGORY_SYSTEM = 3
SDL_LOG_CATEGORY_AUDIO = 4
SDL_LOG_CATEGORY_VIDEO = 5
SDL_LOG_CATEGORY_RENDER = 6
SDL_LOG_CATEGORY_INPUT = 7
SDL_LOG_CATEGORY_TEST = 8
SDL_LOG_CATEGORY_GPU = 9
SDL_LOG_CATEGORY_RESERVED2 = 10
SDL_LOG_CATEGORY_RESERVED3 = 11
SDL_LOG_CATEGORY_RESERVED4 = 12
SDL_LOG_CATEGORY_RESERVED5 = 13
SDL_LOG_CATEGORY_RESERVED6 = 14
SDL_LOG_CATEGORY_RESERVED7 = 15
SDL_LOG_CATEGORY_RESERVED8 = 16
SDL_LOG_CATEGORY_RESERVED9 = 17
SDL_LOG_CATEGORY_RESERVED10 = 18
SDL_LOG_CATEGORY_CUSTOM = 19
# typedef enum SDL_LogPriority
# {
#     SDL_LOG_PRIORITY_INVALID,
#     SDL_LOG_PRIORITY_TRACE,
#     SDL_LOG_PRIORITY_VERBOSE,
#     SDL_LOG_PRIORITY_DEBUG,
#     SDL_LOG_PRIORITY_INFO,
#     SDL_LOG_PRIORITY_WARN,
#     SDL_LOG_PRIORITY_ERROR,
#     SDL_LOG_PRIORITY_CRITICAL,
#     SDL_LOG_PRIORITY_COUNT
# } SDL_LogPriority;
SDL_LOG_PRIORITY_INVALID = 0
SDL_LOG_PRIORITY_TRACE = 1
SDL_LOG_PRIORITY_VERBOSE = 2
SDL_LOG_PRIORITY_DEBUG = 3
SDL_LOG_PRIORITY_INFO = 4
SDL_LOG_PRIORITY_WARN = 5
SDL_LOG_PRIORITY_ERROR = 6
SDL_LOG_PRIORITY_CRITICAL = 7
SDL_LOG_PRIORITY_COUNT = 8


# typedef void (SDLCALL *SDL_LogOutputFunction)(void *userdata, int category, SDL_LogPriority priority, const char *message);
SDL_LogOutputFunction = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p
)


# SDL_LogOutputFunction SDL_GetDefaultLogOutputFunction(void);
SDL_GetDefaultLogOutputFunction = libsdl3.SDL_GetDefaultLogOutputFunction
SDL_GetDefaultLogOutputFunction.argtypes = []
SDL_GetDefaultLogOutputFunction.restype = SDL_LogOutputFunction


# void SDL_GetLogOutputFunction(SDL_LogOutputFunction *callback, void **userdata);
SDL_GetLogOutputFunction = libsdl3.SDL_GetLogOutputFunction
SDL_GetLogOutputFunction.argtypes = [
    ctypes.POINTER(SDL_LogOutputFunction),
    ctypes.POINTER(ctypes.c_void_p),
]
SDL_GetLogOutputFunction.restype = None


# SDL_LogPriority SDL_GetLogPriority(int category);
SDL_GetLogPriority = libsdl3.SDL_GetLogPriority
SDL_GetLogPriority.argtypes = [ctypes.c_int]
SDL_GetLogPriority.restype = ctypes.c_int

# void SDL_Log(const char *fmt, ...);
# void SDL_LogCritical(int category, const char *fmt, ...);
# void SDL_LogDebug(int category, const char *fmt, ...);
# void SDL_LogError(int category, const char *fmt, ...);
# void SDL_LogInfo(int category, const char *fmt, ...);
# void SDL_LogMessage(int category,
#                 SDL_LogPriority priority,
#                 const char *fmt, ...);
# void SDL_LogMessageV(int category,
#                  SDL_LogPriority priority,
#                  const char *fmt, va_list ap);
# void SDL_LogTrace(int category, const char *fmt, ...);
# void SDL_LogVerbose(int category, const char *fmt, ...);
# void SDL_LogWarn(int category, const char *fmt, ...);

# void SDL_ResetLogPriorities(void);
SDL_ResetLogPriorities = libsdl3.SDL_ResetLogPriorities
SDL_ResetLogPriorities.argtypes = []
SDL_ResetLogPriorities.restype = None


# void SDL_SetLogOutputFunction(SDL_LogOutputFunction callback, void *userdata);
SDL_SetLogOutputFunction = libsdl3.SDL_SetLogOutputFunction
SDL_SetLogOutputFunction.argtypes = [SDL_LogOutputFunction, ctypes.c_void_p]
SDL_SetLogOutputFunction.restype = None


# void SDL_SetLogPriorities(SDL_LogPriority priority);
SDL_SetLogPriorities = libsdl3.SDL_SetLogPriorities
SDL_SetLogPriorities.argtypes = [ctypes.c_int]
SDL_SetLogPriorities.restype = None


# void SDL_SetLogPriority(int category, SDL_LogPriority priority);
SDL_SetLogPriority = libsdl3.SDL_SetLogPriority
SDL_SetLogPriority.argtypes = [ctypes.c_int, ctypes.c_int]
SDL_SetLogPriority.restype = None


# bool SDL_SetLogPriorityPrefix(SDL_LogPriority priority, const char *prefix);
SDL_SetLogPriorityPrefix = libsdl3.SDL_SetLogPriorityPrefix
SDL_SetLogPriorityPrefix.argtypes = [ctypes.c_int, ctypes.c_char_p]
SDL_SetLogPriorityPrefix.restype = ctypes.c_bool
