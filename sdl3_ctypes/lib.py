import ctypes
import platform

_sdl3_libname = "libSDL3.so.0"
if platform.system() == "Windows":
    _sdl3_libname = "SDL3.dll"
elif platform.system() == "Darwin":
    _sdl3_libname = "libSDL3.0.dylib"
libsdl3 = ctypes.CDLL(_sdl3_libname)
