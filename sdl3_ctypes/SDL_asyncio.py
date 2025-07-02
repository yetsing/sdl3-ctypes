"""
SDL_asyncio.h
Async I/O
Document: https://wiki.libsdl.org/SDL3/CategoryAsyncIO
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_AsyncIOResult
# {
#     SDL_ASYNCIO_COMPLETE,  /**< request was completed without error */
#     SDL_ASYNCIO_FAILURE,   /**< request failed for some reason; check SDL_GetError()! */
#     SDL_ASYNCIO_CANCELED   /**< request was canceled before completing. */
# } SDL_AsyncIOResult;
SDL_ASYNCIO_COMPLETE = 0
SDL_ASYNCIO_FAILURE = 1
SDL_ASYNCIO_CANCELED = 2
# typedef enum SDL_AsyncIOTaskType
# {
#     SDL_ASYNCIO_TASK_READ,   /**< A read operation. */
#     SDL_ASYNCIO_TASK_WRITE,  /**< A write operation. */
#     SDL_ASYNCIO_TASK_CLOSE   /**< A close operation. */
# } SDL_AsyncIOTaskType;
SDL_ASYNCIO_TASK_READ = 0
SDL_ASYNCIO_TASK_WRITE = 1
SDL_ASYNCIO_TASK_CLOSE = 2


# typedef struct SDL_AsyncIOOutcome
# {
#     SDL_AsyncIO *asyncio;   /**< what generated this task. This pointer will be invalid if it was closed! */
#     SDL_AsyncIOTaskType type;  /**< What sort of task was this? Read, write, etc? */
#     SDL_AsyncIOResult result;  /**< the result of the work (success, failure, cancellation). */
#     void *buffer;  /**< buffer where data was read/written. */
#     Uint64 offset;  /**< offset in the SDL_AsyncIO where data was read/written. */
#     Uint64 bytes_requested;  /**< number of bytes the task was to read/write. */
#     Uint64 bytes_transferred;  /**< actual number of bytes that were read/written. */
#     void *userdata;    /**< pointer provided by the app when starting the task */
# } SDL_AsyncIOOutcome;
class SDL_AsyncIOOutcome(ctypes.Structure):
    _fields_ = [
        ("asyncio", ctypes.c_void_p),
        ("type", ctypes.c_int),
        ("result", ctypes.c_int),
        ("buffer", ctypes.c_void_p),
        ("offset", ctypes.c_uint64),
        ("bytes_requested", ctypes.c_uint64),
        ("bytes_transferred", ctypes.c_uint64),
        ("userdata", ctypes.c_void_p),
    ]


# typedef struct SDL_AsyncIO SDL_AsyncIO;
# typedef struct SDL_AsyncIOQueue SDL_AsyncIOQueue;


# SDL_AsyncIO * SDL_AsyncIOFromFile(const char *file, const char *mode);
SDL_AsyncIOFromFile = libsdl3.SDL_AsyncIOFromFile
SDL_AsyncIOFromFile.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_AsyncIOFromFile.restype = ctypes.c_void_p


# bool SDL_CloseAsyncIO(SDL_AsyncIO *asyncio, bool flush, SDL_AsyncIOQueue *queue, void *userdata);
SDL_CloseAsyncIO = libsdl3.SDL_CloseAsyncIO
SDL_CloseAsyncIO.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.c_void_p,
    ctypes.c_void_p,
]
SDL_CloseAsyncIO.restype = ctypes.c_bool


# SDL_AsyncIOQueue * SDL_CreateAsyncIOQueue(void);
SDL_CreateAsyncIOQueue = libsdl3.SDL_CreateAsyncIOQueue
SDL_CreateAsyncIOQueue.argtypes = []
SDL_CreateAsyncIOQueue.restype = ctypes.c_void_p


# void SDL_DestroyAsyncIOQueue(SDL_AsyncIOQueue *queue);
SDL_DestroyAsyncIOQueue = libsdl3.SDL_DestroyAsyncIOQueue
SDL_DestroyAsyncIOQueue.argtypes = [ctypes.c_void_p]
SDL_DestroyAsyncIOQueue.restype = None


# bool SDL_GetAsyncIOResult(SDL_AsyncIOQueue *queue, SDL_AsyncIOOutcome *outcome);
SDL_GetAsyncIOResult = libsdl3.SDL_GetAsyncIOResult
SDL_GetAsyncIOResult.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_AsyncIOOutcome)]
SDL_GetAsyncIOResult.restype = ctypes.c_bool


# Sint64 SDL_GetAsyncIOSize(SDL_AsyncIO *asyncio);
SDL_GetAsyncIOSize = libsdl3.SDL_GetAsyncIOSize
SDL_GetAsyncIOSize.argtypes = [ctypes.c_void_p]
SDL_GetAsyncIOSize.restype = ctypes.c_int64


# bool SDL_LoadFileAsync(const char *file, SDL_AsyncIOQueue *queue, void *userdata);
SDL_LoadFileAsync = libsdl3.SDL_LoadFileAsync
SDL_LoadFileAsync.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
SDL_LoadFileAsync.restype = ctypes.c_bool


# bool SDL_ReadAsyncIO(SDL_AsyncIO *asyncio, void *ptr, Uint64 offset, Uint64 size, SDL_AsyncIOQueue *queue, void *userdata);
SDL_ReadAsyncIO = libsdl3.SDL_ReadAsyncIO
SDL_ReadAsyncIO.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_uint64,
    ctypes.c_uint64,
    ctypes.c_void_p,
    ctypes.c_void_p,
]
SDL_ReadAsyncIO.restype = ctypes.c_bool


# void SDL_SignalAsyncIOQueue(SDL_AsyncIOQueue *queue);
SDL_SignalAsyncIOQueue = libsdl3.SDL_SignalAsyncIOQueue
SDL_SignalAsyncIOQueue.argtypes = [ctypes.c_void_p]
SDL_SignalAsyncIOQueue.restype = None


# bool SDL_WaitAsyncIOResult(SDL_AsyncIOQueue *queue, SDL_AsyncIOOutcome *outcome, Sint32 timeoutMS);
SDL_WaitAsyncIOResult = libsdl3.SDL_WaitAsyncIOResult
SDL_WaitAsyncIOResult.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_AsyncIOOutcome),
    ctypes.c_int32,
]
SDL_WaitAsyncIOResult.restype = ctypes.c_bool


# bool SDL_WriteAsyncIO(SDL_AsyncIO *asyncio, void *ptr, Uint64 offset, Uint64 size, SDL_AsyncIOQueue *queue, void *userdata);
SDL_WriteAsyncIO = libsdl3.SDL_WriteAsyncIO
SDL_WriteAsyncIO.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_uint64,
    ctypes.c_uint64,
    ctypes.c_void_p,
    ctypes.c_void_p,
]
SDL_WriteAsyncIO.restype = ctypes.c_bool
