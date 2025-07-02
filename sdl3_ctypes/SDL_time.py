"""
SDL_time.h
Date and Time
Document: https://wiki.libsdl.org/SDL3/CategoryTime
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_DateFormat
# {
#     SDL_DATE_FORMAT_YYYYMMDD = 0, /**< Year/Month/Day */
#     SDL_DATE_FORMAT_DDMMYYYY = 1, /**< Day/Month/Year */
#     SDL_DATE_FORMAT_MMDDYYYY = 2  /**< Month/Day/Year */
# } SDL_DateFormat;
SDL_DATE_FORMAT_YYYYMMDD = 0
SDL_DATE_FORMAT_DDMMYYYY = 1
SDL_DATE_FORMAT_MMDDYYYY = 2
# typedef enum SDL_TimeFormat
# {
#     SDL_TIME_FORMAT_24HR = 0, /**< 24 hour time */
#     SDL_TIME_FORMAT_12HR = 1  /**< 12 hour time */
# } SDL_TimeFormat;
SDL_TIME_FORMAT_24HR = 0
SDL_TIME_FORMAT_12HR = 1


# typedef struct SDL_DateTime
# {
#     int year;                  /**< Year */
#     int month;                 /**< Month [01-12] */
#     int day;                   /**< Day of the month [01-31] */
#     int hour;                  /**< Hour [0-23] */
#     int minute;                /**< Minute [0-59] */
#     int second;                /**< Seconds [0-60] */
#     int nanosecond;            /**< Nanoseconds [0-999999999] */
#     int day_of_week;           /**< Day of the week [0-6] (0 being Sunday) */
#     int utc_offset;            /**< Seconds east of UTC */
# } SDL_DateTime;
class SDL_DateTime(ctypes.Structure):
    _fields_ = [
        ("year", ctypes.c_int),
        ("month", ctypes.c_int),
        ("day", ctypes.c_int),
        ("hour", ctypes.c_int),
        ("minute", ctypes.c_int),
        ("second", ctypes.c_int),
        ("nanosecond", ctypes.c_int),
        ("day_of_week", ctypes.c_int),
        ("utc_offset", ctypes.c_int),
    ]


# bool SDL_DateTimeToTime(const SDL_DateTime *dt, SDL_Time *ticks);
SDL_DateTimeToTime = libsdl3.SDL_DateTimeToTime
SDL_DateTimeToTime.argtypes = [
    ctypes.POINTER(SDL_DateTime),
    ctypes.POINTER(ctypes.c_int64),
]
SDL_DateTimeToTime.restype = ctypes.c_bool


# bool SDL_GetCurrentTime(SDL_Time *ticks);
SDL_GetCurrentTime = libsdl3.SDL_GetCurrentTime
SDL_GetCurrentTime.argtypes = [ctypes.POINTER(ctypes.c_int64)]
SDL_GetCurrentTime.restype = ctypes.c_bool


# bool SDL_GetDateTimeLocalePreferences(SDL_DateFormat *dateFormat, SDL_TimeFormat *timeFormat);
SDL_GetDateTimeLocalePreferences = libsdl3.SDL_GetDateTimeLocalePreferences
SDL_GetDateTimeLocalePreferences.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetDateTimeLocalePreferences.restype = ctypes.c_bool


# int SDL_GetDayOfWeek(int year, int month, int day);
SDL_GetDayOfWeek = libsdl3.SDL_GetDayOfWeek
SDL_GetDayOfWeek.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
SDL_GetDayOfWeek.restype = ctypes.c_int


# int SDL_GetDayOfYear(int year, int month, int day);
SDL_GetDayOfYear = libsdl3.SDL_GetDayOfYear
SDL_GetDayOfYear.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
SDL_GetDayOfYear.restype = ctypes.c_int


# int SDL_GetDaysInMonth(int year, int month);
SDL_GetDaysInMonth = libsdl3.SDL_GetDaysInMonth
SDL_GetDaysInMonth.argtypes = [ctypes.c_int, ctypes.c_int]
SDL_GetDaysInMonth.restype = ctypes.c_int


# SDL_Time SDL_TimeFromWindows(Uint32 dwLowDateTime, Uint32 dwHighDateTime);
SDL_TimeFromWindows = libsdl3.SDL_TimeFromWindows
SDL_TimeFromWindows.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
SDL_TimeFromWindows.restype = ctypes.c_int64


# bool SDL_TimeToDateTime(SDL_Time ticks, SDL_DateTime *dt, bool localTime);
SDL_TimeToDateTime = libsdl3.SDL_TimeToDateTime
SDL_TimeToDateTime.argtypes = [
    ctypes.c_int64,
    ctypes.POINTER(SDL_DateTime),
    ctypes.c_bool,
]
SDL_TimeToDateTime.restype = ctypes.c_bool


# void SDL_TimeToWindows(SDL_Time ticks, Uint32 *dwLowDateTime, Uint32 *dwHighDateTime);
SDL_TimeToWindows = libsdl3.SDL_TimeToWindows
SDL_TimeToWindows.argtypes = [
    ctypes.c_int64,
    ctypes.POINTER(ctypes.c_uint32),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_TimeToWindows.restype = None
