"""
SDL_events.h
Event Handling
Document: https://wiki.libsdl.org/SDL3/CategoryEvents
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_EventAction
# {
#     SDL_ADDEVENT,  /**< Add events to the back of the queue. */
#     SDL_PEEKEVENT, /**< Check but don't remove events from the queue front. */
#     SDL_GETEVENT   /**< Retrieve/remove events from the front of the queue. */
# } SDL_EventAction;
SDL_ADDEVENT = 0
SDL_PEEKEVENT = 1
SDL_GETEVENT = 2
# typedef enum SDL_EventType
# {
#     SDL_EVENT_FIRST     = 0,     /**< Unused (do not remove) */
#     /* Application events */
#     SDL_EVENT_QUIT           = 0x100, /**< User-requested quit */
#     /* These application events have special meaning on iOS and Android, see README-ios.md and README-android.md for details */
#     SDL_EVENT_TERMINATING,      /**< The application is being terminated by the OS. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationWillTerminate()
#                                      Called on Android in onDestroy()
#                                 */
#     SDL_EVENT_LOW_MEMORY,       /**< The application is low on memory, free memory if possible. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationDidReceiveMemoryWarning()
#                                      Called on Android in onTrimMemory()
#                                 */
#     SDL_EVENT_WILL_ENTER_BACKGROUND, /**< The application is about to enter the background. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationWillResignActive()
#                                      Called on Android in onPause()
#                                 */
#     SDL_EVENT_DID_ENTER_BACKGROUND, /**< The application did enter the background and may not get CPU for some time. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationDidEnterBackground()
#                                      Called on Android in onPause()
#                                 */
#     SDL_EVENT_WILL_ENTER_FOREGROUND, /**< The application is about to enter the foreground. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationWillEnterForeground()
#                                      Called on Android in onResume()
#                                 */
#     SDL_EVENT_DID_ENTER_FOREGROUND, /**< The application is now interactive. This event must be handled in a callback set with SDL_AddEventWatch().
#                                      Called on iOS in applicationDidBecomeActive()
#                                      Called on Android in onResume()
#                                 */
#     SDL_EVENT_LOCALE_CHANGED,  /**< The user's locale preferences have changed. */
#     SDL_EVENT_SYSTEM_THEME_CHANGED, /**< The system theme changed */
#     /* Display events */
#     /* 0x150 was SDL_DISPLAYEVENT, reserve the number for sdl2-compat */
#     SDL_EVENT_DISPLAY_ORIENTATION = 0x151,   /**< Display orientation has changed to data1 */
#     SDL_EVENT_DISPLAY_ADDED,                 /**< Display has been added to the system */
#     SDL_EVENT_DISPLAY_REMOVED,               /**< Display has been removed from the system */
#     SDL_EVENT_DISPLAY_MOVED,                 /**< Display has changed position */
#     SDL_EVENT_DISPLAY_DESKTOP_MODE_CHANGED,  /**< Display has changed desktop mode */
#     SDL_EVENT_DISPLAY_CURRENT_MODE_CHANGED,  /**< Display has changed current mode */
#     SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED, /**< Display has changed content scale */
#     SDL_EVENT_DISPLAY_FIRST = SDL_EVENT_DISPLAY_ORIENTATION,
#     SDL_EVENT_DISPLAY_LAST = SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED,
#     /* Window events */
#     /* 0x200 was SDL_WINDOWEVENT, reserve the number for sdl2-compat */
#     /* 0x201 was SDL_SYSWMEVENT, reserve the number for sdl2-compat */
#     SDL_EVENT_WINDOW_SHOWN = 0x202,     /**< Window has been shown */
#     SDL_EVENT_WINDOW_HIDDEN,            /**< Window has been hidden */
#     SDL_EVENT_WINDOW_EXPOSED,           /**< Window has been exposed and should be redrawn, and can be redrawn directly from event watchers for this event.
#                                              data1 is 1 for live-resize expose events, 0 otherwise. */
#     SDL_EVENT_WINDOW_MOVED,             /**< Window has been moved to data1, data2 */
#     SDL_EVENT_WINDOW_RESIZED,           /**< Window has been resized to data1xdata2 */
#     SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED,/**< The pixel size of the window has changed to data1xdata2 */
#     SDL_EVENT_WINDOW_METAL_VIEW_RESIZED,/**< The pixel size of a Metal view associated with the window has changed */
#     SDL_EVENT_WINDOW_MINIMIZED,         /**< Window has been minimized */
#     SDL_EVENT_WINDOW_MAXIMIZED,         /**< Window has been maximized */
#     SDL_EVENT_WINDOW_RESTORED,          /**< Window has been restored to normal size and position */
#     SDL_EVENT_WINDOW_MOUSE_ENTER,       /**< Window has gained mouse focus */
#     SDL_EVENT_WINDOW_MOUSE_LEAVE,       /**< Window has lost mouse focus */
#     SDL_EVENT_WINDOW_FOCUS_GAINED,      /**< Window has gained keyboard focus */
#     SDL_EVENT_WINDOW_FOCUS_LOST,        /**< Window has lost keyboard focus */
#     SDL_EVENT_WINDOW_CLOSE_REQUESTED,   /**< The window manager requests that the window be closed */
#     SDL_EVENT_WINDOW_HIT_TEST,          /**< Window had a hit test that wasn't SDL_HITTEST_NORMAL */
#     SDL_EVENT_WINDOW_ICCPROF_CHANGED,   /**< The ICC profile of the window's display has changed */
#     SDL_EVENT_WINDOW_DISPLAY_CHANGED,   /**< Window has been moved to display data1 */
#     SDL_EVENT_WINDOW_DISPLAY_SCALE_CHANGED, /**< Window display scale has been changed */
#     SDL_EVENT_WINDOW_SAFE_AREA_CHANGED, /**< The window safe area has been changed */
#     SDL_EVENT_WINDOW_OCCLUDED,          /**< The window has been occluded */
#     SDL_EVENT_WINDOW_ENTER_FULLSCREEN,  /**< The window has entered fullscreen mode */
#     SDL_EVENT_WINDOW_LEAVE_FULLSCREEN,  /**< The window has left fullscreen mode */
#     SDL_EVENT_WINDOW_DESTROYED,         /**< The window with the associated ID is being or has been destroyed. If this message is being handled
#                                              in an event watcher, the window handle is still valid and can still be used to retrieve any properties
#                                              associated with the window. Otherwise, the handle has already been destroyed and all resources
#                                              associated with it are invalid */
#     SDL_EVENT_WINDOW_HDR_STATE_CHANGED, /**< Window HDR properties have changed */
#     SDL_EVENT_WINDOW_FIRST = SDL_EVENT_WINDOW_SHOWN,
#     SDL_EVENT_WINDOW_LAST = SDL_EVENT_WINDOW_HDR_STATE_CHANGED,
#     /* Keyboard events */
#     SDL_EVENT_KEY_DOWN        = 0x300, /**< Key pressed */
#     SDL_EVENT_KEY_UP,                  /**< Key released */
#     SDL_EVENT_TEXT_EDITING,            /**< Keyboard text editing (composition) */
#     SDL_EVENT_TEXT_INPUT,              /**< Keyboard text input */
#     SDL_EVENT_KEYMAP_CHANGED,          /**< Keymap changed due to a system event such as an
#                                             input language or keyboard layout change. */
#     SDL_EVENT_KEYBOARD_ADDED,          /**< A new keyboard has been inserted into the system */
#     SDL_EVENT_KEYBOARD_REMOVED,        /**< A keyboard has been removed */
#     SDL_EVENT_TEXT_EDITING_CANDIDATES, /**< Keyboard text editing candidates */
#     /* Mouse events */
#     SDL_EVENT_MOUSE_MOTION    = 0x400, /**< Mouse moved */
#     SDL_EVENT_MOUSE_BUTTON_DOWN,       /**< Mouse button pressed */
#     SDL_EVENT_MOUSE_BUTTON_UP,         /**< Mouse button released */
#     SDL_EVENT_MOUSE_WHEEL,             /**< Mouse wheel motion */
#     SDL_EVENT_MOUSE_ADDED,             /**< A new mouse has been inserted into the system */
#     SDL_EVENT_MOUSE_REMOVED,           /**< A mouse has been removed */
#     /* Joystick events */
#     SDL_EVENT_JOYSTICK_AXIS_MOTION  = 0x600, /**< Joystick axis motion */
#     SDL_EVENT_JOYSTICK_BALL_MOTION,          /**< Joystick trackball motion */
#     SDL_EVENT_JOYSTICK_HAT_MOTION,           /**< Joystick hat position change */
#     SDL_EVENT_JOYSTICK_BUTTON_DOWN,          /**< Joystick button pressed */
#     SDL_EVENT_JOYSTICK_BUTTON_UP,            /**< Joystick button released */
#     SDL_EVENT_JOYSTICK_ADDED,                /**< A new joystick has been inserted into the system */
#     SDL_EVENT_JOYSTICK_REMOVED,              /**< An opened joystick has been removed */
#     SDL_EVENT_JOYSTICK_BATTERY_UPDATED,      /**< Joystick battery level change */
#     SDL_EVENT_JOYSTICK_UPDATE_COMPLETE,      /**< Joystick update is complete */
#     /* Gamepad events */
#     SDL_EVENT_GAMEPAD_AXIS_MOTION  = 0x650, /**< Gamepad axis motion */
#     SDL_EVENT_GAMEPAD_BUTTON_DOWN,          /**< Gamepad button pressed */
#     SDL_EVENT_GAMEPAD_BUTTON_UP,            /**< Gamepad button released */
#     SDL_EVENT_GAMEPAD_ADDED,                /**< A new gamepad has been inserted into the system */
#     SDL_EVENT_GAMEPAD_REMOVED,              /**< A gamepad has been removed */
#     SDL_EVENT_GAMEPAD_REMAPPED,             /**< The gamepad mapping was updated */
#     SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN,        /**< Gamepad touchpad was touched */
#     SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION,      /**< Gamepad touchpad finger was moved */
#     SDL_EVENT_GAMEPAD_TOUCHPAD_UP,          /**< Gamepad touchpad finger was lifted */
#     SDL_EVENT_GAMEPAD_SENSOR_UPDATE,        /**< Gamepad sensor was updated */
#     SDL_EVENT_GAMEPAD_UPDATE_COMPLETE,      /**< Gamepad update is complete */
#     SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED,  /**< Gamepad Steam handle has changed */
#     /* Touch events */
#     SDL_EVENT_FINGER_DOWN      = 0x700,
#     SDL_EVENT_FINGER_UP,
#     SDL_EVENT_FINGER_MOTION,
#     SDL_EVENT_FINGER_CANCELED,
#     /* 0x800, 0x801, and 0x802 were the Gesture events from SDL2. Do not reuse these values! sdl2-compat needs them! */
#     /* Clipboard events */
#     SDL_EVENT_CLIPBOARD_UPDATE = 0x900, /**< The clipboard or primary selection changed */
#     /* Drag and drop events */
#     SDL_EVENT_DROP_FILE        = 0x1000, /**< The system requests a file open */
#     SDL_EVENT_DROP_TEXT,                 /**< text/plain drag-and-drop event */
#     SDL_EVENT_DROP_BEGIN,                /**< A new set of drops is beginning (NULL filename) */
#     SDL_EVENT_DROP_COMPLETE,             /**< Current set of drops is now complete (NULL filename) */
#     SDL_EVENT_DROP_POSITION,             /**< Position while moving over the window */
#     /* Audio hotplug events */
#     SDL_EVENT_AUDIO_DEVICE_ADDED = 0x1100,  /**< A new audio device is available */
#     SDL_EVENT_AUDIO_DEVICE_REMOVED,         /**< An audio device has been removed. */
#     SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED,  /**< An audio device's format has been changed by the system. */
#     /* Sensor events */
#     SDL_EVENT_SENSOR_UPDATE = 0x1200,     /**< A sensor was updated */
#     /* Pressure-sensitive pen events */
#     SDL_EVENT_PEN_PROXIMITY_IN = 0x1300,  /**< Pressure-sensitive pen has become available */
#     SDL_EVENT_PEN_PROXIMITY_OUT,          /**< Pressure-sensitive pen has become unavailable */
#     SDL_EVENT_PEN_DOWN,                   /**< Pressure-sensitive pen touched drawing surface */
#     SDL_EVENT_PEN_UP,                     /**< Pressure-sensitive pen stopped touching drawing surface */
#     SDL_EVENT_PEN_BUTTON_DOWN,            /**< Pressure-sensitive pen button pressed */
#     SDL_EVENT_PEN_BUTTON_UP,              /**< Pressure-sensitive pen button released */
#     SDL_EVENT_PEN_MOTION,                 /**< Pressure-sensitive pen is moving on the tablet */
#     SDL_EVENT_PEN_AXIS,                   /**< Pressure-sensitive pen angle/pressure/etc changed */
#     /* Camera hotplug events */
#     SDL_EVENT_CAMERA_DEVICE_ADDED = 0x1400,  /**< A new camera device is available */
#     SDL_EVENT_CAMERA_DEVICE_REMOVED,         /**< A camera device has been removed. */
#     SDL_EVENT_CAMERA_DEVICE_APPROVED,        /**< A camera device has been approved for use by the user. */
#     SDL_EVENT_CAMERA_DEVICE_DENIED,          /**< A camera device has been denied for use by the user. */
#     /* Render events */
#     SDL_EVENT_RENDER_TARGETS_RESET = 0x2000, /**< The render targets have been reset and their contents need to be updated */
#     SDL_EVENT_RENDER_DEVICE_RESET, /**< The device has been reset and all textures need to be recreated */
#     SDL_EVENT_RENDER_DEVICE_LOST, /**< The device has been lost and can't be recovered. */
#     /* Reserved events for private platforms */
#     SDL_EVENT_PRIVATE0 = 0x4000,
#     SDL_EVENT_PRIVATE1,
#     SDL_EVENT_PRIVATE2,
#     SDL_EVENT_PRIVATE3,
#     /* Internal events */
#     SDL_EVENT_POLL_SENTINEL = 0x7F00, /**< Signals the end of an event poll cycle */
#     /** Events SDL_EVENT_USER through SDL_EVENT_LAST are for your use,
#      *  and should be allocated with SDL_RegisterEvents()
#      */
#     SDL_EVENT_USER    = 0x8000,
#     /**
#      *  This last event is only for bounding internal arrays
#      */
#     SDL_EVENT_LAST    = 0xFFFF,
#     /* This just makes sure the enum is the size of Uint32 */
#     SDL_EVENT_ENUM_PADDING = 0x7FFFFFFF
# } SDL_EventType;
SDL_EVENT_FIRST = 0
SDL_EVENT_QUIT = 0x100
SDL_EVENT_TERMINATING = 0x101
SDL_EVENT_LOW_MEMORY = 0x102
SDL_EVENT_WILL_ENTER_BACKGROUND = 0x103
SDL_EVENT_DID_ENTER_BACKGROUND = 0x104
SDL_EVENT_WILL_ENTER_FOREGROUND = 0x105
SDL_EVENT_DID_ENTER_FOREGROUND = 0x106
SDL_EVENT_LOCALE_CHANGED = 0x107
SDL_EVENT_SYSTEM_THEME_CHANGED = 0x108
SDL_EVENT_DISPLAY_ORIENTATION = 0x151
SDL_EVENT_DISPLAY_ADDED = 0x152
SDL_EVENT_DISPLAY_REMOVED = 0x153
SDL_EVENT_DISPLAY_MOVED = 0x154
SDL_EVENT_DISPLAY_DESKTOP_MODE_CHANGED = 0x155
SDL_EVENT_DISPLAY_CURRENT_MODE_CHANGED = 0x156
SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED = 0x157
SDL_EVENT_DISPLAY_FIRST = SDL_EVENT_DISPLAY_ORIENTATION
SDL_EVENT_DISPLAY_LAST = SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED
SDL_EVENT_WINDOW_SHOWN = 0x202
SDL_EVENT_WINDOW_HIDDEN = 0x203
SDL_EVENT_WINDOW_EXPOSED = 0x204
SDL_EVENT_WINDOW_MOVED = 0x205
SDL_EVENT_WINDOW_RESIZED = 0x206
SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED = 0x207
SDL_EVENT_WINDOW_METAL_VIEW_RESIZED = 0x208
SDL_EVENT_WINDOW_MINIMIZED = 0x209
SDL_EVENT_WINDOW_MAXIMIZED = 0x20A
SDL_EVENT_WINDOW_RESTORED = 0x20B
SDL_EVENT_WINDOW_MOUSE_ENTER = 0x20C
SDL_EVENT_WINDOW_MOUSE_LEAVE = 0x20D
SDL_EVENT_WINDOW_FOCUS_GAINED = 0x20E
SDL_EVENT_WINDOW_FOCUS_LOST = 0x20F
SDL_EVENT_WINDOW_CLOSE_REQUESTED = 0x210
SDL_EVENT_WINDOW_HIT_TEST = 0x211
SDL_EVENT_WINDOW_ICCPROF_CHANGED = 0x212
SDL_EVENT_WINDOW_DISPLAY_CHANGED = 0x213
SDL_EVENT_WINDOW_DISPLAY_SCALE_CHANGED = 0x214
SDL_EVENT_WINDOW_SAFE_AREA_CHANGED = 0x215
SDL_EVENT_WINDOW_OCCLUDED = 0x216
SDL_EVENT_WINDOW_ENTER_FULLSCREEN = 0x217
SDL_EVENT_WINDOW_LEAVE_FULLSCREEN = 0x218
SDL_EVENT_WINDOW_DESTROYED = 0x219
SDL_EVENT_WINDOW_HDR_STATE_CHANGED = 0x21A
SDL_EVENT_WINDOW_FIRST = SDL_EVENT_WINDOW_SHOWN
SDL_EVENT_WINDOW_LAST = SDL_EVENT_WINDOW_HDR_STATE_CHANGED
SDL_EVENT_KEY_DOWN = 0x300
SDL_EVENT_KEY_UP = 0x301
SDL_EVENT_TEXT_EDITING = 0x302
SDL_EVENT_TEXT_INPUT = 0x303
SDL_EVENT_KEYMAP_CHANGED = 0x304
SDL_EVENT_KEYBOARD_ADDED = 0x305
SDL_EVENT_KEYBOARD_REMOVED = 0x306
SDL_EVENT_TEXT_EDITING_CANDIDATES = 0x307
SDL_EVENT_MOUSE_MOTION = 0x400
SDL_EVENT_MOUSE_BUTTON_DOWN = 0x401
SDL_EVENT_MOUSE_BUTTON_UP = 0x402
SDL_EVENT_MOUSE_WHEEL = 0x403
SDL_EVENT_MOUSE_ADDED = 0x404
SDL_EVENT_MOUSE_REMOVED = 0x405
SDL_EVENT_JOYSTICK_AXIS_MOTION = 0x600
SDL_EVENT_JOYSTICK_BALL_MOTION = 0x601
SDL_EVENT_JOYSTICK_HAT_MOTION = 0x602
SDL_EVENT_JOYSTICK_BUTTON_DOWN = 0x603
SDL_EVENT_JOYSTICK_BUTTON_UP = 0x604
SDL_EVENT_JOYSTICK_ADDED = 0x605
SDL_EVENT_JOYSTICK_REMOVED = 0x606
SDL_EVENT_JOYSTICK_BATTERY_UPDATED = 0x607
SDL_EVENT_JOYSTICK_UPDATE_COMPLETE = 0x608
SDL_EVENT_GAMEPAD_AXIS_MOTION = 0x650
SDL_EVENT_GAMEPAD_BUTTON_DOWN = 0x651
SDL_EVENT_GAMEPAD_BUTTON_UP = 0x652
SDL_EVENT_GAMEPAD_ADDED = 0x653
SDL_EVENT_GAMEPAD_REMOVED = 0x654
SDL_EVENT_GAMEPAD_REMAPPED = 0x655
SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN = 0x656
SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION = 0x657
SDL_EVENT_GAMEPAD_TOUCHPAD_UP = 0x658
SDL_EVENT_GAMEPAD_SENSOR_UPDATE = 0x659
SDL_EVENT_GAMEPAD_UPDATE_COMPLETE = 0x65A
SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED = 0x65B
SDL_EVENT_FINGER_DOWN = 0x700
SDL_EVENT_FINGER_UP = 0x701
SDL_EVENT_FINGER_MOTION = 0x702
SDL_EVENT_FINGER_CANCELED = 0x703
SDL_EVENT_CLIPBOARD_UPDATE = 0x900
SDL_EVENT_DROP_FILE = 0x1000
SDL_EVENT_DROP_TEXT = 0x1001
SDL_EVENT_DROP_BEGIN = 0x1002
SDL_EVENT_DROP_COMPLETE = 0x1003
SDL_EVENT_DROP_POSITION = 0x1004
SDL_EVENT_AUDIO_DEVICE_ADDED = 0x1100
SDL_EVENT_AUDIO_DEVICE_REMOVED = 0x1101
SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED = 0x1102
SDL_EVENT_SENSOR_UPDATE = 0x1200
SDL_EVENT_PEN_PROXIMITY_IN = 0x1300
SDL_EVENT_PEN_PROXIMITY_OUT = 0x1301
SDL_EVENT_PEN_DOWN = 0x1302
SDL_EVENT_PEN_UP = 0x1303
SDL_EVENT_PEN_BUTTON_DOWN = 0x1304
SDL_EVENT_PEN_BUTTON_UP = 0x1305
SDL_EVENT_PEN_MOTION = 0x1306
SDL_EVENT_PEN_AXIS = 0x1307
SDL_EVENT_CAMERA_DEVICE_ADDED = 0x1400
SDL_EVENT_CAMERA_DEVICE_REMOVED = 0x1401
SDL_EVENT_CAMERA_DEVICE_APPROVED = 0x1402
SDL_EVENT_CAMERA_DEVICE_DENIED = 0x1403
SDL_EVENT_RENDER_TARGETS_RESET = 0x2000
SDL_EVENT_RENDER_DEVICE_RESET = 0x2001
SDL_EVENT_RENDER_DEVICE_LOST = 0x2002
SDL_EVENT_PRIVATE0 = 0x4000
SDL_EVENT_PRIVATE1 = 0x4001
SDL_EVENT_PRIVATE2 = 0x4002
SDL_EVENT_PRIVATE3 = 0x4003
SDL_EVENT_POLL_SENTINEL = 0x7F00
SDL_EVENT_USER = 0x8000
SDL_EVENT_LAST = 0xFFFF
SDL_EVENT_ENUM_PADDING = 0x7FFFFFFF


# typedef struct SDL_AudioDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_AUDIO_DEVICE_ADDED, or SDL_EVENT_AUDIO_DEVICE_REMOVED, or SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_AudioDeviceID which;       /**< SDL_AudioDeviceID for the device being added or removed or changing */
#     bool recording; /**< false if a playback device, true if a recording device. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_AudioDeviceEvent;
class SDL_AudioDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("recording", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_CameraDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_CAMERA_DEVICE_ADDED, SDL_EVENT_CAMERA_DEVICE_REMOVED, SDL_EVENT_CAMERA_DEVICE_APPROVED, SDL_EVENT_CAMERA_DEVICE_DENIED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_CameraID which;       /**< SDL_CameraID for the device being added or removed or changing */
# } SDL_CameraDeviceEvent;
class SDL_CameraDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_ClipboardEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_CLIPBOARD_UPDATE */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     bool owner;         /**< are we owning the clipboard (internal update) */
#     Sint32 num_mime_types;   /**< number of mime types */
#     const char **mime_types; /**< current mime types */
# } SDL_ClipboardEvent;
class SDL_ClipboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("owner", ctypes.c_bool),
        ("num_mime_types", ctypes.c_int32),
        ("mime_types", ctypes.POINTER(ctypes.c_char_p)),
    ]


# typedef struct SDL_CommonEvent
# {
#     Uint32 type;        /**< Event type, shared with all events, Uint32 to cover user events which are not in the SDL_EventType enumeration */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
# } SDL_CommonEvent;
class SDL_CommonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
    ]


# typedef struct SDL_DisplayEvent
# {
#     SDL_EventType type; /**< SDL_DISPLAYEVENT_* */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_DisplayID displayID;/**< The associated display */
#     Sint32 data1;       /**< event dependent data */
#     Sint32 data2;       /**< event dependent data */
# } SDL_DisplayEvent;
class SDL_DisplayEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("displayID", ctypes.c_uint32),
        ("data1", ctypes.c_int32),
        ("data2", ctypes.c_int32),
    ]


# typedef struct SDL_DropEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_DROP_BEGIN or SDL_EVENT_DROP_FILE or SDL_EVENT_DROP_TEXT or SDL_EVENT_DROP_COMPLETE or SDL_EVENT_DROP_POSITION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;    /**< The window that was dropped on, if any */
#     float x;            /**< X coordinate, relative to window (not on begin) */
#     float y;            /**< Y coordinate, relative to window (not on begin) */
#     const char *source; /**< The source app that sent this drop event, or NULL if that isn't available */
#     const char *data;   /**< The text for SDL_EVENT_DROP_TEXT and the file name for SDL_EVENT_DROP_FILE, NULL for other events */
# } SDL_DropEvent;
class SDL_DropEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("source", ctypes.c_char_p),
        ("data", ctypes.c_char_p),
    ]


# typedef struct SDL_GamepadAxisEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_GAMEPAD_AXIS_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 axis;         /**< The gamepad axis (SDL_GamepadAxis) */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
#     Sint16 value;       /**< The axis value (range: -32768 to 32767) */
#     Uint16 padding4;
# } SDL_GamepadAxisEvent;
class SDL_GamepadAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_int16),
        ("padding4", ctypes.c_uint16),
    ]


# typedef struct SDL_GamepadButtonEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_GAMEPAD_BUTTON_DOWN or SDL_EVENT_GAMEPAD_BUTTON_UP */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 button;       /**< The gamepad button (SDL_GamepadButton) */
#     bool down;      /**< true if the button is pressed */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_GamepadButtonEvent;
class SDL_GamepadButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_GamepadDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_GAMEPAD_ADDED, SDL_EVENT_GAMEPAD_REMOVED, or SDL_EVENT_GAMEPAD_REMAPPED, SDL_EVENT_GAMEPAD_UPDATE_COMPLETE or SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which;       /**< The joystick instance id */
# } SDL_GamepadDeviceEvent;
class SDL_GamepadDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_GamepadSensorEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_GAMEPAD_SENSOR_UPDATE */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Sint32 sensor;      /**< The type of the sensor, one of the values of SDL_SensorType */
#     float data[3];      /**< Up to 3 values from the sensor, as defined in SDL_sensor.h */
#     Uint64 sensor_timestamp; /**< The timestamp of the sensor reading in nanoseconds, not necessarily synchronized with the system clock */
# } SDL_GamepadSensorEvent;
class SDL_GamepadSensorEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("sensor", ctypes.c_int32),
        ("data", ctypes.c_float * 3),
        ("sensor_timestamp", ctypes.c_uint64),
    ]


# typedef struct SDL_GamepadTouchpadEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN or SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION or SDL_EVENT_GAMEPAD_TOUCHPAD_UP */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Sint32 touchpad;    /**< The index of the touchpad */
#     Sint32 finger;      /**< The index of the finger on the touchpad */
#     float x;            /**< Normalized in the range 0...1 with 0 being on the left */
#     float y;            /**< Normalized in the range 0...1 with 0 being at the top */
#     float pressure;     /**< Normalized in the range 0...1 */
# } SDL_GamepadTouchpadEvent;
class SDL_GamepadTouchpadEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("touchpad", ctypes.c_int32),
        ("finger", ctypes.c_int32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("pressure", ctypes.c_float),
    ]


# typedef struct SDL_JoyAxisEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_AXIS_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 axis;         /**< The joystick axis index */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
#     Sint16 value;       /**< The axis value (range: -32768 to 32767) */
#     Uint16 padding4;
# } SDL_JoyAxisEvent;
class SDL_JoyAxisEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("axis", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("value", ctypes.c_int16),
        ("padding4", ctypes.c_uint16),
    ]


# typedef struct SDL_JoyBallEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_BALL_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 ball;         /**< The joystick trackball index */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
#     Sint16 xrel;        /**< The relative motion in the X direction */
#     Sint16 yrel;        /**< The relative motion in the Y direction */
# } SDL_JoyBallEvent;
class SDL_JoyBallEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("ball", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
        ("xrel", ctypes.c_int16),
        ("yrel", ctypes.c_int16),
    ]


# typedef struct SDL_JoyBatteryEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_BATTERY_UPDATED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     SDL_PowerState state; /**< The joystick battery state */
#     int percent;          /**< The joystick battery percent charge remaining */
# } SDL_JoyBatteryEvent;
class SDL_JoyBatteryEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("state", ctypes.c_int),
        ("percent", ctypes.c_int),
    ]


# typedef struct SDL_JoyButtonEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_BUTTON_DOWN or SDL_EVENT_JOYSTICK_BUTTON_UP */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 button;       /**< The joystick button index */
#     bool down;      /**< true if the button is pressed */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_JoyButtonEvent;
class SDL_JoyButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_JoyDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_ADDED or SDL_EVENT_JOYSTICK_REMOVED or SDL_EVENT_JOYSTICK_UPDATE_COMPLETE */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which;       /**< The joystick instance id */
# } SDL_JoyDeviceEvent;
class SDL_JoyDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_JoyHatEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_JOYSTICK_HAT_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_JoystickID which; /**< The joystick instance id */
#     Uint8 hat;          /**< The joystick hat index */
#     Uint8 value;        /**< The hat position value.
#                          *   \sa SDL_HAT_LEFTUP SDL_HAT_UP SDL_HAT_RIGHTUP
#                          *   \sa SDL_HAT_LEFT SDL_HAT_CENTERED SDL_HAT_RIGHT
#                          *   \sa SDL_HAT_LEFTDOWN SDL_HAT_DOWN SDL_HAT_RIGHTDOWN
#                          *
#                          *   Note that zero means the POV is centered.
#                          */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_JoyHatEvent;
class SDL_JoyHatEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("hat", ctypes.c_uint8),
        ("value", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_KeyboardDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_KEYBOARD_ADDED or SDL_EVENT_KEYBOARD_REMOVED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_KeyboardID which;   /**< The keyboard instance id */
# } SDL_KeyboardDeviceEvent;
class SDL_KeyboardDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_KeyboardEvent
# {
#     SDL_EventType type;     /**< SDL_EVENT_KEY_DOWN or SDL_EVENT_KEY_UP */
#     Uint32 reserved;
#     Uint64 timestamp;       /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;  /**< The window with keyboard focus, if any */
#     SDL_KeyboardID which;   /**< The keyboard instance id, or 0 if unknown or virtual */
#     SDL_Scancode scancode;  /**< SDL physical key code */
#     SDL_Keycode key;        /**< SDL virtual key code */
#     SDL_Keymod mod;         /**< current key modifiers */
#     Uint16 raw;             /**< The platform dependent scancode for this event */
#     bool down;              /**< true if the key is pressed */
#     bool repeat;            /**< true if this is a key repeat */
# } SDL_KeyboardEvent;
class SDL_KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("scancode", ctypes.c_int),
        ("key", ctypes.c_uint32),
        ("mod", ctypes.c_uint16),
        ("raw", ctypes.c_uint16),
        ("down", ctypes.c_bool),
        ("repeat", ctypes.c_bool),
    ]


# typedef struct SDL_MouseButtonEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_MOUSE_BUTTON_DOWN or SDL_EVENT_MOUSE_BUTTON_UP */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with mouse focus, if any */
#     SDL_MouseID which;  /**< The mouse instance id in relative mode, SDL_TOUCH_MOUSEID for touch events, or 0 */
#     Uint8 button;       /**< The mouse button index */
#     bool down;          /**< true if the button is pressed */
#     Uint8 clicks;       /**< 1 for single-click, 2 for double-click, etc. */
#     Uint8 padding;
#     float x;            /**< X coordinate, relative to window */
#     float y;            /**< Y coordinate, relative to window */
# } SDL_MouseButtonEvent;
class SDL_MouseButtonEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("button", ctypes.c_uint8),
        ("down", ctypes.c_bool),
        ("clicks", ctypes.c_uint8),
        ("padding", ctypes.c_uint8),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]


# typedef struct SDL_MouseDeviceEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_MOUSE_ADDED or SDL_EVENT_MOUSE_REMOVED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_MouseID which;  /**< The mouse instance id */
# } SDL_MouseDeviceEvent;
class SDL_MouseDeviceEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
    ]


# typedef struct SDL_MouseMotionEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_MOUSE_MOTION */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with mouse focus, if any */
#     SDL_MouseID which;  /**< The mouse instance id in relative mode, SDL_TOUCH_MOUSEID for touch events, or 0 */
#     SDL_MouseButtonFlags state;       /**< The current button state */
#     float x;            /**< X coordinate, relative to window */
#     float y;            /**< Y coordinate, relative to window */
#     float xrel;         /**< The relative motion in the X direction */
#     float yrel;         /**< The relative motion in the Y direction */
# } SDL_MouseMotionEvent;
class SDL_MouseMotionEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("state", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("xrel", ctypes.c_float),
        ("yrel", ctypes.c_float),
    ]


# typedef struct SDL_MouseWheelEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_MOUSE_WHEEL */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with mouse focus, if any */
#     SDL_MouseID which;  /**< The mouse instance id in relative mode or 0 */
#     float x;            /**< The amount scrolled horizontally, positive to the right and negative to the left */
#     float y;            /**< The amount scrolled vertically, positive away from the user and negative toward the user */
#     SDL_MouseWheelDirection direction; /**< Set to one of the SDL_MOUSEWHEEL_* defines. When FLIPPED the values in X and Y will be opposite. Multiply by -1 to change them back */
#     float mouse_x;      /**< X coordinate, relative to window */
#     float mouse_y;      /**< Y coordinate, relative to window */
#     Sint32 integer_x;   /**< The amount scrolled horizontally, accumulated to whole scroll "ticks" (added in 3.2.12) */
#     Sint32 integer_y;   /**< The amount scrolled vertically, accumulated to whole scroll "ticks" (added in 3.2.12) */
# } SDL_MouseWheelEvent;
class SDL_MouseWheelEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("which", ctypes.c_uint32),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("direction", ctypes.c_int),
        ("mouse_x", ctypes.c_float),
        ("mouse_y", ctypes.c_float),
        ("integer_x", ctypes.c_int32),
        ("integer_y", ctypes.c_int32),
    ]


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


# typedef struct SDL_QuitEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_QUIT */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
# } SDL_QuitEvent;
class SDL_QuitEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
    ]


# typedef struct SDL_RenderEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_RENDER_TARGETS_RESET, SDL_EVENT_RENDER_DEVICE_RESET, SDL_EVENT_RENDER_DEVICE_LOST */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window containing the renderer in question. */
# } SDL_RenderEvent;
class SDL_RenderEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
    ]


# typedef struct SDL_SensorEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_SENSOR_UPDATE */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_SensorID which; /**< The instance ID of the sensor */
#     float data[6];      /**< Up to 6 values from the sensor - additional values can be queried using SDL_GetSensorData() */
#     Uint64 sensor_timestamp; /**< The timestamp of the sensor reading in nanoseconds, not necessarily synchronized with the system clock */
# } SDL_SensorEvent;
class SDL_SensorEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("which", ctypes.c_uint32),
        ("data", ctypes.c_float * 6),
        ("sensor_timestamp", ctypes.c_uint64),
    ]


# typedef struct SDL_TextEditingCandidatesEvent
# {
#     SDL_EventType type;         /**< SDL_EVENT_TEXT_EDITING_CANDIDATES */
#     Uint32 reserved;
#     Uint64 timestamp;           /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;      /**< The window with keyboard focus, if any */
#     const char * const *candidates;    /**< The list of candidates, or NULL if there are no candidates available */
#     Sint32 num_candidates;      /**< The number of strings in `candidates` */
#     Sint32 selected_candidate;  /**< The index of the selected candidate, or -1 if no candidate is selected */
#     bool horizontal;          /**< true if the list is horizontal, false if it's vertical */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_TextEditingCandidatesEvent;
class SDL_TextEditingCandidatesEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("candidates", ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p))),
        ("num_candidates", ctypes.c_int32),
        ("selected_candidate", ctypes.c_int32),
        ("horizontal", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_TextEditingEvent
# {
#     SDL_EventType type;         /**< SDL_EVENT_TEXT_EDITING */
#     Uint32 reserved;
#     Uint64 timestamp;           /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID;      /**< The window with keyboard focus, if any */
#     const char *text;           /**< The editing text */
#     Sint32 start;               /**< The start cursor of selected editing text, or -1 if not set */
#     Sint32 length;              /**< The length of selected editing text, or -1 if not set */
# } SDL_TextEditingEvent;
class SDL_TextEditingEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("text", ctypes.c_char_p),
        ("start", ctypes.c_int32),
        ("length", ctypes.c_int32),
    ]


# typedef struct SDL_TextInputEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_TEXT_INPUT */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The window with keyboard focus, if any */
#     const char *text;   /**< The input text, UTF-8 encoded */
# } SDL_TextInputEvent;
class SDL_TextInputEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("text", ctypes.c_char_p),
    ]


# typedef struct SDL_TouchFingerEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_FINGER_DOWN, SDL_EVENT_FINGER_UP, SDL_EVENT_FINGER_MOTION, or SDL_EVENT_FINGER_CANCELED */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_TouchID touchID; /**< The touch device id */
#     SDL_FingerID fingerID;
#     float x;            /**< Normalized in the range 0...1 */
#     float y;            /**< Normalized in the range 0...1 */
#     float dx;           /**< Normalized in the range -1...1 */
#     float dy;           /**< Normalized in the range -1...1 */
#     float pressure;     /**< Normalized in the range 0...1 */
#     SDL_WindowID windowID; /**< The window underneath the finger, if any */
# } SDL_TouchFingerEvent;
class SDL_TouchFingerEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("touchID", ctypes.c_uint64),
        ("fingerID", ctypes.c_uint64),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("dx", ctypes.c_float),
        ("dy", ctypes.c_float),
        ("pressure", ctypes.c_float),
        ("windowID", ctypes.c_uint32),
    ]


# typedef struct SDL_UserEvent
# {
#     Uint32 type;        /**< SDL_EVENT_USER through SDL_EVENT_LAST-1, Uint32 because these are not in the SDL_EventType enumeration */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The associated window if any */
#     Sint32 code;        /**< User defined event code */
#     void *data1;        /**< User defined data pointer */
#     void *data2;        /**< User defined data pointer */
# } SDL_UserEvent;
class SDL_UserEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("code", ctypes.c_int32),
        ("data1", ctypes.c_void_p),
        ("data2", ctypes.c_void_p),
    ]


# typedef struct SDL_WindowEvent
# {
#     SDL_EventType type; /**< SDL_EVENT_WINDOW_* */
#     Uint32 reserved;
#     Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
#     SDL_WindowID windowID; /**< The associated window */
#     Sint32 data1;       /**< event dependent data */
#     Sint32 data2;       /**< event dependent data */
# } SDL_WindowEvent;
class SDL_WindowEvent(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("reserved", ctypes.c_uint32),
        ("timestamp", ctypes.c_uint64),
        ("windowID", ctypes.c_uint32),
        ("data1", ctypes.c_int32),
        ("data2", ctypes.c_int32),
    ]


# typedef union SDL_Event
# {
#     Uint32 type;                            /**< Event type, shared with all events, Uint32 to cover user events which are not in the SDL_EventType enumeration */
#     SDL_CommonEvent common;                 /**< Common event data */
#     SDL_DisplayEvent display;               /**< Display event data */
#     SDL_WindowEvent window;                 /**< Window event data */
#     SDL_KeyboardDeviceEvent kdevice;        /**< Keyboard device change event data */
#     SDL_KeyboardEvent key;                  /**< Keyboard event data */
#     SDL_TextEditingEvent edit;              /**< Text editing event data */
#     SDL_TextEditingCandidatesEvent edit_candidates; /**< Text editing candidates event data */
#     SDL_TextInputEvent text;                /**< Text input event data */
#     SDL_MouseDeviceEvent mdevice;           /**< Mouse device change event data */
#     SDL_MouseMotionEvent motion;            /**< Mouse motion event data */
#     SDL_MouseButtonEvent button;            /**< Mouse button event data */
#     SDL_MouseWheelEvent wheel;              /**< Mouse wheel event data */
#     SDL_JoyDeviceEvent jdevice;             /**< Joystick device change event data */
#     SDL_JoyAxisEvent jaxis;                 /**< Joystick axis event data */
#     SDL_JoyBallEvent jball;                 /**< Joystick ball event data */
#     SDL_JoyHatEvent jhat;                   /**< Joystick hat event data */
#     SDL_JoyButtonEvent jbutton;             /**< Joystick button event data */
#     SDL_JoyBatteryEvent jbattery;           /**< Joystick battery event data */
#     SDL_GamepadDeviceEvent gdevice;         /**< Gamepad device event data */
#     SDL_GamepadAxisEvent gaxis;             /**< Gamepad axis event data */
#     SDL_GamepadButtonEvent gbutton;         /**< Gamepad button event data */
#     SDL_GamepadTouchpadEvent gtouchpad;     /**< Gamepad touchpad event data */
#     SDL_GamepadSensorEvent gsensor;         /**< Gamepad sensor event data */
#     SDL_AudioDeviceEvent adevice;           /**< Audio device event data */
#     SDL_CameraDeviceEvent cdevice;          /**< Camera device event data */
#     SDL_SensorEvent sensor;                 /**< Sensor event data */
#     SDL_QuitEvent quit;                     /**< Quit request event data */
#     SDL_UserEvent user;                     /**< Custom event data */
#     SDL_TouchFingerEvent tfinger;           /**< Touch finger event data */
#     SDL_PenProximityEvent pproximity;       /**< Pen proximity event data */
#     SDL_PenTouchEvent ptouch;               /**< Pen tip touching event data */
#     SDL_PenMotionEvent pmotion;             /**< Pen motion event data */
#     SDL_PenButtonEvent pbutton;             /**< Pen button event data */
#     SDL_PenAxisEvent paxis;                 /**< Pen axis event data */
#     SDL_RenderEvent render;                 /**< Render event data */
#     SDL_DropEvent drop;                     /**< Drag and drop event data */
#     SDL_ClipboardEvent clipboard;           /**< Clipboard event data */
#     /* This is necessary for ABI compatibility between Visual C++ and GCC.
#        Visual C++ will respect the push pack pragma and use 52 bytes (size of
#        SDL_TextEditingEvent, the largest structure for 32-bit and 64-bit
#        architectures) for this union, and GCC will use the alignment of the
#        largest datatype within the union, which is 8 bytes on 64-bit
#        architectures.
#        So... we'll add padding to force the size to be the same for both.
#        On architectures where pointers are 16 bytes, this needs rounding up to
#        the next multiple of 16, 64, and on architectures where pointers are
#        even larger the size of SDL_UserEvent will dominate as being 3 pointers.
#     */
#     Uint8 padding[128];
# } SDL_Event;
class SDL_Event(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("common", SDL_CommonEvent),
        ("display", SDL_DisplayEvent),
        ("window", SDL_WindowEvent),
        ("kdevice", SDL_KeyboardDeviceEvent),
        ("key", SDL_KeyboardEvent),
        ("edit", SDL_TextEditingEvent),
        ("edit_candidates", SDL_TextEditingCandidatesEvent),
        ("text", SDL_TextInputEvent),
        ("mdevice", SDL_MouseDeviceEvent),
        ("motion", SDL_MouseMotionEvent),
        ("button", SDL_MouseButtonEvent),
        ("wheel", SDL_MouseWheelEvent),
        ("jdevice", SDL_JoyDeviceEvent),
        ("jaxis", SDL_JoyAxisEvent),
        ("jball", SDL_JoyBallEvent),
        ("jhat", SDL_JoyHatEvent),
        ("jbutton", SDL_JoyButtonEvent),
        ("jbattery", SDL_JoyBatteryEvent),
        ("gdevice", SDL_GamepadDeviceEvent),
        ("gaxis", SDL_GamepadAxisEvent),
        ("gbutton", SDL_GamepadButtonEvent),
        ("gtouchpad", SDL_GamepadTouchpadEvent),
        ("gsensor", SDL_GamepadSensorEvent),
        ("adevice", SDL_AudioDeviceEvent),
        ("cdevice", SDL_CameraDeviceEvent),
        ("sensor", SDL_SensorEvent),
        ("quit", SDL_QuitEvent),
        ("user", SDL_UserEvent),
        ("tfinger", SDL_TouchFingerEvent),
        ("pproximity", SDL_PenProximityEvent),
        ("ptouch", SDL_PenTouchEvent),
        ("pmotion", SDL_PenMotionEvent),
        ("pbutton", SDL_PenButtonEvent),
        ("paxis", SDL_PenAxisEvent),
        ("render", SDL_RenderEvent),
        ("drop", SDL_DropEvent),
        ("clipboard", SDL_ClipboardEvent),
        ("padding", ctypes.c_uint8 * 128),
    ]


# typedef bool (SDLCALL *SDL_EventFilter)(void *userdata, SDL_Event *event);
SDL_EventFilter = ctypes.CFUNCTYPE(
    ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(SDL_Event)
)


# bool SDL_AddEventWatch(SDL_EventFilter filter, void *userdata);
SDL_AddEventWatch = libsdl3.SDL_AddEventWatch
SDL_AddEventWatch.argtypes = [SDL_EventFilter, ctypes.c_void_p]
SDL_AddEventWatch.restype = ctypes.c_bool


# bool SDL_EventEnabled(Uint32 type);
SDL_EventEnabled = libsdl3.SDL_EventEnabled
SDL_EventEnabled.argtypes = [ctypes.c_uint32]
SDL_EventEnabled.restype = ctypes.c_bool


# void SDL_FilterEvents(SDL_EventFilter filter, void *userdata);
SDL_FilterEvents = libsdl3.SDL_FilterEvents
SDL_FilterEvents.argtypes = [SDL_EventFilter, ctypes.c_void_p]
SDL_FilterEvents.restype = None


# void SDL_FlushEvent(Uint32 type);
SDL_FlushEvent = libsdl3.SDL_FlushEvent
SDL_FlushEvent.argtypes = [ctypes.c_uint32]
SDL_FlushEvent.restype = None


# void SDL_FlushEvents(Uint32 minType, Uint32 maxType);
SDL_FlushEvents = libsdl3.SDL_FlushEvents
SDL_FlushEvents.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
SDL_FlushEvents.restype = None


# int SDL_GetEventDescription(const SDL_Event *event, char *buf, int buflen);
SDL_GetEventDescription = libsdl3.SDL_GetEventDescription
SDL_GetEventDescription.argtypes = [
    ctypes.POINTER(SDL_Event),
    ctypes.c_char_p,
    ctypes.c_int,
]
SDL_GetEventDescription.restype = ctypes.c_int


# bool SDL_GetEventFilter(SDL_EventFilter *filter, void **userdata);
SDL_GetEventFilter = libsdl3.SDL_GetEventFilter
SDL_GetEventFilter.argtypes = [
    ctypes.POINTER(SDL_EventFilter),
    ctypes.POINTER(ctypes.c_void_p),
]
SDL_GetEventFilter.restype = ctypes.c_bool


# SDL_Window * SDL_GetWindowFromEvent(const SDL_Event *event);
SDL_GetWindowFromEvent = libsdl3.SDL_GetWindowFromEvent
SDL_GetWindowFromEvent.argtypes = [ctypes.POINTER(SDL_Event)]
SDL_GetWindowFromEvent.restype = ctypes.c_void_p


# bool SDL_HasEvent(Uint32 type);
SDL_HasEvent = libsdl3.SDL_HasEvent
SDL_HasEvent.argtypes = [ctypes.c_uint32]
SDL_HasEvent.restype = ctypes.c_bool


# bool SDL_HasEvents(Uint32 minType, Uint32 maxType);
SDL_HasEvents = libsdl3.SDL_HasEvents
SDL_HasEvents.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
SDL_HasEvents.restype = ctypes.c_bool


# int SDL_PeepEvents(SDL_Event *events, int numevents, SDL_EventAction action, Uint32 minType, Uint32 maxType);
SDL_PeepEvents = libsdl3.SDL_PeepEvents
SDL_PeepEvents.argtypes = [
    ctypes.POINTER(SDL_Event),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_PeepEvents.restype = ctypes.c_int


# bool SDL_PollEvent(SDL_Event *event);
SDL_PollEvent = libsdl3.SDL_PollEvent
SDL_PollEvent.argtypes = [ctypes.POINTER(SDL_Event)]
SDL_PollEvent.restype = ctypes.c_bool


# void SDL_PumpEvents(void);
SDL_PumpEvents = libsdl3.SDL_PumpEvents
SDL_PumpEvents.argtypes = []
SDL_PumpEvents.restype = None


# bool SDL_PushEvent(SDL_Event *event);
SDL_PushEvent = libsdl3.SDL_PushEvent
SDL_PushEvent.argtypes = [ctypes.POINTER(SDL_Event)]
SDL_PushEvent.restype = ctypes.c_bool


# Uint32 SDL_RegisterEvents(int numevents);
SDL_RegisterEvents = libsdl3.SDL_RegisterEvents
SDL_RegisterEvents.argtypes = [ctypes.c_int]
SDL_RegisterEvents.restype = ctypes.c_uint32


# void SDL_RemoveEventWatch(SDL_EventFilter filter, void *userdata);
SDL_RemoveEventWatch = libsdl3.SDL_RemoveEventWatch
SDL_RemoveEventWatch.argtypes = [SDL_EventFilter, ctypes.c_void_p]
SDL_RemoveEventWatch.restype = None


# void SDL_SetEventEnabled(Uint32 type, bool enabled);
SDL_SetEventEnabled = libsdl3.SDL_SetEventEnabled
SDL_SetEventEnabled.argtypes = [ctypes.c_uint32, ctypes.c_bool]
SDL_SetEventEnabled.restype = None


# void SDL_SetEventFilter(SDL_EventFilter filter, void *userdata);
SDL_SetEventFilter = libsdl3.SDL_SetEventFilter
SDL_SetEventFilter.argtypes = [SDL_EventFilter, ctypes.c_void_p]
SDL_SetEventFilter.restype = None


# bool SDL_WaitEvent(SDL_Event *event);
SDL_WaitEvent = libsdl3.SDL_WaitEvent
SDL_WaitEvent.argtypes = [ctypes.POINTER(SDL_Event)]
SDL_WaitEvent.restype = ctypes.c_bool


# bool SDL_WaitEventTimeout(SDL_Event *event, Sint32 timeoutMS);
SDL_WaitEventTimeout = libsdl3.SDL_WaitEventTimeout
SDL_WaitEventTimeout.argtypes = [ctypes.POINTER(SDL_Event), ctypes.c_int32]
SDL_WaitEventTimeout.restype = ctypes.c_bool
