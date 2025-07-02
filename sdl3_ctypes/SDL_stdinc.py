"""
SDL_stdinc.h
Standard Library Functionality
Document: https://wiki.libsdl.org/SDL3/CategoryStdinc
"""

import ctypes

from sdl3_ctypes.lib import libsdl3

# #define SDL_arraysize(array) (sizeof(array)/sizeof(array[0]))
# #define SDL_clamp(x, a, b) (((x) < (a)) ? (a) : (((x) > (b)) ? (b) : (x)))
# #define SDL_COMPILE_TIME_ASSERT(name, x) FailToCompileIf_x_IsFalse(x)
# #define SDL_const_cast(type, expression) const_cast<type>(expression)  /* or `((type)(expression))` in C */
# #define SDL_copyp(dst, src)                                                                 \
#     { SDL_COMPILE_TIME_ASSERT(SDL_copyp, sizeof (*(dst)) == sizeof (*(src))); }             \
#     SDL_memcpy((dst), (src), sizeof(*(src)))
# #define SDL_FLT_EPSILON 1.1920928955078125e-07F /* 0x0.000002p0 */
SDL_FLT_EPSILON = 1.1920928955078125e-07
# #define SDL_FOURCC(A, B, C, D) \
#     ((SDL_static_cast(Uint32, SDL_static_cast(Uint8, (A))) << 0) | \
#      (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (B))) << 8) | \
#      (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (C))) << 16) | \
#      (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (D))) << 24))
# #define SDL_iconv_utf8_locale(S)    SDL_iconv_string("", "UTF-8", S, SDL_strlen(S)+1)
# #define SDL_iconv_utf8_ucs2(S)      (Uint16 *)SDL_iconv_string("UCS-2", "UTF-8", S, SDL_strlen(S)+1)
# #define SDL_iconv_utf8_ucs4(S)      (Uint32 *)SDL_iconv_string("UCS-4", "UTF-8", S, SDL_strlen(S)+1)
# #define SDL_iconv_wchar_utf8(S)     SDL_iconv_string("UTF-8", "WCHAR_T", (char *)S, (SDL_wcslen(S)+1)*sizeof(wchar_t))
# #define SDL_IN_BYTECAP(x) _In_bytecount_(x)
# #define SDL_INIT_INTERFACE(iface)               \
#     do {                                        \
#         SDL_zerop(iface);                       \
#         (iface)->version = sizeof(*(iface));    \
#     } while (0)
# #define SDL_INOUT_Z_CAP(x) _Inout_z_cap_(x)
# #define SDL_INVALID_UNICODE_CODEPOINT 0xFFFD
SDL_INVALID_UNICODE_CODEPOINT = 0xFFFD
# #define SDL_max(x, y) (((x) > (y)) ? (x) : (y))
# #define SDL_min(x, y) (((x) < (y)) ? (x) : (y))
# #define SDL_NOLONGLONG 1
SDL_NOLONGLONG = 1
# #define SDL_OUT_BYTECAP(x) _Out_bytecap_(x)
# #define SDL_OUT_CAP(x) _Out_cap_(x)
# #define SDL_OUT_Z_BYTECAP(x) _Out_z_bytecap_(x)
# #define SDL_OUT_Z_CAP(x) _Out_z_cap_(x)
# #define SDL_PI_D   3.141592653589793238462643383279502884       /**< pi (double) */
SDL_PI_D = 3.141592653589793238462643383279502884
# #define SDL_PI_F   3.141592653589793238462643383279502884F      /**< pi (float) */
SDL_PI_F = 3.141592653589793238462643383279502884
# #define SDL_PRILL_PREFIX "ll"
# #define SDL_PRILLd SDL_PRILL_PREFIX "d"
# #define SDL_PRILLu SDL_PRILL_PREFIX "u"
# #define SDL_PRILLX SDL_PRILL_PREFIX "X"
# #define SDL_PRILLx SDL_PRILL_PREFIX "x"
# #define SDL_PRINTF_FORMAT_STRING _Printf_format_string_
# #define SDL_PRINTF_VARARG_FUNC( fmtargnumber ) __attribute__ (( format( __printf__, fmtargnumber, fmtargnumber+1 )))
# #define SDL_PRINTF_VARARG_FUNCV( fmtargnumber ) __attribute__(( format( __printf__, fmtargnumber, 0 )))
# #define SDL_PRIs32 "d"
# #define SDL_PRIs64 "lld"
SDL_PRIs64 = "lld"
# #define SDL_PRIu32 "u"
# #define SDL_PRIu64 "llu"
# #define SDL_PRIX32 "X"
# #define SDL_PRIx32 "x"
# #define SDL_PRIx64 "llx"
# #define SDL_PRIX64 "llX"
# #define SDL_reinterpret_cast(type, expression) reinterpret_cast<type>(expression)  /* or `((type)(expression))` in C */
# #define SDL_SCANF_FORMAT_STRING _Scanf_format_string_impl_
# #define SDL_SCANF_VARARG_FUNC( fmtargnumber ) __attribute__ (( format( __scanf__, fmtargnumber, fmtargnumber+1 )))
# #define SDL_SCANF_VARARG_FUNCV( fmtargnumber ) __attribute__(( format( __scanf__, fmtargnumber, 0 )))
# #define SDL_SINT64_C(c)  c ## LL  /* or whatever the current compiler uses. */
# #define SDL_SIZE_MAX SIZE_MAX
# #define SDL_stack_alloc(type, count)    (type*)alloca(sizeof(type)*(count))
# #define SDL_static_cast(type, expression) static_cast<type>(expression)  /* or `((type)(expression))` in C */
# #define SDL_STRINGIFY_ARG(arg)  #arg
# #define SDL_UINT64_C(c)  c ## ULL /* or whatever the current compiler uses. */
# #define SDL_WPRINTF_VARARG_FUNC( fmtargnumber ) /* __attribute__ (( format( __wprintf__, fmtargnumber, fmtargnumber+1 ))) */
# #define SDL_WPRINTF_VARARG_FUNCV( fmtargnumber ) /* __attribute__ (( format( __wprintf__, fmtargnumber, 0 ))) */
# #define SDL_zero(x) SDL_memset(&(x), 0, sizeof((x)))
# #define SDL_zeroa(x) SDL_memset((x), 0, sizeof((x)))
# #define SDL_zerop(x) SDL_memset((x), 0, sizeof(*(x)))


