"""
SDL_assert.h
Assertions
Document: https://wiki.libsdl.org/SDL3/CategoryAssert
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_assert(condition) if (assertion_enabled && (condition)) { trigger_assertion; }
# #define SDL_assert_always(condition) SDL_enabled_assert(condition)
# #define SDL_ASSERT_LEVEL SomeNumberBasedOnVariousFactors
# #define SDL_assert_paranoid(condition) SDL_disabled_assert(condition)
# #define SDL_assert_release(condition) SDL_disabled_assert(condition)
# #define SDL_AssertBreakpoint() SDL_TriggerBreakpoint()
# #define SDL_disabled_assert(condition) \
#     do { (void) sizeof ((condition)); } while (SDL_NULL_WHILE_LOOP_CONDITION)
# #define SDL_enabled_assert(condition) \
#     do { \
#         while ( !(condition) ) { \
#             static struct SDL_AssertData sdl_assert_data = { 0, 0, #condition, 0, 0, 0, 0 }; \
#             const SDL_AssertState sdl_assert_state = SDL_ReportAssertion(&sdl_assert_data, SDL_FUNCTION, SDL_FILE, SDL_LINE); \
#             if (sdl_assert_state == SDL_ASSERTION_RETRY) { \
#                 continue; /* go again. */ \
#             } else if (sdl_assert_state == SDL_ASSERTION_BREAK) { \
#                 SDL_AssertBreakpoint(); \
#             } \
#             break; /* not retrying. */ \
#         } \
#     } while (SDL_NULL_WHILE_LOOP_CONDITION)
# #define SDL_FILE    __FILE__
# #define SDL_FUNCTION __FUNCTION__
# #define SDL_LINE    __LINE__
# #define SDL_NULL_WHILE_LOOP_CONDITION (0)
SDL_NULL_WHILE_LOOP_CONDITION = 0
# #define SDL_TriggerBreakpoint() TriggerABreakpointInAPlatformSpecificManner


# typedef enum SDL_AssertState
# {
#     SDL_ASSERTION_RETRY,  /**< Retry the assert immediately. */
#     SDL_ASSERTION_BREAK,  /**< Make the debugger trigger a breakpoint. */
#     SDL_ASSERTION_ABORT,  /**< Terminate the program. */
#     SDL_ASSERTION_IGNORE,  /**< Ignore the assert. */
#     SDL_ASSERTION_ALWAYS_IGNORE  /**< Ignore the assert from now on. */
# } SDL_AssertState;
SDL_ASSERTION_RETRY = 0
SDL_ASSERTION_BREAK = 1
SDL_ASSERTION_ABORT = 2
SDL_ASSERTION_IGNORE = 3
SDL_ASSERTION_ALWAYS_IGNORE = 4


# typedef struct SDL_AssertData
# {
#     bool always_ignore;  /**< true if app should always continue when assertion is triggered. */
#     unsigned int trigger_count; /**< Number of times this assertion has been triggered. */
#     const char *condition;  /**< A string of this assert's test code. */
#     const char *filename;  /**< The source file where this assert lives. */
#     int linenum;  /**< The line in `filename` where this assert lives. */
#     const char *function;  /**< The name of the function where this assert lives. */
#     const struct SDL_AssertData *next;  /**< next item in the linked list. */
# } SDL_AssertData;
class SDL_AssertData(ctypes.Structure):
    _fields_ = [
        ("always_ignore", ctypes.c_bool),
        ("trigger_count", ctypes.c_int),
        ("condition", ctypes.c_char_p),
        ("filename", ctypes.c_char_p),
        ("linenum", ctypes.c_int),
        ("function", ctypes.c_char_p),
        ("next", ctypes.c_void_p),
    ]


# typedef SDL_AssertState (SDLCALL *SDL_AssertionHandler)( const SDL_AssertData *data, void *userdata);
SDL_AssertionHandler = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.POINTER(SDL_AssertData), ctypes.c_void_p
)


# SDL_AssertionHandler SDL_GetAssertionHandler(void **puserdata);
SDL_GetAssertionHandler = libsdl3.SDL_GetAssertionHandler
SDL_GetAssertionHandler.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
SDL_GetAssertionHandler.restype = SDL_AssertionHandler


# const SDL_AssertData * SDL_GetAssertionReport(void);
SDL_GetAssertionReport = libsdl3.SDL_GetAssertionReport
SDL_GetAssertionReport.argtypes = []
SDL_GetAssertionReport.restype = ctypes.POINTER(SDL_AssertData)


# SDL_AssertionHandler SDL_GetDefaultAssertionHandler(void);
SDL_GetDefaultAssertionHandler = libsdl3.SDL_GetDefaultAssertionHandler
SDL_GetDefaultAssertionHandler.argtypes = []
SDL_GetDefaultAssertionHandler.restype = SDL_AssertionHandler


# SDL_AssertState SDL_ReportAssertion(SDL_AssertData *data,
#                                 const char *func,
#                                 const char *file, int line);
SDL_ReportAssertion = libsdl3.SDL_ReportAssertion
SDL_ReportAssertion.argtypes = [
    ctypes.POINTER(SDL_AssertData),
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_int,
]
SDL_ReportAssertion.restype = ctypes.c_int


# void SDL_ResetAssertionReport(void);
SDL_ResetAssertionReport = libsdl3.SDL_ResetAssertionReport
SDL_ResetAssertionReport.argtypes = []
SDL_ResetAssertionReport.restype = None


# void SDL_SetAssertionHandler(
#                 SDL_AssertionHandler handler,
#                 void *userdata);
SDL_SetAssertionHandler = libsdl3.SDL_SetAssertionHandler
SDL_SetAssertionHandler.argtypes = [SDL_AssertionHandler, ctypes.c_void_p]
SDL_SetAssertionHandler.restype = None
