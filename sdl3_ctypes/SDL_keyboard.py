"""
SDL_keyboard.h
Keyboard Support
Document: https://wiki.libsdl.org/SDL3/CategoryKeyboard
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_rect import SDL_Rect

# typedef enum SDL_Capitalization
# {
#     SDL_CAPITALIZE_NONE,        /**< No auto-capitalization will be done */
#     SDL_CAPITALIZE_SENTENCES,   /**< The first letter of sentences will be capitalized */
#     SDL_CAPITALIZE_WORDS,       /**< The first letter of words will be capitalized */
#     SDL_CAPITALIZE_LETTERS      /**< All letters will be capitalized */
# } SDL_Capitalization;
SDL_CAPITALIZE_NONE = 0
SDL_CAPITALIZE_SENTENCES = 1
SDL_CAPITALIZE_WORDS = 2
SDL_CAPITALIZE_LETTERS = 3
# typedef enum SDL_TextInputType
# {
#     SDL_TEXTINPUT_TYPE_TEXT,                        /**< The input is text */
#     SDL_TEXTINPUT_TYPE_TEXT_NAME,                   /**< The input is a person's name */
#     SDL_TEXTINPUT_TYPE_TEXT_EMAIL,                  /**< The input is an e-mail address */
#     SDL_TEXTINPUT_TYPE_TEXT_USERNAME,               /**< The input is a username */
#     SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_HIDDEN,        /**< The input is a secure password that is hidden */
#     SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_VISIBLE,       /**< The input is a secure password that is visible */
#     SDL_TEXTINPUT_TYPE_NUMBER,                      /**< The input is a number */
#     SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_HIDDEN,      /**< The input is a secure PIN that is hidden */
#     SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_VISIBLE      /**< The input is a secure PIN that is visible */
# } SDL_TextInputType;
SDL_TEXTINPUT_TYPE_TEXT = 0
SDL_TEXTINPUT_TYPE_TEXT_NAME = 1
SDL_TEXTINPUT_TYPE_TEXT_EMAIL = 2
SDL_TEXTINPUT_TYPE_TEXT_USERNAME = 3
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_HIDDEN = 4
SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_VISIBLE = 5
SDL_TEXTINPUT_TYPE_NUMBER = 6
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_HIDDEN = 7
SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_VISIBLE = 8


# typedef Uint32 SDL_KeyboardID;


# bool SDL_ClearComposition(SDL_Window *window);
SDL_ClearComposition = libsdl3.SDL_ClearComposition
SDL_ClearComposition.argtypes = [ctypes.c_void_p]
SDL_ClearComposition.restype = ctypes.c_bool


# SDL_Window * SDL_GetKeyboardFocus(void);
SDL_GetKeyboardFocus = libsdl3.SDL_GetKeyboardFocus
SDL_GetKeyboardFocus.argtypes = []
SDL_GetKeyboardFocus.restype = ctypes.c_void_p


# const char * SDL_GetKeyboardNameForID(SDL_KeyboardID instance_id);
SDL_GetKeyboardNameForID = libsdl3.SDL_GetKeyboardNameForID
SDL_GetKeyboardNameForID.argtypes = [ctypes.c_uint32]
SDL_GetKeyboardNameForID.restype = ctypes.c_char_p


# SDL_KeyboardID * SDL_GetKeyboards(int *count);
SDL_GetKeyboards = libsdl3.SDL_GetKeyboards
SDL_GetKeyboards.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetKeyboards.restype = ctypes.POINTER(ctypes.c_uint32)


# const bool * SDL_GetKeyboardState(int *numkeys);
SDL_GetKeyboardState = libsdl3.SDL_GetKeyboardState
SDL_GetKeyboardState.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetKeyboardState.restype = ctypes.POINTER(ctypes.c_bool)


# SDL_Keycode SDL_GetKeyFromName(const char *name);
SDL_GetKeyFromName = libsdl3.SDL_GetKeyFromName
SDL_GetKeyFromName.argtypes = [ctypes.c_char_p]
SDL_GetKeyFromName.restype = ctypes.c_uint32


# SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode, SDL_Keymod modstate, bool key_event);
SDL_GetKeyFromScancode = libsdl3.SDL_GetKeyFromScancode
SDL_GetKeyFromScancode.argtypes = [ctypes.c_int, ctypes.c_uint16, ctypes.c_bool]
SDL_GetKeyFromScancode.restype = ctypes.c_uint32


# const char * SDL_GetKeyName(SDL_Keycode key);
SDL_GetKeyName = libsdl3.SDL_GetKeyName
SDL_GetKeyName.argtypes = [ctypes.c_uint32]
SDL_GetKeyName.restype = ctypes.c_char_p


# SDL_Keymod SDL_GetModState(void);
SDL_GetModState = libsdl3.SDL_GetModState
SDL_GetModState.argtypes = []
SDL_GetModState.restype = ctypes.c_uint16


# SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key, SDL_Keymod *modstate);
SDL_GetScancodeFromKey = libsdl3.SDL_GetScancodeFromKey
SDL_GetScancodeFromKey.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint16)]
SDL_GetScancodeFromKey.restype = ctypes.c_int


# SDL_Scancode SDL_GetScancodeFromName(const char *name);
SDL_GetScancodeFromName = libsdl3.SDL_GetScancodeFromName
SDL_GetScancodeFromName.argtypes = [ctypes.c_char_p]
SDL_GetScancodeFromName.restype = ctypes.c_int


# const char * SDL_GetScancodeName(SDL_Scancode scancode);
SDL_GetScancodeName = libsdl3.SDL_GetScancodeName
SDL_GetScancodeName.argtypes = [ctypes.c_int]
SDL_GetScancodeName.restype = ctypes.c_char_p


# bool SDL_GetTextInputArea(SDL_Window *window, SDL_Rect *rect, int *cursor);
SDL_GetTextInputArea = libsdl3.SDL_GetTextInputArea
SDL_GetTextInputArea.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetTextInputArea.restype = ctypes.c_bool


# bool SDL_HasKeyboard(void);
SDL_HasKeyboard = libsdl3.SDL_HasKeyboard
SDL_HasKeyboard.argtypes = []
SDL_HasKeyboard.restype = ctypes.c_bool


# bool SDL_HasScreenKeyboardSupport(void);
SDL_HasScreenKeyboardSupport = libsdl3.SDL_HasScreenKeyboardSupport
SDL_HasScreenKeyboardSupport.argtypes = []
SDL_HasScreenKeyboardSupport.restype = ctypes.c_bool


# void SDL_ResetKeyboard(void);
SDL_ResetKeyboard = libsdl3.SDL_ResetKeyboard
SDL_ResetKeyboard.argtypes = []
SDL_ResetKeyboard.restype = None


# bool SDL_ScreenKeyboardShown(SDL_Window *window);
SDL_ScreenKeyboardShown = libsdl3.SDL_ScreenKeyboardShown
SDL_ScreenKeyboardShown.argtypes = [ctypes.c_void_p]
SDL_ScreenKeyboardShown.restype = ctypes.c_bool


# void SDL_SetModState(SDL_Keymod modstate);
SDL_SetModState = libsdl3.SDL_SetModState
SDL_SetModState.argtypes = [ctypes.c_uint16]
SDL_SetModState.restype = None


# bool SDL_SetScancodeName(SDL_Scancode scancode, const char *name);
SDL_SetScancodeName = libsdl3.SDL_SetScancodeName
SDL_SetScancodeName.argtypes = [ctypes.c_int, ctypes.c_char_p]
SDL_SetScancodeName.restype = ctypes.c_bool


# bool SDL_SetTextInputArea(SDL_Window *window, const SDL_Rect *rect, int cursor);
SDL_SetTextInputArea = libsdl3.SDL_SetTextInputArea
SDL_SetTextInputArea.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
]
SDL_SetTextInputArea.restype = ctypes.c_bool


# bool SDL_StartTextInput(SDL_Window *window);
SDL_StartTextInput = libsdl3.SDL_StartTextInput
SDL_StartTextInput.argtypes = [ctypes.c_void_p]
SDL_StartTextInput.restype = ctypes.c_bool


# bool SDL_StartTextInputWithProperties(SDL_Window *window, SDL_PropertiesID props);
SDL_StartTextInputWithProperties = libsdl3.SDL_StartTextInputWithProperties
SDL_StartTextInputWithProperties.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_StartTextInputWithProperties.restype = ctypes.c_bool


# bool SDL_StopTextInput(SDL_Window *window);
SDL_StopTextInput = libsdl3.SDL_StopTextInput
SDL_StopTextInput.argtypes = [ctypes.c_void_p]
SDL_StopTextInput.restype = ctypes.c_bool


# bool SDL_TextInputActive(SDL_Window *window);
SDL_TextInputActive = libsdl3.SDL_TextInputActive
SDL_TextInputActive.argtypes = [ctypes.c_void_p]
SDL_TextInputActive.restype = ctypes.c_bool