# typedef void *(SDLCALL *SDL_calloc_func)(size_t nmemb, size_t size);
SDL_calloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t)


# typedef int (SDLCALL *SDL_CompareCallback)(const void *a, const void *b);
SDL_CompareCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)


# typedef int (SDLCALL *SDL_CompareCallback_r)(void *userdata, const void *a, const void *b);
SDL_CompareCallback_r = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
)

# typedef struct SDL_Environment SDL_Environment;

# typedef void (SDLCALL *SDL_free_func)(void *mem);
SDL_free_func = ctypes.CFUNCTYPE(None, ctypes.c_void_p)


# typedef void (*SDL_FunctionPointer)(void);
SDL_FunctionPointer = ctypes.CFUNCTYPE(
    None,
)

# typedef struct SDL_iconv_data_t *SDL_iconv_t;

# typedef void *(SDLCALL *SDL_malloc_func)(size_t size);
SDL_malloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_size_t)


# typedef void *(SDLCALL *SDL_realloc_func)(void *mem, size_t size);
SDL_realloc_func = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)

# typedef Sint64 SDL_Time;
# #define SDL_MAX_TIME SDL_MAX_SINT64
# #define SDL_MIN_TIME SDL_MIN_SINT64
SDL_MAX_TIME = 0x7FFFFFFFFFFFFFFF
SDL_MIN_TIME = -0x8000000000000000
# typedef int16_t Sint16;
# #define SDL_MAX_SINT16  ((Sint16)0x7FFF)        /* 32767 */
# #define SDL_MIN_SINT16  ((Sint16)(~0x7FFF))     /* -32768 */
SDL_MAX_SINT16 = 0x7FFF
SDL_MIN_SINT16 = 0xFFFF8000
# typedef int32_t Sint32;
# #define SDL_MAX_SINT32  ((Sint32)0x7FFFFFFF)    /* 2147483647 */
# #define SDL_MIN_SINT32  ((Sint32)(~0x7FFFFFFF)) /* -2147483648 */
SDL_MAX_SINT32 = 0x7FFFFFFF
SDL_MIN_SINT32 = 0x80000000
# typedef int64_t Sint64;
# #define SDL_MAX_SINT64  SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)   /* 9223372036854775807 */
# #define SDL_MIN_SINT64  ~SDL_SINT64_C(0x7FFFFFFFFFFFFFFF)  /* -9223372036854775808 */
SDL_MAX_SINT64 = 0x7FFFFFFFFFFFFFFF
SDL_MIN_SINT64 = -0x8000000000000000
# typedef int8_t Sint8;
# #define SDL_MAX_SINT8   ((Sint8)0x7F)           /* 127 */
# #define SDL_MIN_SINT8   ((Sint8)(~0x7F))        /* -128 */
SDL_MAX_SINT8 = 0x7F
SDL_MIN_SINT8 = 0xFFFFFF80
# typedef uint16_t Uint16;
# #define SDL_MAX_UINT16  ((Uint16)0xFFFF)        /* 65535 */
# #define SDL_MIN_UINT16  ((Uint16)0x0000)        /* 0 */
SDL_MAX_UINT16 = 0xFFFF
SDL_MIN_UINT16 = 0x0
# typedef uint32_t Uint32;
# #define SDL_MAX_UINT32  ((Uint32)0xFFFFFFFFu)   /* 4294967295 */
# #define SDL_MIN_UINT32  ((Uint32)0x00000000)    /* 0 */
SDL_MAX_UINT32 = 0xFFFFFFFF
SDL_MIN_UINT32 = 0x0
# typedef uint64_t Uint64;
# #define SDL_MAX_UINT64  SDL_UINT64_C(0xFFFFFFFFFFFFFFFF)   /* 18446744073709551615 */
# #define SDL_MIN_UINT64  SDL_UINT64_C(0x0000000000000000)   /* 0 */
SDL_MAX_UINT64 = 0xFFFFFFFFFFFFFFFF
SDL_MIN_UINT64 = 0x0
# typedef uint8_t Uint8;
# #define SDL_MAX_UINT8   ((Uint8)0xFF)           /* 255 */
# #define SDL_MIN_UINT8   ((Uint8)0x00)           /* 0 */
SDL_MAX_UINT8 = 0xFF
SDL_MIN_UINT8 = 0x0


# int SDL_abs(int x);
SDL_abs = libsdl3.SDL_abs
SDL_abs.argtypes = [ctypes.c_int]
SDL_abs.restype = ctypes.c_int


# double SDL_acos(double x);
SDL_acos = libsdl3.SDL_acos
SDL_acos.argtypes = [ctypes.c_double]
SDL_acos.restype = ctypes.c_double


# float SDL_acosf(float x);
SDL_acosf = libsdl3.SDL_acosf
SDL_acosf.argtypes = [ctypes.c_float]
SDL_acosf.restype = ctypes.c_float


# void * SDL_aligned_alloc(size_t alignment, size_t size);
SDL_aligned_alloc = libsdl3.SDL_aligned_alloc
SDL_aligned_alloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
SDL_aligned_alloc.restype = ctypes.c_void_p


# void SDL_aligned_free(void *mem);
SDL_aligned_free = libsdl3.SDL_aligned_free
SDL_aligned_free.argtypes = [ctypes.c_void_p]
SDL_aligned_free.restype = None


# double SDL_asin(double x);
SDL_asin = libsdl3.SDL_asin
SDL_asin.argtypes = [ctypes.c_double]
SDL_asin.restype = ctypes.c_double


# float SDL_asinf(float x);
SDL_asinf = libsdl3.SDL_asinf
SDL_asinf.argtypes = [ctypes.c_float]
SDL_asinf.restype = ctypes.c_float

# int SDL_asprintf(char **strp, const char *fmt, ...);

# double SDL_atan(double x);
SDL_atan = libsdl3.SDL_atan
SDL_atan.argtypes = [ctypes.c_double]
SDL_atan.restype = ctypes.c_double


