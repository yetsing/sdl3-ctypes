"""
SDL_cpuinfo.h
CPU Feature Detection
Document: https://wiki.libsdl.org/SDL3/CategoryCPUInfo
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_CACHELINE_SIZE  128
SDL_CACHELINE_SIZE = 128


# int SDL_GetCPUCacheLineSize(void);
SDL_GetCPUCacheLineSize = libsdl3.SDL_GetCPUCacheLineSize
SDL_GetCPUCacheLineSize.argtypes = []
SDL_GetCPUCacheLineSize.restype = ctypes.c_int


# int SDL_GetNumLogicalCPUCores(void);
SDL_GetNumLogicalCPUCores = libsdl3.SDL_GetNumLogicalCPUCores
SDL_GetNumLogicalCPUCores.argtypes = []
SDL_GetNumLogicalCPUCores.restype = ctypes.c_int


# size_t SDL_GetSIMDAlignment(void);
SDL_GetSIMDAlignment = libsdl3.SDL_GetSIMDAlignment
SDL_GetSIMDAlignment.argtypes = []
SDL_GetSIMDAlignment.restype = ctypes.c_size_t


# int SDL_GetSystemRAM(void);
SDL_GetSystemRAM = libsdl3.SDL_GetSystemRAM
SDL_GetSystemRAM.argtypes = []
SDL_GetSystemRAM.restype = ctypes.c_int


# bool SDL_HasAltiVec(void);
SDL_HasAltiVec = libsdl3.SDL_HasAltiVec
SDL_HasAltiVec.argtypes = []
SDL_HasAltiVec.restype = ctypes.c_bool


# bool SDL_HasARMSIMD(void);
SDL_HasARMSIMD = libsdl3.SDL_HasARMSIMD
SDL_HasARMSIMD.argtypes = []
SDL_HasARMSIMD.restype = ctypes.c_bool


# bool SDL_HasAVX(void);
SDL_HasAVX = libsdl3.SDL_HasAVX
SDL_HasAVX.argtypes = []
SDL_HasAVX.restype = ctypes.c_bool


# bool SDL_HasAVX2(void);
SDL_HasAVX2 = libsdl3.SDL_HasAVX2
SDL_HasAVX2.argtypes = []
SDL_HasAVX2.restype = ctypes.c_bool


# bool SDL_HasAVX512F(void);
SDL_HasAVX512F = libsdl3.SDL_HasAVX512F
SDL_HasAVX512F.argtypes = []
SDL_HasAVX512F.restype = ctypes.c_bool


# bool SDL_HasLASX(void);
SDL_HasLASX = libsdl3.SDL_HasLASX
SDL_HasLASX.argtypes = []
SDL_HasLASX.restype = ctypes.c_bool


# bool SDL_HasLSX(void);
SDL_HasLSX = libsdl3.SDL_HasLSX
SDL_HasLSX.argtypes = []
SDL_HasLSX.restype = ctypes.c_bool


# bool SDL_HasMMX(void);
SDL_HasMMX = libsdl3.SDL_HasMMX
SDL_HasMMX.argtypes = []
SDL_HasMMX.restype = ctypes.c_bool


# bool SDL_HasNEON(void);
SDL_HasNEON = libsdl3.SDL_HasNEON
SDL_HasNEON.argtypes = []
SDL_HasNEON.restype = ctypes.c_bool


# bool SDL_HasSSE(void);
SDL_HasSSE = libsdl3.SDL_HasSSE
SDL_HasSSE.argtypes = []
SDL_HasSSE.restype = ctypes.c_bool


# bool SDL_HasSSE2(void);
SDL_HasSSE2 = libsdl3.SDL_HasSSE2
SDL_HasSSE2.argtypes = []
SDL_HasSSE2.restype = ctypes.c_bool


# bool SDL_HasSSE3(void);
SDL_HasSSE3 = libsdl3.SDL_HasSSE3
SDL_HasSSE3.argtypes = []
SDL_HasSSE3.restype = ctypes.c_bool


# bool SDL_HasSSE41(void);
SDL_HasSSE41 = libsdl3.SDL_HasSSE41
SDL_HasSSE41.argtypes = []
SDL_HasSSE41.restype = ctypes.c_bool


# bool SDL_HasSSE42(void);
SDL_HasSSE42 = libsdl3.SDL_HasSSE42
SDL_HasSSE42.argtypes = []
SDL_HasSSE42.restype = ctypes.c_bool
