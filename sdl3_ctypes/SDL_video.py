"""
SDL_video.h
Display and Window Management
Document: https://wiki.libsdl.org/SDL3/CategoryVideo
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_rect import SDL_Point, SDL_Rect
from sdl3_ctypes.SDL_stdinc import SDL_FunctionPointer
from sdl3_ctypes.SDL_surface import SDL_Surface

# #define SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER "SDL.video.wayland.wl_display"
SDL_PROP_GLOBAL_VIDEO_WAYLAND_WL_DISPLAY_POINTER = "SDL.video.wayland.wl_display"
# #define SDL_WINDOWPOS_CENTERED         SDL_WINDOWPOS_CENTERED_DISPLAY(0)
# #define SDL_WINDOWPOS_CENTERED_DISPLAY(X)  (SDL_WINDOWPOS_CENTERED_MASK|(X))
# #define SDL_WINDOWPOS_CENTERED_MASK    0x2FFF0000u
SDL_WINDOWPOS_CENTERED_MASK = 0x2FFF0000
# #define SDL_WINDOWPOS_ISCENTERED(X)    \
#             (((X)&0xFFFF0000) == SDL_WINDOWPOS_CENTERED_MASK)
# #define SDL_WINDOWPOS_ISUNDEFINED(X)    (((X)&0xFFFF0000) == SDL_WINDOWPOS_UNDEFINED_MASK)
# #define SDL_WINDOWPOS_UNDEFINED         SDL_WINDOWPOS_UNDEFINED_DISPLAY(0)
# #define SDL_WINDOWPOS_UNDEFINED_DISPLAY(X)  (SDL_WINDOWPOS_UNDEFINED_MASK|(X))
# #define SDL_WINDOWPOS_UNDEFINED_MASK    0x1FFF0000u
SDL_WINDOWPOS_UNDEFINED_MASK = 0x1FFF0000


# typedef enum SDL_DisplayOrientation
# {
#     SDL_ORIENTATION_UNKNOWN,            /**< The display orientation can't be determined */
#     SDL_ORIENTATION_LANDSCAPE,          /**< The display is in landscape mode, with the right side up, relative to portrait mode */
#     SDL_ORIENTATION_LANDSCAPE_FLIPPED,  /**< The display is in landscape mode, with the left side up, relative to portrait mode */
#     SDL_ORIENTATION_PORTRAIT,           /**< The display is in portrait mode */
#     SDL_ORIENTATION_PORTRAIT_FLIPPED    /**< The display is in portrait mode, upside down */
# } SDL_DisplayOrientation;
SDL_ORIENTATION_UNKNOWN = 0
SDL_ORIENTATION_LANDSCAPE = 1
SDL_ORIENTATION_LANDSCAPE_FLIPPED = 2
SDL_ORIENTATION_PORTRAIT = 3
SDL_ORIENTATION_PORTRAIT_FLIPPED = 4
# typedef enum SDL_FlashOperation
# {
#     SDL_FLASH_CANCEL,                   /**< Cancel any window flash state */
#     SDL_FLASH_BRIEFLY,                  /**< Flash the window briefly to get attention */
#     SDL_FLASH_UNTIL_FOCUSED             /**< Flash the window until it gets focus */
# } SDL_FlashOperation;
SDL_FLASH_CANCEL = 0
SDL_FLASH_BRIEFLY = 1
SDL_FLASH_UNTIL_FOCUSED = 2
# typedef enum SDL_GLAttr
# {
#     SDL_GL_RED_SIZE,                    /**< the minimum number of bits for the red channel of the color buffer; defaults to 8. */
#     SDL_GL_GREEN_SIZE,                  /**< the minimum number of bits for the green channel of the color buffer; defaults to 8. */
#     SDL_GL_BLUE_SIZE,                   /**< the minimum number of bits for the blue channel of the color buffer; defaults to 8. */
#     SDL_GL_ALPHA_SIZE,                  /**< the minimum number of bits for the alpha channel of the color buffer; defaults to 8. */
#     SDL_GL_BUFFER_SIZE,                 /**< the minimum number of bits for frame buffer size; defaults to 0. */
#     SDL_GL_DOUBLEBUFFER,                /**< whether the output is single or double buffered; defaults to double buffering on. */
#     SDL_GL_DEPTH_SIZE,                  /**< the minimum number of bits in the depth buffer; defaults to 16. */
#     SDL_GL_STENCIL_SIZE,                /**< the minimum number of bits in the stencil buffer; defaults to 0. */
#     SDL_GL_ACCUM_RED_SIZE,              /**< the minimum number of bits for the red channel of the accumulation buffer; defaults to 0. */
#     SDL_GL_ACCUM_GREEN_SIZE,            /**< the minimum number of bits for the green channel of the accumulation buffer; defaults to 0. */
#     SDL_GL_ACCUM_BLUE_SIZE,             /**< the minimum number of bits for the blue channel of the accumulation buffer; defaults to 0. */
#     SDL_GL_ACCUM_ALPHA_SIZE,            /**< the minimum number of bits for the alpha channel of the accumulation buffer; defaults to 0. */
#     SDL_GL_STEREO,                      /**< whether the output is stereo 3D; defaults to off. */
#     SDL_GL_MULTISAMPLEBUFFERS,          /**< the number of buffers used for multisample anti-aliasing; defaults to 0. */
#     SDL_GL_MULTISAMPLESAMPLES,          /**< the number of samples used around the current pixel used for multisample anti-aliasing. */
#     SDL_GL_ACCELERATED_VISUAL,          /**< set to 1 to require hardware acceleration, set to 0 to force software rendering; defaults to allow either. */
#     SDL_GL_RETAINED_BACKING,            /**< not used (deprecated). */
#     SDL_GL_CONTEXT_MAJOR_VERSION,       /**< OpenGL context major version. */
#     SDL_GL_CONTEXT_MINOR_VERSION,       /**< OpenGL context minor version. */
#     SDL_GL_CONTEXT_FLAGS,               /**< some combination of 0 or more of elements of the SDL_GLContextFlag enumeration; defaults to 0. */
#     SDL_GL_CONTEXT_PROFILE_MASK,        /**< type of GL context (Core, Compatibility, ES). See SDL_GLProfile; default value depends on platform. */
#     SDL_GL_SHARE_WITH_CURRENT_CONTEXT,  /**< OpenGL context sharing; defaults to 0. */
#     SDL_GL_FRAMEBUFFER_SRGB_CAPABLE,    /**< requests sRGB capable visual; defaults to 0. */
#     SDL_GL_CONTEXT_RELEASE_BEHAVIOR,    /**< sets context the release behavior. See SDL_GLContextReleaseFlag; defaults to FLUSH. */
#     SDL_GL_CONTEXT_RESET_NOTIFICATION,  /**< set context reset notification. See SDL_GLContextResetNotification; defaults to NO_NOTIFICATION. */
#     SDL_GL_CONTEXT_NO_ERROR,
#     SDL_GL_FLOATBUFFERS,
#     SDL_GL_EGL_PLATFORM
# } SDL_GLAttr;
SDL_GL_RED_SIZE = 0
SDL_GL_GREEN_SIZE = 1
SDL_GL_BLUE_SIZE = 2
SDL_GL_ALPHA_SIZE = 3
SDL_GL_BUFFER_SIZE = 4
SDL_GL_DOUBLEBUFFER = 5
SDL_GL_DEPTH_SIZE = 6
SDL_GL_STENCIL_SIZE = 7
SDL_GL_ACCUM_RED_SIZE = 8
SDL_GL_ACCUM_GREEN_SIZE = 9
SDL_GL_ACCUM_BLUE_SIZE = 10
SDL_GL_ACCUM_ALPHA_SIZE = 11
SDL_GL_STEREO = 12
SDL_GL_MULTISAMPLEBUFFERS = 13
SDL_GL_MULTISAMPLESAMPLES = 14
SDL_GL_ACCELERATED_VISUAL = 15
SDL_GL_RETAINED_BACKING = 16
SDL_GL_CONTEXT_MAJOR_VERSION = 17
SDL_GL_CONTEXT_MINOR_VERSION = 18
SDL_GL_CONTEXT_FLAGS = 19
SDL_GL_CONTEXT_PROFILE_MASK = 20
SDL_GL_SHARE_WITH_CURRENT_CONTEXT = 21
SDL_GL_FRAMEBUFFER_SRGB_CAPABLE = 22
SDL_GL_CONTEXT_RELEASE_BEHAVIOR = 23
SDL_GL_CONTEXT_RESET_NOTIFICATION = 24
SDL_GL_CONTEXT_NO_ERROR = 25
SDL_GL_FLOATBUFFERS = 26
SDL_GL_EGL_PLATFORM = 27
# typedef enum SDL_HitTestResult
# {
#     SDL_HITTEST_NORMAL,             /**< Region is normal. No special properties. */
#     SDL_HITTEST_DRAGGABLE,          /**< Region can drag entire window. */
#     SDL_HITTEST_RESIZE_TOPLEFT,     /**< Region is the resizable top-left corner border. */
#     SDL_HITTEST_RESIZE_TOP,         /**< Region is the resizable top border. */
#     SDL_HITTEST_RESIZE_TOPRIGHT,    /**< Region is the resizable top-right corner border. */
#     SDL_HITTEST_RESIZE_RIGHT,       /**< Region is the resizable right border. */
#     SDL_HITTEST_RESIZE_BOTTOMRIGHT, /**< Region is the resizable bottom-right corner border. */
#     SDL_HITTEST_RESIZE_BOTTOM,      /**< Region is the resizable bottom border. */
#     SDL_HITTEST_RESIZE_BOTTOMLEFT,  /**< Region is the resizable bottom-left corner border. */
#     SDL_HITTEST_RESIZE_LEFT         /**< Region is the resizable left border. */
# } SDL_HitTestResult;
SDL_HITTEST_NORMAL = 0
SDL_HITTEST_DRAGGABLE = 1
SDL_HITTEST_RESIZE_TOPLEFT = 2
SDL_HITTEST_RESIZE_TOP = 3
SDL_HITTEST_RESIZE_TOPRIGHT = 4
SDL_HITTEST_RESIZE_RIGHT = 5
SDL_HITTEST_RESIZE_BOTTOMRIGHT = 6
SDL_HITTEST_RESIZE_BOTTOM = 7
SDL_HITTEST_RESIZE_BOTTOMLEFT = 8
SDL_HITTEST_RESIZE_LEFT = 9
# typedef enum SDL_ProgressState
# {
#     SDL_PROGRESS_STATE_INVALID = -1,    /**< An invalid progress state indicating an error; check SDL_GetError() */
#     SDL_PROGRESS_STATE_NONE,            /**< No progress bar is shown */
#     SDL_PROGRESS_STATE_INDETERMINATE,   /**< The progress bar is shown in a indeterminate state */
#     SDL_PROGRESS_STATE_NORMAL,          /**< The progress bar is shown in a normal state */
#     SDL_PROGRESS_STATE_PAUSED,          /**< The progress bar is shown in a paused state */
#     SDL_PROGRESS_STATE_ERROR            /**< The progress bar is shown in a state indicating the application had an error */
# } SDL_ProgressState;
SDL_PROGRESS_STATE_INVALID = -1
SDL_PROGRESS_STATE_NONE = 0
SDL_PROGRESS_STATE_INDETERMINATE = 1
SDL_PROGRESS_STATE_NORMAL = 2
SDL_PROGRESS_STATE_PAUSED = 3
SDL_PROGRESS_STATE_ERROR = 4
# typedef enum SDL_SystemTheme
# {
#     SDL_SYSTEM_THEME_UNKNOWN,   /**< Unknown system theme */
#     SDL_SYSTEM_THEME_LIGHT,     /**< Light colored system theme */
#     SDL_SYSTEM_THEME_DARK       /**< Dark colored system theme */
# } SDL_SystemTheme;
SDL_SYSTEM_THEME_UNKNOWN = 0
SDL_SYSTEM_THEME_LIGHT = 1
SDL_SYSTEM_THEME_DARK = 2


# typedef struct SDL_DisplayMode
# {
#     SDL_DisplayID displayID;        /**< the display this mode is associated with */
#     SDL_PixelFormat format;         /**< pixel format */
#     int w;                          /**< width */
#     int h;                          /**< height */
#     float pixel_density;            /**< scale converting size to pixels (e.g. a 1920x1080 mode with 2.0 scale would have 3840x2160 pixels) */
#     float refresh_rate;             /**< refresh rate (or 0.0f for unspecified) */
#     int refresh_rate_numerator;     /**< precise refresh rate numerator (or 0 for unspecified) */
#     int refresh_rate_denominator;   /**< precise refresh rate denominator */
#     SDL_DisplayModeData *internal;  /**< Private */
# } SDL_DisplayMode;
class SDL_DisplayMode(ctypes.Structure):
    _fields_ = [
        ("displayID", ctypes.c_uint32),
        ("format", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pixel_density", ctypes.c_float),
        ("refresh_rate", ctypes.c_float),
        ("refresh_rate_numerator", ctypes.c_int),
        ("refresh_rate_denominator", ctypes.c_int),
        ("internal", ctypes.c_void_p),
    ]


# typedef Uint32 SDL_DisplayID;
# typedef struct SDL_DisplayModeData SDL_DisplayModeData;
# typedef intptr_t SDL_EGLAttrib;

# typedef SDL_EGLAttrib *(SDLCALL *SDL_EGLAttribArrayCallback)(void *userdata);
SDL_EGLAttribArrayCallback = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

# typedef void *SDL_EGLConfig;
# typedef void *SDL_EGLDisplay;
# typedef int SDL_EGLint;

# typedef SDL_EGLint *(SDLCALL *SDL_EGLIntArrayCallback)(void *userdata, SDL_EGLDisplay display, SDL_EGLConfig config);
SDL_EGLIntArrayCallback = ctypes.CFUNCTYPE(
    ctypes.POINTER(ctypes.c_int), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
)

# typedef void *SDL_EGLSurface;
# typedef struct SDL_GLContextState *SDL_GLContext;
# typedef Uint32 SDL_GLContextFlag;
# #define SDL_GL_CONTEXT_DEBUG_FLAG              0x0001
# #define SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG 0x0002
# #define SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG      0x0004
# #define SDL_GL_CONTEXT_RESET_ISOLATION_FLAG    0x0008
SDL_GL_CONTEXT_DEBUG_FLAG = 0x1
SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = 0x2
SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG = 0x4
SDL_GL_CONTEXT_RESET_ISOLATION_FLAG = 0x8
# typedef Uint32 SDL_GLContextReleaseFlag;
# #define SDL_GL_CONTEXT_RELEASE_BEHAVIOR_NONE   0x0000
# #define SDL_GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH  0x0001
SDL_GL_CONTEXT_RELEASE_BEHAVIOR_NONE = 0x0
SDL_GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x1
# typedef Uint32 SDL_GLContextResetNotification;
# #define SDL_GL_CONTEXT_RESET_NO_NOTIFICATION  0x0000
# #define SDL_GL_CONTEXT_RESET_LOSE_CONTEXT     0x0001
SDL_GL_CONTEXT_RESET_NO_NOTIFICATION = 0x0
SDL_GL_CONTEXT_RESET_LOSE_CONTEXT = 0x1
# typedef Uint32 SDL_GLProfile;
# #define SDL_GL_CONTEXT_PROFILE_CORE           0x0001  /**< OpenGL Core Profile context */
# #define SDL_GL_CONTEXT_PROFILE_COMPATIBILITY  0x0002  /**< OpenGL Compatibility Profile context */
# #define SDL_GL_CONTEXT_PROFILE_ES             0x0004  /**< GLX_CONTEXT_ES2_PROFILE_BIT_EXT */
SDL_GL_CONTEXT_PROFILE_CORE = 0x1
SDL_GL_CONTEXT_PROFILE_COMPATIBILITY = 0x2
SDL_GL_CONTEXT_PROFILE_ES = 0x4

# typedef SDL_HitTestResult (SDLCALL *SDL_HitTest)(SDL_Window *win, const SDL_Point *area, void *data);
SDL_HitTest = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(SDL_Point), ctypes.c_void_p
)

# typedef struct SDL_Window SDL_Window;
# typedef Uint64 SDL_WindowFlags;
# #define SDL_WINDOW_FULLSCREEN           SDL_UINT64_C(0x0000000000000001)    /**< window is in fullscreen mode */
# #define SDL_WINDOW_OPENGL               SDL_UINT64_C(0x0000000000000002)    /**< window usable with OpenGL context */
# #define SDL_WINDOW_OCCLUDED             SDL_UINT64_C(0x0000000000000004)    /**< window is occluded */
# #define SDL_WINDOW_HIDDEN               SDL_UINT64_C(0x0000000000000008)    /**< window is neither mapped onto the desktop nor shown in the taskbar/dock/window list; SDL_ShowWindow() is required for it to become visible */
# #define SDL_WINDOW_BORDERLESS           SDL_UINT64_C(0x0000000000000010)    /**< no window decoration */
# #define SDL_WINDOW_RESIZABLE            SDL_UINT64_C(0x0000000000000020)    /**< window can be resized */
# #define SDL_WINDOW_MINIMIZED            SDL_UINT64_C(0x0000000000000040)    /**< window is minimized */
# #define SDL_WINDOW_MAXIMIZED            SDL_UINT64_C(0x0000000000000080)    /**< window is maximized */
# #define SDL_WINDOW_MOUSE_GRABBED        SDL_UINT64_C(0x0000000000000100)    /**< window has grabbed mouse input */
# #define SDL_WINDOW_INPUT_FOCUS          SDL_UINT64_C(0x0000000000000200)    /**< window has input focus */
# #define SDL_WINDOW_MOUSE_FOCUS          SDL_UINT64_C(0x0000000000000400)    /**< window has mouse focus */
# #define SDL_WINDOW_EXTERNAL             SDL_UINT64_C(0x0000000000000800)    /**< window not created by SDL */
# #define SDL_WINDOW_MODAL                SDL_UINT64_C(0x0000000000001000)    /**< window is modal */
# #define SDL_WINDOW_HIGH_PIXEL_DENSITY   SDL_UINT64_C(0x0000000000002000)    /**< window uses high pixel density back buffer if possible */
# #define SDL_WINDOW_MOUSE_CAPTURE        SDL_UINT64_C(0x0000000000004000)    /**< window has mouse captured (unrelated to MOUSE_GRABBED) */
# #define SDL_WINDOW_MOUSE_RELATIVE_MODE  SDL_UINT64_C(0x0000000000008000)    /**< window has relative mode enabled */
# #define SDL_WINDOW_ALWAYS_ON_TOP        SDL_UINT64_C(0x0000000000010000)    /**< window should always be above others */
# #define SDL_WINDOW_UTILITY              SDL_UINT64_C(0x0000000000020000)    /**< window should be treated as a utility window, not showing in the task bar and window list */
# #define SDL_WINDOW_TOOLTIP              SDL_UINT64_C(0x0000000000040000)    /**< window should be treated as a tooltip and does not get mouse or keyboard focus, requires a parent window */
# #define SDL_WINDOW_POPUP_MENU           SDL_UINT64_C(0x0000000000080000)    /**< window should be treated as a popup menu, requires a parent window */
# #define SDL_WINDOW_KEYBOARD_GRABBED     SDL_UINT64_C(0x0000000000100000)    /**< window has grabbed keyboard input */
# #define SDL_WINDOW_VULKAN               SDL_UINT64_C(0x0000000010000000)    /**< window usable for Vulkan surface */
# #define SDL_WINDOW_METAL                SDL_UINT64_C(0x0000000020000000)    /**< window usable for Metal view */
# #define SDL_WINDOW_TRANSPARENT          SDL_UINT64_C(0x0000000040000000)    /**< window with transparent buffer */
# #define SDL_WINDOW_NOT_FOCUSABLE        SDL_UINT64_C(0x0000000080000000)    /**< window should not be focusable */
SDL_WINDOW_FULLSCREEN = 0x1
SDL_WINDOW_OPENGL = 0x2
SDL_WINDOW_OCCLUDED = 0x4
SDL_WINDOW_HIDDEN = 0x8
SDL_WINDOW_BORDERLESS = 0x10
SDL_WINDOW_RESIZABLE = 0x20
SDL_WINDOW_MINIMIZED = 0x40
SDL_WINDOW_MAXIMIZED = 0x80
SDL_WINDOW_MOUSE_GRABBED = 0x100
SDL_WINDOW_INPUT_FOCUS = 0x200
SDL_WINDOW_MOUSE_FOCUS = 0x400
SDL_WINDOW_EXTERNAL = 0x800
SDL_WINDOW_MODAL = 0x1000
SDL_WINDOW_HIGH_PIXEL_DENSITY = 0x2000
SDL_WINDOW_MOUSE_CAPTURE = 0x4000
SDL_WINDOW_MOUSE_RELATIVE_MODE = 0x8000
SDL_WINDOW_ALWAYS_ON_TOP = 0x10000
SDL_WINDOW_UTILITY = 0x20000
SDL_WINDOW_TOOLTIP = 0x40000
SDL_WINDOW_POPUP_MENU = 0x80000
SDL_WINDOW_KEYBOARD_GRABBED = 0x100000
SDL_WINDOW_VULKAN = 0x10000000
SDL_WINDOW_METAL = 0x20000000
SDL_WINDOW_TRANSPARENT = 0x40000000
SDL_WINDOW_NOT_FOCUSABLE = 0x80000000
# typedef Uint32 SDL_WindowID;


# SDL_Window * SDL_CreatePopupWindow(SDL_Window *parent, int offset_x, int offset_y, int w, int h, SDL_WindowFlags flags);
SDL_CreatePopupWindow = libsdl3.SDL_CreatePopupWindow
SDL_CreatePopupWindow.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint64,
]
SDL_CreatePopupWindow.restype = ctypes.c_void_p


# SDL_Window * SDL_CreateWindow(const char *title, int w, int h, SDL_WindowFlags flags);
SDL_CreateWindow = libsdl3.SDL_CreateWindow
SDL_CreateWindow.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint64,
]
SDL_CreateWindow.restype = ctypes.c_void_p


# SDL_Window * SDL_CreateWindowWithProperties(SDL_PropertiesID props);
SDL_CreateWindowWithProperties = libsdl3.SDL_CreateWindowWithProperties
SDL_CreateWindowWithProperties.argtypes = [ctypes.c_uint32]
SDL_CreateWindowWithProperties.restype = ctypes.c_void_p


# void SDL_DestroyWindow(SDL_Window *window);
SDL_DestroyWindow = libsdl3.SDL_DestroyWindow
SDL_DestroyWindow.argtypes = [ctypes.c_void_p]
SDL_DestroyWindow.restype = None


# bool SDL_DestroyWindowSurface(SDL_Window *window);
SDL_DestroyWindowSurface = libsdl3.SDL_DestroyWindowSurface
SDL_DestroyWindowSurface.argtypes = [ctypes.c_void_p]
SDL_DestroyWindowSurface.restype = ctypes.c_bool


# bool SDL_DisableScreenSaver(void);
SDL_DisableScreenSaver = libsdl3.SDL_DisableScreenSaver
SDL_DisableScreenSaver.argtypes = []
SDL_DisableScreenSaver.restype = ctypes.c_bool


# SDL_EGLConfig SDL_EGL_GetCurrentConfig(void);
SDL_EGL_GetCurrentConfig = libsdl3.SDL_EGL_GetCurrentConfig
SDL_EGL_GetCurrentConfig.argtypes = []
SDL_EGL_GetCurrentConfig.restype = ctypes.c_void_p


# SDL_EGLDisplay SDL_EGL_GetCurrentDisplay(void);
SDL_EGL_GetCurrentDisplay = libsdl3.SDL_EGL_GetCurrentDisplay
SDL_EGL_GetCurrentDisplay.argtypes = []
SDL_EGL_GetCurrentDisplay.restype = ctypes.c_void_p


# SDL_FunctionPointer SDL_EGL_GetProcAddress(const char *proc);
SDL_EGL_GetProcAddress = libsdl3.SDL_EGL_GetProcAddress
SDL_EGL_GetProcAddress.argtypes = [ctypes.c_char_p]
SDL_EGL_GetProcAddress.restype = SDL_FunctionPointer


# SDL_EGLSurface SDL_EGL_GetWindowSurface(SDL_Window *window);
SDL_EGL_GetWindowSurface = libsdl3.SDL_EGL_GetWindowSurface
SDL_EGL_GetWindowSurface.argtypes = [ctypes.c_void_p]
SDL_EGL_GetWindowSurface.restype = ctypes.c_void_p


# void SDL_EGL_SetAttributeCallbacks(SDL_EGLAttribArrayCallback platformAttribCallback,
#                                    SDL_EGLIntArrayCallback surfaceAttribCallback,
#                                    SDL_EGLIntArrayCallback contextAttribCallback, void *userdata);
SDL_EGL_SetAttributeCallbacks = libsdl3.SDL_EGL_SetAttributeCallbacks
SDL_EGL_SetAttributeCallbacks.argtypes = [
    SDL_EGLAttribArrayCallback,
    SDL_EGLIntArrayCallback,
    SDL_EGLIntArrayCallback,
    ctypes.c_void_p,
]
SDL_EGL_SetAttributeCallbacks.restype = None


# bool SDL_EnableScreenSaver(void);
SDL_EnableScreenSaver = libsdl3.SDL_EnableScreenSaver
SDL_EnableScreenSaver.argtypes = []
SDL_EnableScreenSaver.restype = ctypes.c_bool


# bool SDL_FlashWindow(SDL_Window *window, SDL_FlashOperation operation);
SDL_FlashWindow = libsdl3.SDL_FlashWindow
SDL_FlashWindow.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_FlashWindow.restype = ctypes.c_bool


# bool SDL_GetClosestFullscreenDisplayMode(SDL_DisplayID displayID, int w, int h, float refresh_rate, bool include_high_density_modes, SDL_DisplayMode *closest);
SDL_GetClosestFullscreenDisplayMode = libsdl3.SDL_GetClosestFullscreenDisplayMode
SDL_GetClosestFullscreenDisplayMode.argtypes = [
    ctypes.c_uint32,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_float,
    ctypes.c_bool,
    ctypes.POINTER(SDL_DisplayMode),
]
SDL_GetClosestFullscreenDisplayMode.restype = ctypes.c_bool


# const SDL_DisplayMode * SDL_GetCurrentDisplayMode(SDL_DisplayID displayID);
SDL_GetCurrentDisplayMode = libsdl3.SDL_GetCurrentDisplayMode
SDL_GetCurrentDisplayMode.argtypes = [ctypes.c_uint32]
SDL_GetCurrentDisplayMode.restype = ctypes.POINTER(SDL_DisplayMode)


# SDL_DisplayOrientation SDL_GetCurrentDisplayOrientation(SDL_DisplayID displayID);
SDL_GetCurrentDisplayOrientation = libsdl3.SDL_GetCurrentDisplayOrientation
SDL_GetCurrentDisplayOrientation.argtypes = [ctypes.c_uint32]
SDL_GetCurrentDisplayOrientation.restype = ctypes.c_int


# const char * SDL_GetCurrentVideoDriver(void);
SDL_GetCurrentVideoDriver = libsdl3.SDL_GetCurrentVideoDriver
SDL_GetCurrentVideoDriver.argtypes = []
SDL_GetCurrentVideoDriver.restype = ctypes.c_char_p


# const SDL_DisplayMode * SDL_GetDesktopDisplayMode(SDL_DisplayID displayID);
SDL_GetDesktopDisplayMode = libsdl3.SDL_GetDesktopDisplayMode
SDL_GetDesktopDisplayMode.argtypes = [ctypes.c_uint32]
SDL_GetDesktopDisplayMode.restype = ctypes.POINTER(SDL_DisplayMode)


# bool SDL_GetDisplayBounds(SDL_DisplayID displayID, SDL_Rect *rect);
SDL_GetDisplayBounds = libsdl3.SDL_GetDisplayBounds
SDL_GetDisplayBounds.argtypes = [ctypes.c_uint32, ctypes.POINTER(SDL_Rect)]
SDL_GetDisplayBounds.restype = ctypes.c_bool


# float SDL_GetDisplayContentScale(SDL_DisplayID displayID);
SDL_GetDisplayContentScale = libsdl3.SDL_GetDisplayContentScale
SDL_GetDisplayContentScale.argtypes = [ctypes.c_uint32]
SDL_GetDisplayContentScale.restype = ctypes.c_float


# SDL_DisplayID SDL_GetDisplayForPoint(const SDL_Point *point);
SDL_GetDisplayForPoint = libsdl3.SDL_GetDisplayForPoint
SDL_GetDisplayForPoint.argtypes = [ctypes.POINTER(SDL_Point)]
SDL_GetDisplayForPoint.restype = ctypes.c_uint32


# SDL_DisplayID SDL_GetDisplayForRect(const SDL_Rect *rect);
SDL_GetDisplayForRect = libsdl3.SDL_GetDisplayForRect
SDL_GetDisplayForRect.argtypes = [ctypes.POINTER(SDL_Rect)]
SDL_GetDisplayForRect.restype = ctypes.c_uint32


# SDL_DisplayID SDL_GetDisplayForWindow(SDL_Window *window);
SDL_GetDisplayForWindow = libsdl3.SDL_GetDisplayForWindow
SDL_GetDisplayForWindow.argtypes = [ctypes.c_void_p]
SDL_GetDisplayForWindow.restype = ctypes.c_uint32


# const char * SDL_GetDisplayName(SDL_DisplayID displayID);
SDL_GetDisplayName = libsdl3.SDL_GetDisplayName
SDL_GetDisplayName.argtypes = [ctypes.c_uint32]
SDL_GetDisplayName.restype = ctypes.c_char_p


# SDL_PropertiesID SDL_GetDisplayProperties(SDL_DisplayID displayID);
SDL_GetDisplayProperties = libsdl3.SDL_GetDisplayProperties
SDL_GetDisplayProperties.argtypes = [ctypes.c_uint32]
SDL_GetDisplayProperties.restype = ctypes.c_uint32


# SDL_DisplayID * SDL_GetDisplays(int *count);
SDL_GetDisplays = libsdl3.SDL_GetDisplays
SDL_GetDisplays.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetDisplays.restype = ctypes.POINTER(ctypes.c_uint32)


# bool SDL_GetDisplayUsableBounds(SDL_DisplayID displayID, SDL_Rect *rect);
SDL_GetDisplayUsableBounds = libsdl3.SDL_GetDisplayUsableBounds
SDL_GetDisplayUsableBounds.argtypes = [ctypes.c_uint32, ctypes.POINTER(SDL_Rect)]
SDL_GetDisplayUsableBounds.restype = ctypes.c_bool


# SDL_DisplayMode ** SDL_GetFullscreenDisplayModes(SDL_DisplayID displayID, int *count);
SDL_GetFullscreenDisplayModes = libsdl3.SDL_GetFullscreenDisplayModes
SDL_GetFullscreenDisplayModes.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_int)]
SDL_GetFullscreenDisplayModes.restype = ctypes.POINTER(ctypes.POINTER(SDL_DisplayMode))


# SDL_Window * SDL_GetGrabbedWindow(void);
SDL_GetGrabbedWindow = libsdl3.SDL_GetGrabbedWindow
SDL_GetGrabbedWindow.argtypes = []
SDL_GetGrabbedWindow.restype = ctypes.c_void_p


# SDL_DisplayOrientation SDL_GetNaturalDisplayOrientation(SDL_DisplayID displayID);
SDL_GetNaturalDisplayOrientation = libsdl3.SDL_GetNaturalDisplayOrientation
SDL_GetNaturalDisplayOrientation.argtypes = [ctypes.c_uint32]
SDL_GetNaturalDisplayOrientation.restype = ctypes.c_int


# int SDL_GetNumVideoDrivers(void);
SDL_GetNumVideoDrivers = libsdl3.SDL_GetNumVideoDrivers
SDL_GetNumVideoDrivers.argtypes = []
SDL_GetNumVideoDrivers.restype = ctypes.c_int


# SDL_DisplayID SDL_GetPrimaryDisplay(void);
SDL_GetPrimaryDisplay = libsdl3.SDL_GetPrimaryDisplay
SDL_GetPrimaryDisplay.argtypes = []
SDL_GetPrimaryDisplay.restype = ctypes.c_uint32


# SDL_SystemTheme SDL_GetSystemTheme(void);
SDL_GetSystemTheme = libsdl3.SDL_GetSystemTheme
SDL_GetSystemTheme.argtypes = []
SDL_GetSystemTheme.restype = ctypes.c_int


# const char * SDL_GetVideoDriver(int index);
SDL_GetVideoDriver = libsdl3.SDL_GetVideoDriver
SDL_GetVideoDriver.argtypes = [ctypes.c_int]
SDL_GetVideoDriver.restype = ctypes.c_char_p


# bool SDL_GetWindowAspectRatio(SDL_Window *window, float *min_aspect, float *max_aspect);
SDL_GetWindowAspectRatio = libsdl3.SDL_GetWindowAspectRatio
SDL_GetWindowAspectRatio.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetWindowAspectRatio.restype = ctypes.c_bool


# bool SDL_GetWindowBordersSize(SDL_Window *window, int *top, int *left, int *bottom, int *right);
SDL_GetWindowBordersSize = libsdl3.SDL_GetWindowBordersSize
SDL_GetWindowBordersSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowBordersSize.restype = ctypes.c_bool


# float SDL_GetWindowDisplayScale(SDL_Window *window);
SDL_GetWindowDisplayScale = libsdl3.SDL_GetWindowDisplayScale
SDL_GetWindowDisplayScale.argtypes = [ctypes.c_void_p]
SDL_GetWindowDisplayScale.restype = ctypes.c_float


# SDL_WindowFlags SDL_GetWindowFlags(SDL_Window *window);
SDL_GetWindowFlags = libsdl3.SDL_GetWindowFlags
SDL_GetWindowFlags.argtypes = [ctypes.c_void_p]
SDL_GetWindowFlags.restype = ctypes.c_uint64


# SDL_Window * SDL_GetWindowFromID(SDL_WindowID id);
SDL_GetWindowFromID = libsdl3.SDL_GetWindowFromID
SDL_GetWindowFromID.argtypes = [ctypes.c_uint32]
SDL_GetWindowFromID.restype = ctypes.c_void_p


# const SDL_DisplayMode * SDL_GetWindowFullscreenMode(SDL_Window *window);
SDL_GetWindowFullscreenMode = libsdl3.SDL_GetWindowFullscreenMode
SDL_GetWindowFullscreenMode.argtypes = [ctypes.c_void_p]
SDL_GetWindowFullscreenMode.restype = ctypes.POINTER(SDL_DisplayMode)


# void * SDL_GetWindowICCProfile(SDL_Window *window, size_t *size);
SDL_GetWindowICCProfile = libsdl3.SDL_GetWindowICCProfile
SDL_GetWindowICCProfile.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t)]
SDL_GetWindowICCProfile.restype = ctypes.c_void_p


# SDL_WindowID SDL_GetWindowID(SDL_Window *window);
SDL_GetWindowID = libsdl3.SDL_GetWindowID
SDL_GetWindowID.argtypes = [ctypes.c_void_p]
SDL_GetWindowID.restype = ctypes.c_uint32


# bool SDL_GetWindowKeyboardGrab(SDL_Window *window);
SDL_GetWindowKeyboardGrab = libsdl3.SDL_GetWindowKeyboardGrab
SDL_GetWindowKeyboardGrab.argtypes = [ctypes.c_void_p]
SDL_GetWindowKeyboardGrab.restype = ctypes.c_bool


# bool SDL_GetWindowMaximumSize(SDL_Window *window, int *w, int *h);
SDL_GetWindowMaximumSize = libsdl3.SDL_GetWindowMaximumSize
SDL_GetWindowMaximumSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowMaximumSize.restype = ctypes.c_bool


# bool SDL_GetWindowMinimumSize(SDL_Window *window, int *w, int *h);
SDL_GetWindowMinimumSize = libsdl3.SDL_GetWindowMinimumSize
SDL_GetWindowMinimumSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowMinimumSize.restype = ctypes.c_bool


# bool SDL_GetWindowMouseGrab(SDL_Window *window);
SDL_GetWindowMouseGrab = libsdl3.SDL_GetWindowMouseGrab
SDL_GetWindowMouseGrab.argtypes = [ctypes.c_void_p]
SDL_GetWindowMouseGrab.restype = ctypes.c_bool


# const SDL_Rect * SDL_GetWindowMouseRect(SDL_Window *window);
SDL_GetWindowMouseRect = libsdl3.SDL_GetWindowMouseRect
SDL_GetWindowMouseRect.argtypes = [ctypes.c_void_p]
SDL_GetWindowMouseRect.restype = ctypes.POINTER(SDL_Rect)


# float SDL_GetWindowOpacity(SDL_Window *window);
SDL_GetWindowOpacity = libsdl3.SDL_GetWindowOpacity
SDL_GetWindowOpacity.argtypes = [ctypes.c_void_p]
SDL_GetWindowOpacity.restype = ctypes.c_float


# SDL_Window * SDL_GetWindowParent(SDL_Window *window);
SDL_GetWindowParent = libsdl3.SDL_GetWindowParent
SDL_GetWindowParent.argtypes = [ctypes.c_void_p]
SDL_GetWindowParent.restype = ctypes.c_void_p


# float SDL_GetWindowPixelDensity(SDL_Window *window);
SDL_GetWindowPixelDensity = libsdl3.SDL_GetWindowPixelDensity
SDL_GetWindowPixelDensity.argtypes = [ctypes.c_void_p]
SDL_GetWindowPixelDensity.restype = ctypes.c_float


# SDL_PixelFormat SDL_GetWindowPixelFormat(SDL_Window *window);
SDL_GetWindowPixelFormat = libsdl3.SDL_GetWindowPixelFormat
SDL_GetWindowPixelFormat.argtypes = [ctypes.c_void_p]
SDL_GetWindowPixelFormat.restype = ctypes.c_int


# bool SDL_GetWindowPosition(SDL_Window *window, int *x, int *y);
SDL_GetWindowPosition = libsdl3.SDL_GetWindowPosition
SDL_GetWindowPosition.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowPosition.restype = ctypes.c_bool


# SDL_ProgressState SDL_GetWindowProgressState(SDL_Window *window);
SDL_GetWindowProgressState = libsdl3.SDL_GetWindowProgressState
SDL_GetWindowProgressState.argtypes = [ctypes.c_void_p]
SDL_GetWindowProgressState.restype = ctypes.c_int


# float SDL_GetWindowProgressValue(SDL_Window *window);
SDL_GetWindowProgressValue = libsdl3.SDL_GetWindowProgressValue
SDL_GetWindowProgressValue.argtypes = [ctypes.c_void_p]
SDL_GetWindowProgressValue.restype = ctypes.c_float


# SDL_PropertiesID SDL_GetWindowProperties(SDL_Window *window);
SDL_GetWindowProperties = libsdl3.SDL_GetWindowProperties
SDL_GetWindowProperties.argtypes = [ctypes.c_void_p]
SDL_GetWindowProperties.restype = ctypes.c_uint32


# SDL_Window ** SDL_GetWindows(int *count);
SDL_GetWindows = libsdl3.SDL_GetWindows
SDL_GetWindows.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetWindows.restype = ctypes.POINTER(ctypes.c_void_p)


# bool SDL_GetWindowSafeArea(SDL_Window *window, SDL_Rect *rect);
SDL_GetWindowSafeArea = libsdl3.SDL_GetWindowSafeArea
SDL_GetWindowSafeArea.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_GetWindowSafeArea.restype = ctypes.c_bool


# bool SDL_GetWindowSize(SDL_Window *window, int *w, int *h);
SDL_GetWindowSize = libsdl3.SDL_GetWindowSize
SDL_GetWindowSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowSize.restype = ctypes.c_bool


# bool SDL_GetWindowSizeInPixels(SDL_Window *window, int *w, int *h);
SDL_GetWindowSizeInPixels = libsdl3.SDL_GetWindowSizeInPixels
SDL_GetWindowSizeInPixels.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetWindowSizeInPixels.restype = ctypes.c_bool


# SDL_Surface * SDL_GetWindowSurface(SDL_Window *window);
SDL_GetWindowSurface = libsdl3.SDL_GetWindowSurface
SDL_GetWindowSurface.argtypes = [ctypes.c_void_p]
SDL_GetWindowSurface.restype = ctypes.POINTER(SDL_Surface)


# bool SDL_GetWindowSurfaceVSync(SDL_Window *window, int *vsync);
SDL_GetWindowSurfaceVSync = libsdl3.SDL_GetWindowSurfaceVSync
SDL_GetWindowSurfaceVSync.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_GetWindowSurfaceVSync.restype = ctypes.c_bool


# const char * SDL_GetWindowTitle(SDL_Window *window);
SDL_GetWindowTitle = libsdl3.SDL_GetWindowTitle
SDL_GetWindowTitle.argtypes = [ctypes.c_void_p]
SDL_GetWindowTitle.restype = ctypes.c_char_p


# SDL_GLContext SDL_GL_CreateContext(SDL_Window *window);
SDL_GL_CreateContext = libsdl3.SDL_GL_CreateContext
SDL_GL_CreateContext.argtypes = [ctypes.c_void_p]
SDL_GL_CreateContext.restype = ctypes.c_void_p


# bool SDL_GL_DestroyContext(SDL_GLContext context);
SDL_GL_DestroyContext = libsdl3.SDL_GL_DestroyContext
SDL_GL_DestroyContext.argtypes = [ctypes.c_void_p]
SDL_GL_DestroyContext.restype = ctypes.c_bool


# bool SDL_GL_ExtensionSupported(const char *extension);
SDL_GL_ExtensionSupported = libsdl3.SDL_GL_ExtensionSupported
SDL_GL_ExtensionSupported.argtypes = [ctypes.c_char_p]
SDL_GL_ExtensionSupported.restype = ctypes.c_bool


# bool SDL_GL_GetAttribute(SDL_GLAttr attr, int *value);
SDL_GL_GetAttribute = libsdl3.SDL_GL_GetAttribute
SDL_GL_GetAttribute.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
SDL_GL_GetAttribute.restype = ctypes.c_bool


# SDL_GLContext SDL_GL_GetCurrentContext(void);
SDL_GL_GetCurrentContext = libsdl3.SDL_GL_GetCurrentContext
SDL_GL_GetCurrentContext.argtypes = []
SDL_GL_GetCurrentContext.restype = ctypes.c_void_p


# SDL_Window * SDL_GL_GetCurrentWindow(void);
SDL_GL_GetCurrentWindow = libsdl3.SDL_GL_GetCurrentWindow
SDL_GL_GetCurrentWindow.argtypes = []
SDL_GL_GetCurrentWindow.restype = ctypes.c_void_p


# SDL_FunctionPointer SDL_GL_GetProcAddress(const char *proc);
SDL_GL_GetProcAddress = libsdl3.SDL_GL_GetProcAddress
SDL_GL_GetProcAddress.argtypes = [ctypes.c_char_p]
SDL_GL_GetProcAddress.restype = SDL_FunctionPointer


# bool SDL_GL_GetSwapInterval(int *interval);
SDL_GL_GetSwapInterval = libsdl3.SDL_GL_GetSwapInterval
SDL_GL_GetSwapInterval.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GL_GetSwapInterval.restype = ctypes.c_bool


# bool SDL_GL_LoadLibrary(const char *path);
SDL_GL_LoadLibrary = libsdl3.SDL_GL_LoadLibrary
SDL_GL_LoadLibrary.argtypes = [ctypes.c_char_p]
SDL_GL_LoadLibrary.restype = ctypes.c_bool


# bool SDL_GL_MakeCurrent(SDL_Window *window, SDL_GLContext context);
SDL_GL_MakeCurrent = libsdl3.SDL_GL_MakeCurrent
SDL_GL_MakeCurrent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_GL_MakeCurrent.restype = ctypes.c_bool


# void SDL_GL_ResetAttributes(void);
SDL_GL_ResetAttributes = libsdl3.SDL_GL_ResetAttributes
SDL_GL_ResetAttributes.argtypes = []
SDL_GL_ResetAttributes.restype = None


# bool SDL_GL_SetAttribute(SDL_GLAttr attr, int value);
SDL_GL_SetAttribute = libsdl3.SDL_GL_SetAttribute
SDL_GL_SetAttribute.argtypes = [ctypes.c_int, ctypes.c_int]
SDL_GL_SetAttribute.restype = ctypes.c_bool


# bool SDL_GL_SetSwapInterval(int interval);
SDL_GL_SetSwapInterval = libsdl3.SDL_GL_SetSwapInterval
SDL_GL_SetSwapInterval.argtypes = [ctypes.c_int]
SDL_GL_SetSwapInterval.restype = ctypes.c_bool


# bool SDL_GL_SwapWindow(SDL_Window *window);
SDL_GL_SwapWindow = libsdl3.SDL_GL_SwapWindow
SDL_GL_SwapWindow.argtypes = [ctypes.c_void_p]
SDL_GL_SwapWindow.restype = ctypes.c_bool


# void SDL_GL_UnloadLibrary(void);
SDL_GL_UnloadLibrary = libsdl3.SDL_GL_UnloadLibrary
SDL_GL_UnloadLibrary.argtypes = []
SDL_GL_UnloadLibrary.restype = None


# bool SDL_HideWindow(SDL_Window *window);
SDL_HideWindow = libsdl3.SDL_HideWindow
SDL_HideWindow.argtypes = [ctypes.c_void_p]
SDL_HideWindow.restype = ctypes.c_bool


# bool SDL_MaximizeWindow(SDL_Window *window);
SDL_MaximizeWindow = libsdl3.SDL_MaximizeWindow
SDL_MaximizeWindow.argtypes = [ctypes.c_void_p]
SDL_MaximizeWindow.restype = ctypes.c_bool


# bool SDL_MinimizeWindow(SDL_Window *window);
SDL_MinimizeWindow = libsdl3.SDL_MinimizeWindow
SDL_MinimizeWindow.argtypes = [ctypes.c_void_p]
SDL_MinimizeWindow.restype = ctypes.c_bool


# bool SDL_RaiseWindow(SDL_Window *window);
SDL_RaiseWindow = libsdl3.SDL_RaiseWindow
SDL_RaiseWindow.argtypes = [ctypes.c_void_p]
SDL_RaiseWindow.restype = ctypes.c_bool


# bool SDL_RestoreWindow(SDL_Window *window);
SDL_RestoreWindow = libsdl3.SDL_RestoreWindow
SDL_RestoreWindow.argtypes = [ctypes.c_void_p]
SDL_RestoreWindow.restype = ctypes.c_bool


# bool SDL_ScreenSaverEnabled(void);
SDL_ScreenSaverEnabled = libsdl3.SDL_ScreenSaverEnabled
SDL_ScreenSaverEnabled.argtypes = []
SDL_ScreenSaverEnabled.restype = ctypes.c_bool


# bool SDL_SetWindowAlwaysOnTop(SDL_Window *window, bool on_top);
SDL_SetWindowAlwaysOnTop = libsdl3.SDL_SetWindowAlwaysOnTop
SDL_SetWindowAlwaysOnTop.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowAlwaysOnTop.restype = ctypes.c_bool


# bool SDL_SetWindowAspectRatio(SDL_Window *window, float min_aspect, float max_aspect);
SDL_SetWindowAspectRatio = libsdl3.SDL_SetWindowAspectRatio
SDL_SetWindowAspectRatio.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float]
SDL_SetWindowAspectRatio.restype = ctypes.c_bool


# bool SDL_SetWindowBordered(SDL_Window *window, bool bordered);
SDL_SetWindowBordered = libsdl3.SDL_SetWindowBordered
SDL_SetWindowBordered.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowBordered.restype = ctypes.c_bool


# bool SDL_SetWindowFocusable(SDL_Window *window, bool focusable);
SDL_SetWindowFocusable = libsdl3.SDL_SetWindowFocusable
SDL_SetWindowFocusable.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowFocusable.restype = ctypes.c_bool


# bool SDL_SetWindowFullscreen(SDL_Window *window, bool fullscreen);
SDL_SetWindowFullscreen = libsdl3.SDL_SetWindowFullscreen
SDL_SetWindowFullscreen.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowFullscreen.restype = ctypes.c_bool


# bool SDL_SetWindowFullscreenMode(SDL_Window *window, const SDL_DisplayMode *mode);
SDL_SetWindowFullscreenMode = libsdl3.SDL_SetWindowFullscreenMode
SDL_SetWindowFullscreenMode.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_DisplayMode),
]
SDL_SetWindowFullscreenMode.restype = ctypes.c_bool


# bool SDL_SetWindowHitTest(SDL_Window *window, SDL_HitTest callback, void *callback_data);
SDL_SetWindowHitTest = libsdl3.SDL_SetWindowHitTest
SDL_SetWindowHitTest.argtypes = [ctypes.c_void_p, SDL_HitTest, ctypes.c_void_p]
SDL_SetWindowHitTest.restype = ctypes.c_bool


# bool SDL_SetWindowIcon(SDL_Window *window, SDL_Surface *icon);
SDL_SetWindowIcon = libsdl3.SDL_SetWindowIcon
SDL_SetWindowIcon.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)]
SDL_SetWindowIcon.restype = ctypes.c_bool


# bool SDL_SetWindowKeyboardGrab(SDL_Window *window, bool grabbed);
SDL_SetWindowKeyboardGrab = libsdl3.SDL_SetWindowKeyboardGrab
SDL_SetWindowKeyboardGrab.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowKeyboardGrab.restype = ctypes.c_bool


# bool SDL_SetWindowMaximumSize(SDL_Window *window, int max_w, int max_h);
SDL_SetWindowMaximumSize = libsdl3.SDL_SetWindowMaximumSize
SDL_SetWindowMaximumSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_SetWindowMaximumSize.restype = ctypes.c_bool


# bool SDL_SetWindowMinimumSize(SDL_Window *window, int min_w, int min_h);
SDL_SetWindowMinimumSize = libsdl3.SDL_SetWindowMinimumSize
SDL_SetWindowMinimumSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_SetWindowMinimumSize.restype = ctypes.c_bool


# bool SDL_SetWindowModal(SDL_Window *window, bool modal);
SDL_SetWindowModal = libsdl3.SDL_SetWindowModal
SDL_SetWindowModal.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowModal.restype = ctypes.c_bool


# bool SDL_SetWindowMouseGrab(SDL_Window *window, bool grabbed);
SDL_SetWindowMouseGrab = libsdl3.SDL_SetWindowMouseGrab
SDL_SetWindowMouseGrab.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowMouseGrab.restype = ctypes.c_bool


# bool SDL_SetWindowMouseRect(SDL_Window *window, const SDL_Rect *rect);
SDL_SetWindowMouseRect = libsdl3.SDL_SetWindowMouseRect
SDL_SetWindowMouseRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_SetWindowMouseRect.restype = ctypes.c_bool


# bool SDL_SetWindowOpacity(SDL_Window *window, float opacity);
SDL_SetWindowOpacity = libsdl3.SDL_SetWindowOpacity
SDL_SetWindowOpacity.argtypes = [ctypes.c_void_p, ctypes.c_float]
SDL_SetWindowOpacity.restype = ctypes.c_bool


# bool SDL_SetWindowParent(SDL_Window *window, SDL_Window *parent);
SDL_SetWindowParent = libsdl3.SDL_SetWindowParent
SDL_SetWindowParent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_SetWindowParent.restype = ctypes.c_bool


# bool SDL_SetWindowPosition(SDL_Window *window, int x, int y);
SDL_SetWindowPosition = libsdl3.SDL_SetWindowPosition
SDL_SetWindowPosition.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_SetWindowPosition.restype = ctypes.c_bool


# bool SDL_SetWindowProgressState(SDL_Window *window, SDL_ProgressState state);
SDL_SetWindowProgressState = libsdl3.SDL_SetWindowProgressState
SDL_SetWindowProgressState.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_SetWindowProgressState.restype = ctypes.c_bool


# bool SDL_SetWindowProgressValue(SDL_Window *window, float value);
SDL_SetWindowProgressValue = libsdl3.SDL_SetWindowProgressValue
SDL_SetWindowProgressValue.argtypes = [ctypes.c_void_p, ctypes.c_float]
SDL_SetWindowProgressValue.restype = ctypes.c_bool


# bool SDL_SetWindowResizable(SDL_Window *window, bool resizable);
SDL_SetWindowResizable = libsdl3.SDL_SetWindowResizable
SDL_SetWindowResizable.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowResizable.restype = ctypes.c_bool


# bool SDL_SetWindowShape(SDL_Window *window, SDL_Surface *shape);
SDL_SetWindowShape = libsdl3.SDL_SetWindowShape
SDL_SetWindowShape.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)]
SDL_SetWindowShape.restype = ctypes.c_bool


# bool SDL_SetWindowSize(SDL_Window *window, int w, int h);
SDL_SetWindowSize = libsdl3.SDL_SetWindowSize
SDL_SetWindowSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_SetWindowSize.restype = ctypes.c_bool


# bool SDL_SetWindowSurfaceVSync(SDL_Window *window, int vsync);
# #define SDL_WINDOW_SURFACE_VSYNC_DISABLED 0
# #define SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE (-1)
SDL_SetWindowSurfaceVSync = libsdl3.SDL_SetWindowSurfaceVSync
SDL_SetWindowSurfaceVSync.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_SetWindowSurfaceVSync.restype = ctypes.c_bool
SDL_WINDOW_SURFACE_VSYNC_DISABLED = 0
SDL_WINDOW_SURFACE_VSYNC_ADAPTIVE = -1


# bool SDL_SetWindowTitle(SDL_Window *window, const char *title);
SDL_SetWindowTitle = libsdl3.SDL_SetWindowTitle
SDL_SetWindowTitle.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_SetWindowTitle.restype = ctypes.c_bool


# bool SDL_ShowWindow(SDL_Window *window);
SDL_ShowWindow = libsdl3.SDL_ShowWindow
SDL_ShowWindow.argtypes = [ctypes.c_void_p]
SDL_ShowWindow.restype = ctypes.c_bool


# bool SDL_ShowWindowSystemMenu(SDL_Window *window, int x, int y);
SDL_ShowWindowSystemMenu = libsdl3.SDL_ShowWindowSystemMenu
SDL_ShowWindowSystemMenu.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_ShowWindowSystemMenu.restype = ctypes.c_bool


# bool SDL_SyncWindow(SDL_Window *window);
SDL_SyncWindow = libsdl3.SDL_SyncWindow
SDL_SyncWindow.argtypes = [ctypes.c_void_p]
SDL_SyncWindow.restype = ctypes.c_bool


# bool SDL_UpdateWindowSurface(SDL_Window *window);
SDL_UpdateWindowSurface = libsdl3.SDL_UpdateWindowSurface
SDL_UpdateWindowSurface.argtypes = [ctypes.c_void_p]
SDL_UpdateWindowSurface.restype = ctypes.c_bool


# bool SDL_UpdateWindowSurfaceRects(SDL_Window *window, const SDL_Rect *rects, int numrects);
SDL_UpdateWindowSurfaceRects = libsdl3.SDL_UpdateWindowSurfaceRects
SDL_UpdateWindowSurfaceRects.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
]
SDL_UpdateWindowSurfaceRects.restype = ctypes.c_bool


# bool SDL_WindowHasSurface(SDL_Window *window);
SDL_WindowHasSurface = libsdl3.SDL_WindowHasSurface
SDL_WindowHasSurface.argtypes = [ctypes.c_void_p]
SDL_WindowHasSurface.restype = ctypes.c_bool