# double SDL_atan2(double y, double x);
SDL_atan2 = libsdl3.SDL_atan2
SDL_atan2.argtypes = [ctypes.c_double, ctypes.c_double]
SDL_atan2.restype = ctypes.c_double


# float SDL_atan2f(float y, float x);
SDL_atan2f = libsdl3.SDL_atan2f
SDL_atan2f.argtypes = [ctypes.c_float, ctypes.c_float]
SDL_atan2f.restype = ctypes.c_float


# float SDL_atanf(float x);
SDL_atanf = libsdl3.SDL_atanf
SDL_atanf.argtypes = [ctypes.c_float]
SDL_atanf.restype = ctypes.c_float


# double SDL_atof(const char *str);
SDL_atof = libsdl3.SDL_atof
SDL_atof.argtypes = [ctypes.c_char_p]
SDL_atof.restype = ctypes.c_double


# int SDL_atoi(const char *str);
SDL_atoi = libsdl3.SDL_atoi
SDL_atoi.argtypes = [ctypes.c_char_p]
SDL_atoi.restype = ctypes.c_int


# void * SDL_bsearch(const void *key, const void *base, size_t nmemb, size_t size, SDL_CompareCallback compare);
SDL_bsearch = libsdl3.SDL_bsearch
SDL_bsearch.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    SDL_CompareCallback,
]
SDL_bsearch.restype = ctypes.c_void_p


# void * SDL_bsearch_r(const void *key, const void *base, size_t nmemb, size_t size, SDL_CompareCallback_r compare, void *userdata);
SDL_bsearch_r = libsdl3.SDL_bsearch_r
SDL_bsearch_r.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    SDL_CompareCallback_r,
    ctypes.c_void_p,
]
SDL_bsearch_r.restype = ctypes.c_void_p


# void * SDL_calloc(size_t nmemb, size_t size);
SDL_calloc = libsdl3.SDL_calloc
SDL_calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]
SDL_calloc.restype = ctypes.c_void_p


# double SDL_ceil(double x);
SDL_ceil = libsdl3.SDL_ceil
SDL_ceil.argtypes = [ctypes.c_double]
SDL_ceil.restype = ctypes.c_double


# float SDL_ceilf(float x);
SDL_ceilf = libsdl3.SDL_ceilf
SDL_ceilf.argtypes = [ctypes.c_float]
SDL_ceilf.restype = ctypes.c_float


# double SDL_copysign(double x, double y);
SDL_copysign = libsdl3.SDL_copysign
SDL_copysign.argtypes = [ctypes.c_double, ctypes.c_double]
SDL_copysign.restype = ctypes.c_double


# float SDL_copysignf(float x, float y);
SDL_copysignf = libsdl3.SDL_copysignf
SDL_copysignf.argtypes = [ctypes.c_float, ctypes.c_float]
SDL_copysignf.restype = ctypes.c_float


# double SDL_cos(double x);
SDL_cos = libsdl3.SDL_cos
SDL_cos.argtypes = [ctypes.c_double]
SDL_cos.restype = ctypes.c_double


# float SDL_cosf(float x);
SDL_cosf = libsdl3.SDL_cosf
SDL_cosf.argtypes = [ctypes.c_float]
SDL_cosf.restype = ctypes.c_float


# Uint16 SDL_crc16(Uint16 crc, const void *data, size_t len);
SDL_crc16 = libsdl3.SDL_crc16
SDL_crc16.argtypes = [ctypes.c_uint16, ctypes.c_void_p, ctypes.c_size_t]
SDL_crc16.restype = ctypes.c_uint16


# Uint32 SDL_crc32(Uint32 crc, const void *data, size_t len);
SDL_crc32 = libsdl3.SDL_crc32
SDL_crc32.argtypes = [ctypes.c_uint32, ctypes.c_void_p, ctypes.c_size_t]
SDL_crc32.restype = ctypes.c_uint32


# SDL_Environment * SDL_CreateEnvironment(bool populated);
SDL_CreateEnvironment = libsdl3.SDL_CreateEnvironment
SDL_CreateEnvironment.argtypes = [ctypes.c_bool]
SDL_CreateEnvironment.restype = ctypes.c_void_p


# void SDL_DestroyEnvironment(SDL_Environment *env);
SDL_DestroyEnvironment = libsdl3.SDL_DestroyEnvironment
SDL_DestroyEnvironment.argtypes = [ctypes.c_void_p]
SDL_DestroyEnvironment.restype = None


# double SDL_exp(double x);
SDL_exp = libsdl3.SDL_exp
SDL_exp.argtypes = [ctypes.c_double]
SDL_exp.restype = ctypes.c_double


# float SDL_expf(float x);
SDL_expf = libsdl3.SDL_expf
SDL_expf.argtypes = [ctypes.c_float]
SDL_expf.restype = ctypes.c_float


# double SDL_fabs(double x);
SDL_fabs = libsdl3.SDL_fabs
SDL_fabs.argtypes = [ctypes.c_double]
SDL_fabs.restype = ctypes.c_double


# float SDL_fabsf(float x);
SDL_fabsf = libsdl3.SDL_fabsf
SDL_fabsf.argtypes = [ctypes.c_float]
SDL_fabsf.restype = ctypes.c_float


# double SDL_floor(double x);
SDL_floor = libsdl3.SDL_floor
SDL_floor.argtypes = [ctypes.c_double]
SDL_floor.restype = ctypes.c_double


# float SDL_floorf(float x);
SDL_floorf = libsdl3.SDL_floorf
SDL_floorf.argtypes = [ctypes.c_float]
SDL_floorf.restype = ctypes.c_float


# double SDL_fmod(double x, double y);
SDL_fmod = libsdl3.SDL_fmod
SDL_fmod.argtypes = [ctypes.c_double, ctypes.c_double]
SDL_fmod.restype = ctypes.c_double


# float SDL_fmodf(float x, float y);
SDL_fmodf = libsdl3.SDL_fmodf
SDL_fmodf.argtypes = [ctypes.c_float, ctypes.c_float]
SDL_fmodf.restype = ctypes.c_float


# void SDL_free(void *mem);
SDL_free = libsdl3.SDL_free
SDL_free.argtypes = [ctypes.c_void_p]
SDL_free.restype = None


