"""
SDL_rect.h
Rectangle Functions
Document: https://wiki.libsdl.org/SDL3/CategoryRect
"""

import ctypes

from sdl3_ctypes.lib import libsdl3


# typedef struct SDL_FPoint
# {
#     float x;
#     float y;
# } SDL_FPoint;
class SDL_FPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float)]


# typedef struct SDL_FRect
# {
#     float x;
#     float y;
#     float w;
#     float h;
# } SDL_FRect;
class SDL_FRect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("w", ctypes.c_float),
        ("h", ctypes.c_float),
    ]


# typedef struct SDL_Point
# {
#     int x;
#     int y;
# } SDL_Point;
class SDL_Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


# typedef struct SDL_Rect
# {
#     int x, y;
#     int w, h;
# } SDL_Rect;
class SDL_Rect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
    ]


# bool SDL_GetRectAndLineIntersection(const SDL_Rect *rect, int *X1, int *Y1, int *X2, int *Y2);
SDL_GetRectAndLineIntersection = libsdl3.SDL_GetRectAndLineIntersection
SDL_GetRectAndLineIntersection.argtypes = [
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetRectAndLineIntersection.restype = ctypes.c_bool


# bool SDL_GetRectAndLineIntersectionFloat(const SDL_FRect *rect, float *X1, float *Y1, float *X2, float *Y2);
SDL_GetRectAndLineIntersectionFloat = libsdl3.SDL_GetRectAndLineIntersectionFloat
SDL_GetRectAndLineIntersectionFloat.argtypes = [
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetRectAndLineIntersectionFloat.restype = ctypes.c_bool


# bool SDL_GetRectEnclosingPoints(const SDL_Point *points, int count, const SDL_Rect *clip, SDL_Rect *result);
SDL_GetRectEnclosingPoints = libsdl3.SDL_GetRectEnclosingPoints
SDL_GetRectEnclosingPoints.argtypes = [
    ctypes.POINTER(SDL_Point),
    ctypes.c_int,
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Rect),
]
SDL_GetRectEnclosingPoints.restype = ctypes.c_bool


# bool SDL_GetRectEnclosingPointsFloat(const SDL_FPoint *points, int count, const SDL_FRect *clip, SDL_FRect *result);
SDL_GetRectEnclosingPointsFloat = libsdl3.SDL_GetRectEnclosingPointsFloat
SDL_GetRectEnclosingPointsFloat.argtypes = [
    ctypes.POINTER(SDL_FPoint),
    ctypes.c_int,
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
]
SDL_GetRectEnclosingPointsFloat.restype = ctypes.c_bool


# bool SDL_GetRectIntersection(const SDL_Rect *A, const SDL_Rect *B, SDL_Rect *result);
SDL_GetRectIntersection = libsdl3.SDL_GetRectIntersection
SDL_GetRectIntersection.argtypes = [
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Rect),
]
SDL_GetRectIntersection.restype = ctypes.c_bool


# bool SDL_GetRectIntersectionFloat(const SDL_FRect *A, const SDL_FRect *B, SDL_FRect *result);
SDL_GetRectIntersectionFloat = libsdl3.SDL_GetRectIntersectionFloat
SDL_GetRectIntersectionFloat.argtypes = [
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
]
SDL_GetRectIntersectionFloat.restype = ctypes.c_bool


# bool SDL_GetRectUnion(const SDL_Rect *A, const SDL_Rect *B, SDL_Rect *result);
SDL_GetRectUnion = libsdl3.SDL_GetRectUnion
SDL_GetRectUnion.argtypes = [
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Rect),
]
SDL_GetRectUnion.restype = ctypes.c_bool


# bool SDL_GetRectUnionFloat(const SDL_FRect *A, const SDL_FRect *B, SDL_FRect *result);
SDL_GetRectUnionFloat = libsdl3.SDL_GetRectUnionFloat
SDL_GetRectUnionFloat.argtypes = [
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
]
SDL_GetRectUnionFloat.restype = ctypes.c_bool


# bool SDL_HasRectIntersection(const SDL_Rect *A, const SDL_Rect *B);
SDL_HasRectIntersection = libsdl3.SDL_HasRectIntersection
SDL_HasRectIntersection.argtypes = [ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect)]
SDL_HasRectIntersection.restype = ctypes.c_bool


# bool SDL_HasRectIntersectionFloat(const SDL_FRect *A, const SDL_FRect *B);
SDL_HasRectIntersectionFloat = libsdl3.SDL_HasRectIntersectionFloat
SDL_HasRectIntersectionFloat.argtypes = [
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
]
SDL_HasRectIntersectionFloat.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_PointInRect(const SDL_Point *p, const SDL_Rect *r);
SDL_PointInRect = libsdl3.SDL_PointInRect
SDL_PointInRect.argtypes = [ctypes.POINTER(SDL_Point), ctypes.POINTER(SDL_Rect)]
SDL_PointInRect.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_PointInRectFloat(const SDL_FPoint *p, const SDL_FRect *r);
SDL_PointInRectFloat = libsdl3.SDL_PointInRectFloat
SDL_PointInRectFloat.argtypes = [ctypes.POINTER(SDL_FPoint), ctypes.POINTER(SDL_FRect)]
SDL_PointInRectFloat.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_RectEmpty(const SDL_Rect *r);
SDL_RectEmpty = libsdl3.SDL_RectEmpty
SDL_RectEmpty.argtypes = [ctypes.POINTER(SDL_Rect)]
SDL_RectEmpty.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_RectEmptyFloat(const SDL_FRect *r);
SDL_RectEmptyFloat = libsdl3.SDL_RectEmptyFloat
SDL_RectEmptyFloat.argtypes = [ctypes.POINTER(SDL_FRect)]
SDL_RectEmptyFloat.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_RectsEqual(const SDL_Rect *a, const SDL_Rect *b);
SDL_RectsEqual = libsdl3.SDL_RectsEqual
SDL_RectsEqual.argtypes = [ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_Rect)]
SDL_RectsEqual.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_RectsEqualEpsilon(const SDL_FRect *a, const SDL_FRect *b, float epsilon);
SDL_RectsEqualEpsilon = libsdl3.SDL_RectsEqualEpsilon
SDL_RectsEqualEpsilon.argtypes = [
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
    ctypes.c_float,
]
SDL_RectsEqualEpsilon.restype = ctypes.c_bool


# SDL_FORCE_INLINE bool SDL_RectsEqualFloat(const SDL_FRect *a, const SDL_FRect *b);
SDL_RectsEqualFloat = libsdl3.SDL_RectsEqualFloat
SDL_RectsEqualFloat.argtypes = [ctypes.POINTER(SDL_FRect), ctypes.POINTER(SDL_FRect)]
SDL_RectsEqualFloat.restype = ctypes.c_bool


# SDL_FORCE_INLINE void SDL_RectToFRect(const SDL_Rect *rect, SDL_FRect *frect);
SDL_RectToFRect = libsdl3.SDL_RectToFRect
SDL_RectToFRect.argtypes = [ctypes.POINTER(SDL_Rect), ctypes.POINTER(SDL_FRect)]
SDL_RectToFRect.restype = None
