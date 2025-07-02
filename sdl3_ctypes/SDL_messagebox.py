"""
SDL_messagebox.h
Message Boxes
Document: https://wiki.libsdl.org/SDL3/CategoryMessagebox
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_MessageBoxColorType
# {
#     SDL_MESSAGEBOX_COLOR_BACKGROUND,
#     SDL_MESSAGEBOX_COLOR_TEXT,
#     SDL_MESSAGEBOX_COLOR_BUTTON_BORDER,
#     SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND,
#     SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED,
#     SDL_MESSAGEBOX_COLOR_COUNT                    /**< Size of the colors array of SDL_MessageBoxColorScheme. */
# } SDL_MessageBoxColorType;
SDL_MESSAGEBOX_COLOR_BACKGROUND = 0
SDL_MESSAGEBOX_COLOR_TEXT = 1
SDL_MESSAGEBOX_COLOR_BUTTON_BORDER = 2
SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND = 3
SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED = 4
SDL_MESSAGEBOX_COLOR_COUNT = 5


# typedef struct SDL_MessageBoxButtonData
# {
#     SDL_MessageBoxButtonFlags flags;
#     int buttonID;       /**< User defined button id (value returned via SDL_ShowMessageBox) */
#     const char *text;   /**< The UTF-8 button text */
# } SDL_MessageBoxButtonData;
class SDL_MessageBoxButtonData(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("buttonID", ctypes.c_int),
        ("text", ctypes.c_char_p),
    ]


# typedef struct SDL_MessageBoxColor
# {
#     Uint8 r, g, b;
# } SDL_MessageBoxColor;
class SDL_MessageBoxColor(ctypes.Structure):
    _fields_ = [("r", ctypes.c_uint8), ("g", ctypes.c_uint8), ("b", ctypes.c_uint8)]


# typedef struct SDL_MessageBoxColorScheme
# {
#     SDL_MessageBoxColor colors[SDL_MESSAGEBOX_COLOR_COUNT];
# } SDL_MessageBoxColorScheme;
class SDL_MessageBoxColorScheme(ctypes.Structure):
    _fields_ = [("colors", SDL_MessageBoxColor * 5)]


# typedef struct SDL_MessageBoxData
# {
#     SDL_MessageBoxFlags flags;
#     SDL_Window *window;                 /**< Parent window, can be NULL */
#     const char *title;                  /**< UTF-8 title */
#     const char *message;                /**< UTF-8 message text */
#     int numbuttons;
#     const SDL_MessageBoxButtonData *buttons;
#     const SDL_MessageBoxColorScheme *colorScheme;   /**< SDL_MessageBoxColorScheme, can be NULL to use system settings */
# } SDL_MessageBoxData;
class SDL_MessageBoxData(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("window", ctypes.c_void_p),
        ("title", ctypes.c_char_p),
        ("message", ctypes.c_char_p),
        ("numbuttons", ctypes.c_int),
        ("buttons", ctypes.POINTER(SDL_MessageBoxButtonData)),
        ("colorScheme", ctypes.POINTER(SDL_MessageBoxColorScheme)),
    ]


# typedef Uint32 SDL_MessageBoxButtonFlags;
# #define SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT 0x00000001u /**< Marks the default button when return is hit */
# #define SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT 0x00000002u /**< Marks the default button when escape is hit */
SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 0x1
SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 0x2
# typedef Uint32 SDL_MessageBoxFlags;
# #define SDL_MESSAGEBOX_ERROR                    0x00000010u /**< error dialog */
# #define SDL_MESSAGEBOX_WARNING                  0x00000020u /**< warning dialog */
# #define SDL_MESSAGEBOX_INFORMATION              0x00000040u /**< informational dialog */
# #define SDL_MESSAGEBOX_BUTTONS_LEFT_TO_RIGHT    0x00000080u /**< buttons placed left to right */
# #define SDL_MESSAGEBOX_BUTTONS_RIGHT_TO_LEFT    0x00000100u /**< buttons placed right to left */
SDL_MESSAGEBOX_ERROR = 0x10
SDL_MESSAGEBOX_WARNING = 0x20
SDL_MESSAGEBOX_INFORMATION = 0x40
SDL_MESSAGEBOX_BUTTONS_LEFT_TO_RIGHT = 0x80
SDL_MESSAGEBOX_BUTTONS_RIGHT_TO_LEFT = 0x100


# bool SDL_ShowMessageBox(const SDL_MessageBoxData *messageboxdata, int *buttonid);
SDL_ShowMessageBox = libsdl3.SDL_ShowMessageBox
SDL_ShowMessageBox.argtypes = [
    ctypes.POINTER(SDL_MessageBoxData),
    ctypes.POINTER(ctypes.c_int),
]
SDL_ShowMessageBox.restype = ctypes.c_bool


# bool SDL_ShowSimpleMessageBox(SDL_MessageBoxFlags flags, const char *title, const char *message, SDL_Window *window);
SDL_ShowSimpleMessageBox = libsdl3.SDL_ShowSimpleMessageBox
SDL_ShowSimpleMessageBox.argtypes = [
    ctypes.c_uint32,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_void_p,
]
SDL_ShowSimpleMessageBox.restype = ctypes.c_bool