# const char * SDL_getenv(const char *name);
SDL_getenv = libsdl3.SDL_getenv
SDL_getenv.argtypes = [ctypes.c_char_p]
SDL_getenv.restype = ctypes.c_char_p


# const char * SDL_getenv_unsafe(const char *name);
SDL_getenv_unsafe = libsdl3.SDL_getenv_unsafe
SDL_getenv_unsafe.argtypes = [ctypes.c_char_p]
SDL_getenv_unsafe.restype = ctypes.c_char_p


# SDL_Environment * SDL_GetEnvironment(void);
SDL_GetEnvironment = libsdl3.SDL_GetEnvironment
SDL_GetEnvironment.argtypes = []
SDL_GetEnvironment.restype = ctypes.c_void_p


# const char * SDL_GetEnvironmentVariable(SDL_Environment *env, const char *name);
SDL_GetEnvironmentVariable = libsdl3.SDL_GetEnvironmentVariable
SDL_GetEnvironmentVariable.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_GetEnvironmentVariable.restype = ctypes.c_char_p


# char ** SDL_GetEnvironmentVariables(SDL_Environment *env);
SDL_GetEnvironmentVariables = libsdl3.SDL_GetEnvironmentVariables
SDL_GetEnvironmentVariables.argtypes = [ctypes.c_void_p]
SDL_GetEnvironmentVariables.restype = ctypes.POINTER(ctypes.c_char_p)


# void SDL_GetMemoryFunctions(SDL_malloc_func *malloc_func,
#                         SDL_calloc_func *calloc_func,
#                         SDL_realloc_func *realloc_func,
#                         SDL_free_func *free_func);
SDL_GetMemoryFunctions = libsdl3.SDL_GetMemoryFunctions
SDL_GetMemoryFunctions.argtypes = [
    ctypes.POINTER(SDL_malloc_func),
    ctypes.POINTER(SDL_calloc_func),
    ctypes.POINTER(SDL_realloc_func),
    ctypes.POINTER(SDL_free_func),
]
SDL_GetMemoryFunctions.restype = None


# int SDL_GetNumAllocations(void);
SDL_GetNumAllocations = libsdl3.SDL_GetNumAllocations
SDL_GetNumAllocations.argtypes = []
SDL_GetNumAllocations.restype = ctypes.c_int


# void SDL_GetOriginalMemoryFunctions(SDL_malloc_func *malloc_func,
#                                 SDL_calloc_func *calloc_func,
#                                 SDL_realloc_func *realloc_func,
#                                 SDL_free_func *free_func);
SDL_GetOriginalMemoryFunctions = libsdl3.SDL_GetOriginalMemoryFunctions
SDL_GetOriginalMemoryFunctions.argtypes = [
    ctypes.POINTER(SDL_malloc_func),
    ctypes.POINTER(SDL_calloc_func),
    ctypes.POINTER(SDL_realloc_func),
    ctypes.POINTER(SDL_free_func),
]
SDL_GetOriginalMemoryFunctions.restype = None


# size_t SDL_iconv(SDL_iconv_t cd, const char **inbuf,
#              size_t *inbytesleft, char **outbuf,
#              size_t *outbytesleft);
# #define SDL_ICONV_ERROR     (size_t)-1  /**< Generic error. Check SDL_GetError()? */
# #define SDL_ICONV_E2BIG     (size_t)-2  /**< Output buffer was too small. */
# #define SDL_ICONV_EILSEQ    (size_t)-3  /**< Invalid input sequence was encountered. */
# #define SDL_ICONV_EINVAL    (size_t)-4  /**< Incomplete input sequence was encountered. */
SDL_iconv = libsdl3.SDL_iconv
SDL_iconv.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_size_t),
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_size_t),
]
SDL_iconv.restype = ctypes.c_size_t


# int SDL_iconv_close(SDL_iconv_t cd);
SDL_iconv_close = libsdl3.SDL_iconv_close
SDL_iconv_close.argtypes = [ctypes.c_void_p]
SDL_iconv_close.restype = ctypes.c_int


# SDL_iconv_t SDL_iconv_open(const char *tocode,
#                        const char *fromcode);
SDL_iconv_open = libsdl3.SDL_iconv_open
SDL_iconv_open.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_iconv_open.restype = ctypes.c_void_p


# char * SDL_iconv_string(const char *tocode,
#                    const char *fromcode,
#                    const char *inbuf,
#                    size_t inbytesleft);
SDL_iconv_string = libsdl3.SDL_iconv_string
SDL_iconv_string.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_size_t,
]
SDL_iconv_string.restype = ctypes.c_char_p


# int SDL_isalnum(int x);
SDL_isalnum = libsdl3.SDL_isalnum
SDL_isalnum.argtypes = [ctypes.c_int]
SDL_isalnum.restype = ctypes.c_int


# int SDL_isalpha(int x);
SDL_isalpha = libsdl3.SDL_isalpha
SDL_isalpha.argtypes = [ctypes.c_int]
SDL_isalpha.restype = ctypes.c_int


# int SDL_isblank(int x);
SDL_isblank = libsdl3.SDL_isblank
SDL_isblank.argtypes = [ctypes.c_int]
SDL_isblank.restype = ctypes.c_int


# int SDL_iscntrl(int x);
SDL_iscntrl = libsdl3.SDL_iscntrl
SDL_iscntrl.argtypes = [ctypes.c_int]
SDL_iscntrl.restype = ctypes.c_int


# int SDL_isdigit(int x);
SDL_isdigit = libsdl3.SDL_isdigit
SDL_isdigit.argtypes = [ctypes.c_int]
SDL_isdigit.restype = ctypes.c_int


# int SDL_isgraph(int x);
SDL_isgraph = libsdl3.SDL_isgraph
SDL_isgraph.argtypes = [ctypes.c_int]
SDL_isgraph.restype = ctypes.c_int


# int SDL_isinf(double x);
SDL_isinf = libsdl3.SDL_isinf
SDL_isinf.argtypes = [ctypes.c_double]
SDL_isinf.restype = ctypes.c_int


# int SDL_isinff(float x);
SDL_isinff = libsdl3.SDL_isinff
SDL_isinff.argtypes = [ctypes.c_float]
SDL_isinff.restype = ctypes.c_int


