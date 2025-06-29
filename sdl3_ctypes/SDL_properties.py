"""
SDL_properties.h
Object Properties
Document: https://wiki.libsdl.org/SDL3/CategoryProperties
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_PropertyType
# {
#     SDL_PROPERTY_TYPE_INVALID,
#     SDL_PROPERTY_TYPE_POINTER,
#     SDL_PROPERTY_TYPE_STRING,
#     SDL_PROPERTY_TYPE_NUMBER,
#     SDL_PROPERTY_TYPE_FLOAT,
#     SDL_PROPERTY_TYPE_BOOLEAN
# } SDL_PropertyType;
SDL_PROPERTY_TYPE_INVALID = 0
SDL_PROPERTY_TYPE_POINTER = 1
SDL_PROPERTY_TYPE_STRING = 2
SDL_PROPERTY_TYPE_NUMBER = 3
SDL_PROPERTY_TYPE_FLOAT = 4
SDL_PROPERTY_TYPE_BOOLEAN = 5


# typedef void (SDLCALL *SDL_CleanupPropertyCallback)(void *userdata, void *value);
SDL_CleanupPropertyCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)


# typedef void (SDLCALL *SDL_EnumeratePropertiesCallback)(void *userdata, SDL_PropertiesID props, const char *name);
SDL_EnumeratePropertiesCallback = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p
)

# typedef Uint32 SDL_PropertiesID;


# bool SDL_ClearProperty(SDL_PropertiesID props, const char *name);
SDL_ClearProperty = libsdl3.SDL_ClearProperty
SDL_ClearProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_ClearProperty.restype = ctypes.c_bool


# bool SDL_CopyProperties(SDL_PropertiesID src, SDL_PropertiesID dst);
SDL_CopyProperties = libsdl3.SDL_CopyProperties
SDL_CopyProperties.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
SDL_CopyProperties.restype = ctypes.c_bool


# SDL_PropertiesID SDL_CreateProperties(void);
SDL_CreateProperties = libsdl3.SDL_CreateProperties
SDL_CreateProperties.argtypes = []
SDL_CreateProperties.restype = ctypes.c_uint32


# void SDL_DestroyProperties(SDL_PropertiesID props);
SDL_DestroyProperties = libsdl3.SDL_DestroyProperties
SDL_DestroyProperties.argtypes = [ctypes.c_uint32]
SDL_DestroyProperties.restype = None


# bool SDL_EnumerateProperties(SDL_PropertiesID props, SDL_EnumeratePropertiesCallback callback, void *userdata);
SDL_EnumerateProperties = libsdl3.SDL_EnumerateProperties
SDL_EnumerateProperties.argtypes = [
    ctypes.c_uint32,
    SDL_EnumeratePropertiesCallback,
    ctypes.c_void_p,
]
SDL_EnumerateProperties.restype = ctypes.c_bool


# bool SDL_GetBooleanProperty(SDL_PropertiesID props, const char *name, bool default_value);
SDL_GetBooleanProperty = libsdl3.SDL_GetBooleanProperty
SDL_GetBooleanProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_bool]
SDL_GetBooleanProperty.restype = ctypes.c_bool


# float SDL_GetFloatProperty(SDL_PropertiesID props, const char *name, float default_value);
SDL_GetFloatProperty = libsdl3.SDL_GetFloatProperty
SDL_GetFloatProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_float]
SDL_GetFloatProperty.restype = ctypes.c_float


# SDL_PropertiesID SDL_GetGlobalProperties(void);
SDL_GetGlobalProperties = libsdl3.SDL_GetGlobalProperties
SDL_GetGlobalProperties.argtypes = []
SDL_GetGlobalProperties.restype = ctypes.c_uint32


# Sint64 SDL_GetNumberProperty(SDL_PropertiesID props, const char *name, Sint64 default_value);
SDL_GetNumberProperty = libsdl3.SDL_GetNumberProperty
SDL_GetNumberProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_int64]
SDL_GetNumberProperty.restype = ctypes.c_int64


# void * SDL_GetPointerProperty(SDL_PropertiesID props, const char *name, void *default_value);
SDL_GetPointerProperty = libsdl3.SDL_GetPointerProperty
SDL_GetPointerProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_void_p]
SDL_GetPointerProperty.restype = ctypes.c_void_p


# SDL_PropertyType SDL_GetPropertyType(SDL_PropertiesID props, const char *name);
SDL_GetPropertyType = libsdl3.SDL_GetPropertyType
SDL_GetPropertyType.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_GetPropertyType.restype = ctypes.c_int


# const char * SDL_GetStringProperty(SDL_PropertiesID props, const char *name, const char *default_value);
SDL_GetStringProperty = libsdl3.SDL_GetStringProperty
SDL_GetStringProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p]
SDL_GetStringProperty.restype = ctypes.c_char_p


# bool SDL_HasProperty(SDL_PropertiesID props, const char *name);
SDL_HasProperty = libsdl3.SDL_HasProperty
SDL_HasProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_HasProperty.restype = ctypes.c_bool


# bool SDL_LockProperties(SDL_PropertiesID props);
SDL_LockProperties = libsdl3.SDL_LockProperties
SDL_LockProperties.argtypes = [ctypes.c_uint32]
SDL_LockProperties.restype = ctypes.c_bool


# bool SDL_SetBooleanProperty(SDL_PropertiesID props, const char *name, bool value);
SDL_SetBooleanProperty = libsdl3.SDL_SetBooleanProperty
SDL_SetBooleanProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_bool]
SDL_SetBooleanProperty.restype = ctypes.c_bool


# bool SDL_SetFloatProperty(SDL_PropertiesID props, const char *name, float value);
SDL_SetFloatProperty = libsdl3.SDL_SetFloatProperty
SDL_SetFloatProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_float]
SDL_SetFloatProperty.restype = ctypes.c_bool


# bool SDL_SetNumberProperty(SDL_PropertiesID props, const char *name, Sint64 value);
SDL_SetNumberProperty = libsdl3.SDL_SetNumberProperty
SDL_SetNumberProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_int64]
SDL_SetNumberProperty.restype = ctypes.c_bool


# bool SDL_SetPointerProperty(SDL_PropertiesID props, const char *name, void *value);
SDL_SetPointerProperty = libsdl3.SDL_SetPointerProperty
SDL_SetPointerProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_void_p]
SDL_SetPointerProperty.restype = ctypes.c_bool


# bool SDL_SetPointerPropertyWithCleanup(SDL_PropertiesID props, const char *name, void *value, SDL_CleanupPropertyCallback cleanup, void *userdata);
SDL_SetPointerPropertyWithCleanup = libsdl3.SDL_SetPointerPropertyWithCleanup
SDL_SetPointerPropertyWithCleanup.argtypes = [
    ctypes.c_uint32,
    ctypes.c_char_p,
    ctypes.c_void_p,
    SDL_CleanupPropertyCallback,
    ctypes.c_void_p,
]
SDL_SetPointerPropertyWithCleanup.restype = ctypes.c_bool


# bool SDL_SetStringProperty(SDL_PropertiesID props, const char *name, const char *value);
SDL_SetStringProperty = libsdl3.SDL_SetStringProperty
SDL_SetStringProperty.argtypes = [ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p]
SDL_SetStringProperty.restype = ctypes.c_bool


# void SDL_UnlockProperties(SDL_PropertiesID props);
SDL_UnlockProperties = libsdl3.SDL_UnlockProperties
SDL_UnlockProperties.argtypes = [ctypes.c_uint32]
SDL_UnlockProperties.restype = None
