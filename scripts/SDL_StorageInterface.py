class SDL_StorageInterface(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("close", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        ("ready", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
        ("enumerate", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p,
                              SDL_EnumerateDirectoryCallback, ctypes.c_void_p)),
        ("info", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(SDL_PathInfo))),
        ("read_file", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)),
        ("write_file", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint64)),
        ("mkdir", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        ("remove", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)),
        ("rename", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)),
        ("copy", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)),
        ("space_remaining", ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_void_p))
    ]