# int SDL_islower(int x);
SDL_islower = libsdl3.SDL_islower
SDL_islower.argtypes = [ctypes.c_int]
SDL_islower.restype = ctypes.c_int


# int SDL_isnan(double x);
SDL_isnan = libsdl3.SDL_isnan
SDL_isnan.argtypes = [ctypes.c_double]
SDL_isnan.restype = ctypes.c_int


# int SDL_isnanf(float x);
SDL_isnanf = libsdl3.SDL_isnanf
SDL_isnanf.argtypes = [ctypes.c_float]
SDL_isnanf.restype = ctypes.c_int


# int SDL_isprint(int x);
SDL_isprint = libsdl3.SDL_isprint
SDL_isprint.argtypes = [ctypes.c_int]
SDL_isprint.restype = ctypes.c_int


# int SDL_ispunct(int x);
SDL_ispunct = libsdl3.SDL_ispunct
SDL_ispunct.argtypes = [ctypes.c_int]
SDL_ispunct.restype = ctypes.c_int


# int SDL_isspace(int x);
SDL_isspace = libsdl3.SDL_isspace
SDL_isspace.argtypes = [ctypes.c_int]
SDL_isspace.restype = ctypes.c_int


# int SDL_isupper(int x);
SDL_isupper = libsdl3.SDL_isupper
SDL_isupper.argtypes = [ctypes.c_int]
SDL_isupper.restype = ctypes.c_int


# int SDL_isxdigit(int x);
SDL_isxdigit = libsdl3.SDL_isxdigit
SDL_isxdigit.argtypes = [ctypes.c_int]
SDL_isxdigit.restype = ctypes.c_int


# char * SDL_itoa(int value, char *str, int radix);
SDL_itoa = libsdl3.SDL_itoa
SDL_itoa.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
SDL_itoa.restype = ctypes.c_char_p


# char * SDL_lltoa(long long value, char *str, int radix);
SDL_lltoa = libsdl3.SDL_lltoa
SDL_lltoa.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_int]
SDL_lltoa.restype = ctypes.c_char_p


# double SDL_log(double x);
SDL_log = libsdl3.SDL_log
SDL_log.argtypes = [ctypes.c_double]
SDL_log.restype = ctypes.c_double


# double SDL_log10(double x);
SDL_log10 = libsdl3.SDL_log10
SDL_log10.argtypes = [ctypes.c_double]
SDL_log10.restype = ctypes.c_double


# float SDL_log10f(float x);
SDL_log10f = libsdl3.SDL_log10f
SDL_log10f.argtypes = [ctypes.c_float]
SDL_log10f.restype = ctypes.c_float


# float SDL_logf(float x);
SDL_logf = libsdl3.SDL_logf
SDL_logf.argtypes = [ctypes.c_float]
SDL_logf.restype = ctypes.c_float


# long SDL_lround(double x);
SDL_lround = libsdl3.SDL_lround
SDL_lround.argtypes = [ctypes.c_double]
SDL_lround.restype = ctypes.c_long


# long SDL_lroundf(float x);
SDL_lroundf = libsdl3.SDL_lroundf
SDL_lroundf.argtypes = [ctypes.c_float]
SDL_lroundf.restype = ctypes.c_long


# char * SDL_ltoa(long value, char *str, int radix);
SDL_ltoa = libsdl3.SDL_ltoa
SDL_ltoa.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_int]
SDL_ltoa.restype = ctypes.c_char_p


# void * SDL_malloc(size_t size);
SDL_malloc = libsdl3.SDL_malloc
SDL_malloc.argtypes = [ctypes.c_size_t]
SDL_malloc.restype = ctypes.c_void_p


# int SDL_memcmp(const void *s1, const void *s2, size_t len);
SDL_memcmp = libsdl3.SDL_memcmp
SDL_memcmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_memcmp.restype = ctypes.c_int


# void * SDL_memcpy(void *dst, const void *src, size_t len);
SDL_memcpy = libsdl3.SDL_memcpy
SDL_memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_memcpy.restype = ctypes.c_void_p


# void * SDL_memmove(void *dst, const void *src, size_t len);
SDL_memmove = libsdl3.SDL_memmove
SDL_memmove.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_memmove.restype = ctypes.c_void_p


# void * SDL_memset(void *dst, int c, size_t len);
SDL_memset = libsdl3.SDL_memset
SDL_memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]
SDL_memset.restype = ctypes.c_void_p


# void * SDL_memset4(void *dst, Uint32 val, size_t dwords);
SDL_memset4 = libsdl3.SDL_memset4
SDL_memset4.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_size_t]
SDL_memset4.restype = ctypes.c_void_p


# double SDL_modf(double x, double *y);
SDL_modf = libsdl3.SDL_modf
SDL_modf.argtypes = [ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
SDL_modf.restype = ctypes.c_double


# float SDL_modff(float x, float *y);
SDL_modff = libsdl3.SDL_modff
SDL_modff.argtypes = [ctypes.c_float, ctypes.POINTER(ctypes.c_float)]
SDL_modff.restype = ctypes.c_float


# Uint32 SDL_murmur3_32(const void *data, size_t len, Uint32 seed);
SDL_murmur3_32 = libsdl3.SDL_murmur3_32
SDL_murmur3_32.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_uint32]
SDL_murmur3_32.restype = ctypes.c_uint32


# double SDL_pow(double x, double y);
SDL_pow = libsdl3.SDL_pow
SDL_pow.argtypes = [ctypes.c_double, ctypes.c_double]
SDL_pow.restype = ctypes.c_double


# float SDL_powf(float x, float y);
SDL_powf = libsdl3.SDL_powf
SDL_powf.argtypes = [ctypes.c_float, ctypes.c_float]
SDL_powf.restype = ctypes.c_float


# void SDL_qsort(void *base, size_t nmemb, size_t size, SDL_CompareCallback compare);
SDL_qsort = libsdl3.SDL_qsort
SDL_qsort.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    SDL_CompareCallback,
]
SDL_qsort.restype = None


# void SDL_qsort_r(void *base, size_t nmemb, size_t size, SDL_CompareCallback_r compare, void *userdata);
SDL_qsort_r = libsdl3.SDL_qsort_r
SDL_qsort_r.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    SDL_CompareCallback_r,
    ctypes.c_void_p,
]
SDL_qsort_r.restype = None


