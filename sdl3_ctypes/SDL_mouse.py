"""
SDL_mouse.h
Mouse Support
Document: https://wiki.libsdl.org/SDL3/CategoryMouse
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_rect import SDL_Rect
from sdl3_ctypes.SDL_surface import SDL_Surface

# #define SDL_TOUCH_MOUSEID ((SDL_MouseID)-1)


# typedef enum SDL_MouseWheelDirection
# {
#     SDL_MOUSEWHEEL_NORMAL,    /**< The scroll direction is normal */
#     SDL_MOUSEWHEEL_FLIPPED    /**< The scroll direction is flipped / natural */
# } SDL_MouseWheelDirection;
SDL_MOUSEWHEEL_NORMAL = 0
SDL_MOUSEWHEEL_FLIPPED = 1
# typedef enum SDL_SystemCursor
# {
#     SDL_SYSTEM_CURSOR_DEFAULT,      /**< Default cursor. Usually an arrow. */
#     SDL_SYSTEM_CURSOR_TEXT,         /**< Text selection. Usually an I-beam. */
#     SDL_SYSTEM_CURSOR_WAIT,         /**< Wait. Usually an hourglass or watch or spinning ball. */
#     SDL_SYSTEM_CURSOR_CROSSHAIR,    /**< Crosshair. */
#     SDL_SYSTEM_CURSOR_PROGRESS,     /**< Program is busy but still interactive. Usually it's WAIT with an arrow. */
#     SDL_SYSTEM_CURSOR_NWSE_RESIZE,  /**< Double arrow pointing northwest and southeast. */
#     SDL_SYSTEM_CURSOR_NESW_RESIZE,  /**< Double arrow pointing northeast and southwest. */
#     SDL_SYSTEM_CURSOR_EW_RESIZE,    /**< Double arrow pointing west and east. */
#     SDL_SYSTEM_CURSOR_NS_RESIZE,    /**< Double arrow pointing north and south. */
#     SDL_SYSTEM_CURSOR_MOVE,         /**< Four pointed arrow pointing north, south, east, and west. */
#     SDL_SYSTEM_CURSOR_NOT_ALLOWED,  /**< Not permitted. Usually a slashed circle or crossbones. */
#     SDL_SYSTEM_CURSOR_POINTER,      /**< Pointer that indicates a link. Usually a pointing hand. */
#     SDL_SYSTEM_CURSOR_NW_RESIZE,    /**< Window resize top-left. This may be a single arrow or a double arrow like NWSE_RESIZE. */
#     SDL_SYSTEM_CURSOR_N_RESIZE,     /**< Window resize top. May be NS_RESIZE. */
#     SDL_SYSTEM_CURSOR_NE_RESIZE,    /**< Window resize top-right. May be NESW_RESIZE. */
#     SDL_SYSTEM_CURSOR_E_RESIZE,     /**< Window resize right. May be EW_RESIZE. */
#     SDL_SYSTEM_CURSOR_SE_RESIZE,    /**< Window resize bottom-right. May be NWSE_RESIZE. */
#     SDL_SYSTEM_CURSOR_S_RESIZE,     /**< Window resize bottom. May be NS_RESIZE. */
#     SDL_SYSTEM_CURSOR_SW_RESIZE,    /**< Window resize bottom-left. May be NESW_RESIZE. */
#     SDL_SYSTEM_CURSOR_W_RESIZE,     /**< Window resize left. May be EW_RESIZE. */
#     SDL_SYSTEM_CURSOR_COUNT
# } SDL_SystemCursor;
SDL_SYSTEM_CURSOR_DEFAULT = 0
SDL_SYSTEM_CURSOR_TEXT = 1
SDL_SYSTEM_CURSOR_WAIT = 2
SDL_SYSTEM_CURSOR_CROSSHAIR = 3
SDL_SYSTEM_CURSOR_PROGRESS = 4
SDL_SYSTEM_CURSOR_NWSE_RESIZE = 5
SDL_SYSTEM_CURSOR_NESW_RESIZE = 6
SDL_SYSTEM_CURSOR_EW_RESIZE = 7
SDL_SYSTEM_CURSOR_NS_RESIZE = 8
SDL_SYSTEM_CURSOR_MOVE = 9
SDL_SYSTEM_CURSOR_NOT_ALLOWED = 10
SDL_SYSTEM_CURSOR_POINTER = 11
SDL_SYSTEM_CURSOR_NW_RESIZE = 12
SDL_SYSTEM_CURSOR_N_RESIZE = 13
SDL_SYSTEM_CURSOR_NE_RESIZE = 14
SDL_SYSTEM_CURSOR_E_RESIZE = 15
SDL_SYSTEM_CURSOR_SE_RESIZE = 16
SDL_SYSTEM_CURSOR_S_RESIZE = 17
SDL_SYSTEM_CURSOR_SW_RESIZE = 18
SDL_SYSTEM_CURSOR_W_RESIZE = 19
SDL_SYSTEM_CURSOR_COUNT = 20


# typedef struct SDL_Cursor SDL_Cursor;
# typedef Uint32 SDL_MouseButtonFlags;
# #define SDL_BUTTON_LEFT     1
# #define SDL_BUTTON_MIDDLE   2
# #define SDL_BUTTON_RIGHT    3
# #define SDL_BUTTON_X1       4
# #define SDL_BUTTON_X2       5
# #define SDL_BUTTON_MASK(X)  (1u << ((X)-1))
# #define SDL_BUTTON_LMASK    SDL_BUTTON_MASK(SDL_BUTTON_LEFT)
# #define SDL_BUTTON_MMASK    SDL_BUTTON_MASK(SDL_BUTTON_MIDDLE)
# #define SDL_BUTTON_RMASK    SDL_BUTTON_MASK(SDL_BUTTON_RIGHT)
# #define SDL_BUTTON_X1MASK   SDL_BUTTON_MASK(SDL_BUTTON_X1)
# #define SDL_BUTTON_X2MASK   SDL_BUTTON_MASK(SDL_BUTTON_X2)
SDL_BUTTON_LEFT = 0x1
SDL_BUTTON_MIDDLE = 0x2
SDL_BUTTON_RIGHT = 0x3
SDL_BUTTON_X1 = 0x4
SDL_BUTTON_X2 = 0x5
SDL_BUTTON_LMASK = 0x1
SDL_BUTTON_MMASK = 0x2
SDL_BUTTON_RMASK = 0x4
SDL_BUTTON_X1MASK = 0x8
SDL_BUTTON_X2MASK = 0x10
# typedef Uint32 SDL_MouseID;

# typedef void (SDLCALL *SDL_MouseMotionTransformCallback)( void *userdata, Uint64 timestamp, SDL_Window *window, SDL_MouseID mouseID, float *x, float *y);
SDL_MouseMotionTransformCallback = ctypes.CFUNCTYPE(
    None,
    ctypes.c_void_p,
    ctypes.c_uint64,
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
)


# bool SDL_CaptureMouse(bool enabled);
SDL_CaptureMouse = libsdl3.SDL_CaptureMouse
SDL_CaptureMouse.argtypes = [ctypes.c_bool]
SDL_CaptureMouse.restype = ctypes.c_bool


# SDL_Cursor * SDL_CreateColorCursor(SDL_Surface *surface,
#                               int hot_x,
#                               int hot_y);
SDL_CreateColorCursor = libsdl3.SDL_CreateColorCursor
SDL_CreateColorCursor.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
]
SDL_CreateColorCursor.restype = ctypes.c_void_p


# SDL_Cursor * SDL_CreateCursor(const Uint8 *data,
#                          const Uint8 *mask,
#                          int w, int h, int hot_x,
#                          int hot_y);
SDL_CreateCursor = libsdl3.SDL_CreateCursor
SDL_CreateCursor.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_CreateCursor.restype = ctypes.c_void_p


# SDL_Cursor * SDL_CreateSystemCursor(SDL_SystemCursor id);
SDL_CreateSystemCursor = libsdl3.SDL_CreateSystemCursor
SDL_CreateSystemCursor.argtypes = [ctypes.c_int]
SDL_CreateSystemCursor.restype = ctypes.c_void_p


# bool SDL_CursorVisible(void);
SDL_CursorVisible = libsdl3.SDL_CursorVisible
SDL_CursorVisible.argtypes = []
SDL_CursorVisible.restype = ctypes.c_bool


# void SDL_DestroyCursor(SDL_Cursor *cursor);
SDL_DestroyCursor = libsdl3.SDL_DestroyCursor
SDL_DestroyCursor.argtypes = [ctypes.c_void_p]
SDL_DestroyCursor.restype = None


# SDL_Cursor * SDL_GetCursor(void);
SDL_GetCursor = libsdl3.SDL_GetCursor
SDL_GetCursor.argtypes = []
SDL_GetCursor.restype = ctypes.c_void_p


# SDL_Cursor * SDL_GetDefaultCursor(void);
SDL_GetDefaultCursor = libsdl3.SDL_GetDefaultCursor
SDL_GetDefaultCursor.argtypes = []
SDL_GetDefaultCursor.restype = ctypes.c_void_p


# SDL_MouseButtonFlags SDL_GetGlobalMouseState(float *x, float *y);
SDL_GetGlobalMouseState = libsdl3.SDL_GetGlobalMouseState
SDL_GetGlobalMouseState.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetGlobalMouseState.restype = ctypes.c_uint32


# SDL_MouseID * SDL_GetMice(int *count);
SDL_GetMice = libsdl3.SDL_GetMice
SDL_GetMice.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetMice.restype = ctypes.POINTER(ctypes.c_uint32)


# SDL_Window * SDL_GetMouseFocus(void);
SDL_GetMouseFocus = libsdl3.SDL_GetMouseFocus
SDL_GetMouseFocus.argtypes = []
SDL_GetMouseFocus.restype = ctypes.c_void_p


# const char * SDL_GetMouseNameForID(SDL_MouseID instance_id);
SDL_GetMouseNameForID = libsdl3.SDL_GetMouseNameForID
SDL_GetMouseNameForID.argtypes = [ctypes.c_uint32]
SDL_GetMouseNameForID.restype = ctypes.c_char_p


# SDL_MouseButtonFlags SDL_GetMouseState(float *x, float *y);
SDL_GetMouseState = libsdl3.SDL_GetMouseState
SDL_GetMouseState.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetMouseState.restype = ctypes.c_uint32


# SDL_MouseButtonFlags SDL_GetRelativeMouseState(float *x, float *y);
SDL_GetRelativeMouseState = libsdl3.SDL_GetRelativeMouseState
SDL_GetRelativeMouseState.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetRelativeMouseState.restype = ctypes.c_uint32


# bool SDL_GetWindowMouseGrab(SDL_Window *window);
SDL_GetWindowMouseGrab = libsdl3.SDL_GetWindowMouseGrab
SDL_GetWindowMouseGrab.argtypes = [ctypes.c_void_p]
SDL_GetWindowMouseGrab.restype = ctypes.c_bool


# const SDL_Rect * SDL_GetWindowMouseRect(SDL_Window *window);
SDL_GetWindowMouseRect = libsdl3.SDL_GetWindowMouseRect
SDL_GetWindowMouseRect.argtypes = [ctypes.c_void_p]
SDL_GetWindowMouseRect.restype = ctypes.POINTER(SDL_Rect)


# bool SDL_GetWindowRelativeMouseMode(SDL_Window *window);
SDL_GetWindowRelativeMouseMode = libsdl3.SDL_GetWindowRelativeMouseMode
SDL_GetWindowRelativeMouseMode.argtypes = [ctypes.c_void_p]
SDL_GetWindowRelativeMouseMode.restype = ctypes.c_bool


# bool SDL_HasMouse(void);
SDL_HasMouse = libsdl3.SDL_HasMouse
SDL_HasMouse.argtypes = []
SDL_HasMouse.restype = ctypes.c_bool


# bool SDL_HideCursor(void);
SDL_HideCursor = libsdl3.SDL_HideCursor
SDL_HideCursor.argtypes = []
SDL_HideCursor.restype = ctypes.c_bool


# bool SDL_SetCursor(SDL_Cursor *cursor);
SDL_SetCursor = libsdl3.SDL_SetCursor
SDL_SetCursor.argtypes = [ctypes.c_void_p]
SDL_SetCursor.restype = ctypes.c_bool


# bool SDL_SetRelativeMouseTransform(SDL_MouseMotionTransformCallback callback, void *userdata);
SDL_SetRelativeMouseTransform = libsdl3.SDL_SetRelativeMouseTransform
SDL_SetRelativeMouseTransform.argtypes = [
    SDL_MouseMotionTransformCallback,
    ctypes.c_void_p,
]
SDL_SetRelativeMouseTransform.restype = ctypes.c_bool


# bool SDL_SetWindowMouseGrab(SDL_Window *window, bool grabbed);
SDL_SetWindowMouseGrab = libsdl3.SDL_SetWindowMouseGrab
SDL_SetWindowMouseGrab.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowMouseGrab.restype = ctypes.c_bool


# bool SDL_SetWindowMouseRect(SDL_Window *window, const SDL_Rect *rect);
SDL_SetWindowMouseRect = libsdl3.SDL_SetWindowMouseRect
SDL_SetWindowMouseRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_SetWindowMouseRect.restype = ctypes.c_bool


# bool SDL_SetWindowRelativeMouseMode(SDL_Window *window, bool enabled);
SDL_SetWindowRelativeMouseMode = libsdl3.SDL_SetWindowRelativeMouseMode
SDL_SetWindowRelativeMouseMode.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetWindowRelativeMouseMode.restype = ctypes.c_bool


# bool SDL_ShowCursor(void);
SDL_ShowCursor = libsdl3.SDL_ShowCursor
SDL_ShowCursor.argtypes = []
SDL_ShowCursor.restype = ctypes.c_bool


# bool SDL_WarpMouseGlobal(float x, float y);
SDL_WarpMouseGlobal = libsdl3.SDL_WarpMouseGlobal
SDL_WarpMouseGlobal.argtypes = [ctypes.c_float, ctypes.c_float]
SDL_WarpMouseGlobal.restype = ctypes.c_bool


# void SDL_WarpMouseInWindow(SDL_Window *window,
#                        float x, float y);
SDL_WarpMouseInWindow = libsdl3.SDL_WarpMouseInWindow
SDL_WarpMouseInWindow.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float]
SDL_WarpMouseInWindow.restype = None
