"""
SDL_process.h
Process Control
Document: https://wiki.libsdl.org/SDL3/CategoryProcess
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_ProcessIO
# {
#     SDL_PROCESS_STDIO_INHERITED,    /**< The I/O stream is inherited from the application. */
#     SDL_PROCESS_STDIO_NULL,         /**< The I/O stream is ignored. */
#     SDL_PROCESS_STDIO_APP,          /**< The I/O stream is connected to a new SDL_IOStream that the application can read or write */
#     SDL_PROCESS_STDIO_REDIRECT      /**< The I/O stream is redirected to an existing SDL_IOStream. */
# } SDL_ProcessIO;
SDL_PROCESS_STDIO_INHERITED = 0
SDL_PROCESS_STDIO_NULL = 1
SDL_PROCESS_STDIO_APP = 2
SDL_PROCESS_STDIO_REDIRECT = 3


# typedef struct SDL_Process SDL_Process;


# SDL_Process * SDL_CreateProcess(const char * const *args, bool pipe_stdio);
SDL_CreateProcess = libsdl3.SDL_CreateProcess
SDL_CreateProcess.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
    ctypes.c_bool,
]
SDL_CreateProcess.restype = ctypes.c_void_p


# SDL_Process * SDL_CreateProcessWithProperties(SDL_PropertiesID props);
SDL_CreateProcessWithProperties = libsdl3.SDL_CreateProcessWithProperties
SDL_CreateProcessWithProperties.argtypes = [ctypes.c_uint32]
SDL_CreateProcessWithProperties.restype = ctypes.c_void_p


# void SDL_DestroyProcess(SDL_Process *process);
SDL_DestroyProcess = libsdl3.SDL_DestroyProcess
SDL_DestroyProcess.argtypes = [ctypes.c_void_p]
SDL_DestroyProcess.restype = None


# SDL_IOStream * SDL_GetProcessInput(SDL_Process *process);
SDL_GetProcessInput = libsdl3.SDL_GetProcessInput
SDL_GetProcessInput.argtypes = [ctypes.c_void_p]
SDL_GetProcessInput.restype = ctypes.c_void_p


# SDL_IOStream * SDL_GetProcessOutput(SDL_Process *process);
SDL_GetProcessOutput = libsdl3.SDL_GetProcessOutput
SDL_GetProcessOutput.argtypes = [ctypes.c_void_p]
SDL_GetProcessOutput.restype = ctypes.c_void_p


# SDL_PropertiesID SDL_GetProcessProperties(SDL_Process *process);
SDL_GetProcessProperties = libsdl3.SDL_GetProcessProperties
SDL_GetProcessProperties.argtypes = [ctypes.c_void_p]
SDL_GetProcessProperties.restype = ctypes.c_uint32


# bool SDL_KillProcess(SDL_Process *process, bool force);
SDL_KillProcess = libsdl3.SDL_KillProcess
SDL_KillProcess.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_KillProcess.restype = ctypes.c_bool


# void * SDL_ReadProcess(SDL_Process *process, size_t *datasize, int *exitcode);
SDL_ReadProcess = libsdl3.SDL_ReadProcess
SDL_ReadProcess.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_size_t),
    ctypes.POINTER(ctypes.c_int),
]
SDL_ReadProcess.restype = ctypes.c_void_p


# bool SDL_WaitProcess(SDL_Process *process, bool block, int *exitcode);
SDL_WaitProcess = libsdl3.SDL_WaitProcess
SDL_WaitProcess.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.POINTER(ctypes.c_int),
]
SDL_WaitProcess.restype = ctypes.c_bool