# Sint32 SDL_rand(Sint32 n);
SDL_rand = libsdl3.SDL_rand
SDL_rand.argtypes = [ctypes.c_int32]
SDL_rand.restype = ctypes.c_int32


# Uint32 SDL_rand_bits(void);
SDL_rand_bits = libsdl3.SDL_rand_bits
SDL_rand_bits.argtypes = []
SDL_rand_bits.restype = ctypes.c_uint32


# Uint32 SDL_rand_bits_r(Uint64 *state);
SDL_rand_bits_r = libsdl3.SDL_rand_bits_r
SDL_rand_bits_r.argtypes = [ctypes.POINTER(ctypes.c_uint64)]
SDL_rand_bits_r.restype = ctypes.c_uint32


# Sint32 SDL_rand_r(Uint64 *state, Sint32 n);
SDL_rand_r = libsdl3.SDL_rand_r
SDL_rand_r.argtypes = [ctypes.POINTER(ctypes.c_uint64), ctypes.c_int32]
SDL_rand_r.restype = ctypes.c_int32


# float SDL_randf(void);
SDL_randf = libsdl3.SDL_randf
SDL_randf.argtypes = []
SDL_randf.restype = ctypes.c_float


# float SDL_randf_r(Uint64 *state);
SDL_randf_r = libsdl3.SDL_randf_r
SDL_randf_r.argtypes = [ctypes.POINTER(ctypes.c_uint64)]
SDL_randf_r.restype = ctypes.c_float


# void * SDL_realloc(void *mem, size_t size);
SDL_realloc = libsdl3.SDL_realloc
SDL_realloc.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
SDL_realloc.restype = ctypes.c_void_p


# double SDL_round(double x);
SDL_round = libsdl3.SDL_round
SDL_round.argtypes = [ctypes.c_double]
SDL_round.restype = ctypes.c_double


# float SDL_roundf(float x);
SDL_roundf = libsdl3.SDL_roundf
SDL_roundf.argtypes = [ctypes.c_float]
SDL_roundf.restype = ctypes.c_float


# double SDL_scalbn(double x, int n);
SDL_scalbn = libsdl3.SDL_scalbn
SDL_scalbn.argtypes = [ctypes.c_double, ctypes.c_int]
SDL_scalbn.restype = ctypes.c_double


# float SDL_scalbnf(float x, int n);
SDL_scalbnf = libsdl3.SDL_scalbnf
SDL_scalbnf.argtypes = [ctypes.c_float, ctypes.c_int]
SDL_scalbnf.restype = ctypes.c_float


# int SDL_setenv_unsafe(const char *name, const char *value, int overwrite);
SDL_setenv_unsafe = libsdl3.SDL_setenv_unsafe
SDL_setenv_unsafe.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
SDL_setenv_unsafe.restype = ctypes.c_int


# bool SDL_SetEnvironmentVariable(SDL_Environment *env, const char *name, const char *value, bool overwrite);
SDL_SetEnvironmentVariable = libsdl3.SDL_SetEnvironmentVariable
SDL_SetEnvironmentVariable.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_bool,
]
SDL_SetEnvironmentVariable.restype = ctypes.c_bool


# bool SDL_SetMemoryFunctions(SDL_malloc_func malloc_func,
#                                 SDL_calloc_func calloc_func,
#                                 SDL_realloc_func realloc_func,
#                                 SDL_free_func free_func);
SDL_SetMemoryFunctions = libsdl3.SDL_SetMemoryFunctions
SDL_SetMemoryFunctions.argtypes = [
    SDL_malloc_func,
    SDL_calloc_func,
    SDL_realloc_func,
    SDL_free_func,
]
SDL_SetMemoryFunctions.restype = ctypes.c_bool


# double SDL_sin(double x);
SDL_sin = libsdl3.SDL_sin
SDL_sin.argtypes = [ctypes.c_double]
SDL_sin.restype = ctypes.c_double


# float SDL_sinf(float x);
SDL_sinf = libsdl3.SDL_sinf
SDL_sinf.argtypes = [ctypes.c_float]
SDL_sinf.restype = ctypes.c_float


# SDL_FORCE_INLINE bool SDL_size_add_check_overflow(size_t a, size_t b, size_t *ret);
SDL_size_add_check_overflow = libsdl3.SDL_size_add_check_overflow
SDL_size_add_check_overflow.argtypes = [
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t),
]
SDL_size_add_check_overflow.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_size_mul_check_overflow(size_t a, size_t b, size_t *ret);
SDL_size_mul_check_overflow = libsdl3.SDL_size_mul_check_overflow
SDL_size_mul_check_overflow.argtypes = [
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t),
]
SDL_size_mul_check_overflow.restype = ctypes.c_bool

# int SDL_snprintf(char *text, size_t maxlen, const char *fmt, ...);

# double SDL_sqrt(double x);
SDL_sqrt = libsdl3.SDL_sqrt
SDL_sqrt.argtypes = [ctypes.c_double]
SDL_sqrt.restype = ctypes.c_double


# float SDL_sqrtf(float x);
SDL_sqrtf = libsdl3.SDL_sqrtf
SDL_sqrtf.argtypes = [ctypes.c_float]
SDL_sqrtf.restype = ctypes.c_float


# void SDL_srand(Uint64 seed);
SDL_srand = libsdl3.SDL_srand
SDL_srand.argtypes = [ctypes.c_uint64]
SDL_srand.restype = None

# int SDL_sscanf(const char *text, const char *fmt, ...);

# Uint32 SDL_StepBackUTF8(const char *start, const char **pstr);
SDL_StepBackUTF8 = libsdl3.SDL_StepBackUTF8
SDL_StepBackUTF8.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
SDL_StepBackUTF8.restype = ctypes.c_uint32


# Uint32 SDL_StepUTF8(const char **pstr, size_t *pslen);
SDL_StepUTF8 = libsdl3.SDL_StepUTF8
SDL_StepUTF8.argtypes = [
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_size_t),
]
SDL_StepUTF8.restype = ctypes.c_uint32


