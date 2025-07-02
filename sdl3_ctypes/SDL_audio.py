"""
SDL_audio.h
Audio Playback, Recording, and Mixing
Document: https://wiki.libsdl.org/SDL3/CategoryAudio
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_AUDIO_BITSIZE(x)         ((x) & SDL_AUDIO_MASK_BITSIZE)
# #define SDL_AUDIO_BYTESIZE(x)        (SDL_AUDIO_BITSIZE(x) / 8)
# #define SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK ((SDL_AudioDeviceID) 0xFFFFFFFFu)
SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK = 0xFFFFFFFF
# #define SDL_AUDIO_DEVICE_DEFAULT_RECORDING ((SDL_AudioDeviceID) 0xFFFFFFFEu)
SDL_AUDIO_DEVICE_DEFAULT_RECORDING = 0xFFFFFFFE
# #define SDL_AUDIO_FRAMESIZE(x) (SDL_AUDIO_BYTESIZE((x).format) * (x).channels)
# #define SDL_AUDIO_ISBIGENDIAN(x)     ((x) & SDL_AUDIO_MASK_BIG_ENDIAN)
# #define SDL_AUDIO_ISFLOAT(x)         ((x) & SDL_AUDIO_MASK_FLOAT)
# #define SDL_AUDIO_ISINT(x)           (!SDL_AUDIO_ISFLOAT(x))
# #define SDL_AUDIO_ISLITTLEENDIAN(x)  (!SDL_AUDIO_ISBIGENDIAN(x))
# #define SDL_AUDIO_ISSIGNED(x)        ((x) & SDL_AUDIO_MASK_SIGNED)
# #define SDL_AUDIO_ISUNSIGNED(x)      (!SDL_AUDIO_ISSIGNED(x))
# #define SDL_AUDIO_MASK_BIG_ENDIAN    (1u<<12)
SDL_AUDIO_MASK_BIG_ENDIAN = 1 << 12
# #define SDL_AUDIO_MASK_BITSIZE       (0xFFu)
SDL_AUDIO_MASK_BITSIZE = 0xFF
# #define SDL_AUDIO_MASK_FLOAT         (1u<<8)
SDL_AUDIO_MASK_FLOAT = 1 << 8
# #define SDL_AUDIO_MASK_SIGNED        (1u<<15)
SDL_AUDIO_MASK_SIGNED = 1 << 15
# #define SDL_DEFINE_AUDIO_FORMAT(signed, bigendian, flt, size) \
#     (((Uint16)(signed) << 15) | ((Uint16)(bigendian) << 12) | ((Uint16)(flt) << 8) | ((size) & SDL_AUDIO_MASK_BITSIZE))


# typedef enum SDL_AudioFormat
# {
#     SDL_AUDIO_UNKNOWN   = 0x0000u,  /**< Unspecified audio format */
#     SDL_AUDIO_U8        = 0x0008u,  /**< Unsigned 8-bit samples */
#         /* SDL_DEFINE_AUDIO_FORMAT(0, 0, 0, 8), */
#     SDL_AUDIO_S8        = 0x8008u,  /**< Signed 8-bit samples */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 8), */
#     SDL_AUDIO_S16LE     = 0x8010u,  /**< Signed 16-bit samples */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 16), */
#     SDL_AUDIO_S16BE     = 0x9010u,  /**< As above, but big-endian byte order */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 0, 16), */
#     SDL_AUDIO_S32LE     = 0x8020u,  /**< 32-bit integer samples */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 0, 32), */
#     SDL_AUDIO_S32BE     = 0x9020u,  /**< As above, but big-endian byte order */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 0, 32), */
#     SDL_AUDIO_F32LE     = 0x8120u,  /**< 32-bit floating point samples */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 0, 1, 32), */
#     SDL_AUDIO_F32BE     = 0x9120u,  /**< As above, but big-endian byte order */
#         /* SDL_DEFINE_AUDIO_FORMAT(1, 1, 1, 32), */
#     /* These represent the current system's byteorder. */
#     #if SDL_BYTEORDER == SDL_LIL_ENDIAN
#     SDL_AUDIO_S16 = SDL_AUDIO_S16LE,
#     SDL_AUDIO_S32 = SDL_AUDIO_S32LE,
#     SDL_AUDIO_F32 = SDL_AUDIO_F32LE
#     #else
#     SDL_AUDIO_S16 = SDL_AUDIO_S16BE,
#     SDL_AUDIO_S32 = SDL_AUDIO_S32BE,
#     SDL_AUDIO_F32 = SDL_AUDIO_F32BE
#     #endif
# } SDL_AudioFormat;
import sys

SDL_AUDIO_UNKNOWN = 0x0000
SDL_AUDIO_U8 = 0x0008
SDL_AUDIO_S8 = 0x8008
SDL_AUDIO_S16LE = 0x8010
SDL_AUDIO_S16BE = 0x9010
SDL_AUDIO_S32LE = 0x8020
SDL_AUDIO_S32BE = 0x9020
SDL_AUDIO_F32LE = 0x8120
SDL_AUDIO_F32BE = 0x9120
if sys.byteorder == "little":
    SDL_AUDIO_S16 = SDL_AUDIO_S16LE
    SDL_AUDIO_S32 = SDL_AUDIO_S32LE
    SDL_AUDIO_F32 = SDL_AUDIO_F32LE
else:
    SDL_AUDIO_S16 = SDL_AUDIO_S16BE
    SDL_AUDIO_S32 = SDL_AUDIO_S32BE
    SDL_AUDIO_F32 = SDL_AUDIO_F32BE


# typedef struct SDL_AudioSpec
# {
#     SDL_AudioFormat format;     /**< Audio data format */
#     int channels;               /**< Number of channels: 1 mono, 2 stereo, etc */
#     int freq;                   /**< sample rate: sample frames per second */
# } SDL_AudioSpec;
class SDL_AudioSpec(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_int),
        ("channels", ctypes.c_int),
        ("freq", ctypes.c_int),
    ]


# typedef Uint32 SDL_AudioDeviceID;

# typedef void (SDLCALL *SDL_AudioIterationCallback)(void *userdata, SDL_AudioDeviceID devid, bool start);
SDL_AudioIterationCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_bool
)


# typedef void (SDLCALL *SDL_AudioPostmixCallback)(void *userdata, const SDL_AudioSpec *spec, float *buffer, int buflen);
SDL_AudioPostmixCallback = ctypes.CFUNCTYPE(
    None,
    ctypes.c_void_p,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
)

# typedef struct SDL_AudioStream SDL_AudioStream;

# typedef void (SDLCALL *SDL_AudioStreamCallback)(void *userdata, SDL_AudioStream *stream, int additional_amount, int total_amount);
SDL_AudioStreamCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int
)


# typedef void (SDLCALL *SDL_AudioStreamDataCompleteCallback)(void *userdata, const void *buf, int buflen);
SDL_AudioStreamDataCompleteCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int
)


# bool SDL_AudioDevicePaused(SDL_AudioDeviceID devid);
SDL_AudioDevicePaused = libsdl3.SDL_AudioDevicePaused
SDL_AudioDevicePaused.argtypes = [ctypes.c_uint32]
SDL_AudioDevicePaused.restype = ctypes.c_bool


# bool SDL_AudioStreamDevicePaused(SDL_AudioStream *stream);
SDL_AudioStreamDevicePaused = libsdl3.SDL_AudioStreamDevicePaused
SDL_AudioStreamDevicePaused.argtypes = [ctypes.c_void_p]
SDL_AudioStreamDevicePaused.restype = ctypes.c_bool


# bool SDL_BindAudioStream(SDL_AudioDeviceID devid, SDL_AudioStream *stream);
SDL_BindAudioStream = libsdl3.SDL_BindAudioStream
SDL_BindAudioStream.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
SDL_BindAudioStream.restype = ctypes.c_bool


# bool SDL_BindAudioStreams(SDL_AudioDeviceID devid, SDL_AudioStream * const *streams, int num_streams);
SDL_BindAudioStreams = libsdl3.SDL_BindAudioStreams
SDL_BindAudioStreams.argtypes = [
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_int,
]
SDL_BindAudioStreams.restype = ctypes.c_bool


# bool SDL_ClearAudioStream(SDL_AudioStream *stream);
SDL_ClearAudioStream = libsdl3.SDL_ClearAudioStream
SDL_ClearAudioStream.argtypes = [ctypes.c_void_p]
SDL_ClearAudioStream.restype = ctypes.c_bool


# void SDL_CloseAudioDevice(SDL_AudioDeviceID devid);
SDL_CloseAudioDevice = libsdl3.SDL_CloseAudioDevice
SDL_CloseAudioDevice.argtypes = [ctypes.c_uint32]
SDL_CloseAudioDevice.restype = None


# bool SDL_ConvertAudioSamples(const SDL_AudioSpec *src_spec, const Uint8 *src_data, int src_len, const SDL_AudioSpec *dst_spec, Uint8 **dst_data, int *dst_len);
SDL_ConvertAudioSamples = libsdl3.SDL_ConvertAudioSamples
SDL_ConvertAudioSamples.argtypes = [
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
    ctypes.POINTER(ctypes.c_int),
]
SDL_ConvertAudioSamples.restype = ctypes.c_bool


# SDL_AudioStream * SDL_CreateAudioStream(const SDL_AudioSpec *src_spec, const SDL_AudioSpec *dst_spec);
SDL_CreateAudioStream = libsdl3.SDL_CreateAudioStream
SDL_CreateAudioStream.argtypes = [
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(SDL_AudioSpec),
]
SDL_CreateAudioStream.restype = ctypes.c_void_p


# void SDL_DestroyAudioStream(SDL_AudioStream *stream);
SDL_DestroyAudioStream = libsdl3.SDL_DestroyAudioStream
SDL_DestroyAudioStream.argtypes = [ctypes.c_void_p]
SDL_DestroyAudioStream.restype = None


# bool SDL_FlushAudioStream(SDL_AudioStream *stream);
SDL_FlushAudioStream = libsdl3.SDL_FlushAudioStream
SDL_FlushAudioStream.argtypes = [ctypes.c_void_p]
SDL_FlushAudioStream.restype = ctypes.c_bool


# int * SDL_GetAudioDeviceChannelMap(SDL_AudioDeviceID devid, int *count);
SDL_GetAudioDeviceChannelMap = libsdl3.SDL_GetAudioDeviceChannelMap
SDL_GetAudioDeviceChannelMap.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_int)]
SDL_GetAudioDeviceChannelMap.restype = ctypes.POINTER(ctypes.c_int)


# bool SDL_GetAudioDeviceFormat(SDL_AudioDeviceID devid, SDL_AudioSpec *spec, int *sample_frames);
SDL_GetAudioDeviceFormat = libsdl3.SDL_GetAudioDeviceFormat
SDL_GetAudioDeviceFormat.argtypes = [
    ctypes.c_uint32,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetAudioDeviceFormat.restype = ctypes.c_bool


# float SDL_GetAudioDeviceGain(SDL_AudioDeviceID devid);
SDL_GetAudioDeviceGain = libsdl3.SDL_GetAudioDeviceGain
SDL_GetAudioDeviceGain.argtypes = [ctypes.c_uint32]
SDL_GetAudioDeviceGain.restype = ctypes.c_float


# const char * SDL_GetAudioDeviceName(SDL_AudioDeviceID devid);
SDL_GetAudioDeviceName = libsdl3.SDL_GetAudioDeviceName
SDL_GetAudioDeviceName.argtypes = [ctypes.c_uint32]
SDL_GetAudioDeviceName.restype = ctypes.c_char_p


# const char * SDL_GetAudioDriver(int index);
SDL_GetAudioDriver = libsdl3.SDL_GetAudioDriver
SDL_GetAudioDriver.argtypes = [ctypes.c_int]
SDL_GetAudioDriver.restype = ctypes.c_char_p


# const char * SDL_GetAudioFormatName(SDL_AudioFormat format);
SDL_GetAudioFormatName = libsdl3.SDL_GetAudioFormatName
SDL_GetAudioFormatName.argtypes = [ctypes.c_int]
SDL_GetAudioFormatName.restype = ctypes.c_char_p


# SDL_AudioDeviceID * SDL_GetAudioPlaybackDevices(int *count);
SDL_GetAudioPlaybackDevices = libsdl3.SDL_GetAudioPlaybackDevices
SDL_GetAudioPlaybackDevices.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetAudioPlaybackDevices.restype = ctypes.POINTER(ctypes.c_uint32)


# SDL_AudioDeviceID * SDL_GetAudioRecordingDevices(int *count);
SDL_GetAudioRecordingDevices = libsdl3.SDL_GetAudioRecordingDevices
SDL_GetAudioRecordingDevices.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetAudioRecordingDevices.restype = ctypes.POINTER(ctypes.c_uint32)


# int SDL_GetAudioStreamAvailable(SDL_AudioStream *stream);
SDL_GetAudioStreamAvailable = libsdl3.SDL_GetAudioStreamAvailable
SDL_GetAudioStreamAvailable.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamAvailable.restype = ctypes.c_int


# int SDL_GetAudioStreamData(SDL_AudioStream *stream, void *buf, int len);
SDL_GetAudioStreamData = libsdl3.SDL_GetAudioStreamData
SDL_GetAudioStreamData.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
SDL_GetAudioStreamData.restype = ctypes.c_int


# SDL_AudioDeviceID SDL_GetAudioStreamDevice(SDL_AudioStream *stream);
SDL_GetAudioStreamDevice = libsdl3.SDL_GetAudioStreamDevice
SDL_GetAudioStreamDevice.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamDevice.restype = ctypes.c_uint32


# bool SDL_GetAudioStreamFormat(SDL_AudioStream *stream, SDL_AudioSpec *src_spec, SDL_AudioSpec *dst_spec);
SDL_GetAudioStreamFormat = libsdl3.SDL_GetAudioStreamFormat
SDL_GetAudioStreamFormat.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(SDL_AudioSpec),
]
SDL_GetAudioStreamFormat.restype = ctypes.c_bool


# float SDL_GetAudioStreamFrequencyRatio(SDL_AudioStream *stream);
SDL_GetAudioStreamFrequencyRatio = libsdl3.SDL_GetAudioStreamFrequencyRatio
SDL_GetAudioStreamFrequencyRatio.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamFrequencyRatio.restype = ctypes.c_float


# float SDL_GetAudioStreamGain(SDL_AudioStream *stream);
SDL_GetAudioStreamGain = libsdl3.SDL_GetAudioStreamGain
SDL_GetAudioStreamGain.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamGain.restype = ctypes.c_float


# int * SDL_GetAudioStreamInputChannelMap(SDL_AudioStream *stream, int *count);
SDL_GetAudioStreamInputChannelMap = libsdl3.SDL_GetAudioStreamInputChannelMap
SDL_GetAudioStreamInputChannelMap.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetAudioStreamInputChannelMap.restype = ctypes.POINTER(ctypes.c_int)


# int * SDL_GetAudioStreamOutputChannelMap(SDL_AudioStream *stream, int *count);
SDL_GetAudioStreamOutputChannelMap = libsdl3.SDL_GetAudioStreamOutputChannelMap
SDL_GetAudioStreamOutputChannelMap.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetAudioStreamOutputChannelMap.restype = ctypes.POINTER(ctypes.c_int)


# SDL_PropertiesID SDL_GetAudioStreamProperties(SDL_AudioStream *stream);
SDL_GetAudioStreamProperties = libsdl3.SDL_GetAudioStreamProperties
SDL_GetAudioStreamProperties.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamProperties.restype = ctypes.c_uint32


# int SDL_GetAudioStreamQueued(SDL_AudioStream *stream);
SDL_GetAudioStreamQueued = libsdl3.SDL_GetAudioStreamQueued
SDL_GetAudioStreamQueued.argtypes = [ctypes.c_void_p]
SDL_GetAudioStreamQueued.restype = ctypes.c_int


# const char * SDL_GetCurrentAudioDriver(void);
SDL_GetCurrentAudioDriver = libsdl3.SDL_GetCurrentAudioDriver
SDL_GetCurrentAudioDriver.argtypes = []
SDL_GetCurrentAudioDriver.restype = ctypes.c_char_p


# int SDL_GetNumAudioDrivers(void);
SDL_GetNumAudioDrivers = libsdl3.SDL_GetNumAudioDrivers
SDL_GetNumAudioDrivers.argtypes = []
SDL_GetNumAudioDrivers.restype = ctypes.c_int


# int SDL_GetSilenceValueForFormat(SDL_AudioFormat format);
SDL_GetSilenceValueForFormat = libsdl3.SDL_GetSilenceValueForFormat
SDL_GetSilenceValueForFormat.argtypes = [ctypes.c_int]
SDL_GetSilenceValueForFormat.restype = ctypes.c_int


# bool SDL_IsAudioDevicePhysical(SDL_AudioDeviceID devid);
SDL_IsAudioDevicePhysical = libsdl3.SDL_IsAudioDevicePhysical
SDL_IsAudioDevicePhysical.argtypes = [ctypes.c_uint32]
SDL_IsAudioDevicePhysical.restype = ctypes.c_bool


# bool SDL_IsAudioDevicePlayback(SDL_AudioDeviceID devid);
SDL_IsAudioDevicePlayback = libsdl3.SDL_IsAudioDevicePlayback
SDL_IsAudioDevicePlayback.argtypes = [ctypes.c_uint32]
SDL_IsAudioDevicePlayback.restype = ctypes.c_bool


# bool SDL_LoadWAV(const char *path, SDL_AudioSpec *spec, Uint8 **audio_buf, Uint32 *audio_len);
SDL_LoadWAV = libsdl3.SDL_LoadWAV
SDL_LoadWAV.argtypes = [
    ctypes.c_char_p,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_LoadWAV.restype = ctypes.c_bool


# bool SDL_LoadWAV_IO(SDL_IOStream *src, bool closeio, SDL_AudioSpec *spec, Uint8 **audio_buf, Uint32 *audio_len);
SDL_LoadWAV_IO = libsdl3.SDL_LoadWAV_IO
SDL_LoadWAV_IO.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_LoadWAV_IO.restype = ctypes.c_bool


# bool SDL_LockAudioStream(SDL_AudioStream *stream);
SDL_LockAudioStream = libsdl3.SDL_LockAudioStream
SDL_LockAudioStream.argtypes = [ctypes.c_void_p]
SDL_LockAudioStream.restype = ctypes.c_bool


# bool SDL_MixAudio(Uint8 *dst, const Uint8 *src, SDL_AudioFormat format, Uint32 len, float volume);
SDL_MixAudio = libsdl3.SDL_MixAudio
SDL_MixAudio.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.c_uint32,
    ctypes.c_float,
]
SDL_MixAudio.restype = ctypes.c_bool


# SDL_AudioDeviceID SDL_OpenAudioDevice(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);
SDL_OpenAudioDevice = libsdl3.SDL_OpenAudioDevice
SDL_OpenAudioDevice.argtypes = [ctypes.c_uint32, ctypes.POINTER(SDL_AudioSpec)]
SDL_OpenAudioDevice.restype = ctypes.c_uint32


# SDL_AudioStream * SDL_OpenAudioDeviceStream(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec, SDL_AudioStreamCallback callback, void *userdata);
SDL_OpenAudioDeviceStream = libsdl3.SDL_OpenAudioDeviceStream
SDL_OpenAudioDeviceStream.argtypes = [
    ctypes.c_uint32,
    ctypes.POINTER(SDL_AudioSpec),
    SDL_AudioStreamCallback,
    ctypes.c_void_p,
]
SDL_OpenAudioDeviceStream.restype = ctypes.c_void_p


# bool SDL_PauseAudioDevice(SDL_AudioDeviceID devid);
SDL_PauseAudioDevice = libsdl3.SDL_PauseAudioDevice
SDL_PauseAudioDevice.argtypes = [ctypes.c_uint32]
SDL_PauseAudioDevice.restype = ctypes.c_bool


# bool SDL_PauseAudioStreamDevice(SDL_AudioStream *stream);
SDL_PauseAudioStreamDevice = libsdl3.SDL_PauseAudioStreamDevice
SDL_PauseAudioStreamDevice.argtypes = [ctypes.c_void_p]
SDL_PauseAudioStreamDevice.restype = ctypes.c_bool


# bool SDL_PutAudioStreamData(SDL_AudioStream *stream, const void *buf, int len);
SDL_PutAudioStreamData = libsdl3.SDL_PutAudioStreamData
SDL_PutAudioStreamData.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
SDL_PutAudioStreamData.restype = ctypes.c_bool


# bool SDL_PutAudioStreamDataNoCopy(SDL_AudioStream *stream, const void *buf, int len, SDL_AudioStreamDataCompleteCallback callback, void *userdata);
SDL_PutAudioStreamDataNoCopy = libsdl3.SDL_PutAudioStreamDataNoCopy
SDL_PutAudioStreamDataNoCopy.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
    SDL_AudioStreamDataCompleteCallback,
    ctypes.c_void_p,
]
SDL_PutAudioStreamDataNoCopy.restype = ctypes.c_bool


# bool SDL_PutAudioStreamPlanarData(SDL_AudioStream *stream, const void * const *channel_buffers, int num_channels, int num_samples);
SDL_PutAudioStreamPlanarData = libsdl3.SDL_PutAudioStreamPlanarData
SDL_PutAudioStreamPlanarData.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_int,
    ctypes.c_int,
]
SDL_PutAudioStreamPlanarData.restype = ctypes.c_bool


# bool SDL_ResumeAudioDevice(SDL_AudioDeviceID devid);
SDL_ResumeAudioDevice = libsdl3.SDL_ResumeAudioDevice
SDL_ResumeAudioDevice.argtypes = [ctypes.c_uint32]
SDL_ResumeAudioDevice.restype = ctypes.c_bool


# bool SDL_ResumeAudioStreamDevice(SDL_AudioStream *stream);
SDL_ResumeAudioStreamDevice = libsdl3.SDL_ResumeAudioStreamDevice
SDL_ResumeAudioStreamDevice.argtypes = [ctypes.c_void_p]
SDL_ResumeAudioStreamDevice.restype = ctypes.c_bool


# bool SDL_SetAudioDeviceGain(SDL_AudioDeviceID devid, float gain);
SDL_SetAudioDeviceGain = libsdl3.SDL_SetAudioDeviceGain
SDL_SetAudioDeviceGain.argtypes = [ctypes.c_uint32, ctypes.c_float]
SDL_SetAudioDeviceGain.restype = ctypes.c_bool


# bool SDL_SetAudioIterationCallbacks(SDL_AudioDeviceID devid, SDL_AudioIterationCallback start, SDL_AudioIterationCallback end, void *userdata);
SDL_SetAudioIterationCallbacks = libsdl3.SDL_SetAudioIterationCallbacks
SDL_SetAudioIterationCallbacks.argtypes = [
    ctypes.c_uint32,
    SDL_AudioIterationCallback,
    SDL_AudioIterationCallback,
    ctypes.c_void_p,
]
SDL_SetAudioIterationCallbacks.restype = ctypes.c_bool


# bool SDL_SetAudioPostmixCallback(SDL_AudioDeviceID devid, SDL_AudioPostmixCallback callback, void *userdata);
SDL_SetAudioPostmixCallback = libsdl3.SDL_SetAudioPostmixCallback
SDL_SetAudioPostmixCallback.argtypes = [
    ctypes.c_uint32,
    SDL_AudioPostmixCallback,
    ctypes.c_void_p,
]
SDL_SetAudioPostmixCallback.restype = ctypes.c_bool


# bool SDL_SetAudioStreamFormat(SDL_AudioStream *stream, const SDL_AudioSpec *src_spec, const SDL_AudioSpec *dst_spec);
SDL_SetAudioStreamFormat = libsdl3.SDL_SetAudioStreamFormat
SDL_SetAudioStreamFormat.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_AudioSpec),
    ctypes.POINTER(SDL_AudioSpec),
]
SDL_SetAudioStreamFormat.restype = ctypes.c_bool


# bool SDL_SetAudioStreamFrequencyRatio(SDL_AudioStream *stream, float ratio);
SDL_SetAudioStreamFrequencyRatio = libsdl3.SDL_SetAudioStreamFrequencyRatio
SDL_SetAudioStreamFrequencyRatio.argtypes = [ctypes.c_void_p, ctypes.c_float]
SDL_SetAudioStreamFrequencyRatio.restype = ctypes.c_bool


# bool SDL_SetAudioStreamGain(SDL_AudioStream *stream, float gain);
SDL_SetAudioStreamGain = libsdl3.SDL_SetAudioStreamGain
SDL_SetAudioStreamGain.argtypes = [ctypes.c_void_p, ctypes.c_float]
SDL_SetAudioStreamGain.restype = ctypes.c_bool


# bool SDL_SetAudioStreamGetCallback(SDL_AudioStream *stream, SDL_AudioStreamCallback callback, void *userdata);
SDL_SetAudioStreamGetCallback = libsdl3.SDL_SetAudioStreamGetCallback
SDL_SetAudioStreamGetCallback.argtypes = [
    ctypes.c_void_p,
    SDL_AudioStreamCallback,
    ctypes.c_void_p,
]
SDL_SetAudioStreamGetCallback.restype = ctypes.c_bool


# bool SDL_SetAudioStreamInputChannelMap(SDL_AudioStream *stream, const int *chmap, int count);
SDL_SetAudioStreamInputChannelMap = libsdl3.SDL_SetAudioStreamInputChannelMap
SDL_SetAudioStreamInputChannelMap.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
SDL_SetAudioStreamInputChannelMap.restype = ctypes.c_bool


# bool SDL_SetAudioStreamOutputChannelMap(SDL_AudioStream *stream, const int *chmap, int count);
SDL_SetAudioStreamOutputChannelMap = libsdl3.SDL_SetAudioStreamOutputChannelMap
SDL_SetAudioStreamOutputChannelMap.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
SDL_SetAudioStreamOutputChannelMap.restype = ctypes.c_bool


# bool SDL_SetAudioStreamPutCallback(SDL_AudioStream *stream, SDL_AudioStreamCallback callback, void *userdata);
SDL_SetAudioStreamPutCallback = libsdl3.SDL_SetAudioStreamPutCallback
SDL_SetAudioStreamPutCallback.argtypes = [
    ctypes.c_void_p,
    SDL_AudioStreamCallback,
    ctypes.c_void_p,
]
SDL_SetAudioStreamPutCallback.restype = ctypes.c_bool


# void SDL_UnbindAudioStream(SDL_AudioStream *stream);
SDL_UnbindAudioStream = libsdl3.SDL_UnbindAudioStream
SDL_UnbindAudioStream.argtypes = [ctypes.c_void_p]
SDL_UnbindAudioStream.restype = None


# void SDL_UnbindAudioStreams(SDL_AudioStream * const *streams, int num_streams);
SDL_UnbindAudioStreams = libsdl3.SDL_UnbindAudioStreams
SDL_UnbindAudioStreams.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_int,
]
SDL_UnbindAudioStreams.restype = None


# bool SDL_UnlockAudioStream(SDL_AudioStream *stream);
SDL_UnlockAudioStream = libsdl3.SDL_UnlockAudioStream
SDL_UnlockAudioStream.argtypes = [ctypes.c_void_p]
SDL_UnlockAudioStream.restype = ctypes.c_bool
