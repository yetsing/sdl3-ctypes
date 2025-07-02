class SDL_IOStreamInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("size", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p)),
        ("seek", ctypes.CFUNCTYPE(ctypes.c_int64, ctypes.c_void_p, ctypes.c_int64, ctypes.c_int)),
        ("read", ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int))),
        ("write", ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int))),
        ("flush", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int))),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p))
    ]