# int SDL_strcasecmp(const char *str1, const char *str2);
SDL_strcasecmp = libsdl3.SDL_strcasecmp
SDL_strcasecmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_strcasecmp.restype = ctypes.c_int


# char * SDL_strcasestr(const char *haystack, const char *needle);
SDL_strcasestr = libsdl3.SDL_strcasestr
SDL_strcasestr.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_strcasestr.restype = ctypes.c_char_p


# char * SDL_strchr(const char *str, int c);
SDL_strchr = libsdl3.SDL_strchr
SDL_strchr.argtypes = [ctypes.c_char_p, ctypes.c_int]
SDL_strchr.restype = ctypes.c_char_p


# int SDL_strcmp(const char *str1, const char *str2);
SDL_strcmp = libsdl3.SDL_strcmp
SDL_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_strcmp.restype = ctypes.c_int


# char * SDL_strdup(const char *str);
SDL_strdup = libsdl3.SDL_strdup
SDL_strdup.argtypes = [ctypes.c_char_p]
SDL_strdup.restype = ctypes.c_char_p


# size_t SDL_strlcat(char *dst, const char *src, size_t maxlen);
SDL_strlcat = libsdl3.SDL_strlcat
SDL_strlcat.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_strlcat.restype = ctypes.c_size_t


# size_t SDL_strlcpy(char *dst, const char *src, size_t maxlen);
SDL_strlcpy = libsdl3.SDL_strlcpy
SDL_strlcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_strlcpy.restype = ctypes.c_size_t


# size_t SDL_strlen(const char *str);
SDL_strlen = libsdl3.SDL_strlen
SDL_strlen.argtypes = [ctypes.c_char_p]
SDL_strlen.restype = ctypes.c_size_t


# char * SDL_strlwr(char *str);
SDL_strlwr = libsdl3.SDL_strlwr
SDL_strlwr.argtypes = [ctypes.c_char_p]
SDL_strlwr.restype = ctypes.c_char_p


# int SDL_strncasecmp(const char *str1, const char *str2, size_t maxlen);
SDL_strncasecmp = libsdl3.SDL_strncasecmp
SDL_strncasecmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_strncasecmp.restype = ctypes.c_int


# int SDL_strncmp(const char *str1, const char *str2, size_t maxlen);
SDL_strncmp = libsdl3.SDL_strncmp
SDL_strncmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_strncmp.restype = ctypes.c_int


# char * SDL_strndup(const char *str, size_t maxlen);
SDL_strndup = libsdl3.SDL_strndup
SDL_strndup.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
SDL_strndup.restype = ctypes.c_char_p


# size_t SDL_strnlen(const char *str, size_t maxlen);
SDL_strnlen = libsdl3.SDL_strnlen
SDL_strnlen.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
SDL_strnlen.restype = ctypes.c_size_t


# char * SDL_strnstr(const char *haystack, const char *needle, size_t maxlen);
SDL_strnstr = libsdl3.SDL_strnstr
SDL_strnstr.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_strnstr.restype = ctypes.c_char_p


# char * SDL_strpbrk(const char *str, const char *breakset);
SDL_strpbrk = libsdl3.SDL_strpbrk
SDL_strpbrk.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_strpbrk.restype = ctypes.c_char_p


# char * SDL_strrchr(const char *str, int c);
SDL_strrchr = libsdl3.SDL_strrchr
SDL_strrchr.argtypes = [ctypes.c_char_p, ctypes.c_int]
SDL_strrchr.restype = ctypes.c_char_p


# char * SDL_strrev(char *str);
SDL_strrev = libsdl3.SDL_strrev
SDL_strrev.argtypes = [ctypes.c_char_p]
SDL_strrev.restype = ctypes.c_char_p


# char * SDL_strstr(const char *haystack, const char *needle);
SDL_strstr = libsdl3.SDL_strstr
SDL_strstr.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SDL_strstr.restype = ctypes.c_char_p


# double SDL_strtod(const char *str, char **endp);
SDL_strtod = libsdl3.SDL_strtod
SDL_strtod.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
SDL_strtod.restype = ctypes.c_double


# char * SDL_strtok_r(char *str, const char *delim, char **saveptr);
SDL_strtok_r = libsdl3.SDL_strtok_r
SDL_strtok_r.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_char_p),
]
SDL_strtok_r.restype = ctypes.c_char_p


# long SDL_strtol(const char *str, char **endp, int base);
SDL_strtol = libsdl3.SDL_strtol
SDL_strtol.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int]
SDL_strtol.restype = ctypes.c_long


# long long SDL_strtoll(const char *str, char **endp, int base);
SDL_strtoll = libsdl3.SDL_strtoll
SDL_strtoll.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int]
SDL_strtoll.restype = ctypes.c_long


# unsigned long SDL_strtoul(const char *str, char **endp, int base);
SDL_strtoul = libsdl3.SDL_strtoul
SDL_strtoul.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int]
SDL_strtoul.restype = ctypes.c_long


# unsigned long long SDL_strtoull(const char *str, char **endp, int base);
SDL_strtoull = libsdl3.SDL_strtoull
SDL_strtoull.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int]
SDL_strtoull.restype = ctypes.c_long


# char * SDL_strupr(char *str);
SDL_strupr = libsdl3.SDL_strupr
SDL_strupr.argtypes = [ctypes.c_char_p]
SDL_strupr.restype = ctypes.c_char_p

# int SDL_swprintf(wchar_t *text, size_t maxlen, const wchar_t *fmt, ...);

# double SDL_tan(double x);
SDL_tan = libsdl3.SDL_tan
SDL_tan.argtypes = [ctypes.c_double]
SDL_tan.restype = ctypes.c_double


# float SDL_tanf(float x);
SDL_tanf = libsdl3.SDL_tanf
SDL_tanf.argtypes = [ctypes.c_float]
SDL_tanf.restype = ctypes.c_float


# int SDL_tolower(int x);
SDL_tolower = libsdl3.SDL_tolower
SDL_tolower.argtypes = [ctypes.c_int]
SDL_tolower.restype = ctypes.c_int


# int SDL_toupper(int x);
SDL_toupper = libsdl3.SDL_toupper
SDL_toupper.argtypes = [ctypes.c_int]
SDL_toupper.restype = ctypes.c_int


