"""
SDL_atomic.h
Atomic Operations
Document: https://wiki.libsdl.org/SDL3/CategoryAtomic
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_AtomicDecRef(a)    (SDL_AddAtomicInt(a, -1) == 1)
# #define SDL_AtomicIncRef(a)    SDL_AddAtomicInt(a, 1)
# #define SDL_CompilerBarrier() DoCompilerSpecificReadWriteBarrier()
# #define SDL_CPUPauseInstruction() DoACPUPauseInACompilerAndArchitectureSpecificWay
# #define SDL_MemoryBarrierAcquire() SDL_MemoryBarrierAcquireFunction()
# #define SDL_MemoryBarrierRelease() SDL_MemoryBarrierReleaseFunction()


# typedef struct SDL_AtomicInt { int value; } SDL_AtomicInt;
class SDL_AtomicInt(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]


# typedef struct SDL_AtomicU32 { Uint32 value; } SDL_AtomicU32;
class SDL_AtomicU32(ctypes.Structure):
    _fields_ = [("value", ctypes.c_uint32)]


# typedef int SDL_SpinLock;


# int SDL_AddAtomicInt(SDL_AtomicInt *a, int v);
SDL_AddAtomicInt = libsdl3.SDL_AddAtomicInt
SDL_AddAtomicInt.argtypes = [ctypes.POINTER(SDL_AtomicInt), ctypes.c_int]
SDL_AddAtomicInt.restype = ctypes.c_int


# bool SDL_CompareAndSwapAtomicInt(SDL_AtomicInt *a, int oldval, int newval);
SDL_CompareAndSwapAtomicInt = libsdl3.SDL_CompareAndSwapAtomicInt
SDL_CompareAndSwapAtomicInt.argtypes = [
    ctypes.POINTER(SDL_AtomicInt),
    ctypes.c_int,
    ctypes.c_int,
]
SDL_CompareAndSwapAtomicInt.restype = ctypes.c_bool


# bool SDL_CompareAndSwapAtomicPointer(void **a, void *oldval, void *newval);
SDL_CompareAndSwapAtomicPointer = libsdl3.SDL_CompareAndSwapAtomicPointer
SDL_CompareAndSwapAtomicPointer.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_void_p,
    ctypes.c_void_p,
]
SDL_CompareAndSwapAtomicPointer.restype = ctypes.c_bool


# bool SDL_CompareAndSwapAtomicU32(SDL_AtomicU32 *a, Uint32 oldval, Uint32 newval);
SDL_CompareAndSwapAtomicU32 = libsdl3.SDL_CompareAndSwapAtomicU32
SDL_CompareAndSwapAtomicU32.argtypes = [
    ctypes.POINTER(SDL_AtomicU32),
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_CompareAndSwapAtomicU32.restype = ctypes.c_bool


# int SDL_GetAtomicInt(SDL_AtomicInt *a);
SDL_GetAtomicInt = libsdl3.SDL_GetAtomicInt
SDL_GetAtomicInt.argtypes = [ctypes.POINTER(SDL_AtomicInt)]
SDL_GetAtomicInt.restype = ctypes.c_int


# void * SDL_GetAtomicPointer(void **a);
SDL_GetAtomicPointer = libsdl3.SDL_GetAtomicPointer
SDL_GetAtomicPointer.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
SDL_GetAtomicPointer.restype = ctypes.c_void_p


# Uint32 SDL_GetAtomicU32(SDL_AtomicU32 *a);
SDL_GetAtomicU32 = libsdl3.SDL_GetAtomicU32
SDL_GetAtomicU32.argtypes = [ctypes.POINTER(SDL_AtomicU32)]
SDL_GetAtomicU32.restype = ctypes.c_uint32


# void SDL_LockSpinlock(SDL_SpinLock *lock);
SDL_LockSpinlock = libsdl3.SDL_LockSpinlock
SDL_LockSpinlock.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_LockSpinlock.restype = None


# void SDL_MemoryBarrierAcquireFunction(void);
SDL_MemoryBarrierAcquireFunction = libsdl3.SDL_MemoryBarrierAcquireFunction
SDL_MemoryBarrierAcquireFunction.argtypes = []
SDL_MemoryBarrierAcquireFunction.restype = None


# void SDL_MemoryBarrierReleaseFunction(void);
SDL_MemoryBarrierReleaseFunction = libsdl3.SDL_MemoryBarrierReleaseFunction
SDL_MemoryBarrierReleaseFunction.argtypes = []
SDL_MemoryBarrierReleaseFunction.restype = None


# int SDL_SetAtomicInt(SDL_AtomicInt *a, int v);
SDL_SetAtomicInt = libsdl3.SDL_SetAtomicInt
SDL_SetAtomicInt.argtypes = [ctypes.POINTER(SDL_AtomicInt), ctypes.c_int]
SDL_SetAtomicInt.restype = ctypes.c_int


# void * SDL_SetAtomicPointer(void **a, void *v);
SDL_SetAtomicPointer = libsdl3.SDL_SetAtomicPointer
SDL_SetAtomicPointer.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p]
SDL_SetAtomicPointer.restype = ctypes.c_void_p


# Uint32 SDL_SetAtomicU32(SDL_AtomicU32 *a, Uint32 v);
SDL_SetAtomicU32 = libsdl3.SDL_SetAtomicU32
SDL_SetAtomicU32.argtypes = [ctypes.POINTER(SDL_AtomicU32), ctypes.c_uint32]
SDL_SetAtomicU32.restype = ctypes.c_uint32


# bool SDL_TryLockSpinlock(SDL_SpinLock *lock);
SDL_TryLockSpinlock = libsdl3.SDL_TryLockSpinlock
SDL_TryLockSpinlock.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_TryLockSpinlock.restype = ctypes.c_bool


# void SDL_UnlockSpinlock(SDL_SpinLock *lock);
SDL_UnlockSpinlock = libsdl3.SDL_UnlockSpinlock
SDL_UnlockSpinlock.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_UnlockSpinlock.restype = None
