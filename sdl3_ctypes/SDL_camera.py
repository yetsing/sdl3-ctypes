"""
SDL_camera.h
Camera Support
Document: https://wiki.libsdl.org/SDL3/CategoryCamera
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_surface import SDL_Surface

# typedef enum SDL_CameraPosition
# {
#     SDL_CAMERA_POSITION_UNKNOWN,
#     SDL_CAMERA_POSITION_FRONT_FACING,
#     SDL_CAMERA_POSITION_BACK_FACING
# } SDL_CameraPosition;
SDL_CAMERA_POSITION_UNKNOWN = 0
SDL_CAMERA_POSITION_FRONT_FACING = 1
SDL_CAMERA_POSITION_BACK_FACING = 2


# typedef struct SDL_CameraSpec
# {
#     SDL_PixelFormat format;     /**< Frame format */
#     SDL_Colorspace colorspace;  /**< Frame colorspace */
#     int width;                  /**< Frame width */
#     int height;                 /**< Frame height */
#     int framerate_numerator;     /**< Frame rate numerator ((num / denom) == FPS, (denom / num) == duration in seconds) */
#     int framerate_denominator;   /**< Frame rate demoninator ((num / denom) == FPS, (denom / num) == duration in seconds) */
# } SDL_CameraSpec;
class SDL_CameraSpec(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_int),
        ("colorspace", ctypes.c_int),
        ("width", ctypes.c_int),
        ("height", ctypes.c_int),
        ("framerate_numerator", ctypes.c_int),
        ("framerate_denominator", ctypes.c_int),
    ]


# typedef struct SDL_Camera SDL_Camera;
# typedef Uint32 SDL_CameraID;


# SDL_Surface * SDL_AcquireCameraFrame(SDL_Camera *camera, Uint64 *timestampNS);
SDL_AcquireCameraFrame = libsdl3.SDL_AcquireCameraFrame
SDL_AcquireCameraFrame.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64)]
SDL_AcquireCameraFrame.restype = ctypes.POINTER(SDL_Surface)


# void SDL_CloseCamera(SDL_Camera *camera);
SDL_CloseCamera = libsdl3.SDL_CloseCamera
SDL_CloseCamera.argtypes = [ctypes.c_void_p]
SDL_CloseCamera.restype = None


# const char * SDL_GetCameraDriver(int index);
SDL_GetCameraDriver = libsdl3.SDL_GetCameraDriver
SDL_GetCameraDriver.argtypes = [ctypes.c_int]
SDL_GetCameraDriver.restype = ctypes.c_char_p


# bool SDL_GetCameraFormat(SDL_Camera *camera, SDL_CameraSpec *spec);
SDL_GetCameraFormat = libsdl3.SDL_GetCameraFormat
SDL_GetCameraFormat.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_CameraSpec)]
SDL_GetCameraFormat.restype = ctypes.c_bool


# SDL_CameraID SDL_GetCameraID(SDL_Camera *camera);
SDL_GetCameraID = libsdl3.SDL_GetCameraID
SDL_GetCameraID.argtypes = [ctypes.c_void_p]
SDL_GetCameraID.restype = ctypes.c_uint32


# const char * SDL_GetCameraName(SDL_CameraID instance_id);
SDL_GetCameraName = libsdl3.SDL_GetCameraName
SDL_GetCameraName.argtypes = [ctypes.c_uint32]
SDL_GetCameraName.restype = ctypes.c_char_p


# int SDL_GetCameraPermissionState(SDL_Camera *camera);
SDL_GetCameraPermissionState = libsdl3.SDL_GetCameraPermissionState
SDL_GetCameraPermissionState.argtypes = [ctypes.c_void_p]
SDL_GetCameraPermissionState.restype = ctypes.c_int


# SDL_CameraPosition SDL_GetCameraPosition(SDL_CameraID instance_id);
SDL_GetCameraPosition = libsdl3.SDL_GetCameraPosition
SDL_GetCameraPosition.argtypes = [ctypes.c_uint32]
SDL_GetCameraPosition.restype = ctypes.c_int


# SDL_PropertiesID SDL_GetCameraProperties(SDL_Camera *camera);
SDL_GetCameraProperties = libsdl3.SDL_GetCameraProperties
SDL_GetCameraProperties.argtypes = [ctypes.c_void_p]
SDL_GetCameraProperties.restype = ctypes.c_uint32


# SDL_CameraID * SDL_GetCameras(int *count);
SDL_GetCameras = libsdl3.SDL_GetCameras
SDL_GetCameras.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetCameras.restype = ctypes.POINTER(ctypes.c_uint32)


# SDL_CameraSpec ** SDL_GetCameraSupportedFormats(SDL_CameraID instance_id, int *count);
SDL_GetCameraSupportedFormats = libsdl3.SDL_GetCameraSupportedFormats
SDL_GetCameraSupportedFormats.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_int)]
SDL_GetCameraSupportedFormats.restype = ctypes.POINTER(ctypes.POINTER(SDL_CameraSpec))


# const char * SDL_GetCurrentCameraDriver(void);
SDL_GetCurrentCameraDriver = libsdl3.SDL_GetCurrentCameraDriver
SDL_GetCurrentCameraDriver.argtypes = []
SDL_GetCurrentCameraDriver.restype = ctypes.c_char_p


# int SDL_GetNumCameraDrivers(void);
SDL_GetNumCameraDrivers = libsdl3.SDL_GetNumCameraDrivers
SDL_GetNumCameraDrivers.argtypes = []
SDL_GetNumCameraDrivers.restype = ctypes.c_int


# SDL_Camera * SDL_OpenCamera(SDL_CameraID instance_id, const SDL_CameraSpec *spec);
SDL_OpenCamera = libsdl3.SDL_OpenCamera
SDL_OpenCamera.argtypes = [ctypes.c_uint32, ctypes.POINTER(SDL_CameraSpec)]
SDL_OpenCamera.restype = ctypes.c_void_p


# void SDL_ReleaseCameraFrame(SDL_Camera *camera, SDL_Surface *frame);
SDL_ReleaseCameraFrame = libsdl3.SDL_ReleaseCameraFrame
SDL_ReleaseCameraFrame.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)]
SDL_ReleaseCameraFrame.restype = None