# double SDL_trunc(double x);
SDL_trunc = libsdl3.SDL_trunc
SDL_trunc.argtypes = [ctypes.c_double]
SDL_trunc.restype = ctypes.c_double


# float SDL_truncf(float x);
SDL_truncf = libsdl3.SDL_truncf
SDL_truncf.argtypes = [ctypes.c_float]
SDL_truncf.restype = ctypes.c_float


# char * SDL_UCS4ToUTF8(Uint32 codepoint, char *dst);
SDL_UCS4ToUTF8 = libsdl3.SDL_UCS4ToUTF8
SDL_UCS4ToUTF8.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_UCS4ToUTF8.restype = ctypes.c_char_p


# char * SDL_uitoa(unsigned int value, char *str, int radix);
SDL_uitoa = libsdl3.SDL_uitoa
SDL_uitoa.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
SDL_uitoa.restype = ctypes.c_char_p


# char * SDL_ulltoa(unsigned long long value, char *str, int radix);
SDL_ulltoa = libsdl3.SDL_ulltoa
SDL_ulltoa.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_int]
SDL_ulltoa.restype = ctypes.c_char_p


# char * SDL_ultoa(unsigned long value, char *str, int radix);
SDL_ultoa = libsdl3.SDL_ultoa
SDL_ultoa.argtypes = [ctypes.c_long, ctypes.c_char_p, ctypes.c_int]
SDL_ultoa.restype = ctypes.c_char_p


# int SDL_unsetenv_unsafe(const char *name);
SDL_unsetenv_unsafe = libsdl3.SDL_unsetenv_unsafe
SDL_unsetenv_unsafe.argtypes = [ctypes.c_char_p]
SDL_unsetenv_unsafe.restype = ctypes.c_int


# bool SDL_UnsetEnvironmentVariable(SDL_Environment *env, const char *name);
SDL_UnsetEnvironmentVariable = libsdl3.SDL_UnsetEnvironmentVariable
SDL_UnsetEnvironmentVariable.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_UnsetEnvironmentVariable.restype = ctypes.c_bool


# size_t SDL_utf8strlcpy(char *dst, const char *src, size_t dst_bytes);
SDL_utf8strlcpy = libsdl3.SDL_utf8strlcpy
SDL_utf8strlcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
SDL_utf8strlcpy.restype = ctypes.c_size_t


# size_t SDL_utf8strlen(const char *str);
SDL_utf8strlen = libsdl3.SDL_utf8strlen
SDL_utf8strlen.argtypes = [ctypes.c_char_p]
SDL_utf8strlen.restype = ctypes.c_size_t


# size_t SDL_utf8strnlen(const char *str, size_t bytes);
SDL_utf8strnlen = libsdl3.SDL_utf8strnlen
SDL_utf8strnlen.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
SDL_utf8strnlen.restype = ctypes.c_size_t

# int SDL_vasprintf(char **strp, const char *fmt, va_list ap);
# int SDL_vsnprintf(char *text, size_t maxlen, const char *fmt, va_list ap);
# int SDL_vsscanf(const char *text, const char *fmt, va_list ap);
# int SDL_vswprintf(wchar_t *text, size_t maxlen, const wchar_t *fmt, va_list ap);

# int SDL_wcscasecmp(const wchar_t *str1, const wchar_t *str2);
SDL_wcscasecmp = libsdl3.SDL_wcscasecmp
SDL_wcscasecmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_wcscasecmp.restype = ctypes.c_int


# int SDL_wcscmp(const wchar_t *str1, const wchar_t *str2);
SDL_wcscmp = libsdl3.SDL_wcscmp
SDL_wcscmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_wcscmp.restype = ctypes.c_int


# wchar_t * SDL_wcsdup(const wchar_t *wstr);
SDL_wcsdup = libsdl3.SDL_wcsdup
SDL_wcsdup.argtypes = [ctypes.c_void_p]
SDL_wcsdup.restype = ctypes.c_void_p


# size_t SDL_wcslcat(wchar_t *dst, const wchar_t *src, size_t maxlen);
SDL_wcslcat = libsdl3.SDL_wcslcat
SDL_wcslcat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_wcslcat.restype = ctypes.c_size_t


# size_t SDL_wcslcpy(wchar_t *dst, const wchar_t *src, size_t maxlen);
SDL_wcslcpy = libsdl3.SDL_wcslcpy
SDL_wcslcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_wcslcpy.restype = ctypes.c_size_t


# size_t SDL_wcslen(const wchar_t *wstr);
SDL_wcslen = libsdl3.SDL_wcslen
SDL_wcslen.argtypes = [ctypes.c_void_p]
SDL_wcslen.restype = ctypes.c_size_t


# int SDL_wcsncasecmp(const wchar_t *str1, const wchar_t *str2, size_t maxlen);
SDL_wcsncasecmp = libsdl3.SDL_wcsncasecmp
SDL_wcsncasecmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_wcsncasecmp.restype = ctypes.c_int


# int SDL_wcsncmp(const wchar_t *str1, const wchar_t *str2, size_t maxlen);
SDL_wcsncmp = libsdl3.SDL_wcsncmp
SDL_wcsncmp.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_wcsncmp.restype = ctypes.c_int


# size_t SDL_wcsnlen(const wchar_t *wstr, size_t maxlen);
SDL_wcsnlen = libsdl3.SDL_wcsnlen
SDL_wcsnlen.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
SDL_wcsnlen.restype = ctypes.c_size_t


# wchar_t * SDL_wcsnstr(const wchar_t *haystack, const wchar_t *needle, size_t maxlen);
SDL_wcsnstr = libsdl3.SDL_wcsnstr
SDL_wcsnstr.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
SDL_wcsnstr.restype = ctypes.c_void_p


# wchar_t * SDL_wcsstr(const wchar_t *haystack, const wchar_t *needle);
SDL_wcsstr = libsdl3.SDL_wcsstr
SDL_wcsstr.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_wcsstr.restype = ctypes.c_void_p


# long SDL_wcstol(const wchar_t *str, wchar_t **endp, int base);
SDL_wcstol = libsdl3.SDL_wcstol
SDL_wcstol.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
SDL_wcstol.restype = ctypes.c_long
