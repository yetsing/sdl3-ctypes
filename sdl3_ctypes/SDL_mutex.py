"""
SDL_mutex.h
Thread Synchronization Primitives
Document: https://wiki.libsdl.org/SDL3/CategoryMutex
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_atomic import SDL_AtomicInt

# #define SDL_ACQUIRE(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(acquire_capability(x))
# #define SDL_ACQUIRE_SHARED(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(acquire_shared_capability(x))
# #define SDL_ACQUIRED_AFTER(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(acquired_after(x))
# #define SDL_ACQUIRED_BEFORE(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(acquired_before(x))
# #define SDL_ASSERT_CAPABILITY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(assert_capability(x))
# #define SDL_ASSERT_SHARED_CAPABILITY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(assert_shared_capability(x))
# #define SDL_CAPABILITY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(capability(x))
# #define SDL_EXCLUDES(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(locks_excluded(x))
# #define SDL_GUARDED_BY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(guarded_by(x))
# #define SDL_NO_THREAD_SAFETY_ANALYSIS \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(no_thread_safety_analysis)
# #define SDL_PT_GUARDED_BY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(pt_guarded_by(x))
# #define SDL_RELEASE(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(release_capability(x))
# #define SDL_RELEASE_GENERIC(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(release_generic_capability(x))
# #define SDL_RELEASE_SHARED(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(release_shared_capability(x))
# #define SDL_REQUIRES(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(requires_capability(x))
# #define SDL_REQUIRES_SHARED(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(requires_shared_capability(x))
# #define SDL_RETURN_CAPABILITY(x) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(lock_returned(x))
# #define SDL_SCOPED_CAPABILITY \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(scoped_lockable)
# #define SDL_THREAD_ANNOTATION_ATTRIBUTE__(x)   __attribute__((x))
# #define SDL_TRY_ACQUIRE(x, y) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(try_acquire_capability(x, y))
# #define SDL_TRY_ACQUIRE_SHARED(x, y) \
#   SDL_THREAD_ANNOTATION_ATTRIBUTE__(try_acquire_shared_capability(x, y))


# typedef enum SDL_InitStatus
# {
#     SDL_INIT_STATUS_UNINITIALIZED,
#     SDL_INIT_STATUS_INITIALIZING,
#     SDL_INIT_STATUS_INITIALIZED,
#     SDL_INIT_STATUS_UNINITIALIZING
# } SDL_InitStatus;
SDL_INIT_STATUS_UNINITIALIZED = 0
SDL_INIT_STATUS_INITIALIZING = 1
SDL_INIT_STATUS_INITIALIZED = 2
SDL_INIT_STATUS_UNINITIALIZING = 3


# typedef struct SDL_InitState
# {
#     SDL_AtomicInt status;
#     SDL_ThreadID thread;
#     void *reserved;
# } SDL_InitState;
class SDL_InitState(ctypes.Structure):
    _fields_ = [
        ("status", SDL_AtomicInt),
        ("thread", ctypes.c_uint64),
        ("reserved", ctypes.c_void_p),
    ]


# typedef struct SDL_Condition SDL_Condition;
# typedef struct SDL_Mutex SDL_Mutex;
# typedef struct SDL_RWLock SDL_RWLock;
# typedef struct SDL_Semaphore SDL_Semaphore;


# void SDL_BroadcastCondition(SDL_Condition *cond);
SDL_BroadcastCondition = libsdl3.SDL_BroadcastCondition
SDL_BroadcastCondition.argtypes = [ctypes.c_void_p]
SDL_BroadcastCondition.restype = None


# SDL_Condition * SDL_CreateCondition(void);
SDL_CreateCondition = libsdl3.SDL_CreateCondition
SDL_CreateCondition.argtypes = []
SDL_CreateCondition.restype = ctypes.c_void_p


# SDL_Mutex * SDL_CreateMutex(void);
SDL_CreateMutex = libsdl3.SDL_CreateMutex
SDL_CreateMutex.argtypes = []
SDL_CreateMutex.restype = ctypes.c_void_p


# SDL_RWLock * SDL_CreateRWLock(void);
SDL_CreateRWLock = libsdl3.SDL_CreateRWLock
SDL_CreateRWLock.argtypes = []
SDL_CreateRWLock.restype = ctypes.c_void_p


# SDL_Semaphore * SDL_CreateSemaphore(Uint32 initial_value);
SDL_CreateSemaphore = libsdl3.SDL_CreateSemaphore
SDL_CreateSemaphore.argtypes = [ctypes.c_uint32]
SDL_CreateSemaphore.restype = ctypes.c_void_p


# void SDL_DestroyCondition(SDL_Condition *cond);
SDL_DestroyCondition = libsdl3.SDL_DestroyCondition
SDL_DestroyCondition.argtypes = [ctypes.c_void_p]
SDL_DestroyCondition.restype = None


# void SDL_DestroyMutex(SDL_Mutex *mutex);
SDL_DestroyMutex = libsdl3.SDL_DestroyMutex
SDL_DestroyMutex.argtypes = [ctypes.c_void_p]
SDL_DestroyMutex.restype = None


# void SDL_DestroyRWLock(SDL_RWLock *rwlock);
SDL_DestroyRWLock = libsdl3.SDL_DestroyRWLock
SDL_DestroyRWLock.argtypes = [ctypes.c_void_p]
SDL_DestroyRWLock.restype = None


# void SDL_DestroySemaphore(SDL_Semaphore *sem);
SDL_DestroySemaphore = libsdl3.SDL_DestroySemaphore
SDL_DestroySemaphore.argtypes = [ctypes.c_void_p]
SDL_DestroySemaphore.restype = None


# Uint32 SDL_GetSemaphoreValue(SDL_Semaphore *sem);
SDL_GetSemaphoreValue = libsdl3.SDL_GetSemaphoreValue
SDL_GetSemaphoreValue.argtypes = [ctypes.c_void_p]
SDL_GetSemaphoreValue.restype = ctypes.c_uint32


# void SDL_LockMutex(SDL_Mutex *mutex);
SDL_LockMutex = libsdl3.SDL_LockMutex
SDL_LockMutex.argtypes = [ctypes.c_void_p]
SDL_LockMutex.restype = None


# void SDL_LockRWLockForReading(SDL_RWLock *rwlock);
SDL_LockRWLockForReading = libsdl3.SDL_LockRWLockForReading
SDL_LockRWLockForReading.argtypes = [ctypes.c_void_p]
SDL_LockRWLockForReading.restype = None


# void SDL_LockRWLockForWriting(SDL_RWLock *rwlock);
SDL_LockRWLockForWriting = libsdl3.SDL_LockRWLockForWriting
SDL_LockRWLockForWriting.argtypes = [ctypes.c_void_p]
SDL_LockRWLockForWriting.restype = None


# void SDL_SetInitialized(SDL_InitState *state, bool initialized);
SDL_SetInitialized = libsdl3.SDL_SetInitialized
SDL_SetInitialized.argtypes = [ctypes.POINTER(SDL_InitState), ctypes.c_bool]
SDL_SetInitialized.restype = None


# bool SDL_ShouldInit(SDL_InitState *state);
SDL_ShouldInit = libsdl3.SDL_ShouldInit
SDL_ShouldInit.argtypes = [ctypes.POINTER(SDL_InitState)]
SDL_ShouldInit.restype = ctypes.c_bool


# bool SDL_ShouldQuit(SDL_InitState *state);
SDL_ShouldQuit = libsdl3.SDL_ShouldQuit
SDL_ShouldQuit.argtypes = [ctypes.POINTER(SDL_InitState)]
SDL_ShouldQuit.restype = ctypes.c_bool


# void SDL_SignalCondition(SDL_Condition *cond);
SDL_SignalCondition = libsdl3.SDL_SignalCondition
SDL_SignalCondition.argtypes = [ctypes.c_void_p]
SDL_SignalCondition.restype = None


# void SDL_SignalSemaphore(SDL_Semaphore *sem);
SDL_SignalSemaphore = libsdl3.SDL_SignalSemaphore
SDL_SignalSemaphore.argtypes = [ctypes.c_void_p]
SDL_SignalSemaphore.restype = None


# bool SDL_TryLockMutex(SDL_Mutex *mutex);
SDL_TryLockMutex = libsdl3.SDL_TryLockMutex
SDL_TryLockMutex.argtypes = [ctypes.c_void_p]
SDL_TryLockMutex.restype = ctypes.c_bool


# bool SDL_TryLockRWLockForReading(SDL_RWLock *rwlock);
SDL_TryLockRWLockForReading = libsdl3.SDL_TryLockRWLockForReading
SDL_TryLockRWLockForReading.argtypes = [ctypes.c_void_p]
SDL_TryLockRWLockForReading.restype = ctypes.c_bool


# bool SDL_TryLockRWLockForWriting(SDL_RWLock *rwlock);
SDL_TryLockRWLockForWriting = libsdl3.SDL_TryLockRWLockForWriting
SDL_TryLockRWLockForWriting.argtypes = [ctypes.c_void_p]
SDL_TryLockRWLockForWriting.restype = ctypes.c_bool


# bool SDL_TryWaitSemaphore(SDL_Semaphore *sem);
SDL_TryWaitSemaphore = libsdl3.SDL_TryWaitSemaphore
SDL_TryWaitSemaphore.argtypes = [ctypes.c_void_p]
SDL_TryWaitSemaphore.restype = ctypes.c_bool


# void SDL_UnlockMutex(SDL_Mutex *mutex);
SDL_UnlockMutex = libsdl3.SDL_UnlockMutex
SDL_UnlockMutex.argtypes = [ctypes.c_void_p]
SDL_UnlockMutex.restype = None


# void SDL_UnlockRWLock(SDL_RWLock *rwlock);
SDL_UnlockRWLock = libsdl3.SDL_UnlockRWLock
SDL_UnlockRWLock.argtypes = [ctypes.c_void_p]
SDL_UnlockRWLock.restype = None


# void SDL_WaitCondition(SDL_Condition *cond, SDL_Mutex *mutex);
SDL_WaitCondition = libsdl3.SDL_WaitCondition
SDL_WaitCondition.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_WaitCondition.restype = None


# bool SDL_WaitConditionTimeout(SDL_Condition *cond,
#                     SDL_Mutex *mutex, Sint32 timeoutMS);
SDL_WaitConditionTimeout = libsdl3.SDL_WaitConditionTimeout
SDL_WaitConditionTimeout.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32]
SDL_WaitConditionTimeout.restype = ctypes.c_bool


# void SDL_WaitSemaphore(SDL_Semaphore *sem);
SDL_WaitSemaphore = libsdl3.SDL_WaitSemaphore
SDL_WaitSemaphore.argtypes = [ctypes.c_void_p]
SDL_WaitSemaphore.restype = None


# bool SDL_WaitSemaphoreTimeout(SDL_Semaphore *sem, Sint32 timeoutMS);
SDL_WaitSemaphoreTimeout = libsdl3.SDL_WaitSemaphoreTimeout
SDL_WaitSemaphoreTimeout.argtypes = [ctypes.c_void_p, ctypes.c_int32]
SDL_WaitSemaphoreTimeout.restype = ctypes.c_bool
