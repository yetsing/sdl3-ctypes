"""
SDL_gamepad.h
Gamepad Support
Document: https://wiki.libsdl.org/SDL3/CategoryGamepad
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_guid import SDL_GUID

# typedef enum SDL_GamepadAxis
# {
#     SDL_GAMEPAD_AXIS_INVALID = -1,
#     SDL_GAMEPAD_AXIS_LEFTX,
#     SDL_GAMEPAD_AXIS_LEFTY,
#     SDL_GAMEPAD_AXIS_RIGHTX,
#     SDL_GAMEPAD_AXIS_RIGHTY,
#     SDL_GAMEPAD_AXIS_LEFT_TRIGGER,
#     SDL_GAMEPAD_AXIS_RIGHT_TRIGGER,
#     SDL_GAMEPAD_AXIS_COUNT
# } SDL_GamepadAxis;
SDL_GAMEPAD_AXIS_INVALID = -1
SDL_GAMEPAD_AXIS_LEFTX = 0
SDL_GAMEPAD_AXIS_LEFTY = 1
SDL_GAMEPAD_AXIS_RIGHTX = 2
SDL_GAMEPAD_AXIS_RIGHTY = 3
SDL_GAMEPAD_AXIS_LEFT_TRIGGER = 4
SDL_GAMEPAD_AXIS_RIGHT_TRIGGER = 5
SDL_GAMEPAD_AXIS_COUNT = 6
# typedef enum SDL_GamepadBindingType
# {
#     SDL_GAMEPAD_BINDTYPE_NONE = 0,
#     SDL_GAMEPAD_BINDTYPE_BUTTON,
#     SDL_GAMEPAD_BINDTYPE_AXIS,
#     SDL_GAMEPAD_BINDTYPE_HAT
# } SDL_GamepadBindingType;
SDL_GAMEPAD_BINDTYPE_NONE = 0
SDL_GAMEPAD_BINDTYPE_BUTTON = 1
SDL_GAMEPAD_BINDTYPE_AXIS = 2
SDL_GAMEPAD_BINDTYPE_HAT = 3
# typedef enum SDL_GamepadButton
# {
#     SDL_GAMEPAD_BUTTON_INVALID = -1,
#     SDL_GAMEPAD_BUTTON_SOUTH,           /**< Bottom face button (e.g. Xbox A button) */
#     SDL_GAMEPAD_BUTTON_EAST,            /**< Right face button (e.g. Xbox B button) */
#     SDL_GAMEPAD_BUTTON_WEST,            /**< Left face button (e.g. Xbox X button) */
#     SDL_GAMEPAD_BUTTON_NORTH,           /**< Top face button (e.g. Xbox Y button) */
#     SDL_GAMEPAD_BUTTON_BACK,
#     SDL_GAMEPAD_BUTTON_GUIDE,
#     SDL_GAMEPAD_BUTTON_START,
#     SDL_GAMEPAD_BUTTON_LEFT_STICK,
#     SDL_GAMEPAD_BUTTON_RIGHT_STICK,
#     SDL_GAMEPAD_BUTTON_LEFT_SHOULDER,
#     SDL_GAMEPAD_BUTTON_RIGHT_SHOULDER,
#     SDL_GAMEPAD_BUTTON_DPAD_UP,
#     SDL_GAMEPAD_BUTTON_DPAD_DOWN,
#     SDL_GAMEPAD_BUTTON_DPAD_LEFT,
#     SDL_GAMEPAD_BUTTON_DPAD_RIGHT,
#     SDL_GAMEPAD_BUTTON_MISC1,           /**< Additional button (e.g. Xbox Series X share button, PS5 microphone button, Nintendo Switch Pro capture button, Amazon Luna microphone button, Google Stadia capture button) */
#     SDL_GAMEPAD_BUTTON_RIGHT_PADDLE1,   /**< Upper or primary paddle, under your right hand (e.g. Xbox Elite paddle P1) */
#     SDL_GAMEPAD_BUTTON_LEFT_PADDLE1,    /**< Upper or primary paddle, under your left hand (e.g. Xbox Elite paddle P3) */
#     SDL_GAMEPAD_BUTTON_RIGHT_PADDLE2,   /**< Lower or secondary paddle, under your right hand (e.g. Xbox Elite paddle P2) */
#     SDL_GAMEPAD_BUTTON_LEFT_PADDLE2,    /**< Lower or secondary paddle, under your left hand (e.g. Xbox Elite paddle P4) */
#     SDL_GAMEPAD_BUTTON_TOUCHPAD,        /**< PS4/PS5 touchpad button */
#     SDL_GAMEPAD_BUTTON_MISC2,           /**< Additional button */
#     SDL_GAMEPAD_BUTTON_MISC3,           /**< Additional button */
#     SDL_GAMEPAD_BUTTON_MISC4,           /**< Additional button */
#     SDL_GAMEPAD_BUTTON_MISC5,           /**< Additional button */
#     SDL_GAMEPAD_BUTTON_MISC6,           /**< Additional button */
#     SDL_GAMEPAD_BUTTON_COUNT
# } SDL_GamepadButton;
SDL_GAMEPAD_BUTTON_INVALID = -1
SDL_GAMEPAD_BUTTON_SOUTH = 0
SDL_GAMEPAD_BUTTON_EAST = 1
SDL_GAMEPAD_BUTTON_WEST = 2
SDL_GAMEPAD_BUTTON_NORTH = 3
SDL_GAMEPAD_BUTTON_BACK = 4
SDL_GAMEPAD_BUTTON_GUIDE = 5
SDL_GAMEPAD_BUTTON_START = 6
SDL_GAMEPAD_BUTTON_LEFT_STICK = 7
SDL_GAMEPAD_BUTTON_RIGHT_STICK = 8
SDL_GAMEPAD_BUTTON_LEFT_SHOULDER = 9
SDL_GAMEPAD_BUTTON_RIGHT_SHOULDER = 10
SDL_GAMEPAD_BUTTON_DPAD_UP = 11
SDL_GAMEPAD_BUTTON_DPAD_DOWN = 12
SDL_GAMEPAD_BUTTON_DPAD_LEFT = 13
SDL_GAMEPAD_BUTTON_DPAD_RIGHT = 14
SDL_GAMEPAD_BUTTON_MISC1 = 15
SDL_GAMEPAD_BUTTON_RIGHT_PADDLE1 = 16
SDL_GAMEPAD_BUTTON_LEFT_PADDLE1 = 17
SDL_GAMEPAD_BUTTON_RIGHT_PADDLE2 = 18
SDL_GAMEPAD_BUTTON_LEFT_PADDLE2 = 19
SDL_GAMEPAD_BUTTON_TOUCHPAD = 20
SDL_GAMEPAD_BUTTON_MISC2 = 21
SDL_GAMEPAD_BUTTON_MISC3 = 22
SDL_GAMEPAD_BUTTON_MISC4 = 23
SDL_GAMEPAD_BUTTON_MISC5 = 24
SDL_GAMEPAD_BUTTON_MISC6 = 25
SDL_GAMEPAD_BUTTON_COUNT = 26
# typedef enum SDL_GamepadButtonLabel
# {
#     SDL_GAMEPAD_BUTTON_LABEL_UNKNOWN,
#     SDL_GAMEPAD_BUTTON_LABEL_A,
#     SDL_GAMEPAD_BUTTON_LABEL_B,
#     SDL_GAMEPAD_BUTTON_LABEL_X,
#     SDL_GAMEPAD_BUTTON_LABEL_Y,
#     SDL_GAMEPAD_BUTTON_LABEL_CROSS,
#     SDL_GAMEPAD_BUTTON_LABEL_CIRCLE,
#     SDL_GAMEPAD_BUTTON_LABEL_SQUARE,
#     SDL_GAMEPAD_BUTTON_LABEL_TRIANGLE
# } SDL_GamepadButtonLabel;
SDL_GAMEPAD_BUTTON_LABEL_UNKNOWN = 0
SDL_GAMEPAD_BUTTON_LABEL_A = 1
SDL_GAMEPAD_BUTTON_LABEL_B = 2
SDL_GAMEPAD_BUTTON_LABEL_X = 3
SDL_GAMEPAD_BUTTON_LABEL_Y = 4
SDL_GAMEPAD_BUTTON_LABEL_CROSS = 5
SDL_GAMEPAD_BUTTON_LABEL_CIRCLE = 6
SDL_GAMEPAD_BUTTON_LABEL_SQUARE = 7
SDL_GAMEPAD_BUTTON_LABEL_TRIANGLE = 8
# typedef enum SDL_GamepadType
# {
#     SDL_GAMEPAD_TYPE_UNKNOWN = 0,
#     SDL_GAMEPAD_TYPE_STANDARD,
#     SDL_GAMEPAD_TYPE_XBOX360,
#     SDL_GAMEPAD_TYPE_XBOXONE,
#     SDL_GAMEPAD_TYPE_PS3,
#     SDL_GAMEPAD_TYPE_PS4,
#     SDL_GAMEPAD_TYPE_PS5,
#     SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_PRO,
#     SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_LEFT,
#     SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT,
#     SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_PAIR,
#     SDL_GAMEPAD_TYPE_GAMECUBE,
#     SDL_GAMEPAD_TYPE_COUNT
# } SDL_GamepadType;
SDL_GAMEPAD_TYPE_UNKNOWN = 0
SDL_GAMEPAD_TYPE_STANDARD = 1
SDL_GAMEPAD_TYPE_XBOX360 = 2
SDL_GAMEPAD_TYPE_XBOXONE = 3
SDL_GAMEPAD_TYPE_PS3 = 4
SDL_GAMEPAD_TYPE_PS4 = 5
SDL_GAMEPAD_TYPE_PS5 = 6
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_PRO = 7
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_LEFT = 8
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT = 9
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_PAIR = 10
SDL_GAMEPAD_TYPE_GAMECUBE = 11
SDL_GAMEPAD_TYPE_COUNT = 12


# typedef struct SDL_GamepadBinding
# {
#     SDL_GamepadBindingType input_type;
#     union
#     {
#         int button;
#         struct
#         {
#             int axis;
#             int axis_min;
#             int axis_max;
#         } axis;
#         struct
#         {
#             int hat;
#             int hat_mask;
#         } hat;
#     } input;
#     SDL_GamepadBindingType output_type;
#     union
#     {
#         SDL_GamepadButton button;
#         struct
#         {
#             SDL_GamepadAxis axis;
#             int axis_min;
#             int axis_max;
#         } axis;
#     } output;
# } SDL_GamepadBinding;
class SDL_GamepadBinding(ctypes.Union):
    _fields_ = [
        ("input_type", ctypes.c_int),
        ("button", ctypes.c_int),
        ("axis", ctypes.c_int),
        ("axis_min", ctypes.c_int),
        ("axis_max", ctypes.c_int),
    ]


# typedef struct SDL_Gamepad SDL_Gamepad;


# int SDL_AddGamepadMapping(const char *mapping);
SDL_AddGamepadMapping = libsdl3.SDL_AddGamepadMapping
SDL_AddGamepadMapping.argtypes = [ctypes.c_char_p]
SDL_AddGamepadMapping.restype = ctypes.c_int


# int SDL_AddGamepadMappingsFromFile(const char *file);
SDL_AddGamepadMappingsFromFile = libsdl3.SDL_AddGamepadMappingsFromFile
SDL_AddGamepadMappingsFromFile.argtypes = [ctypes.c_char_p]
SDL_AddGamepadMappingsFromFile.restype = ctypes.c_int


# int SDL_AddGamepadMappingsFromIO(SDL_IOStream *src, bool closeio);
SDL_AddGamepadMappingsFromIO = libsdl3.SDL_AddGamepadMappingsFromIO
SDL_AddGamepadMappingsFromIO.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_AddGamepadMappingsFromIO.restype = ctypes.c_int


# void SDL_CloseGamepad(SDL_Gamepad *gamepad);
SDL_CloseGamepad = libsdl3.SDL_CloseGamepad
SDL_CloseGamepad.argtypes = [ctypes.c_void_p]
SDL_CloseGamepad.restype = None


# bool SDL_GamepadConnected(SDL_Gamepad *gamepad);
SDL_GamepadConnected = libsdl3.SDL_GamepadConnected
SDL_GamepadConnected.argtypes = [ctypes.c_void_p]
SDL_GamepadConnected.restype = ctypes.c_bool


# bool SDL_GamepadEventsEnabled(void);
SDL_GamepadEventsEnabled = libsdl3.SDL_GamepadEventsEnabled
SDL_GamepadEventsEnabled.argtypes = []
SDL_GamepadEventsEnabled.restype = ctypes.c_bool


# bool SDL_GamepadHasAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
SDL_GamepadHasAxis = libsdl3.SDL_GamepadHasAxis
SDL_GamepadHasAxis.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GamepadHasAxis.restype = ctypes.c_bool


# bool SDL_GamepadHasButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
SDL_GamepadHasButton = libsdl3.SDL_GamepadHasButton
SDL_GamepadHasButton.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GamepadHasButton.restype = ctypes.c_bool


# bool SDL_GamepadHasSensor(SDL_Gamepad *gamepad, SDL_SensorType type);
SDL_GamepadHasSensor = libsdl3.SDL_GamepadHasSensor
SDL_GamepadHasSensor.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GamepadHasSensor.restype = ctypes.c_bool


# bool SDL_GamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type);
SDL_GamepadSensorEnabled = libsdl3.SDL_GamepadSensorEnabled
SDL_GamepadSensorEnabled.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GamepadSensorEnabled.restype = ctypes.c_bool


# const char * SDL_GetGamepadAppleSFSymbolsNameForAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
SDL_GetGamepadAppleSFSymbolsNameForAxis = (
    libsdl3.SDL_GetGamepadAppleSFSymbolsNameForAxis
)
SDL_GetGamepadAppleSFSymbolsNameForAxis.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadAppleSFSymbolsNameForAxis.restype = ctypes.c_char_p


# const char * SDL_GetGamepadAppleSFSymbolsNameForButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
SDL_GetGamepadAppleSFSymbolsNameForButton = (
    libsdl3.SDL_GetGamepadAppleSFSymbolsNameForButton
)
SDL_GetGamepadAppleSFSymbolsNameForButton.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadAppleSFSymbolsNameForButton.restype = ctypes.c_char_p


# Sint16 SDL_GetGamepadAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
SDL_GetGamepadAxis = libsdl3.SDL_GetGamepadAxis
SDL_GetGamepadAxis.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadAxis.restype = ctypes.c_int16


# SDL_GamepadAxis SDL_GetGamepadAxisFromString(const char *str);
SDL_GetGamepadAxisFromString = libsdl3.SDL_GetGamepadAxisFromString
SDL_GetGamepadAxisFromString.argtypes = [ctypes.c_char_p]
SDL_GetGamepadAxisFromString.restype = ctypes.c_int


# SDL_GamepadBinding ** SDL_GetGamepadBindings(SDL_Gamepad *gamepad, int *count);
SDL_GetGamepadBindings = libsdl3.SDL_GetGamepadBindings
SDL_GetGamepadBindings.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_GetGamepadBindings.restype = ctypes.POINTER(ctypes.POINTER(SDL_GamepadBinding))


# bool SDL_GetGamepadButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
SDL_GetGamepadButton = libsdl3.SDL_GetGamepadButton
SDL_GetGamepadButton.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadButton.restype = ctypes.c_bool


# SDL_GamepadButton SDL_GetGamepadButtonFromString(const char *str);
SDL_GetGamepadButtonFromString = libsdl3.SDL_GetGamepadButtonFromString
SDL_GetGamepadButtonFromString.argtypes = [ctypes.c_char_p]
SDL_GetGamepadButtonFromString.restype = ctypes.c_int


# SDL_GamepadButtonLabel SDL_GetGamepadButtonLabel(SDL_Gamepad *gamepad, SDL_GamepadButton button);
SDL_GetGamepadButtonLabel = libsdl3.SDL_GetGamepadButtonLabel
SDL_GetGamepadButtonLabel.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadButtonLabel.restype = ctypes.c_int


# SDL_GamepadButtonLabel SDL_GetGamepadButtonLabelForType(SDL_GamepadType type, SDL_GamepadButton button);
SDL_GetGamepadButtonLabelForType = libsdl3.SDL_GetGamepadButtonLabelForType
SDL_GetGamepadButtonLabelForType.argtypes = [ctypes.c_int, ctypes.c_int]
SDL_GetGamepadButtonLabelForType.restype = ctypes.c_int


# SDL_JoystickConnectionState SDL_GetGamepadConnectionState(SDL_Gamepad *gamepad);
SDL_GetGamepadConnectionState = libsdl3.SDL_GetGamepadConnectionState
SDL_GetGamepadConnectionState.argtypes = [ctypes.c_void_p]
SDL_GetGamepadConnectionState.restype = ctypes.c_int


# Uint16 SDL_GetGamepadFirmwareVersion(SDL_Gamepad *gamepad);
SDL_GetGamepadFirmwareVersion = libsdl3.SDL_GetGamepadFirmwareVersion
SDL_GetGamepadFirmwareVersion.argtypes = [ctypes.c_void_p]
SDL_GetGamepadFirmwareVersion.restype = ctypes.c_uint16


# SDL_Gamepad * SDL_GetGamepadFromID(SDL_JoystickID instance_id);
SDL_GetGamepadFromID = libsdl3.SDL_GetGamepadFromID
SDL_GetGamepadFromID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadFromID.restype = ctypes.c_void_p


# SDL_Gamepad * SDL_GetGamepadFromPlayerIndex(int player_index);
SDL_GetGamepadFromPlayerIndex = libsdl3.SDL_GetGamepadFromPlayerIndex
SDL_GetGamepadFromPlayerIndex.argtypes = [ctypes.c_int]
SDL_GetGamepadFromPlayerIndex.restype = ctypes.c_void_p


# SDL_GUID SDL_GetGamepadGUIDForID(SDL_JoystickID instance_id);
SDL_GetGamepadGUIDForID = libsdl3.SDL_GetGamepadGUIDForID
SDL_GetGamepadGUIDForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadGUIDForID.restype = SDL_GUID


# SDL_JoystickID SDL_GetGamepadID(SDL_Gamepad *gamepad);
SDL_GetGamepadID = libsdl3.SDL_GetGamepadID
SDL_GetGamepadID.argtypes = [ctypes.c_void_p]
SDL_GetGamepadID.restype = ctypes.c_uint32


# SDL_Joystick * SDL_GetGamepadJoystick(SDL_Gamepad *gamepad);
SDL_GetGamepadJoystick = libsdl3.SDL_GetGamepadJoystick
SDL_GetGamepadJoystick.argtypes = [ctypes.c_void_p]
SDL_GetGamepadJoystick.restype = ctypes.c_void_p


# char * SDL_GetGamepadMapping(SDL_Gamepad *gamepad);
SDL_GetGamepadMapping = libsdl3.SDL_GetGamepadMapping
SDL_GetGamepadMapping.argtypes = [ctypes.c_void_p]
SDL_GetGamepadMapping.restype = ctypes.c_char_p


# char * SDL_GetGamepadMappingForGUID(SDL_GUID guid);
SDL_GetGamepadMappingForGUID = libsdl3.SDL_GetGamepadMappingForGUID
SDL_GetGamepadMappingForGUID.argtypes = [SDL_GUID]
SDL_GetGamepadMappingForGUID.restype = ctypes.c_char_p


# char * SDL_GetGamepadMappingForID(SDL_JoystickID instance_id);
SDL_GetGamepadMappingForID = libsdl3.SDL_GetGamepadMappingForID
SDL_GetGamepadMappingForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadMappingForID.restype = ctypes.c_char_p


# char ** SDL_GetGamepadMappings(int *count);
SDL_GetGamepadMappings = libsdl3.SDL_GetGamepadMappings
SDL_GetGamepadMappings.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetGamepadMappings.restype = ctypes.POINTER(ctypes.c_char_p)


# const char * SDL_GetGamepadName(SDL_Gamepad *gamepad);
SDL_GetGamepadName = libsdl3.SDL_GetGamepadName
SDL_GetGamepadName.argtypes = [ctypes.c_void_p]
SDL_GetGamepadName.restype = ctypes.c_char_p


# const char * SDL_GetGamepadNameForID(SDL_JoystickID instance_id);
SDL_GetGamepadNameForID = libsdl3.SDL_GetGamepadNameForID
SDL_GetGamepadNameForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadNameForID.restype = ctypes.c_char_p


# const char * SDL_GetGamepadPath(SDL_Gamepad *gamepad);
SDL_GetGamepadPath = libsdl3.SDL_GetGamepadPath
SDL_GetGamepadPath.argtypes = [ctypes.c_void_p]
SDL_GetGamepadPath.restype = ctypes.c_char_p


# const char * SDL_GetGamepadPathForID(SDL_JoystickID instance_id);
SDL_GetGamepadPathForID = libsdl3.SDL_GetGamepadPathForID
SDL_GetGamepadPathForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadPathForID.restype = ctypes.c_char_p


# int SDL_GetGamepadPlayerIndex(SDL_Gamepad *gamepad);
SDL_GetGamepadPlayerIndex = libsdl3.SDL_GetGamepadPlayerIndex
SDL_GetGamepadPlayerIndex.argtypes = [ctypes.c_void_p]
SDL_GetGamepadPlayerIndex.restype = ctypes.c_int


# int SDL_GetGamepadPlayerIndexForID(SDL_JoystickID instance_id);
SDL_GetGamepadPlayerIndexForID = libsdl3.SDL_GetGamepadPlayerIndexForID
SDL_GetGamepadPlayerIndexForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadPlayerIndexForID.restype = ctypes.c_int


# SDL_PowerState SDL_GetGamepadPowerInfo(SDL_Gamepad *gamepad, int *percent);
SDL_GetGamepadPowerInfo = libsdl3.SDL_GetGamepadPowerInfo
SDL_GetGamepadPowerInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_GetGamepadPowerInfo.restype = ctypes.c_int


# Uint16 SDL_GetGamepadProduct(SDL_Gamepad *gamepad);
SDL_GetGamepadProduct = libsdl3.SDL_GetGamepadProduct
SDL_GetGamepadProduct.argtypes = [ctypes.c_void_p]
SDL_GetGamepadProduct.restype = ctypes.c_uint16


# Uint16 SDL_GetGamepadProductForID(SDL_JoystickID instance_id);
SDL_GetGamepadProductForID = libsdl3.SDL_GetGamepadProductForID
SDL_GetGamepadProductForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadProductForID.restype = ctypes.c_uint16


# Uint16 SDL_GetGamepadProductVersion(SDL_Gamepad *gamepad);
SDL_GetGamepadProductVersion = libsdl3.SDL_GetGamepadProductVersion
SDL_GetGamepadProductVersion.argtypes = [ctypes.c_void_p]
SDL_GetGamepadProductVersion.restype = ctypes.c_uint16


# Uint16 SDL_GetGamepadProductVersionForID(SDL_JoystickID instance_id);
SDL_GetGamepadProductVersionForID = libsdl3.SDL_GetGamepadProductVersionForID
SDL_GetGamepadProductVersionForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadProductVersionForID.restype = ctypes.c_uint16


# SDL_PropertiesID SDL_GetGamepadProperties(SDL_Gamepad *gamepad);
SDL_GetGamepadProperties = libsdl3.SDL_GetGamepadProperties
SDL_GetGamepadProperties.argtypes = [ctypes.c_void_p]
SDL_GetGamepadProperties.restype = ctypes.c_uint32


# SDL_JoystickID * SDL_GetGamepads(int *count);
SDL_GetGamepads = libsdl3.SDL_GetGamepads
SDL_GetGamepads.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetGamepads.restype = ctypes.POINTER(ctypes.c_uint32)


# bool SDL_GetGamepadSensorData(SDL_Gamepad *gamepad, SDL_SensorType type, float *data, int num_values);
SDL_GetGamepadSensorData = libsdl3.SDL_GetGamepadSensorData
SDL_GetGamepadSensorData.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
]
SDL_GetGamepadSensorData.restype = ctypes.c_bool


# float SDL_GetGamepadSensorDataRate(SDL_Gamepad *gamepad, SDL_SensorType type);
SDL_GetGamepadSensorDataRate = libsdl3.SDL_GetGamepadSensorDataRate
SDL_GetGamepadSensorDataRate.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetGamepadSensorDataRate.restype = ctypes.c_float


# const char * SDL_GetGamepadSerial(SDL_Gamepad *gamepad);
SDL_GetGamepadSerial = libsdl3.SDL_GetGamepadSerial
SDL_GetGamepadSerial.argtypes = [ctypes.c_void_p]
SDL_GetGamepadSerial.restype = ctypes.c_char_p


# Uint64 SDL_GetGamepadSteamHandle(SDL_Gamepad *gamepad);
SDL_GetGamepadSteamHandle = libsdl3.SDL_GetGamepadSteamHandle
SDL_GetGamepadSteamHandle.argtypes = [ctypes.c_void_p]
SDL_GetGamepadSteamHandle.restype = ctypes.c_uint64


# const char * SDL_GetGamepadStringForAxis(SDL_GamepadAxis axis);
SDL_GetGamepadStringForAxis = libsdl3.SDL_GetGamepadStringForAxis
SDL_GetGamepadStringForAxis.argtypes = [ctypes.c_int]
SDL_GetGamepadStringForAxis.restype = ctypes.c_char_p


# const char * SDL_GetGamepadStringForButton(SDL_GamepadButton button);
SDL_GetGamepadStringForButton = libsdl3.SDL_GetGamepadStringForButton
SDL_GetGamepadStringForButton.argtypes = [ctypes.c_int]
SDL_GetGamepadStringForButton.restype = ctypes.c_char_p


# const char * SDL_GetGamepadStringForType(SDL_GamepadType type);
SDL_GetGamepadStringForType = libsdl3.SDL_GetGamepadStringForType
SDL_GetGamepadStringForType.argtypes = [ctypes.c_int]
SDL_GetGamepadStringForType.restype = ctypes.c_char_p


# bool SDL_GetGamepadTouchpadFinger(SDL_Gamepad *gamepad, int touchpad, int finger, bool *down, float *x, float *y, float *pressure);
SDL_GetGamepadTouchpadFinger = libsdl3.SDL_GetGamepadTouchpadFinger
SDL_GetGamepadTouchpadFinger.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_bool),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetGamepadTouchpadFinger.restype = ctypes.c_bool


# SDL_GamepadType SDL_GetGamepadType(SDL_Gamepad *gamepad);
SDL_GetGamepadType = libsdl3.SDL_GetGamepadType
SDL_GetGamepadType.argtypes = [ctypes.c_void_p]
SDL_GetGamepadType.restype = ctypes.c_int


# SDL_GamepadType SDL_GetGamepadTypeForID(SDL_JoystickID instance_id);
SDL_GetGamepadTypeForID = libsdl3.SDL_GetGamepadTypeForID
SDL_GetGamepadTypeForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadTypeForID.restype = ctypes.c_int


# SDL_GamepadType SDL_GetGamepadTypeFromString(const char *str);
SDL_GetGamepadTypeFromString = libsdl3.SDL_GetGamepadTypeFromString
SDL_GetGamepadTypeFromString.argtypes = [ctypes.c_char_p]
SDL_GetGamepadTypeFromString.restype = ctypes.c_int


# Uint16 SDL_GetGamepadVendor(SDL_Gamepad *gamepad);
SDL_GetGamepadVendor = libsdl3.SDL_GetGamepadVendor
SDL_GetGamepadVendor.argtypes = [ctypes.c_void_p]
SDL_GetGamepadVendor.restype = ctypes.c_uint16


# Uint16 SDL_GetGamepadVendorForID(SDL_JoystickID instance_id);
SDL_GetGamepadVendorForID = libsdl3.SDL_GetGamepadVendorForID
SDL_GetGamepadVendorForID.argtypes = [ctypes.c_uint32]
SDL_GetGamepadVendorForID.restype = ctypes.c_uint16


# int SDL_GetNumGamepadTouchpadFingers(SDL_Gamepad *gamepad, int touchpad);
SDL_GetNumGamepadTouchpadFingers = libsdl3.SDL_GetNumGamepadTouchpadFingers
SDL_GetNumGamepadTouchpadFingers.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_GetNumGamepadTouchpadFingers.restype = ctypes.c_int


# int SDL_GetNumGamepadTouchpads(SDL_Gamepad *gamepad);
SDL_GetNumGamepadTouchpads = libsdl3.SDL_GetNumGamepadTouchpads
SDL_GetNumGamepadTouchpads.argtypes = [ctypes.c_void_p]
SDL_GetNumGamepadTouchpads.restype = ctypes.c_int


# SDL_GamepadType SDL_GetRealGamepadType(SDL_Gamepad *gamepad);
SDL_GetRealGamepadType = libsdl3.SDL_GetRealGamepadType
SDL_GetRealGamepadType.argtypes = [ctypes.c_void_p]
SDL_GetRealGamepadType.restype = ctypes.c_int


# SDL_GamepadType SDL_GetRealGamepadTypeForID(SDL_JoystickID instance_id);
SDL_GetRealGamepadTypeForID = libsdl3.SDL_GetRealGamepadTypeForID
SDL_GetRealGamepadTypeForID.argtypes = [ctypes.c_uint32]
SDL_GetRealGamepadTypeForID.restype = ctypes.c_int


# bool SDL_HasGamepad(void);
SDL_HasGamepad = libsdl3.SDL_HasGamepad
SDL_HasGamepad.argtypes = []
SDL_HasGamepad.restype = ctypes.c_bool


# bool SDL_IsGamepad(SDL_JoystickID instance_id);
SDL_IsGamepad = libsdl3.SDL_IsGamepad
SDL_IsGamepad.argtypes = [ctypes.c_uint32]
SDL_IsGamepad.restype = ctypes.c_bool


# SDL_Gamepad * SDL_OpenGamepad(SDL_JoystickID instance_id);
SDL_OpenGamepad = libsdl3.SDL_OpenGamepad
SDL_OpenGamepad.argtypes = [ctypes.c_uint32]
SDL_OpenGamepad.restype = ctypes.c_void_p


# bool SDL_ReloadGamepadMappings(void);
SDL_ReloadGamepadMappings = libsdl3.SDL_ReloadGamepadMappings
SDL_ReloadGamepadMappings.argtypes = []
SDL_ReloadGamepadMappings.restype = ctypes.c_bool


# bool SDL_RumbleGamepad(SDL_Gamepad *gamepad, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble, Uint32 duration_ms);
SDL_RumbleGamepad = libsdl3.SDL_RumbleGamepad
SDL_RumbleGamepad.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint16,
    ctypes.c_uint16,
    ctypes.c_uint32,
]
SDL_RumbleGamepad.restype = ctypes.c_bool


# bool SDL_RumbleGamepadTriggers(SDL_Gamepad *gamepad, Uint16 left_rumble, Uint16 right_rumble, Uint32 duration_ms);
SDL_RumbleGamepadTriggers = libsdl3.SDL_RumbleGamepadTriggers
SDL_RumbleGamepadTriggers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint16,
    ctypes.c_uint16,
    ctypes.c_uint32,
]
SDL_RumbleGamepadTriggers.restype = ctypes.c_bool


# bool SDL_SendGamepadEffect(SDL_Gamepad *gamepad, const void *data, int size);
SDL_SendGamepadEffect = libsdl3.SDL_SendGamepadEffect
SDL_SendGamepadEffect.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
SDL_SendGamepadEffect.restype = ctypes.c_bool


# void SDL_SetGamepadEventsEnabled(bool enabled);
SDL_SetGamepadEventsEnabled = libsdl3.SDL_SetGamepadEventsEnabled
SDL_SetGamepadEventsEnabled.argtypes = [ctypes.c_bool]
SDL_SetGamepadEventsEnabled.restype = None


# bool SDL_SetGamepadLED(SDL_Gamepad *gamepad, Uint8 red, Uint8 green, Uint8 blue);
SDL_SetGamepadLED = libsdl3.SDL_SetGamepadLED
SDL_SetGamepadLED.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_SetGamepadLED.restype = ctypes.c_bool


# bool SDL_SetGamepadMapping(SDL_JoystickID instance_id, const char *mapping);
SDL_SetGamepadMapping = libsdl3.SDL_SetGamepadMapping
SDL_SetGamepadMapping.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_SetGamepadMapping.restype = ctypes.c_bool


# bool SDL_SetGamepadPlayerIndex(SDL_Gamepad *gamepad, int player_index);
SDL_SetGamepadPlayerIndex = libsdl3.SDL_SetGamepadPlayerIndex
SDL_SetGamepadPlayerIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_SetGamepadPlayerIndex.restype = ctypes.c_bool


# bool SDL_SetGamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type, bool enabled);
SDL_SetGamepadSensorEnabled = libsdl3.SDL_SetGamepadSensorEnabled
SDL_SetGamepadSensorEnabled.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_bool]
SDL_SetGamepadSensorEnabled.restype = ctypes.c_bool


# void SDL_UpdateGamepads(void);
SDL_UpdateGamepads = libsdl3.SDL_UpdateGamepads
SDL_UpdateGamepads.argtypes = []
SDL_UpdateGamepads.restype = None
