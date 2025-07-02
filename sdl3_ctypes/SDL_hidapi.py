"""
SDL_hidapi.h
HIDAPI
Document: https://wiki.libsdl.org/SDL3/CategoryHIDAPI
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# typedef enum SDL_hid_bus_type {
#     /** Unknown bus type */
#     SDL_HID_API_BUS_UNKNOWN = 0x00,
#     /** USB bus
#        Specifications:
#        https://usb.org/hid */
#     SDL_HID_API_BUS_USB = 0x01,
#     /** Bluetooth or Bluetooth LE bus
#        Specifications:
#        https://www.bluetooth.com/specifications/specs/human-interface-device-profile-1-1-1/
#        https://www.bluetooth.com/specifications/specs/hid-service-1-0/
#        https://www.bluetooth.com/specifications/specs/hid-over-gatt-profile-1-0/ */
#     SDL_HID_API_BUS_BLUETOOTH = 0x02,
#     /** I2C bus
#        Specifications:
#        https://docs.microsoft.com/previous-versions/windows/hardware/design/dn642101(v=vs.85) */
#     SDL_HID_API_BUS_I2C = 0x03,
#     /** SPI bus
#        Specifications:
#        https://www.microsoft.com/download/details.aspx?id=103325 */
#     SDL_HID_API_BUS_SPI = 0x04
# } SDL_hid_bus_type;
SDL_HID_API_BUS_UNKNOWN = 0
SDL_HID_API_BUS_USB = 1
SDL_HID_API_BUS_BLUETOOTH = 2
SDL_HID_API_BUS_I2C = 3
SDL_HID_API_BUS_SPI = 4


# typedef struct SDL_hid_device_info
# {
#     /** Platform-specific device path */
#     char *path;
#     /** Device Vendor ID */
#     unsigned short vendor_id;
#     /** Device Product ID */
#     unsigned short product_id;
#     /** Serial Number */
#     wchar_t *serial_number;
#     /** Device Release Number in binary-coded decimal,
#         also known as Device Version Number */
#     unsigned short release_number;
#     /** Manufacturer String */
#     wchar_t *manufacturer_string;
#     /** Product string */
#     wchar_t *product_string;
#     /** Usage Page for this Device/Interface
#         (Windows/Mac/hidraw only) */
#     unsigned short usage_page;
#     /** Usage for this Device/Interface
#         (Windows/Mac/hidraw only) */
#     unsigned short usage;
#     /** The USB interface which this logical device
#         represents.
#         Valid only if the device is a USB HID device.
#         Set to -1 in all other cases.
#     */
#     int interface_number;
#     /** Additional information about the USB interface.
#         Valid on libusb and Android implementations. */
#     int interface_class;
#     int interface_subclass;
#     int interface_protocol;
#     /** Underlying bus type */
#     SDL_hid_bus_type bus_type;
#     /** Pointer to the next device */
#     struct SDL_hid_device_info *next;
# } SDL_hid_device_info;
class SDL_hid_device_info(ctypes.Structure):
    _fields_ = [
        ("path", ctypes.c_char_p),
        ("vendor_id", ctypes.c_short),
        ("product_id", ctypes.c_short),
        ("serial_number", ctypes.c_void_p),
        ("release_number", ctypes.c_short),
        ("manufacturer_string", ctypes.c_void_p),
        ("product_string", ctypes.c_void_p),
        ("usage_page", ctypes.c_short),
        ("usage", ctypes.c_short),
        ("interface_number", ctypes.c_int),
        ("interface_class", ctypes.c_int),
        ("interface_subclass", ctypes.c_int),
        ("interface_protocol", ctypes.c_int),
        ("bus_type", ctypes.c_int),
        ("next", ctypes.c_void_p),
    ]


# typedef struct SDL_hid_device SDL_hid_device;


# void SDL_hid_ble_scan(bool active);
SDL_hid_ble_scan = libsdl3.SDL_hid_ble_scan
SDL_hid_ble_scan.argtypes = [ctypes.c_bool]
SDL_hid_ble_scan.restype = None


# int SDL_hid_close(SDL_hid_device *dev);
SDL_hid_close = libsdl3.SDL_hid_close
SDL_hid_close.argtypes = [ctypes.c_void_p]
SDL_hid_close.restype = ctypes.c_int


# Uint32 SDL_hid_device_change_count(void);
SDL_hid_device_change_count = libsdl3.SDL_hid_device_change_count
SDL_hid_device_change_count.argtypes = []
SDL_hid_device_change_count.restype = ctypes.c_uint32


# SDL_hid_device_info * SDL_hid_enumerate(unsigned short vendor_id, unsigned short product_id);
SDL_hid_enumerate = libsdl3.SDL_hid_enumerate
SDL_hid_enumerate.argtypes = [ctypes.c_short, ctypes.c_short]
SDL_hid_enumerate.restype = ctypes.POINTER(SDL_hid_device_info)


# int SDL_hid_exit(void);
SDL_hid_exit = libsdl3.SDL_hid_exit
SDL_hid_exit.argtypes = []
SDL_hid_exit.restype = ctypes.c_int


# void SDL_hid_free_enumeration(SDL_hid_device_info *devs);
SDL_hid_free_enumeration = libsdl3.SDL_hid_free_enumeration
SDL_hid_free_enumeration.argtypes = [ctypes.POINTER(SDL_hid_device_info)]
SDL_hid_free_enumeration.restype = None


# SDL_hid_device_info * SDL_hid_get_device_info(SDL_hid_device *dev);
SDL_hid_get_device_info = libsdl3.SDL_hid_get_device_info
SDL_hid_get_device_info.argtypes = [ctypes.c_void_p]
SDL_hid_get_device_info.restype = ctypes.POINTER(SDL_hid_device_info)


# int SDL_hid_get_feature_report(SDL_hid_device *dev, unsigned char *data, size_t length);
SDL_hid_get_feature_report = libsdl3.SDL_hid_get_feature_report
SDL_hid_get_feature_report.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
]
SDL_hid_get_feature_report.restype = ctypes.c_int


# int SDL_hid_get_indexed_string(SDL_hid_device *dev, int string_index, wchar_t *string, size_t maxlen);
SDL_hid_get_indexed_string = libsdl3.SDL_hid_get_indexed_string
SDL_hid_get_indexed_string.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_size_t,
]
SDL_hid_get_indexed_string.restype = ctypes.c_int


# int SDL_hid_get_input_report(SDL_hid_device *dev, unsigned char *data, size_t length);
SDL_hid_get_input_report = libsdl3.SDL_hid_get_input_report
SDL_hid_get_input_report.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_hid_get_input_report.restype = ctypes.c_int


# int SDL_hid_get_manufacturer_string(SDL_hid_device *dev, wchar_t *string, size_t maxlen);
SDL_hid_get_manufacturer_string = libsdl3.SDL_hid_get_manufacturer_string
SDL_hid_get_manufacturer_string.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
]
SDL_hid_get_manufacturer_string.restype = ctypes.c_int


# int SDL_hid_get_product_string(SDL_hid_device *dev, wchar_t *string, size_t maxlen);
SDL_hid_get_product_string = libsdl3.SDL_hid_get_product_string
SDL_hid_get_product_string.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
]
SDL_hid_get_product_string.restype = ctypes.c_int


# int SDL_hid_get_report_descriptor(SDL_hid_device *dev, unsigned char *buf, size_t buf_size);
SDL_hid_get_report_descriptor = libsdl3.SDL_hid_get_report_descriptor
SDL_hid_get_report_descriptor.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
]
SDL_hid_get_report_descriptor.restype = ctypes.c_int


# int SDL_hid_get_serial_number_string(SDL_hid_device *dev, wchar_t *string, size_t maxlen);
SDL_hid_get_serial_number_string = libsdl3.SDL_hid_get_serial_number_string
SDL_hid_get_serial_number_string.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
]
SDL_hid_get_serial_number_string.restype = ctypes.c_int


# int SDL_hid_init(void);
SDL_hid_init = libsdl3.SDL_hid_init
SDL_hid_init.argtypes = []
SDL_hid_init.restype = ctypes.c_int


# SDL_hid_device * SDL_hid_open(unsigned short vendor_id, unsigned short product_id, const wchar_t *serial_number);
SDL_hid_open = libsdl3.SDL_hid_open
SDL_hid_open.argtypes = [ctypes.c_short, ctypes.c_short, ctypes.c_void_p]
SDL_hid_open.restype = ctypes.c_void_p


# SDL_hid_device * SDL_hid_open_path(const char *path);
SDL_hid_open_path = libsdl3.SDL_hid_open_path
SDL_hid_open_path.argtypes = [ctypes.c_char_p]
SDL_hid_open_path.restype = ctypes.c_void_p


# int SDL_hid_read(SDL_hid_device *dev, unsigned char *data, size_t length);
SDL_hid_read = libsdl3.SDL_hid_read
SDL_hid_read.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_hid_read.restype = ctypes.c_int


# int SDL_hid_read_timeout(SDL_hid_device *dev, unsigned char *data, size_t length, int milliseconds);
SDL_hid_read_timeout = libsdl3.SDL_hid_read_timeout
SDL_hid_read_timeout.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
    ctypes.c_int,
]
SDL_hid_read_timeout.restype = ctypes.c_int


# int SDL_hid_send_feature_report(SDL_hid_device *dev, const unsigned char *data, size_t length);
SDL_hid_send_feature_report = libsdl3.SDL_hid_send_feature_report
SDL_hid_send_feature_report.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
]
SDL_hid_send_feature_report.restype = ctypes.c_int


# int SDL_hid_set_nonblocking(SDL_hid_device *dev, int nonblock);
SDL_hid_set_nonblocking = libsdl3.SDL_hid_set_nonblocking
SDL_hid_set_nonblocking.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_hid_set_nonblocking.restype = ctypes.c_int


# int SDL_hid_write(SDL_hid_device *dev, const unsigned char *data, size_t length);
SDL_hid_write = libsdl3.SDL_hid_write
SDL_hid_write.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_hid_write.restype = ctypes.c_int
