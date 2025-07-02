"""
SDL_sensor.h
Sensors
Document: https://wiki.libsdl.org/SDL3/CategorySensor
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_STANDARD_GRAVITY    9.80665f
SDL_STANDARD_GRAVITY = 9.80665


# typedef enum SDL_SensorType
# {
#     SDL_SENSOR_INVALID = -1,    /**< Returned for an invalid sensor */
#     SDL_SENSOR_UNKNOWN,         /**< Unknown sensor type */
#     SDL_SENSOR_ACCEL,           /**< Accelerometer */
#     SDL_SENSOR_GYRO,            /**< Gyroscope */
#     SDL_SENSOR_ACCEL_L,         /**< Accelerometer for left Joy-Con controller and Wii nunchuk */
#     SDL_SENSOR_GYRO_L,          /**< Gyroscope for left Joy-Con controller */
#     SDL_SENSOR_ACCEL_R,         /**< Accelerometer for right Joy-Con controller */
#     SDL_SENSOR_GYRO_R           /**< Gyroscope for right Joy-Con controller */
# } SDL_SensorType;
SDL_SENSOR_INVALID = -1
SDL_SENSOR_UNKNOWN = 0
SDL_SENSOR_ACCEL = 1
SDL_SENSOR_GYRO = 2
SDL_SENSOR_ACCEL_L = 3
SDL_SENSOR_GYRO_L = 4
SDL_SENSOR_ACCEL_R = 5
SDL_SENSOR_GYRO_R = 6


# typedef struct SDL_Sensor SDL_Sensor;
# typedef Uint32 SDL_SensorID;


# void SDL_CloseSensor(SDL_Sensor *sensor);
SDL_CloseSensor = libsdl3.SDL_CloseSensor
SDL_CloseSensor.argtypes = [ctypes.c_void_p]
SDL_CloseSensor.restype = None


# bool SDL_GetSensorData(SDL_Sensor *sensor, float *data, int num_values);
SDL_GetSensorData = libsdl3.SDL_GetSensorData
SDL_GetSensorData.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
]
SDL_GetSensorData.restype = ctypes.c_bool


# SDL_Sensor * SDL_GetSensorFromID(SDL_SensorID instance_id);
SDL_GetSensorFromID = libsdl3.SDL_GetSensorFromID
SDL_GetSensorFromID.argtypes = [ctypes.c_uint32]
SDL_GetSensorFromID.restype = ctypes.c_void_p


# SDL_SensorID SDL_GetSensorID(SDL_Sensor *sensor);
SDL_GetSensorID = libsdl3.SDL_GetSensorID
SDL_GetSensorID.argtypes = [ctypes.c_void_p]
SDL_GetSensorID.restype = ctypes.c_uint32


# const char * SDL_GetSensorName(SDL_Sensor *sensor);
SDL_GetSensorName = libsdl3.SDL_GetSensorName
SDL_GetSensorName.argtypes = [ctypes.c_void_p]
SDL_GetSensorName.restype = ctypes.c_char_p


# const char * SDL_GetSensorNameForID(SDL_SensorID instance_id);
SDL_GetSensorNameForID = libsdl3.SDL_GetSensorNameForID
SDL_GetSensorNameForID.argtypes = [ctypes.c_uint32]
SDL_GetSensorNameForID.restype = ctypes.c_char_p


# int SDL_GetSensorNonPortableType(SDL_Sensor *sensor);
SDL_GetSensorNonPortableType = libsdl3.SDL_GetSensorNonPortableType
SDL_GetSensorNonPortableType.argtypes = [ctypes.c_void_p]
SDL_GetSensorNonPortableType.restype = ctypes.c_int


# int SDL_GetSensorNonPortableTypeForID(SDL_SensorID instance_id);
SDL_GetSensorNonPortableTypeForID = libsdl3.SDL_GetSensorNonPortableTypeForID
SDL_GetSensorNonPortableTypeForID.argtypes = [ctypes.c_uint32]
SDL_GetSensorNonPortableTypeForID.restype = ctypes.c_int


# SDL_PropertiesID SDL_GetSensorProperties(SDL_Sensor *sensor);
SDL_GetSensorProperties = libsdl3.SDL_GetSensorProperties
SDL_GetSensorProperties.argtypes = [ctypes.c_void_p]
SDL_GetSensorProperties.restype = ctypes.c_uint32


# SDL_SensorID * SDL_GetSensors(int *count);
SDL_GetSensors = libsdl3.SDL_GetSensors
SDL_GetSensors.argtypes = [ctypes.POINTER(ctypes.c_int)]
SDL_GetSensors.restype = ctypes.POINTER(ctypes.c_uint32)


# SDL_SensorType SDL_GetSensorType(SDL_Sensor *sensor);
SDL_GetSensorType = libsdl3.SDL_GetSensorType
SDL_GetSensorType.argtypes = [ctypes.c_void_p]
SDL_GetSensorType.restype = ctypes.c_int


# SDL_SensorType SDL_GetSensorTypeForID(SDL_SensorID instance_id);
SDL_GetSensorTypeForID = libsdl3.SDL_GetSensorTypeForID
SDL_GetSensorTypeForID.argtypes = [ctypes.c_uint32]
SDL_GetSensorTypeForID.restype = ctypes.c_int


# SDL_Sensor * SDL_OpenSensor(SDL_SensorID instance_id);
SDL_OpenSensor = libsdl3.SDL_OpenSensor
SDL_OpenSensor.argtypes = [ctypes.c_uint32]
SDL_OpenSensor.restype = ctypes.c_void_p


# void SDL_UpdateSensors(void);
SDL_UpdateSensors = libsdl3.SDL_UpdateSensors
SDL_UpdateSensors.argtypes = []
SDL_UpdateSensors.restype = None
