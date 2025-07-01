"""
SDL_render.h
2D Accelerated Rendering
Document: https://wiki.libsdl.org/SDL3/CategoryRender
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_events import SDL_Event
from sdl3_ctypes.SDL_gpu import SDL_GPUTextureSamplerBinding
from sdl3_ctypes.SDL_pixels import SDL_FColor
from sdl3_ctypes.SDL_rect import SDL_FPoint, SDL_FRect, SDL_Rect
from sdl3_ctypes.SDL_surface import SDL_Surface

# #define SDL_DEBUG_TEXT_FONT_CHARACTER_SIZE 8
SDL_DEBUG_TEXT_FONT_CHARACTER_SIZE = 8
# #define SDL_SOFTWARE_RENDERER   "software"
SDL_SOFTWARE_RENDERER = "software"


# typedef enum SDL_RendererLogicalPresentation
# {
#     SDL_LOGICAL_PRESENTATION_DISABLED,  /**< There is no logical size in effect */
#     SDL_LOGICAL_PRESENTATION_STRETCH,   /**< The rendered content is stretched to the output resolution */
#     SDL_LOGICAL_PRESENTATION_LETTERBOX, /**< The rendered content is fit to the largest dimension and the other dimension is letterboxed with black bars */
#     SDL_LOGICAL_PRESENTATION_OVERSCAN,  /**< The rendered content is fit to the smallest dimension and the other dimension extends beyond the output bounds */
#     SDL_LOGICAL_PRESENTATION_INTEGER_SCALE   /**< The rendered content is scaled up by integer multiples to fit the output resolution */
# } SDL_RendererLogicalPresentation;
SDL_LOGICAL_PRESENTATION_DISABLED = 0
SDL_LOGICAL_PRESENTATION_STRETCH = 1
SDL_LOGICAL_PRESENTATION_LETTERBOX = 2
SDL_LOGICAL_PRESENTATION_OVERSCAN = 3
SDL_LOGICAL_PRESENTATION_INTEGER_SCALE = 4
# typedef enum SDL_TextureAccess
# {
#     SDL_TEXTUREACCESS_STATIC,    /**< Changes rarely, not lockable */
#     SDL_TEXTUREACCESS_STREAMING, /**< Changes frequently, lockable */
#     SDL_TEXTUREACCESS_TARGET     /**< Texture can be used as a render target */
# } SDL_TextureAccess;
SDL_TEXTUREACCESS_STATIC = 0
SDL_TEXTUREACCESS_STREAMING = 1
SDL_TEXTUREACCESS_TARGET = 2
# typedef enum SDL_TextureAddressMode
# {
#     SDL_TEXTURE_ADDRESS_INVALID = -1,
#     SDL_TEXTURE_ADDRESS_AUTO,   /**< Wrapping is enabled if texture coordinates are outside [0, 1], this is the default */
#     SDL_TEXTURE_ADDRESS_CLAMP,  /**< Texture coordinates are clamped to the [0, 1] range */
#     SDL_TEXTURE_ADDRESS_WRAP,   /**< The texture is repeated (tiled) */
# } SDL_TextureAddressMode;
SDL_TEXTURE_ADDRESS_INVALID = -1
SDL_TEXTURE_ADDRESS_AUTO = 0
SDL_TEXTURE_ADDRESS_CLAMP = 1
SDL_TEXTURE_ADDRESS_WRAP = 2


# typedef struct SDL_GPURenderStateDesc
# {
#     Uint32 version;                 /**< the version of this interface */
#     SDL_GPUShader *fragment_shader; /**< The fragment shader to use when this render state is active */
#     Sint32 num_sampler_bindings;    /**< The number of additional fragment samplers to bind when this render state is active */
#     const SDL_GPUTextureSamplerBinding *sampler_bindings;   /**< Additional fragment samplers to bind when this render state is active */
#     Sint32 num_storage_textures;    /**< The number of storage textures to bind when this render state is active */
#     SDL_GPUTexture *const *storage_textures;    /**< Storage textures to bind when this render state is active */
#     Sint32 num_storage_buffers;    /**< The number of storage buffers to bind when this render state is active */
#     SDL_GPUBuffer *const *storage_buffers;      /**< Storage buffers to bind when this render state is active */
# } SDL_GPURenderStateDesc;
class SDL_GPURenderStateDesc(ctypes.Structure):
    _fields_ = [
        ("version", ctypes.c_uint32),
        ("fragment_shader", ctypes.c_void_p),
        ("num_sampler_bindings", ctypes.c_int32),
        ("sampler_bindings", ctypes.POINTER(SDL_GPUTextureSamplerBinding)),
        ("num_storage_textures", ctypes.c_int32),
        ("storage_textures", ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))),
        ("num_storage_buffers", ctypes.c_int32),
        ("storage_buffers", ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))),
    ]


# struct SDL_Texture
# {
#     SDL_PixelFormat format;     /**< The format of the texture, read-only */
#     int w;                      /**< The width of the texture, read-only. */
#     int h;                      /**< The height of the texture, read-only. */
#     int refcount;               /**< Application reference count, used when freeing texture */
# };
class SDL_Texture(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("refcount", ctypes.c_int),
    ]


# typedef struct SDL_Vertex
# {
#     SDL_FPoint position;        /**< Vertex position, in SDL_Renderer coordinates  */
#     SDL_FColor color;           /**< Vertex color */
#     SDL_FPoint tex_coord;       /**< Normalized texture coordinates, if needed */
# } SDL_Vertex;
class SDL_Vertex(ctypes.Structure):
    _fields_ = [
        ("position", SDL_FPoint),
        ("color", SDL_FColor),
        ("tex_coord", SDL_FPoint),
    ]


# typedef struct SDL_GPURenderState SDL_GPURenderState;
# typedef struct SDL_Renderer SDL_Renderer;


# bool SDL_AddVulkanRenderSemaphores(SDL_Renderer *renderer, Uint32 wait_stage_mask, Sint64 wait_semaphore, Sint64 signal_semaphore);
SDL_AddVulkanRenderSemaphores = libsdl3.SDL_AddVulkanRenderSemaphores
SDL_AddVulkanRenderSemaphores.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_int64,
    ctypes.c_int64,
]
SDL_AddVulkanRenderSemaphores.restype = ctypes.c_bool


# bool SDL_ConvertEventToRenderCoordinates(SDL_Renderer *renderer, SDL_Event *event);
SDL_ConvertEventToRenderCoordinates = libsdl3.SDL_ConvertEventToRenderCoordinates
SDL_ConvertEventToRenderCoordinates.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Event),
]
SDL_ConvertEventToRenderCoordinates.restype = ctypes.c_bool


# SDL_Renderer * SDL_CreateGPURenderer(SDL_Window *window, SDL_GPUShaderFormat format_flags, SDL_GPUDevice **device);
SDL_CreateGPURenderer = libsdl3.SDL_CreateGPURenderer
SDL_CreateGPURenderer.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_void_p),
]
SDL_CreateGPURenderer.restype = ctypes.c_void_p


# SDL_GPURenderState * SDL_CreateGPURenderState(SDL_Renderer *renderer, SDL_GPURenderStateDesc *desc);
SDL_CreateGPURenderState = libsdl3.SDL_CreateGPURenderState
SDL_CreateGPURenderState.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPURenderStateDesc),
]
SDL_CreateGPURenderState.restype = ctypes.c_void_p


# SDL_Renderer * SDL_CreateRenderer(SDL_Window *window, const char *name);
SDL_CreateRenderer = libsdl3.SDL_CreateRenderer
SDL_CreateRenderer.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_CreateRenderer.restype = ctypes.c_void_p


# SDL_Renderer * SDL_CreateRendererWithProperties(SDL_PropertiesID props);
SDL_CreateRendererWithProperties = libsdl3.SDL_CreateRendererWithProperties
SDL_CreateRendererWithProperties.argtypes = [ctypes.c_uint32]
SDL_CreateRendererWithProperties.restype = ctypes.c_void_p


# SDL_Renderer * SDL_CreateSoftwareRenderer(SDL_Surface *surface);
SDL_CreateSoftwareRenderer = libsdl3.SDL_CreateSoftwareRenderer
SDL_CreateSoftwareRenderer.argtypes = [ctypes.POINTER(SDL_Surface)]
SDL_CreateSoftwareRenderer.restype = ctypes.c_void_p


# SDL_Texture * SDL_CreateTexture(SDL_Renderer *renderer, SDL_PixelFormat format, SDL_TextureAccess access, int w, int h);
SDL_CreateTexture = libsdl3.SDL_CreateTexture
SDL_CreateTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_CreateTexture.restype = ctypes.POINTER(SDL_Texture)


# SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer *renderer, SDL_Surface *surface);
SDL_CreateTextureFromSurface = libsdl3.SDL_CreateTextureFromSurface
SDL_CreateTextureFromSurface.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)]
SDL_CreateTextureFromSurface.restype = ctypes.POINTER(SDL_Texture)


# SDL_Texture * SDL_CreateTextureWithProperties(SDL_Renderer *renderer, SDL_PropertiesID props);
SDL_CreateTextureWithProperties = libsdl3.SDL_CreateTextureWithProperties
SDL_CreateTextureWithProperties.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_CreateTextureWithProperties.restype = ctypes.POINTER(SDL_Texture)


# bool SDL_CreateWindowAndRenderer(const char *title, int width, int height, SDL_WindowFlags window_flags, SDL_Window **window, SDL_Renderer **renderer);
SDL_CreateWindowAndRenderer = libsdl3.SDL_CreateWindowAndRenderer
SDL_CreateWindowAndRenderer.argtypes = [
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint64,
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.POINTER(ctypes.c_void_p),
]
SDL_CreateWindowAndRenderer.restype = ctypes.c_bool


# void SDL_DestroyGPURenderState(SDL_GPURenderState *state);
SDL_DestroyGPURenderState = libsdl3.SDL_DestroyGPURenderState
SDL_DestroyGPURenderState.argtypes = [ctypes.c_void_p]
SDL_DestroyGPURenderState.restype = None


# void SDL_DestroyRenderer(SDL_Renderer *renderer);
SDL_DestroyRenderer = libsdl3.SDL_DestroyRenderer
SDL_DestroyRenderer.argtypes = [ctypes.c_void_p]
SDL_DestroyRenderer.restype = None


# void SDL_DestroyTexture(SDL_Texture *texture);
SDL_DestroyTexture = libsdl3.SDL_DestroyTexture
SDL_DestroyTexture.argtypes = [ctypes.POINTER(SDL_Texture)]
SDL_DestroyTexture.restype = None


# bool SDL_FlushRenderer(SDL_Renderer *renderer);
SDL_FlushRenderer = libsdl3.SDL_FlushRenderer
SDL_FlushRenderer.argtypes = [ctypes.c_void_p]
SDL_FlushRenderer.restype = ctypes.c_bool


# bool SDL_GetCurrentRenderOutputSize(SDL_Renderer *renderer, int *w, int *h);
SDL_GetCurrentRenderOutputSize = libsdl3.SDL_GetCurrentRenderOutputSize
SDL_GetCurrentRenderOutputSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetCurrentRenderOutputSize.restype = ctypes.c_bool


# bool SDL_GetDefaultTextureScaleMode(SDL_Renderer *renderer, SDL_ScaleMode *scale_mode);
SDL_GetDefaultTextureScaleMode = libsdl3.SDL_GetDefaultTextureScaleMode
SDL_GetDefaultTextureScaleMode.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetDefaultTextureScaleMode.restype = ctypes.c_bool


# int SDL_GetNumRenderDrivers(void);
SDL_GetNumRenderDrivers = libsdl3.SDL_GetNumRenderDrivers
SDL_GetNumRenderDrivers.argtypes = []
SDL_GetNumRenderDrivers.restype = ctypes.c_int


# bool SDL_GetRenderClipRect(SDL_Renderer *renderer, SDL_Rect *rect);
SDL_GetRenderClipRect = libsdl3.SDL_GetRenderClipRect
SDL_GetRenderClipRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_GetRenderClipRect.restype = ctypes.c_bool


# bool SDL_GetRenderColorScale(SDL_Renderer *renderer, float *scale);
SDL_GetRenderColorScale = libsdl3.SDL_GetRenderColorScale
SDL_GetRenderColorScale.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float)]
SDL_GetRenderColorScale.restype = ctypes.c_bool


# bool SDL_GetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode *blendMode);
SDL_GetRenderDrawBlendMode = libsdl3.SDL_GetRenderDrawBlendMode
SDL_GetRenderDrawBlendMode.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
SDL_GetRenderDrawBlendMode.restype = ctypes.c_bool


# bool SDL_GetRenderDrawColor(SDL_Renderer *renderer, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
SDL_GetRenderDrawColor = libsdl3.SDL_GetRenderDrawColor
SDL_GetRenderDrawColor.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_GetRenderDrawColor.restype = ctypes.c_bool


# bool SDL_GetRenderDrawColorFloat(SDL_Renderer *renderer, float *r, float *g, float *b, float *a);
SDL_GetRenderDrawColorFloat = libsdl3.SDL_GetRenderDrawColorFloat
SDL_GetRenderDrawColorFloat.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetRenderDrawColorFloat.restype = ctypes.c_bool


# const char * SDL_GetRenderDriver(int index);
SDL_GetRenderDriver = libsdl3.SDL_GetRenderDriver
SDL_GetRenderDriver.argtypes = [ctypes.c_int]
SDL_GetRenderDriver.restype = ctypes.c_char_p


# SDL_Renderer * SDL_GetRenderer(SDL_Window *window);
SDL_GetRenderer = libsdl3.SDL_GetRenderer
SDL_GetRenderer.argtypes = [ctypes.c_void_p]
SDL_GetRenderer.restype = ctypes.c_void_p


# SDL_Renderer * SDL_GetRendererFromTexture(SDL_Texture *texture);
SDL_GetRendererFromTexture = libsdl3.SDL_GetRendererFromTexture
SDL_GetRendererFromTexture.argtypes = [ctypes.POINTER(SDL_Texture)]
SDL_GetRendererFromTexture.restype = ctypes.c_void_p


# const char * SDL_GetRendererName(SDL_Renderer *renderer);
SDL_GetRendererName = libsdl3.SDL_GetRendererName
SDL_GetRendererName.argtypes = [ctypes.c_void_p]
SDL_GetRendererName.restype = ctypes.c_char_p


# SDL_PropertiesID SDL_GetRendererProperties(SDL_Renderer *renderer);
SDL_GetRendererProperties = libsdl3.SDL_GetRendererProperties
SDL_GetRendererProperties.argtypes = [ctypes.c_void_p]
SDL_GetRendererProperties.restype = ctypes.c_uint32


# bool SDL_GetRenderLogicalPresentation(SDL_Renderer *renderer, int *w, int *h, SDL_RendererLogicalPresentation *mode);
SDL_GetRenderLogicalPresentation = libsdl3.SDL_GetRenderLogicalPresentation
SDL_GetRenderLogicalPresentation.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetRenderLogicalPresentation.restype = ctypes.c_bool


# bool SDL_GetRenderLogicalPresentationRect(SDL_Renderer *renderer, SDL_FRect *rect);
SDL_GetRenderLogicalPresentationRect = libsdl3.SDL_GetRenderLogicalPresentationRect
SDL_GetRenderLogicalPresentationRect.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_FRect),
]
SDL_GetRenderLogicalPresentationRect.restype = ctypes.c_bool


# void * SDL_GetRenderMetalCommandEncoder(SDL_Renderer *renderer);
SDL_GetRenderMetalCommandEncoder = libsdl3.SDL_GetRenderMetalCommandEncoder
SDL_GetRenderMetalCommandEncoder.argtypes = [ctypes.c_void_p]
SDL_GetRenderMetalCommandEncoder.restype = ctypes.c_void_p


# void * SDL_GetRenderMetalLayer(SDL_Renderer *renderer);
SDL_GetRenderMetalLayer = libsdl3.SDL_GetRenderMetalLayer
SDL_GetRenderMetalLayer.argtypes = [ctypes.c_void_p]
SDL_GetRenderMetalLayer.restype = ctypes.c_void_p


# bool SDL_GetRenderOutputSize(SDL_Renderer *renderer, int *w, int *h);
SDL_GetRenderOutputSize = libsdl3.SDL_GetRenderOutputSize
SDL_GetRenderOutputSize.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetRenderOutputSize.restype = ctypes.c_bool


# bool SDL_GetRenderSafeArea(SDL_Renderer *renderer, SDL_Rect *rect);
SDL_GetRenderSafeArea = libsdl3.SDL_GetRenderSafeArea
SDL_GetRenderSafeArea.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_GetRenderSafeArea.restype = ctypes.c_bool


# bool SDL_GetRenderScale(SDL_Renderer *renderer, float *scaleX, float *scaleY);
SDL_GetRenderScale = libsdl3.SDL_GetRenderScale
SDL_GetRenderScale.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetRenderScale.restype = ctypes.c_bool


# SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *renderer);
SDL_GetRenderTarget = libsdl3.SDL_GetRenderTarget
SDL_GetRenderTarget.argtypes = [ctypes.c_void_p]
SDL_GetRenderTarget.restype = ctypes.POINTER(SDL_Texture)


# bool SDL_GetRenderTextureAddressMode(SDL_Renderer *renderer, SDL_TextureAddressMode *u_mode, SDL_TextureAddressMode *v_mode);
SDL_GetRenderTextureAddressMode = libsdl3.SDL_GetRenderTextureAddressMode
SDL_GetRenderTextureAddressMode.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetRenderTextureAddressMode.restype = ctypes.c_bool


# bool SDL_GetRenderViewport(SDL_Renderer *renderer, SDL_Rect *rect);
SDL_GetRenderViewport = libsdl3.SDL_GetRenderViewport
SDL_GetRenderViewport.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_GetRenderViewport.restype = ctypes.c_bool


# bool SDL_GetRenderVSync(SDL_Renderer *renderer, int *vsync);
SDL_GetRenderVSync = libsdl3.SDL_GetRenderVSync
SDL_GetRenderVSync.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_GetRenderVSync.restype = ctypes.c_bool


# SDL_Window * SDL_GetRenderWindow(SDL_Renderer *renderer);
SDL_GetRenderWindow = libsdl3.SDL_GetRenderWindow
SDL_GetRenderWindow.argtypes = [ctypes.c_void_p]
SDL_GetRenderWindow.restype = ctypes.c_void_p


# bool SDL_GetTextureAlphaMod(SDL_Texture *texture, Uint8 *alpha);
SDL_GetTextureAlphaMod = libsdl3.SDL_GetTextureAlphaMod
SDL_GetTextureAlphaMod.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_GetTextureAlphaMod.restype = ctypes.c_bool


# bool SDL_GetTextureAlphaModFloat(SDL_Texture *texture, float *alpha);
SDL_GetTextureAlphaModFloat = libsdl3.SDL_GetTextureAlphaModFloat
SDL_GetTextureAlphaModFloat.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetTextureAlphaModFloat.restype = ctypes.c_bool


# bool SDL_GetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode *blendMode);
SDL_GetTextureBlendMode = libsdl3.SDL_GetTextureBlendMode
SDL_GetTextureBlendMode.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_GetTextureBlendMode.restype = ctypes.c_bool


# bool SDL_GetTextureColorMod(SDL_Texture *texture, Uint8 *r, Uint8 *g, Uint8 *b);
SDL_GetTextureColorMod = libsdl3.SDL_GetTextureColorMod
SDL_GetTextureColorMod.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8),
]
SDL_GetTextureColorMod.restype = ctypes.c_bool


# bool SDL_GetTextureColorModFloat(SDL_Texture *texture, float *r, float *g, float *b);
SDL_GetTextureColorModFloat = libsdl3.SDL_GetTextureColorModFloat
SDL_GetTextureColorModFloat.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetTextureColorModFloat.restype = ctypes.c_bool


# SDL_PropertiesID SDL_GetTextureProperties(SDL_Texture *texture);
SDL_GetTextureProperties = libsdl3.SDL_GetTextureProperties
SDL_GetTextureProperties.argtypes = [ctypes.POINTER(SDL_Texture)]
SDL_GetTextureProperties.restype = ctypes.c_uint32


# bool SDL_GetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode *scaleMode);
SDL_GetTextureScaleMode = libsdl3.SDL_GetTextureScaleMode
SDL_GetTextureScaleMode.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_int),
]
SDL_GetTextureScaleMode.restype = ctypes.c_bool


# bool SDL_GetTextureSize(SDL_Texture *texture, float *w, float *h);
SDL_GetTextureSize = libsdl3.SDL_GetTextureSize
SDL_GetTextureSize.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_GetTextureSize.restype = ctypes.c_bool


# bool SDL_LockTexture(SDL_Texture *texture,
#                 const SDL_Rect *rect,
#                 void **pixels, int *pitch);
SDL_LockTexture = libsdl3.SDL_LockTexture
SDL_LockTexture.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.POINTER(ctypes.c_int),
]
SDL_LockTexture.restype = ctypes.c_bool


# bool SDL_LockTextureToSurface(SDL_Texture *texture, const SDL_Rect *rect, SDL_Surface **surface);
SDL_LockTextureToSurface = libsdl3.SDL_LockTextureToSurface
SDL_LockTextureToSurface.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.POINTER(SDL_Surface)),
]
SDL_LockTextureToSurface.restype = ctypes.c_bool


# bool SDL_RenderClear(SDL_Renderer *renderer);
SDL_RenderClear = libsdl3.SDL_RenderClear
SDL_RenderClear.argtypes = [ctypes.c_void_p]
SDL_RenderClear.restype = ctypes.c_bool


# bool SDL_RenderClipEnabled(SDL_Renderer *renderer);
SDL_RenderClipEnabled = libsdl3.SDL_RenderClipEnabled
SDL_RenderClipEnabled.argtypes = [ctypes.c_void_p]
SDL_RenderClipEnabled.restype = ctypes.c_bool


# bool SDL_RenderCoordinatesFromWindow(SDL_Renderer *renderer, float window_x, float window_y, float *x, float *y);
SDL_RenderCoordinatesFromWindow = libsdl3.SDL_RenderCoordinatesFromWindow
SDL_RenderCoordinatesFromWindow.argtypes = [
    ctypes.c_void_p,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_RenderCoordinatesFromWindow.restype = ctypes.c_bool


# bool SDL_RenderCoordinatesToWindow(SDL_Renderer *renderer, float x, float y, float *window_x, float *window_y);
SDL_RenderCoordinatesToWindow = libsdl3.SDL_RenderCoordinatesToWindow
SDL_RenderCoordinatesToWindow.argtypes = [
    ctypes.c_void_p,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
SDL_RenderCoordinatesToWindow.restype = ctypes.c_bool


# bool SDL_RenderDebugText(SDL_Renderer *renderer, float x, float y, const char *str);
SDL_RenderDebugText = libsdl3.SDL_RenderDebugText
SDL_RenderDebugText.argtypes = [
    ctypes.c_void_p,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_char_p,
]
SDL_RenderDebugText.restype = ctypes.c_bool

# bool SDL_RenderDebugTextFormat(SDL_Renderer *renderer, float x, float y, const char *fmt, ...);

# bool SDL_RenderFillRect(SDL_Renderer *renderer, const SDL_FRect *rect);
SDL_RenderFillRect = libsdl3.SDL_RenderFillRect
SDL_RenderFillRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_FRect)]
SDL_RenderFillRect.restype = ctypes.c_bool


# bool SDL_RenderFillRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count);
SDL_RenderFillRects = libsdl3.SDL_RenderFillRects
SDL_RenderFillRects.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_FRect),
    ctypes.c_int,
]
SDL_RenderFillRects.restype = ctypes.c_bool


# bool SDL_RenderGeometry(SDL_Renderer *renderer,
#                    SDL_Texture *texture,
#                    const SDL_Vertex *vertices, int num_vertices,
#                    const int *indices, int num_indices);
SDL_RenderGeometry = libsdl3.SDL_RenderGeometry
SDL_RenderGeometry.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Vertex),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
SDL_RenderGeometry.restype = ctypes.c_bool


# bool SDL_RenderGeometryRaw(SDL_Renderer *renderer,
#                    SDL_Texture *texture,
#                    const float *xy, int xy_stride,
#                    const SDL_FColor *color, int color_stride,
#                    const float *uv, int uv_stride,
#                    int num_vertices,
#                    const void *indices, int num_indices, int size_indices);
SDL_RenderGeometryRaw = libsdl3.SDL_RenderGeometryRaw
SDL_RenderGeometryRaw.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
    ctypes.POINTER(SDL_FColor),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_RenderGeometryRaw.restype = ctypes.c_bool


# bool SDL_RenderLine(SDL_Renderer *renderer, float x1, float y1, float x2, float y2);
SDL_RenderLine = libsdl3.SDL_RenderLine
SDL_RenderLine.argtypes = [
    ctypes.c_void_p,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
SDL_RenderLine.restype = ctypes.c_bool


# bool SDL_RenderLines(SDL_Renderer *renderer, const SDL_FPoint *points, int count);
SDL_RenderLines = libsdl3.SDL_RenderLines
SDL_RenderLines.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_FPoint), ctypes.c_int]
SDL_RenderLines.restype = ctypes.c_bool


# bool SDL_RenderPoint(SDL_Renderer *renderer, float x, float y);
SDL_RenderPoint = libsdl3.SDL_RenderPoint
SDL_RenderPoint.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float]
SDL_RenderPoint.restype = ctypes.c_bool


# bool SDL_RenderPoints(SDL_Renderer *renderer, const SDL_FPoint *points, int count);
SDL_RenderPoints = libsdl3.SDL_RenderPoints
SDL_RenderPoints.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_FPoint), ctypes.c_int]
SDL_RenderPoints.restype = ctypes.c_bool


# bool SDL_RenderPresent(SDL_Renderer *renderer);
SDL_RenderPresent = libsdl3.SDL_RenderPresent
SDL_RenderPresent.argtypes = [ctypes.c_void_p]
SDL_RenderPresent.restype = ctypes.c_bool


# SDL_Surface * SDL_RenderReadPixels(SDL_Renderer *renderer, const SDL_Rect *rect);
SDL_RenderReadPixels = libsdl3.SDL_RenderReadPixels
SDL_RenderReadPixels.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_RenderReadPixels.restype = ctypes.POINTER(SDL_Surface)


# bool SDL_RenderRect(SDL_Renderer *renderer, const SDL_FRect *rect);
SDL_RenderRect = libsdl3.SDL_RenderRect
SDL_RenderRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_FRect)]
SDL_RenderRect.restype = ctypes.c_bool


# bool SDL_RenderRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count);
SDL_RenderRects = libsdl3.SDL_RenderRects
SDL_RenderRects.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_FRect), ctypes.c_int]
SDL_RenderRects.restype = ctypes.c_bool


# bool SDL_RenderTexture(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, const SDL_FRect *dstrect);
SDL_RenderTexture = libsdl3.SDL_RenderTexture
SDL_RenderTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
]
SDL_RenderTexture.restype = ctypes.c_bool


# bool SDL_RenderTexture9Grid(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, float left_width, float right_width, float top_height, float bottom_height, float scale, const SDL_FRect *dstrect);
SDL_RenderTexture9Grid = libsdl3.SDL_RenderTexture9Grid
SDL_RenderTexture9Grid.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(SDL_FRect),
]
SDL_RenderTexture9Grid.restype = ctypes.c_bool


# bool SDL_RenderTexture9GridTiled(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, float left_width, float right_width, float top_height, float bottom_height, float scale, const SDL_FRect *dstrect, float tileScale);
SDL_RenderTexture9GridTiled = libsdl3.SDL_RenderTexture9GridTiled
SDL_RenderTexture9GridTiled.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(SDL_FRect),
    ctypes.c_float,
]
SDL_RenderTexture9GridTiled.restype = ctypes.c_bool


# bool SDL_RenderTextureAffine(SDL_Renderer *renderer, SDL_Texture *texture,
#                          const SDL_FRect *srcrect, const SDL_FPoint *origin,
#                          const SDL_FPoint *right, const SDL_FPoint *down);
SDL_RenderTextureAffine = libsdl3.SDL_RenderTextureAffine
SDL_RenderTextureAffine.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FPoint),
    ctypes.POINTER(SDL_FPoint),
    ctypes.POINTER(SDL_FPoint),
]
SDL_RenderTextureAffine.restype = ctypes.c_bool


# bool SDL_RenderTextureRotated(SDL_Renderer *renderer, SDL_Texture *texture,
#                          const SDL_FRect *srcrect, const SDL_FRect *dstrect,
#                          double angle, const SDL_FPoint *center,
#                          SDL_FlipMode flip);
SDL_RenderTextureRotated = libsdl3.SDL_RenderTextureRotated
SDL_RenderTextureRotated.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.POINTER(SDL_FRect),
    ctypes.c_double,
    ctypes.POINTER(SDL_FPoint),
    ctypes.c_int,
]
SDL_RenderTextureRotated.restype = ctypes.c_bool


# bool SDL_RenderTextureTiled(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, float scale, const SDL_FRect *dstrect);
SDL_RenderTextureTiled = libsdl3.SDL_RenderTextureTiled
SDL_RenderTextureTiled.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_FRect),
    ctypes.c_float,
    ctypes.POINTER(SDL_FRect),
]
SDL_RenderTextureTiled.restype = ctypes.c_bool


# bool SDL_RenderViewportSet(SDL_Renderer *renderer);
SDL_RenderViewportSet = libsdl3.SDL_RenderViewportSet
SDL_RenderViewportSet.argtypes = [ctypes.c_void_p]
SDL_RenderViewportSet.restype = ctypes.c_bool


# bool SDL_SetDefaultTextureScaleMode(SDL_Renderer *renderer, SDL_ScaleMode scale_mode);
SDL_SetDefaultTextureScaleMode = libsdl3.SDL_SetDefaultTextureScaleMode
SDL_SetDefaultTextureScaleMode.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_SetDefaultTextureScaleMode.restype = ctypes.c_bool


# bool SDL_SetGPURenderStateFragmentUniforms(SDL_GPURenderState *state, Uint32 slot_index, const void *data, Uint32 length);
SDL_SetGPURenderStateFragmentUniforms = libsdl3.SDL_SetGPURenderStateFragmentUniforms
SDL_SetGPURenderStateFragmentUniforms.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_SetGPURenderStateFragmentUniforms.restype = ctypes.c_bool


# bool SDL_SetRenderClipRect(SDL_Renderer *renderer, const SDL_Rect *rect);
SDL_SetRenderClipRect = libsdl3.SDL_SetRenderClipRect
SDL_SetRenderClipRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_SetRenderClipRect.restype = ctypes.c_bool


# bool SDL_SetRenderColorScale(SDL_Renderer *renderer, float scale);
SDL_SetRenderColorScale = libsdl3.SDL_SetRenderColorScale
SDL_SetRenderColorScale.argtypes = [ctypes.c_void_p, ctypes.c_float]
SDL_SetRenderColorScale.restype = ctypes.c_bool


# bool SDL_SetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode blendMode);
SDL_SetRenderDrawBlendMode = libsdl3.SDL_SetRenderDrawBlendMode
SDL_SetRenderDrawBlendMode.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_SetRenderDrawBlendMode.restype = ctypes.c_bool


# bool SDL_SetRenderDrawColor(SDL_Renderer *renderer, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
SDL_SetRenderDrawColor = libsdl3.SDL_SetRenderDrawColor
SDL_SetRenderDrawColor.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_SetRenderDrawColor.restype = ctypes.c_bool


# bool SDL_SetRenderDrawColorFloat(SDL_Renderer *renderer, float r, float g, float b, float a);
SDL_SetRenderDrawColorFloat = libsdl3.SDL_SetRenderDrawColorFloat
SDL_SetRenderDrawColorFloat.argtypes = [
    ctypes.c_void_p,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
SDL_SetRenderDrawColorFloat.restype = ctypes.c_bool


# bool SDL_SetRenderGPUState(SDL_Renderer *renderer, SDL_GPURenderState *state);
SDL_SetRenderGPUState = libsdl3.SDL_SetRenderGPUState
SDL_SetRenderGPUState.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_SetRenderGPUState.restype = ctypes.c_bool


# bool SDL_SetRenderLogicalPresentation(SDL_Renderer *renderer, int w, int h, SDL_RendererLogicalPresentation mode);
SDL_SetRenderLogicalPresentation = libsdl3.SDL_SetRenderLogicalPresentation
SDL_SetRenderLogicalPresentation.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_SetRenderLogicalPresentation.restype = ctypes.c_bool


# bool SDL_SetRenderScale(SDL_Renderer *renderer, float scaleX, float scaleY);
SDL_SetRenderScale = libsdl3.SDL_SetRenderScale
SDL_SetRenderScale.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float]
SDL_SetRenderScale.restype = ctypes.c_bool


# bool SDL_SetRenderTarget(SDL_Renderer *renderer, SDL_Texture *texture);
SDL_SetRenderTarget = libsdl3.SDL_SetRenderTarget
SDL_SetRenderTarget.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Texture)]
SDL_SetRenderTarget.restype = ctypes.c_bool


# bool SDL_SetRenderTextureAddressMode(SDL_Renderer *renderer, SDL_TextureAddressMode u_mode, SDL_TextureAddressMode v_mode);
SDL_SetRenderTextureAddressMode = libsdl3.SDL_SetRenderTextureAddressMode
SDL_SetRenderTextureAddressMode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
SDL_SetRenderTextureAddressMode.restype = ctypes.c_bool


# bool SDL_SetRenderViewport(SDL_Renderer *renderer, const SDL_Rect *rect);
SDL_SetRenderViewport = libsdl3.SDL_SetRenderViewport
SDL_SetRenderViewport.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_SetRenderViewport.restype = ctypes.c_bool


# bool SDL_SetRenderVSync(SDL_Renderer *renderer, int vsync);
# #define SDL_RENDERER_VSYNC_DISABLED 0
# #define SDL_RENDERER_VSYNC_ADAPTIVE (-1)
SDL_SetRenderVSync = libsdl3.SDL_SetRenderVSync
SDL_SetRenderVSync.argtypes = [ctypes.c_void_p, ctypes.c_int]
SDL_SetRenderVSync.restype = ctypes.c_bool


# bool SDL_SetTextureAlphaMod(SDL_Texture *texture, Uint8 alpha);
SDL_SetTextureAlphaMod = libsdl3.SDL_SetTextureAlphaMod
SDL_SetTextureAlphaMod.argtypes = [ctypes.POINTER(SDL_Texture), ctypes.c_uint8]
SDL_SetTextureAlphaMod.restype = ctypes.c_bool


# bool SDL_SetTextureAlphaModFloat(SDL_Texture *texture, float alpha);
SDL_SetTextureAlphaModFloat = libsdl3.SDL_SetTextureAlphaModFloat
SDL_SetTextureAlphaModFloat.argtypes = [ctypes.POINTER(SDL_Texture), ctypes.c_float]
SDL_SetTextureAlphaModFloat.restype = ctypes.c_bool


# bool SDL_SetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode blendMode);
SDL_SetTextureBlendMode = libsdl3.SDL_SetTextureBlendMode
SDL_SetTextureBlendMode.argtypes = [ctypes.POINTER(SDL_Texture), ctypes.c_uint32]
SDL_SetTextureBlendMode.restype = ctypes.c_bool


# bool SDL_SetTextureColorMod(SDL_Texture *texture, Uint8 r, Uint8 g, Uint8 b);
SDL_SetTextureColorMod = libsdl3.SDL_SetTextureColorMod
SDL_SetTextureColorMod.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.c_uint8,
    ctypes.c_uint8,
    ctypes.c_uint8,
]
SDL_SetTextureColorMod.restype = ctypes.c_bool


# bool SDL_SetTextureColorModFloat(SDL_Texture *texture, float r, float g, float b);
SDL_SetTextureColorModFloat = libsdl3.SDL_SetTextureColorModFloat
SDL_SetTextureColorModFloat.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
SDL_SetTextureColorModFloat.restype = ctypes.c_bool


# bool SDL_SetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode scaleMode);
SDL_SetTextureScaleMode = libsdl3.SDL_SetTextureScaleMode
SDL_SetTextureScaleMode.argtypes = [ctypes.POINTER(SDL_Texture), ctypes.c_int]
SDL_SetTextureScaleMode.restype = ctypes.c_bool


# void SDL_UnlockTexture(SDL_Texture *texture);
SDL_UnlockTexture = libsdl3.SDL_UnlockTexture
SDL_UnlockTexture.argtypes = [ctypes.POINTER(SDL_Texture)]
SDL_UnlockTexture.restype = None


# bool SDL_UpdateNVTexture(SDL_Texture *texture,
#                      const SDL_Rect *rect,
#                      const Uint8 *Yplane, int Ypitch,
#                      const Uint8 *UVplane, int UVpitch);
SDL_UpdateNVTexture = libsdl3.SDL_UpdateNVTexture
SDL_UpdateNVTexture.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
]
SDL_UpdateNVTexture.restype = ctypes.c_bool


# bool SDL_UpdateTexture(SDL_Texture *texture, const SDL_Rect *rect, const void *pixels, int pitch);
SDL_UpdateTexture = libsdl3.SDL_UpdateTexture
SDL_UpdateTexture.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Rect),
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_UpdateTexture.restype = ctypes.c_bool


# bool SDL_UpdateYUVTexture(SDL_Texture *texture,
#                      const SDL_Rect *rect,
#                      const Uint8 *Yplane, int Ypitch,
#                      const Uint8 *Uplane, int Upitch,
#                      const Uint8 *Vplane, int Vpitch);
SDL_UpdateYUVTexture = libsdl3.SDL_UpdateYUVTexture
SDL_UpdateYUVTexture.argtypes = [
    ctypes.POINTER(SDL_Texture),
    ctypes.POINTER(SDL_Rect),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.c_int,
]
SDL_UpdateYUVTexture.restype = ctypes.c_bool
