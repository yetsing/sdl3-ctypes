"""
SDL_surface.h
Surface Creation and Simple Drawing
Document: https://wiki.libsdl.org/SDL3/CategorySurface
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_pixels import SDL_Palette
from sdl3_ctypes.SDL_rect import SDL_Rect

# #define SDL_MUSTLOCK(S) (((S)->flags & SDL_SURFACE_LOCK_NEEDED) == SDL_SURFACE_LOCK_NEEDED)


# typedef enum SDL_FlipMode
# {
#     SDL_FLIP_NONE,          /**< Do not flip */
#     SDL_FLIP_HORIZONTAL,    /**< flip horizontally */
#     SDL_FLIP_VERTICAL       /**< flip vertically */
# } SDL_FlipMode;
SDL_FLIP_NONE = 0
SDL_FLIP_HORIZONTAL = 1
SDL_FLIP_VERTICAL = 2
# typedef enum SDL_ScaleMode
# {
#     SDL_SCALEMODE_INVALID = -1,
#     SDL_SCALEMODE_NEAREST,  /**< nearest pixel sampling */
#     SDL_SCALEMODE_LINEAR,   /**< linear filtering */
#     SDL_SCALEMODE_PIXELART  /**< nearest pixel sampling with improved scaling for pixel art */
# } SDL_ScaleMode;
SDL_SCALEMODE_INVALID = -1
SDL_SCALEMODE_NEAREST = 0
SDL_SCALEMODE_LINEAR = 1
SDL_SCALEMODE_PIXELART = 2


# struct SDL_Surface
# {
#     SDL_SurfaceFlags flags;     /**< The flags of the surface, read-only */
#     SDL_PixelFormat format;     /**< The format of the surface, read-only */
#     int w;                      /**< The width of the surface, read-only. */
#     int h;                      /**< The height of the surface, read-only. */
#     int pitch;                  /**< The distance in bytes between rows of pixels, read-only */
#     void *pixels;               /**< A pointer to the pixels of the surface, the pixels are writeable if non-NULL */
#     int refcount;               /**< Application reference count, used when freeing surface */
#     void *reserved;             /**< Reserved for internal use */
# };
class SDL_Surface(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("format", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("pitch", ctypes.c_int),
        ("pixels", ctypes.c_void_p),
        ("refcount", ctypes.c_int),
        ("reserved", ctypes.c_void_p),
    ]


# typedef Uint32 SDL_SurfaceFlags;
# #define SDL_SURFACE_PREALLOCATED    0x00000001u /**< Surface uses preallocated pixel memory */
# #define SDL_SURFACE_LOCK_NEEDED     0x00000002u /**< Surface needs to be locked to access pixels */
# #define SDL_SURFACE_LOCKED          0x00000004u /**< Surface is currently locked */
# #define SDL_SURFACE_SIMD_ALIGNED    0x00000008u /**< Surface uses pixel memory allocated with SDL_aligned_alloc() */
SDL_SURFACE_PREALLOCATED = 0x1
SDL_SURFACE_LOCK_NEEDED = 0x2
SDL_SURFACE_LOCKED = 0x4
SDL_SURFACE_SIMD_ALIGNED = 0x8


# bool SDL_AddSurfaceAlternateImage(SDL_Surface *surface, SDL_Surface *image);
SDL_AddSurfaceAlternateImage = libsdl3.SDL_AddSurfaceAlternateImage
SDL_AddSurfaceAlternateImage.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Surface),
]
SDL_AddSurfaceAlternateImage.restype = ctypes.c_bool


# bool SDL_BlitSurface(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect);
SDL_BlitSurface = libsdl3.SDL_BlitSurface
SDL_BlitSurface.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_BlitSurface.restype = ctypes.c_bool


# bool SDL_BlitSurface9Grid(SDL_Surface *src, const SDL_Rect *srcrect, int left_width, int right_width, int top_height, int bottom_height, float scale, SDL_ScaleMode scaleMode, SDL_Surface *dst, const SDL_Rect *dstrect);
SDL_BlitSurface9Grid = libsdl3.SDL_BlitSurface9Grid
SDL_BlitSurface9Grid.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_float,
    ctypes.c_int,
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_BlitSurface9Grid.restype = ctypes.c_bool


# bool SDL_BlitSurfaceScaled(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);
SDL_BlitSurfaceScaled = libsdl3.SDL_BlitSurfaceScaled
SDL_BlitSurfaceScaled.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
]
SDL_BlitSurfaceScaled.restype = ctypes.c_bool


# bool SDL_BlitSurfaceTiled(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect);
SDL_BlitSurfaceTiled = libsdl3.SDL_BlitSurfaceTiled
SDL_BlitSurfaceTiled.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_BlitSurfaceTiled.restype = ctypes.c_bool


# bool SDL_BlitSurfaceTiledWithScale(SDL_Surface *src, const SDL_Rect *srcrect, float scale, SDL_ScaleMode scaleMode, SDL_Surface *dst, const SDL_Rect *dstrect);
SDL_BlitSurfaceTiledWithScale = libsdl3.SDL_BlitSurfaceTiledWithScale
SDL_BlitSurfaceTiledWithScale.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_float,
    ctypes.c_int,
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_BlitSurfaceTiledWithScale.restype = ctypes.c_bool


# bool SDL_BlitSurfaceUnchecked(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect);
SDL_BlitSurfaceUnchecked = libsdl3.SDL_BlitSurfaceUnchecked
SDL_BlitSurfaceUnchecked.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_BlitSurfaceUnchecked.restype = ctypes.c_bool


# bool SDL_BlitSurfaceUncheckedScaled(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);
SDL_BlitSurfaceUncheckedScaled = libsdl3.SDL_BlitSurfaceUncheckedScaled
SDL_BlitSurfaceUncheckedScaled.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
]
SDL_BlitSurfaceUncheckedScaled.restype = ctypes.c_bool


# bool SDL_ClearSurface(SDL_Surface *surface, float r, float g, float b, float a);
SDL_ClearSurface = libsdl3.SDL_ClearSurface
SDL_ClearSurface.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
SDL_ClearSurface.restype = ctypes.c_bool


# bool SDL_ConvertPixels(int width, int height, SDL_PixelFormat src_format, const void *src, int src_pitch, SDL_PixelFormat dst_format, void *dst, int dst_pitch);
SDL_ConvertPixels = libsdl3.SDL_ConvertPixels
SDL_ConvertPixels.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_ConvertPixels.restype = ctypes.c_bool


# bool SDL_ConvertPixelsAndColorspace(int width, int height, SDL_PixelFormat src_format, SDL_Colorspace src_colorspace, SDL_PropertiesID src_properties, const void *src, int src_pitch, SDL_PixelFormat dst_format, SDL_Colorspace dst_colorspace, SDL_PropertiesID dst_properties, void *dst, int dst_pitch);
SDL_ConvertPixelsAndColorspace = libsdl3.SDL_ConvertPixelsAndColorspace
SDL_ConvertPixelsAndColorspace.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_ConvertPixelsAndColorspace.restype = ctypes.c_bool


# SDL_Surface * SDL_ConvertSurface(SDL_Surface *surface, SDL_PixelFormat format);
SDL_ConvertSurface = libsdl3.SDL_ConvertSurface
SDL_ConvertSurface.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_int]
SDL_ConvertSurface.restype = ctypes.POINTER(SDL_Surface)


# SDL_Surface * SDL_ConvertSurfaceAndColorspace(SDL_Surface *surface, SDL_PixelFormat format, SDL_Palette *palette, SDL_Colorspace colorspace, SDL_PropertiesID props);
SDL_ConvertSurfaceAndColorspace = libsdl3.SDL_ConvertSurfaceAndColorspace
SDL_ConvertSurfaceAndColorspace.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.POINTER(SDL_Palette),
    ctypes.c_int,
    ctypes.c_uint32,
]
SDL_ConvertSurfaceAndColorspace.restype = ctypes.POINTER(SDL_Surface)


# SDL_Surface * SDL_CreateSurface(int width, int height, SDL_PixelFormat format);
SDL_CreateSurface = libsdl3.SDL_CreateSurface
SDL_CreateSurface.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
SDL_CreateSurface.restype = ctypes.POINTER(SDL_Surface)


# SDL_Surface * SDL_CreateSurfaceFrom(int width, int height, SDL_PixelFormat format, void *pixels, int pitch);
SDL_CreateSurfaceFrom = libsdl3.SDL_CreateSurfaceFrom
SDL_CreateSurfaceFrom.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_CreateSurfaceFrom.restype = ctypes.POINTER(SDL_Surface)


# SDL_Palette * SDL_CreateSurfacePalette(SDL_Surface *surface);
SDL_CreateSurfacePalette = libsdl3.SDL_CreateSurfacePalette
SDL_CreateSurfacePalette.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_CreateSurfacePalette.restype = ctypes.POINTER(SDL_Palette)


# void SDL_DestroySurface(SDL_Surface *surface);
SDL_DestroySurface = libsdl3.SDL_DestroySurface
SDL_DestroySurface.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_DestroySurface.restype = None


# SDL_Surface * SDL_DuplicateSurface(SDL_Surface *surface);
SDL_DuplicateSurface = libsdl3.SDL_DuplicateSurface
SDL_DuplicateSurface.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_DuplicateSurface.restype = ctypes.POINTER(SDL_Surface)


# bool SDL_FillSurfaceRect(SDL_Surface *dst, const SDL_Rect *rect, Uint32 color);
SDL_FillSurfaceRect = libsdl3.SDL_FillSurfaceRect
SDL_FillSurfaceRect.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_uint32,
]
SDL_FillSurfaceRect.restype = ctypes.c_bool


# bool SDL_FillSurfaceRects(SDL_Surface *dst, const SDL_Rect *rects, int count, Uint32 color);
SDL_FillSurfaceRects = libsdl3.SDL_FillSurfaceRects
SDL_FillSurfaceRects.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
    ctypes.c_uint32,
]
SDL_FillSurfaceRects.restype = ctypes.c_bool


# bool SDL_FlipSurface(SDL_Surface *surface, SDL_FlipMode flip);
SDL_FlipSurface = libsdl3.SDL_FlipSurface
SDL_FlipSurface.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_int]
SDL_FlipSurface.restype = ctypes.c_bool


# bool SDL_GetSurfaceAlphaMod(SDL_Surface *surface, Uint8 *alpha);
SDL_GetSurfaceAlphaMod = libsdl3.SDL_GetSurfaceAlphaMod
SDL_GetSurfaceAlphaMod.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_GetSurfaceAlphaMod.restype = ctypes.c_bool


# bool SDL_GetSurfaceBlendMode(SDL_Surface *surface, SDL_BlendMode *blendMode);
SDL_GetSurfaceBlendMode = libsdl3.SDL_GetSurfaceBlendMode
SDL_GetSurfaceBlendMode.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_GetSurfaceBlendMode.restype = ctypes.c_bool


# bool SDL_GetSurfaceClipRect(SDL_Surface *surface, SDL_Rect *rect);
SDL_GetSurfaceClipRect = libsdl3.SDL_GetSurfaceClipRect
SDL_GetSurfaceClipRect.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_GetSurfaceClipRect.restype = ctypes.c_bool


# bool SDL_GetSurfaceColorKey(SDL_Surface *surface, Uint32 *key);
SDL_GetSurfaceColorKey = libsdl3.SDL_GetSurfaceColorKey
SDL_GetSurfaceColorKey.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_GetSurfaceColorKey.restype = ctypes.c_bool


# bool SDL_GetSurfaceColorMod(SDL_Surface *surface, Uint8 *r, Uint8 *g, Uint8 *b);
SDL_GetSurfaceColorMod = libsdl3.SDL_GetSurfaceColorMod
SDL_GetSurfaceColorMod.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_GetSurfaceColorMod.restype = ctypes.c_bool


# SDL_Colorspace SDL_GetSurfaceColorspace(SDL_Surface *surface);
SDL_GetSurfaceColorspace = libsdl3.SDL_GetSurfaceColorspace
SDL_GetSurfaceColorspace.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_GetSurfaceColorspace.restype = ctypes.c_int


# SDL_Surface ** SDL_GetSurfaceImages(SDL_Surface *surface, int *count);
SDL_GetSurfaceImages = libsdl3.SDL_GetSurfaceImages
SDL_GetSurfaceImages.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetSurfaceImages.restype = ctypes.POINTER(ctypes.POINTER(SDL_Surface))


# SDL_Palette * SDL_GetSurfacePalette(SDL_Surface *surface);
SDL_GetSurfacePalette = libsdl3.SDL_GetSurfacePalette
SDL_GetSurfacePalette.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_GetSurfacePalette.restype = ctypes.POINTER(SDL_Palette)


# SDL_PropertiesID SDL_GetSurfaceProperties(SDL_Surface *surface);
SDL_GetSurfaceProperties = libsdl3.SDL_GetSurfaceProperties
SDL_GetSurfaceProperties.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_GetSurfaceProperties.restype = ctypes.c_uint32


# SDL_Surface * SDL_LoadBMP(const char *file);
SDL_LoadBMP = libsdl3.SDL_LoadBMP
SDL_LoadBMP.argtypes = [ctypes.c_char_p]
SDL_LoadBMP.restype = ctypes.POINTER(SDL_Surface)


# SDL_Surface * SDL_LoadBMP_IO(SDL_IOStream *src, bool closeio);
SDL_LoadBMP_IO = libsdl3.SDL_LoadBMP_IO
SDL_LoadBMP_IO.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_LoadBMP_IO.restype = ctypes.POINTER(SDL_Surface)


# bool SDL_LockSurface(SDL_Surface *surface);
SDL_LockSurface = libsdl3.SDL_LockSurface
SDL_LockSurface.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_LockSurface.restype = ctypes.c_bool


# Uint32 SDL_MapSurfaceRGB(SDL_Surface *surface, Uint8 r, Uint8 g, Uint8 b);
SDL_MapSurfaceRGB = libsdl3.SDL_MapSurfaceRGB
SDL_MapSurfaceRGB.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_MapSurfaceRGB.restype = ctypes.c_uint32


# Uint32 SDL_MapSurfaceRGBA(SDL_Surface *surface, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
SDL_MapSurfaceRGBA = libsdl3.SDL_MapSurfaceRGBA
SDL_MapSurfaceRGBA.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_MapSurfaceRGBA.restype = ctypes.c_uint32


# bool SDL_PremultiplyAlpha(int width, int height, SDL_PixelFormat src_format, const void *src, int src_pitch, SDL_PixelFormat dst_format, void *dst, int dst_pitch, bool linear);
SDL_PremultiplyAlpha = libsdl3.SDL_PremultiplyAlpha
SDL_PremultiplyAlpha.argtypes = [
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_bool,
]
SDL_PremultiplyAlpha.restype = ctypes.c_bool


# bool SDL_PremultiplySurfaceAlpha(SDL_Surface *surface, bool linear);
SDL_PremultiplySurfaceAlpha = libsdl3.SDL_PremultiplySurfaceAlpha
SDL_PremultiplySurfaceAlpha.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_bool]
SDL_PremultiplySurfaceAlpha.restype = ctypes.c_bool


# bool SDL_ReadSurfacePixel(SDL_Surface *surface, int x, int y, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
SDL_ReadSurfacePixel = libsdl3.SDL_ReadSurfacePixel
SDL_ReadSurfacePixel.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_ReadSurfacePixel.restype = ctypes.c_bool


# bool SDL_ReadSurfacePixelFloat(SDL_Surface *surface, int x, int y, float *r, float *g, float *b, float *a);
SDL_ReadSurfacePixelFloat = libsdl3.SDL_ReadSurfacePixelFloat
SDL_ReadSurfacePixelFloat.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_ReadSurfacePixelFloat.restype = ctypes.c_bool


# void SDL_RemoveSurfaceAlternateImages(SDL_Surface *surface);
SDL_RemoveSurfaceAlternateImages = libsdl3.SDL_RemoveSurfaceAlternateImages
SDL_RemoveSurfaceAlternateImages.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_RemoveSurfaceAlternateImages.restype = None


# bool SDL_SaveBMP(SDL_Surface *surface, const char *file);
SDL_SaveBMP = libsdl3.SDL_SaveBMP
SDL_SaveBMP.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_char_p]
SDL_SaveBMP.restype = ctypes.c_bool


# bool SDL_SaveBMP_IO(SDL_Surface *surface, SDL_IOStream *dst, bool closeio);
SDL_SaveBMP_IO = libsdl3.SDL_SaveBMP_IO
SDL_SaveBMP_IO.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_void_p, ctypes.c_bool]
SDL_SaveBMP_IO.restype = ctypes.c_bool


# SDL_Surface * SDL_ScaleSurface(SDL_Surface *surface, int width, int height, SDL_ScaleMode scaleMode);
SDL_ScaleSurface = libsdl3.SDL_ScaleSurface
SDL_ScaleSurface.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_ScaleSurface.restype = ctypes.POINTER(SDL_Surface)


# bool SDL_SetSurfaceAlphaMod(SDL_Surface *surface, Uint8 alpha);
SDL_SetSurfaceAlphaMod = libsdl3.SDL_SetSurfaceAlphaMod
SDL_SetSurfaceAlphaMod.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_uint8]
SDL_SetSurfaceAlphaMod.restype = ctypes.c_bool


# bool SDL_SetSurfaceBlendMode(SDL_Surface *surface, SDL_BlendMode blendMode);
SDL_SetSurfaceBlendMode = libsdl3.SDL_SetSurfaceBlendMode
SDL_SetSurfaceBlendMode.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_uint32]
SDL_SetSurfaceBlendMode.restype = ctypes.c_bool


# bool SDL_SetSurfaceClipRect(SDL_Surface *surface, const SDL_Rect *rect);
SDL_SetSurfaceClipRect = libsdl3.SDL_SetSurfaceClipRect
SDL_SetSurfaceClipRect.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
]
SDL_SetSurfaceClipRect.restype = ctypes.c_bool


# bool SDL_SetSurfaceColorKey(SDL_Surface *surface, bool enabled, Uint32 key);
SDL_SetSurfaceColorKey = libsdl3.SDL_SetSurfaceColorKey
SDL_SetSurfaceColorKey.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_bool,
    ctypes.c_uint32,
]
SDL_SetSurfaceColorKey.restype = ctypes.c_bool


# bool SDL_SetSurfaceColorMod(SDL_Surface *surface, Uint8 r, Uint8 g, Uint8 b);
SDL_SetSurfaceColorMod = libsdl3.SDL_SetSurfaceColorMod
SDL_SetSurfaceColorMod.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_SetSurfaceColorMod.restype = ctypes.c_bool


# bool SDL_SetSurfaceColorspace(SDL_Surface *surface, SDL_Colorspace colorspace);
SDL_SetSurfaceColorspace = libsdl3.SDL_SetSurfaceColorspace
SDL_SetSurfaceColorspace.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_int]
SDL_SetSurfaceColorspace.restype = ctypes.c_bool


# bool SDL_SetSurfacePalette(SDL_Surface *surface, SDL_Palette *palette);
SDL_SetSurfacePalette = libsdl3.SDL_SetSurfacePalette
SDL_SetSurfacePalette.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Palette),
]
SDL_SetSurfacePalette.restype = ctypes.c_bool


# bool SDL_SetSurfaceRLE(SDL_Surface *surface, bool enabled);
SDL_SetSurfaceRLE = libsdl3.SDL_SetSurfaceRLE
SDL_SetSurfaceRLE.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_bool]
SDL_SetSurfaceRLE.restype = ctypes.c_bool


# bool SDL_StretchSurface(SDL_Surface *src, const SDL_Rect *srcrect, SDL_Surface *dst, const SDL_Rect *dstrect, SDL_ScaleMode scaleMode);
SDL_StretchSurface = libsdl3.SDL_StretchSurface
SDL_StretchSurface.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(SDL_Surface),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_int,
]
SDL_StretchSurface.restype = ctypes.c_bool


# bool SDL_SurfaceHasAlternateImages(SDL_Surface *surface);
SDL_SurfaceHasAlternateImages = libsdl3.SDL_SurfaceHasAlternateImages
SDL_SurfaceHasAlternateImages.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_SurfaceHasAlternateImages.restype = ctypes.c_bool


# bool SDL_SurfaceHasColorKey(SDL_Surface *surface);
SDL_SurfaceHasColorKey = libsdl3.SDL_SurfaceHasColorKey
SDL_SurfaceHasColorKey.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_SurfaceHasColorKey.restype = ctypes.c_bool


# bool SDL_SurfaceHasRLE(SDL_Surface *surface);
SDL_SurfaceHasRLE = libsdl3.SDL_SurfaceHasRLE
SDL_SurfaceHasRLE.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_SurfaceHasRLE.restype = ctypes.c_bool


# void SDL_UnlockSurface(SDL_Surface *surface);
SDL_UnlockSurface = libsdl3.SDL_UnlockSurface
SDL_UnlockSurface.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_UnlockSurface.restype = None


# bool SDL_WriteSurfacePixel(SDL_Surface *surface, int x, int y, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
SDL_WriteSurfacePixel = libsdl3.SDL_WriteSurfacePixel
SDL_WriteSurfacePixel.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_WriteSurfacePixel.restype = ctypes.c_bool


# bool SDL_WriteSurfacePixelFloat(SDL_Surface *surface, int x, int y, float r, float g, float b, float a);
SDL_WriteSurfacePixelFloat = libsdl3.SDL_WriteSurfacePixelFloat
SDL_WriteSurfacePixelFloat.argtypes = [
    ctypes.POINTER(SDL_Surface),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
SDL_WriteSurfacePixelFloat.restype = ctypes.c_bool
