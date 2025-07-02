"""
SDL_pen.h
Pen Support
Document: https://wiki.libsdl.org/SDL3/CategoryPen
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_PEN_MOUSEID ((SDL_MouseID)-2)
# #define SDL_PEN_TOUCHID ((SDL_TouchID)-2)


# typedef enum SDL_PenAxis
# {
#     SDL_PEN_AXIS_PRESSURE,  /**< Pen pressure.  Unidirectional: 0 to 1.0 */
#     SDL_PEN_AXIS_XTILT,     /**< Pen horizontal tilt angle.  Bidirectional: -90.0 to 90.0 (left-to-right). */
#     SDL_PEN_AXIS_YTILT,     /**< Pen vertical tilt angle.  Bidirectional: -90.0 to 90.0 (top-to-down). */
#     SDL_PEN_AXIS_DISTANCE,  /**< Pen distance to drawing surface.  Unidirectional: 0.0 to 1.0 */
#     SDL_PEN_AXIS_ROTATION,  /**< Pen barrel rotation.  Bidirectional: -180 to 179.9 (clockwise, 0 is facing up, -180.0 is facing down). */
#     SDL_PEN_AXIS_SLIDER,    /**< Pen finger wheel or slider (e.g., Airbrush Pen).  Unidirectional: 0 to 1.0 */
#     SDL_PEN_AXIS_TANGENTIAL_PRESSURE,    /**< Pressure from squeezing the pen ("barrel pressure"). */
#     SDL_PEN_AXIS_COUNT       /**< Total known pen axis types in this version of SDL. This number may grow in future releases! */
# } SDL_PenAxis;
SDL_PEN_AXIS_PRESSURE = 0
SDL_PEN_AXIS_XTILT = 1
SDL_PEN_AXIS_YTILT = 2
SDL_PEN_AXIS_DISTANCE = 3
SDL_PEN_AXIS_ROTATION = 4
SDL_PEN_AXIS_SLIDER = 5
SDL_PEN_AXIS_TANGENTIAL_PRESSURE = 6
SDL_PEN_AXIS_COUNT = 7


# typedef struct SDL_PenAxisEvent
# {
#     SDL_EventType type;     /**< SDL_EVENT_PEN_AXIS */
#     Uint32 reserved;
#     Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;  /**< The window with pen focus, if any */
#     SDL_PenID which;        /**< The pen instance id */
#     SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
#     float x;                /**< X coordinate, relative to window */
#     float y;                /**< Y coordinate, relative to window */
#     SDL_PenAxis axis;       /**< Axis that has changed */
#     float value;            /**< New value of axis */
# } SDL_PenAxisEvent;
class SDL_PenAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("pen_state", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("axis", ctypes.c_int),
        ("value", ctypes.c_float),
    ]


# typedef struct SDL_PenButtonEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_PEN_BUTTON_DOWN or SDL_EVENT_PEN_BUTTON_UP */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with mouse focus, if any */
#     SDL_PenID which;        /**< The pen instance id */
#     SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
#     float x;                /**< X coordinate, relative to window */
#     float y;                /**< Y coordinate, relative to window */
#     Uint8 button;       /**< The pen button index (first button is 1). */
#     bool down;      /**< true if the button is pressed */
# } SDL_PenButtonEvent;
class SDL_PenButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("pen_state", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
    ]


# typedef struct SDL_PenMotionEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_PEN_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with pen focus, if any */
#     SDL_PenID which;        /**< The pen instance id */
#     SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
#     float x;                /**< X coordinate, relative to window */
#     float y;                /**< Y coordinate, relative to window */
# } SDL_PenMotionEvent;
class SDL_PenMotionEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("pen_state", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]


# typedef struct SDL_PenProximityEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_PEN_PROXIMITY_IN or SDL_EVENT_PEN_PROXIMITY_OUT */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with pen focus, if any */
#     SDL_PenID which;        /**< The pen instance id */
# } SDL_PenProximityEvent;
class SDL_PenProximityEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_PenTouchEvent
# {
#     SDL_EventType type;     /**< SDL_EVENT_PEN_DOWN or SDL_EVENT_PEN_UP */
#     Uint32 reserved;
#     Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;  /**< The window with pen focus, if any */
#     SDL_PenID which;        /**< The pen instance id */
#     SDL_PenInputFlags pen_state;   /**< Complete pen input state at time of event */
#     float x;                /**< X coordinate, relative to window */
#     float y;                /**< Y coordinate, relative to window */
#     bool eraser;        /**< true if eraser end is used (not all pens support this). */
#     bool down;          /**< true if the pen is touching or false if the pen is lifted off */
# } SDL_PenTouchEvent;
class SDL_PenTouchEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("pen_state", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("eraser", ctypes.c_bool),
        ("down", ctypes.c_bool),
    ]


# typedef Uint32 SDL_PenID;
# typedef Uint32 SDL_PenInputFlags;
# #define SDL_PEN_INPUT_DOWN       (1u << 0)  /**< pen is pressed down */
# #define SDL_PEN_INPUT_BUTTON_1   (1u << 1)  /**< button 1 is pressed */
# #define SDL_PEN_INPUT_BUTTON_2   (1u << 2)  /**< button 2 is pressed */
# #define SDL_PEN_INPUT_BUTTON_3   (1u << 3)  /**< button 3 is pressed */
# #define SDL_PEN_INPUT_BUTTON_4   (1u << 4)  /**< button 4 is pressed */
# #define SDL_PEN_INPUT_BUTTON_5   (1u << 5)  /**< button 5 is pressed */
# #define SDL_PEN_INPUT_ERASER_TIP (1u << 30) /**< eraser tip is used */
SDL_PEN_INPUT_DOWN = 0x1
SDL_PEN_INPUT_BUTTON_1 = 0x2
SDL_PEN_INPUT_BUTTON_2 = 0x4
SDL_PEN_INPUT_BUTTON_3 = 0x8
SDL_PEN_INPUT_BUTTON_4 = 0x10
SDL_PEN_INPUT_BUTTON_5 = 0x20
SDL_PEN_INPUT_ERASER_TIP = 0x40000000
