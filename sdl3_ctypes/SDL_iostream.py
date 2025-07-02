"""
SDL_iostream.h
I/O Streams
Document: https://wiki.libsdl.org/SDL3/CategoryIOStream
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_IOStatus
# {
#     SDL_IO_STATUS_READY,     /**< Everything is ready (no errors and not EOF). */
#     SDL_IO_STATUS_ERROR,     /**< Read or write I/O error */
#     SDL_IO_STATUS_EOF,       /**< End of file */
#     SDL_IO_STATUS_NOT_READY, /**< Non blocking I/O, not ready */
#     SDL_IO_STATUS_READONLY,  /**< Tried to write a read-only buffer */
#     SDL_IO_STATUS_WRITEONLY  /**< Tried to read a write-only buffer */
# } SDL_IOStatus;
SDL_IO_STATUS_READY = 0
SDL_IO_STATUS_ERROR = 1
SDL_IO_STATUS_EOF = 2
SDL_IO_STATUS_NOT_READY = 3
SDL_IO_STATUS_READONLY = 4
SDL_IO_STATUS_WRITEONLY = 5
# typedef enum SDL_IOWhence
# {
#     SDL_IO_SEEK_SET,  /**< Seek from the beginning of data */
#     SDL_IO_SEEK_CUR,  /**< Seek relative to current read point */
#     SDL_IO_SEEK_END   /**< Seek relative to the end of data */
# } SDL_IOWhence;
SDL_IO_SEEK_SET = 0
SDL_IO_SEEK_CUR = 1
SDL_IO_SEEK_END = 2


# typedef struct SDL_IOStreamInterface
# {
#     /* The version of this interface */
#     Uint32 version;
#     /**
#      *  Return the number of bytes in this SDL_IOStream
#      *
#      *  \return the total size of the data stream, or -1 on error.
#      */
#     Sint64 (SDLCALL *size)(void *userdata);
#     /**
#      *  Seek to `offset` relative to `whence`, one of stdio's whence values:
#      *  SDL_IO_SEEK_SET, SDL_IO_SEEK_CUR, SDL_IO_SEEK_END
#      *
#      *  \return the final offset in the data stream, or -1 on error.
#      */
#     Sint64 (SDLCALL *seek)(void *userdata, Sint64 offset, SDL_IOWhence whence);
#     /**
#      *  Read up to `size` bytes from the data stream to the area pointed
#      *  at by `ptr`.
#      *
#      *  On an incomplete read, you should set `*status` to a value from the
#      *  SDL_IOStatus enum. You do not have to explicitly set this on
#      *  a complete, successful read.
#      *
#      *  \return the number of bytes read
#      */
#     size_t (SDLCALL *read)(void *userdata, void *ptr, size_t size, SDL_IOStatus *status);
#     /**
#      *  Write exactly `size` bytes from the area pointed at by `ptr`
#      *  to data stream.
#      *
#      *  On an incomplete write, you should set `*status` to a value from the
#      *  SDL_IOStatus enum. You do not have to explicitly set this on
#      *  a complete, successful write.
#      *
#      *  \return the number of bytes written
#      */
#     size_t (SDLCALL *write)(void *userdata, const void *ptr, size_t size, SDL_IOStatus *status);
#     /**
#      *  If the stream is buffering, make sure the data is written out.
#      *
#      *  On failure, you should set `*status` to a value from the
#      *  SDL_IOStatus enum. You do not have to explicitly set this on
#      *  a successful flush.
#      *
#      *  \return true if successful or false on write error when flushing data.
#      */
#     bool (SDLCALL *flush)(void *userdata, SDL_IOStatus *status);
#     /**
#      *  Close and free any allocated resources.
#      *
#      *  This does not guarantee file writes will sync to physical media; they
#      *  can be in the system's file cache, waiting to go to disk.
#      *
#      *  The SDL_IOStream is still destroyed even if this fails, so clean up anything
#      *  even if flushing buffers, etc, returns an error.
#      *
#      *  \return true if successful or false on write error when flushing data.
#      */
#     bool (SDLCALL *close)(void *userdata);
# } SDL_IOStreamInterface;
class SDL_IOStreamInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("size", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p)),
        (
            "seek",
            ctypes.CFUNCTYPE(
                ctypes.c_int64, ctypes.c_void_p, ctypes.c_int64, ctypes.c_int
            ),
        ),
        (
            "read",
            ctypes.CFUNCTYPE(
                ctypes.c_size_t,
                ctypes.c_void_p,
                ctypes.c_void_p,
                ctypes.c_size_t,
                ctypes.POINTER(ctypes.c_int),
            ),
        ),
        (
            "write",
            ctypes.CFUNCTYPE(
                ctypes.c_size_t,
                ctypes.c_void_p,
                ctypes.c_void_p,
                ctypes.c_size_t,
                ctypes.POINTER(ctypes.c_int),
            ),
        ),
        (
            "flush",
            ctypes.CFUNCTYPE(
                ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)
            ),
        ),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
    ]


# typedef struct SDL_IOStream SDL_IOStream;


# bool SDL_CloseIO(SDL_IOStream *context);
SDL_CloseIO = libsdl3.SDL_CloseIO
SDL_CloseIO.argtypes = [ctypes.c_void_p]
SDL_CloseIO.restype = ctypes.c_bool


# bool SDL_FlushIO(SDL_IOStream *context);
SDL_FlushIO = libsdl3.SDL_FlushIO
SDL_FlushIO.argtypes = [ctypes.c_void_p]
SDL_FlushIO.restype = ctypes.c_bool


# SDL_PropertiesID SDL_GetIOProperties(SDL_IOStream *context);
SDL_GetIOProperties = libsdl3.SDL_GetIOProperties
SDL_GetIOProperties.argtypes = [ctypes.c_void_p]
SDL_GetIOProperties.restype = ctypes.c_uint32


# Sint64 SDL_GetIOSize(SDL_IOStream *context);
SDL_GetIOSize = libsdl3.SDL_GetIOSize
SDL_GetIOSize.argtypes = [ctypes.c_void_p]
SDL_GetIOSize.restype = ctypes.c_int64


# SDL_IOStatus SDL_GetIOStatus(SDL_IOStream *context);
SDL_GetIOStatus = libsdl3.SDL_GetIOStatus
SDL_GetIOStatus.argtypes = [ctypes.c_void_p]
SDL_GetIOStatus.restype = ctypes.c_int


# SDL_IOStream * SDL_IOFromConstMem(const void *mem, size_t size);
SDL_IOFromConstMem = libsdl3.SDL_IOFromConstMem
SDL_IOFromConstMem.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
SDL_IOFromConstMem.restype = ctypes.c_void_p


# SDL_IOStream * SDL_IOFromDynamicMem(void);
SDL_IOFromDynamicMem = libsdl3.SDL_IOFromDynamicMem
SDL_IOFromDynamicMem.argtypes = []
SDL_IOFromDynamicMem.restype = ctypes.c_void_p


# SDL_IOStream * SDL_IOFromFile(const char *file, const char *mode);
SDL_IOFromFile = libsdl3.SDL_IOFromFile
SDL_IOFromFile.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_IOFromFile.restype = ctypes.c_void_p


# SDL_IOStream * SDL_IOFromMem(void *mem, size_t size);
SDL_IOFromMem = libsdl3.SDL_IOFromMem
SDL_IOFromMem.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
SDL_IOFromMem.restype = ctypes.c_void_p

# size_t SDL_IOprintf(SDL_IOStream *context, const char *fmt, ...);
# size_t SDL_IOvprintf(SDL_IOStream *context, const char *fmt, va_list ap);

# void * SDL_LoadFile(const char *file, size_t *datasize);
SDL_LoadFile = libsdl3.SDL_LoadFile
SDL_LoadFile.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)]
SDL_LoadFile.restype = ctypes.c_void_p


# void * SDL_LoadFile_IO(SDL_IOStream *src, size_t *datasize, bool closeio);
SDL_LoadFile_IO = libsdl3.SDL_LoadFile_IO
SDL_LoadFile_IO.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_size_t),
    ctypes.c_bool,
]
SDL_LoadFile_IO.restype = ctypes.c_void_p


# SDL_IOStream * SDL_OpenIO(const SDL_IOStreamInterface *iface, void *userdata);
SDL_OpenIO = libsdl3.SDL_OpenIO
SDL_OpenIO.argtypes = [ctypes.POINTER(SDL_IOStreamInterface), ctypes.c_void_p]
SDL_OpenIO.restype = ctypes.c_void_p


# size_t SDL_ReadIO(SDL_IOStream *context, void *ptr, size_t size);
SDL_ReadIO = libsdl3.SDL_ReadIO
SDL_ReadIO.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_ReadIO.restype = ctypes.c_size_t


# bool SDL_ReadS16BE(SDL_IOStream *src, Sint16 *value);
SDL_ReadS16BE = libsdl3.SDL_ReadS16BE
SDL_ReadS16BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int16)]
SDL_ReadS16BE.restype = ctypes.c_bool


# bool SDL_ReadS16LE(SDL_IOStream *src, Sint16 *value);
SDL_ReadS16LE = libsdl3.SDL_ReadS16LE
SDL_ReadS16LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int16)]
SDL_ReadS16LE.restype = ctypes.c_bool


# bool SDL_ReadS32BE(SDL_IOStream *src, Sint32 *value);
SDL_ReadS32BE = libsdl3.SDL_ReadS32BE
SDL_ReadS32BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
SDL_ReadS32BE.restype = ctypes.c_bool


# bool SDL_ReadS32LE(SDL_IOStream *src, Sint32 *value);
SDL_ReadS32LE = libsdl3.SDL_ReadS32LE
SDL_ReadS32LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32)]
SDL_ReadS32LE.restype = ctypes.c_bool


# bool SDL_ReadS64BE(SDL_IOStream *src, Sint64 *value);
SDL_ReadS64BE = libsdl3.SDL_ReadS64BE
SDL_ReadS64BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int64)]
SDL_ReadS64BE.restype = ctypes.c_bool


# bool SDL_ReadS64LE(SDL_IOStream *src, Sint64 *value);
SDL_ReadS64LE = libsdl3.SDL_ReadS64LE
SDL_ReadS64LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int64)]
SDL_ReadS64LE.restype = ctypes.c_bool


# bool SDL_ReadS8(SDL_IOStream *src, Sint8 *value);
SDL_ReadS8 = libsdl3.SDL_ReadS8
SDL_ReadS8.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int8)]
SDL_ReadS8.restype = ctypes.c_bool


# bool SDL_ReadU16BE(SDL_IOStream *src, Uint16 *value);
SDL_ReadU16BE = libsdl3.SDL_ReadU16BE
SDL_ReadU16BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint16)]
SDL_ReadU16BE.restype = ctypes.c_bool


# bool SDL_ReadU16LE(SDL_IOStream *src, Uint16 *value);
SDL_ReadU16LE = libsdl3.SDL_ReadU16LE
SDL_ReadU16LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint16)]
SDL_ReadU16LE.restype = ctypes.c_bool


# bool SDL_ReadU32BE(SDL_IOStream *src, Uint32 *value);
SDL_ReadU32BE = libsdl3.SDL_ReadU32BE
SDL_ReadU32BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
SDL_ReadU32BE.restype = ctypes.c_bool


# bool SDL_ReadU32LE(SDL_IOStream *src, Uint32 *value);
SDL_ReadU32LE = libsdl3.SDL_ReadU32LE
SDL_ReadU32LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
SDL_ReadU32LE.restype = ctypes.c_bool


# bool SDL_ReadU64BE(SDL_IOStream *src, Uint64 *value);
SDL_ReadU64BE = libsdl3.SDL_ReadU64BE
SDL_ReadU64BE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64)]
SDL_ReadU64BE.restype = ctypes.c_bool


# bool SDL_ReadU64LE(SDL_IOStream *src, Uint64 *value);
SDL_ReadU64LE = libsdl3.SDL_ReadU64LE
SDL_ReadU64LE.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64)]
SDL_ReadU64LE.restype = ctypes.c_bool


# bool SDL_ReadU8(SDL_IOStream *src, Uint8 *value);
SDL_ReadU8 = libsdl3.SDL_ReadU8
SDL_ReadU8.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8)]
SDL_ReadU8.restype = ctypes.c_bool


# bool SDL_SaveFile(const char *file, const void *data, size_t datasize);
SDL_SaveFile = libsdl3.SDL_SaveFile
SDL_SaveFile.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_SaveFile.restype = ctypes.c_bool


# bool SDL_SaveFile_IO(SDL_IOStream *src, const void *data, size_t datasize, bool closeio);
SDL_SaveFile_IO = libsdl3.SDL_SaveFile_IO
SDL_SaveFile_IO.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_bool,
]
SDL_SaveFile_IO.restype = ctypes.c_bool


# Sint64 SDL_SeekIO(SDL_IOStream *context, Sint64 offset, SDL_IOWhence whence);
SDL_SeekIO = libsdl3.SDL_SeekIO
SDL_SeekIO.argtypes = [ctypes.c_void_p, ctypes.c_int64, ctypes.c_int]
SDL_SeekIO.restype = ctypes.c_int64


# Sint64 SDL_TellIO(SDL_IOStream *context);
SDL_TellIO = libsdl3.SDL_TellIO
SDL_TellIO.argtypes = [ctypes.c_void_p]
SDL_TellIO.restype = ctypes.c_int64


# size_t SDL_WriteIO(SDL_IOStream *context, const void *ptr, size_t size);
SDL_WriteIO = libsdl3.SDL_WriteIO
SDL_WriteIO.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_WriteIO.restype = ctypes.c_size_t


# bool SDL_WriteS16BE(SDL_IOStream *dst, Sint16 value);
SDL_WriteS16BE = libsdl3.SDL_WriteS16BE
SDL_WriteS16BE.argtypes = [ctypes.c_void_p, ctypes.c_int16]
SDL_WriteS16BE.restype = ctypes.c_bool


# bool SDL_WriteS16LE(SDL_IOStream *dst, Sint16 value);
SDL_WriteS16LE = libsdl3.SDL_WriteS16LE
SDL_WriteS16LE.argtypes = [ctypes.c_void_p, ctypes.c_int16]
SDL_WriteS16LE.restype = ctypes.c_bool


# bool SDL_WriteS32BE(SDL_IOStream *dst, Sint32 value);
SDL_WriteS32BE = libsdl3.SDL_WriteS32BE
SDL_WriteS32BE.argtypes = [ctypes.c_void_p, ctypes.c_int32]
SDL_WriteS32BE.restype = ctypes.c_bool


# bool SDL_WriteS32LE(SDL_IOStream *dst, Sint32 value);
SDL_WriteS32LE = libsdl3.SDL_WriteS32LE
SDL_WriteS32LE.argtypes = [ctypes.c_void_p, ctypes.c_int32]
SDL_WriteS32LE.restype = ctypes.c_bool


# bool SDL_WriteS64BE(SDL_IOStream *dst, Sint64 value);
SDL_WriteS64BE = libsdl3.SDL_WriteS64BE
SDL_WriteS64BE.argtypes = [ctypes.c_void_p, ctypes.c_int64]
SDL_WriteS64BE.restype = ctypes.c_bool


# bool SDL_WriteS64LE(SDL_IOStream *dst, Sint64 value);
SDL_WriteS64LE = libsdl3.SDL_WriteS64LE
SDL_WriteS64LE.argtypes = [ctypes.c_void_p, ctypes.c_int64]
SDL_WriteS64LE.restype = ctypes.c_bool


# bool SDL_WriteS8(SDL_IOStream *dst, Sint8 value);
SDL_WriteS8 = libsdl3.SDL_WriteS8
SDL_WriteS8.argtypes = [ctypes.c_void_p, ctypes.c_int8]
SDL_WriteS8.restype = ctypes.c_bool


# bool SDL_WriteU16BE(SDL_IOStream *dst, Uint16 value);
SDL_WriteU16BE = libsdl3.SDL_WriteU16BE
SDL_WriteU16BE.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
SDL_WriteU16BE.restype = ctypes.c_bool


# bool SDL_WriteU16LE(SDL_IOStream *dst, Uint16 value);
SDL_WriteU16LE = libsdl3.SDL_WriteU16LE
SDL_WriteU16LE.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
SDL_WriteU16LE.restype = ctypes.c_bool


# bool SDL_WriteU32BE(SDL_IOStream *dst, Uint32 value);
SDL_WriteU32BE = libsdl3.SDL_WriteU32BE
SDL_WriteU32BE.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_WriteU32BE.restype = ctypes.c_bool


# bool SDL_WriteU32LE(SDL_IOStream *dst, Uint32 value);
SDL_WriteU32LE = libsdl3.SDL_WriteU32LE
SDL_WriteU32LE.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_WriteU32LE.restype = ctypes.c_bool


# bool SDL_WriteU64BE(SDL_IOStream *dst, Uint64 value);
SDL_WriteU64BE = libsdl3.SDL_WriteU64BE
SDL_WriteU64BE.argtypes = [ctypes.c_void_p, ctypes.c_uint64]
SDL_WriteU64BE.restype = ctypes.c_bool


# bool SDL_WriteU64LE(SDL_IOStream *dst, Uint64 value);
SDL_WriteU64LE = libsdl3.SDL_WriteU64LE
SDL_WriteU64LE.argtypes = [ctypes.c_void_p, ctypes.c_uint64]
SDL_WriteU64LE.restype = ctypes.c_bool


# bool SDL_WriteU8(SDL_IOStream *dst, Uint8 value);
SDL_WriteU8 = libsdl3.SDL_WriteU8
SDL_WriteU8.argtypes = [ctypes.c_void_p, ctypes.c_uint8]
SDL_WriteU8.restype = ctypes.c_bool
