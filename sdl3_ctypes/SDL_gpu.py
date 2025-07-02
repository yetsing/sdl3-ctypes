"""
SDL_gpu.h
3D Rendering and GPU Compute
Document: https://wiki.libsdl.org/SDL3/CategoryGPU
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_pixels import SDL_FColor
from sdl3_ctypes.SDL_rect import SDL_Rect

# typedef enum SDL_GPUBlendFactor
# {
#     SDL_GPU_BLENDFACTOR_INVALID,
#     SDL_GPU_BLENDFACTOR_ZERO,                      /**< 0 */
#     SDL_GPU_BLENDFACTOR_ONE,                       /**< 1 */
#     SDL_GPU_BLENDFACTOR_SRC_COLOR,                 /**< source color */
#     SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_COLOR,       /**< 1 - source color */
#     SDL_GPU_BLENDFACTOR_DST_COLOR,                 /**< destination color */
#     SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_COLOR,       /**< 1 - destination color */
#     SDL_GPU_BLENDFACTOR_SRC_ALPHA,                 /**< source alpha */
#     SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_ALPHA,       /**< 1 - source alpha */
#     SDL_GPU_BLENDFACTOR_DST_ALPHA,                 /**< destination alpha */
#     SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_ALPHA,       /**< 1 - destination alpha */
#     SDL_GPU_BLENDFACTOR_CONSTANT_COLOR,            /**< blend constant */
#     SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR,  /**< 1 - blend constant */
#     SDL_GPU_BLENDFACTOR_SRC_ALPHA_SATURATE         /**< min(source alpha, 1 - destination alpha) */
# } SDL_GPUBlendFactor;
SDL_GPU_BLENDFACTOR_INVALID = 0
SDL_GPU_BLENDFACTOR_ZERO = 1
SDL_GPU_BLENDFACTOR_ONE = 2
SDL_GPU_BLENDFACTOR_SRC_COLOR = 3
SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_COLOR = 4
SDL_GPU_BLENDFACTOR_DST_COLOR = 5
SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_COLOR = 6
SDL_GPU_BLENDFACTOR_SRC_ALPHA = 7
SDL_GPU_BLENDFACTOR_ONE_MINUS_SRC_ALPHA = 8
SDL_GPU_BLENDFACTOR_DST_ALPHA = 9
SDL_GPU_BLENDFACTOR_ONE_MINUS_DST_ALPHA = 10
SDL_GPU_BLENDFACTOR_CONSTANT_COLOR = 11
SDL_GPU_BLENDFACTOR_ONE_MINUS_CONSTANT_COLOR = 12
SDL_GPU_BLENDFACTOR_SRC_ALPHA_SATURATE = 13
# typedef enum SDL_GPUBlendOp
# {
#     SDL_GPU_BLENDOP_INVALID,
#     SDL_GPU_BLENDOP_ADD,               /**< (source * source_factor) + (destination * destination_factor) */
#     SDL_GPU_BLENDOP_SUBTRACT,          /**< (source * source_factor) - (destination * destination_factor) */
#     SDL_GPU_BLENDOP_REVERSE_SUBTRACT,  /**< (destination * destination_factor) - (source * source_factor) */
#     SDL_GPU_BLENDOP_MIN,               /**< min(source, destination) */
#     SDL_GPU_BLENDOP_MAX                /**< max(source, destination) */
# } SDL_GPUBlendOp;
SDL_GPU_BLENDOP_INVALID = 0
SDL_GPU_BLENDOP_ADD = 1
SDL_GPU_BLENDOP_SUBTRACT = 2
SDL_GPU_BLENDOP_REVERSE_SUBTRACT = 3
SDL_GPU_BLENDOP_MIN = 4
SDL_GPU_BLENDOP_MAX = 5
# typedef enum SDL_GPUCompareOp
# {
#     SDL_GPU_COMPAREOP_INVALID,
#     SDL_GPU_COMPAREOP_NEVER,             /**< The comparison always evaluates false. */
#     SDL_GPU_COMPAREOP_LESS,              /**< The comparison evaluates reference < test. */
#     SDL_GPU_COMPAREOP_EQUAL,             /**< The comparison evaluates reference == test. */
#     SDL_GPU_COMPAREOP_LESS_OR_EQUAL,     /**< The comparison evaluates reference <= test. */
#     SDL_GPU_COMPAREOP_GREATER,           /**< The comparison evaluates reference > test. */
#     SDL_GPU_COMPAREOP_NOT_EQUAL,         /**< The comparison evaluates reference != test. */
#     SDL_GPU_COMPAREOP_GREATER_OR_EQUAL,  /**< The comparison evalutes reference >= test. */
#     SDL_GPU_COMPAREOP_ALWAYS             /**< The comparison always evaluates true. */
# } SDL_GPUCompareOp;
SDL_GPU_COMPAREOP_INVALID = 0
SDL_GPU_COMPAREOP_NEVER = 1
SDL_GPU_COMPAREOP_LESS = 2
SDL_GPU_COMPAREOP_EQUAL = 3
SDL_GPU_COMPAREOP_LESS_OR_EQUAL = 4
SDL_GPU_COMPAREOP_GREATER = 5
SDL_GPU_COMPAREOP_NOT_EQUAL = 6
SDL_GPU_COMPAREOP_GREATER_OR_EQUAL = 7
SDL_GPU_COMPAREOP_ALWAYS = 8
# typedef enum SDL_GPUCubeMapFace
# {
#     SDL_GPU_CUBEMAPFACE_POSITIVEX,
#     SDL_GPU_CUBEMAPFACE_NEGATIVEX,
#     SDL_GPU_CUBEMAPFACE_POSITIVEY,
#     SDL_GPU_CUBEMAPFACE_NEGATIVEY,
#     SDL_GPU_CUBEMAPFACE_POSITIVEZ,
#     SDL_GPU_CUBEMAPFACE_NEGATIVEZ
# } SDL_GPUCubeMapFace;
SDL_GPU_CUBEMAPFACE_POSITIVEX = 0
SDL_GPU_CUBEMAPFACE_NEGATIVEX = 1
SDL_GPU_CUBEMAPFACE_POSITIVEY = 2
SDL_GPU_CUBEMAPFACE_NEGATIVEY = 3
SDL_GPU_CUBEMAPFACE_POSITIVEZ = 4
SDL_GPU_CUBEMAPFACE_NEGATIVEZ = 5
# typedef enum SDL_GPUCullMode
# {
#     SDL_GPU_CULLMODE_NONE,   /**< No triangles are culled. */
#     SDL_GPU_CULLMODE_FRONT,  /**< Front-facing triangles are culled. */
#     SDL_GPU_CULLMODE_BACK    /**< Back-facing triangles are culled. */
# } SDL_GPUCullMode;
SDL_GPU_CULLMODE_NONE = 0
SDL_GPU_CULLMODE_FRONT = 1
SDL_GPU_CULLMODE_BACK = 2
# typedef enum SDL_GPUFillMode
# {
#     SDL_GPU_FILLMODE_FILL,  /**< Polygons will be rendered via rasterization. */
#     SDL_GPU_FILLMODE_LINE   /**< Polygon edges will be drawn as line segments. */
# } SDL_GPUFillMode;
SDL_GPU_FILLMODE_FILL = 0
SDL_GPU_FILLMODE_LINE = 1
# typedef enum SDL_GPUFilter
# {
#     SDL_GPU_FILTER_NEAREST,  /**< Point filtering. */
#     SDL_GPU_FILTER_LINEAR    /**< Linear filtering. */
# } SDL_GPUFilter;
SDL_GPU_FILTER_NEAREST = 0
SDL_GPU_FILTER_LINEAR = 1
# typedef enum SDL_GPUFrontFace
# {
#     SDL_GPU_FRONTFACE_COUNTER_CLOCKWISE,  /**< A triangle with counter-clockwise vertex winding will be considered front-facing. */
#     SDL_GPU_FRONTFACE_CLOCKWISE           /**< A triangle with clockwise vertex winding will be considered front-facing. */
# } SDL_GPUFrontFace;
SDL_GPU_FRONTFACE_COUNTER_CLOCKWISE = 0
SDL_GPU_FRONTFACE_CLOCKWISE = 1
# typedef enum SDL_GPUIndexElementSize
# {
#     SDL_GPU_INDEXELEMENTSIZE_16BIT, /**< The index elements are 16-bit. */
#     SDL_GPU_INDEXELEMENTSIZE_32BIT  /**< The index elements are 32-bit. */
# } SDL_GPUIndexElementSize;
SDL_GPU_INDEXELEMENTSIZE_16BIT = 0
SDL_GPU_INDEXELEMENTSIZE_32BIT = 1
# typedef enum SDL_GPULoadOp
# {
#     SDL_GPU_LOADOP_LOAD,      /**< The previous contents of the texture will be preserved. */
#     SDL_GPU_LOADOP_CLEAR,     /**< The contents of the texture will be cleared to a color. */
#     SDL_GPU_LOADOP_DONT_CARE  /**< The previous contents of the texture need not be preserved. The contents will be undefined. */
# } SDL_GPULoadOp;
SDL_GPU_LOADOP_LOAD = 0
SDL_GPU_LOADOP_CLEAR = 1
SDL_GPU_LOADOP_DONT_CARE = 2
# typedef enum SDL_GPUPresentMode
# {
#     SDL_GPU_PRESENTMODE_VSYNC,
#     SDL_GPU_PRESENTMODE_IMMEDIATE,
#     SDL_GPU_PRESENTMODE_MAILBOX
# } SDL_GPUPresentMode;
SDL_GPU_PRESENTMODE_VSYNC = 0
SDL_GPU_PRESENTMODE_IMMEDIATE = 1
SDL_GPU_PRESENTMODE_MAILBOX = 2
# typedef enum SDL_GPUPrimitiveType
# {
#     SDL_GPU_PRIMITIVETYPE_TRIANGLELIST,  /**< A series of separate triangles. */
#     SDL_GPU_PRIMITIVETYPE_TRIANGLESTRIP, /**< A series of connected triangles. */
#     SDL_GPU_PRIMITIVETYPE_LINELIST,      /**< A series of separate lines. */
#     SDL_GPU_PRIMITIVETYPE_LINESTRIP,     /**< A series of connected lines. */
#     SDL_GPU_PRIMITIVETYPE_POINTLIST      /**< A series of separate points. */
# } SDL_GPUPrimitiveType;
SDL_GPU_PRIMITIVETYPE_TRIANGLELIST = 0
SDL_GPU_PRIMITIVETYPE_TRIANGLESTRIP = 1
SDL_GPU_PRIMITIVETYPE_LINELIST = 2
SDL_GPU_PRIMITIVETYPE_LINESTRIP = 3
SDL_GPU_PRIMITIVETYPE_POINTLIST = 4
# typedef enum SDL_GPUSampleCount
# {
#     SDL_GPU_SAMPLECOUNT_1,  /**< No multisampling. */
#     SDL_GPU_SAMPLECOUNT_2,  /**< MSAA 2x */
#     SDL_GPU_SAMPLECOUNT_4,  /**< MSAA 4x */
#     SDL_GPU_SAMPLECOUNT_8   /**< MSAA 8x */
# } SDL_GPUSampleCount;
SDL_GPU_SAMPLECOUNT_1 = 0
SDL_GPU_SAMPLECOUNT_2 = 1
SDL_GPU_SAMPLECOUNT_4 = 2
SDL_GPU_SAMPLECOUNT_8 = 3
# typedef enum SDL_GPUSamplerAddressMode
# {
#     SDL_GPU_SAMPLERADDRESSMODE_REPEAT,           /**< Specifies that the coordinates will wrap around. */
#     SDL_GPU_SAMPLERADDRESSMODE_MIRRORED_REPEAT,  /**< Specifies that the coordinates will wrap around mirrored. */
#     SDL_GPU_SAMPLERADDRESSMODE_CLAMP_TO_EDGE     /**< Specifies that the coordinates will clamp to the 0-1 range. */
# } SDL_GPUSamplerAddressMode;
SDL_GPU_SAMPLERADDRESSMODE_REPEAT = 0
SDL_GPU_SAMPLERADDRESSMODE_MIRRORED_REPEAT = 1
SDL_GPU_SAMPLERADDRESSMODE_CLAMP_TO_EDGE = 2
# typedef enum SDL_GPUSamplerMipmapMode
# {
#     SDL_GPU_SAMPLERMIPMAPMODE_NEAREST,  /**< Point filtering. */
#     SDL_GPU_SAMPLERMIPMAPMODE_LINEAR    /**< Linear filtering. */
# } SDL_GPUSamplerMipmapMode;
SDL_GPU_SAMPLERMIPMAPMODE_NEAREST = 0
SDL_GPU_SAMPLERMIPMAPMODE_LINEAR = 1
# typedef enum SDL_GPUShaderStage
# {
#     SDL_GPU_SHADERSTAGE_VERTEX,
#     SDL_GPU_SHADERSTAGE_FRAGMENT
# } SDL_GPUShaderStage;
SDL_GPU_SHADERSTAGE_VERTEX = 0
SDL_GPU_SHADERSTAGE_FRAGMENT = 1
# typedef enum SDL_GPUStencilOp
# {
#     SDL_GPU_STENCILOP_INVALID,
#     SDL_GPU_STENCILOP_KEEP,                 /**< Keeps the current value. */
#     SDL_GPU_STENCILOP_ZERO,                 /**< Sets the value to 0. */
#     SDL_GPU_STENCILOP_REPLACE,              /**< Sets the value to reference. */
#     SDL_GPU_STENCILOP_INCREMENT_AND_CLAMP,  /**< Increments the current value and clamps to the maximum value. */
#     SDL_GPU_STENCILOP_DECREMENT_AND_CLAMP,  /**< Decrements the current value and clamps to 0. */
#     SDL_GPU_STENCILOP_INVERT,               /**< Bitwise-inverts the current value. */
#     SDL_GPU_STENCILOP_INCREMENT_AND_WRAP,   /**< Increments the current value and wraps back to 0. */
#     SDL_GPU_STENCILOP_DECREMENT_AND_WRAP    /**< Decrements the current value and wraps to the maximum value. */
# } SDL_GPUStencilOp;
SDL_GPU_STENCILOP_INVALID = 0
SDL_GPU_STENCILOP_KEEP = 1
SDL_GPU_STENCILOP_ZERO = 2
SDL_GPU_STENCILOP_REPLACE = 3
SDL_GPU_STENCILOP_INCREMENT_AND_CLAMP = 4
SDL_GPU_STENCILOP_DECREMENT_AND_CLAMP = 5
SDL_GPU_STENCILOP_INVERT = 6
SDL_GPU_STENCILOP_INCREMENT_AND_WRAP = 7
SDL_GPU_STENCILOP_DECREMENT_AND_WRAP = 8
# typedef enum SDL_GPUStoreOp
# {
#     SDL_GPU_STOREOP_STORE,             /**< The contents generated during the render pass will be written to memory. */
#     SDL_GPU_STOREOP_DONT_CARE,         /**< The contents generated during the render pass are not needed and may be discarded. The contents will be undefined. */
#     SDL_GPU_STOREOP_RESOLVE,           /**< The multisample contents generated during the render pass will be resolved to a non-multisample texture. The contents in the multisample texture may then be discarded and will be undefined. */
#     SDL_GPU_STOREOP_RESOLVE_AND_STORE  /**< The multisample contents generated during the render pass will be resolved to a non-multisample texture. The contents in the multisample texture will be written to memory. */
# } SDL_GPUStoreOp;
SDL_GPU_STOREOP_STORE = 0
SDL_GPU_STOREOP_DONT_CARE = 1
SDL_GPU_STOREOP_RESOLVE = 2
SDL_GPU_STOREOP_RESOLVE_AND_STORE = 3
# typedef enum SDL_GPUSwapchainComposition
# {
#     SDL_GPU_SWAPCHAINCOMPOSITION_SDR,
#     SDL_GPU_SWAPCHAINCOMPOSITION_SDR_LINEAR,
#     SDL_GPU_SWAPCHAINCOMPOSITION_HDR_EXTENDED_LINEAR,
#     SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2084
# } SDL_GPUSwapchainComposition;
SDL_GPU_SWAPCHAINCOMPOSITION_SDR = 0
SDL_GPU_SWAPCHAINCOMPOSITION_SDR_LINEAR = 1
SDL_GPU_SWAPCHAINCOMPOSITION_HDR_EXTENDED_LINEAR = 2
SDL_GPU_SWAPCHAINCOMPOSITION_HDR10_ST2084 = 3
# typedef enum SDL_GPUTextureFormat
# {
#     SDL_GPU_TEXTUREFORMAT_INVALID,
#     /* Unsigned Normalized Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_A8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R8G8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R16_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R16G16_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UNORM,
#     SDL_GPU_TEXTUREFORMAT_R10G10B10A2_UNORM,
#     SDL_GPU_TEXTUREFORMAT_B5G6R5_UNORM,
#     SDL_GPU_TEXTUREFORMAT_B5G5R5A1_UNORM,
#     SDL_GPU_TEXTUREFORMAT_B4G4R4A4_UNORM,
#     SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM,
#     /* Compressed Unsigned Normalized Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM,
#     SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM,
#     SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM,
#     SDL_GPU_TEXTUREFORMAT_BC4_R_UNORM,
#     SDL_GPU_TEXTUREFORMAT_BC5_RG_UNORM,
#     SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM,
#     /* Compressed Signed Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_BC6H_RGB_FLOAT,
#     /* Compressed Unsigned Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_BC6H_RGB_UFLOAT,
#     /* Signed Normalized Float Color Formats  */
#     SDL_GPU_TEXTUREFORMAT_R8_SNORM,
#     SDL_GPU_TEXTUREFORMAT_R8G8_SNORM,
#     SDL_GPU_TEXTUREFORMAT_R8G8B8A8_SNORM,
#     SDL_GPU_TEXTUREFORMAT_R16_SNORM,
#     SDL_GPU_TEXTUREFORMAT_R16G16_SNORM,
#     SDL_GPU_TEXTUREFORMAT_R16G16B16A16_SNORM,
#     /* Signed Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_R16_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_R16G16_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_R16G16B16A16_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_R32_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_R32G32_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_R32G32B32A32_FLOAT,
#     /* Unsigned Float Color Formats */
#     SDL_GPU_TEXTUREFORMAT_R11G11B10_UFLOAT,
#     /* Unsigned Integer Color Formats */
#     SDL_GPU_TEXTUREFORMAT_R8_UINT,
#     SDL_GPU_TEXTUREFORMAT_R8G8_UINT,
#     SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UINT,
#     SDL_GPU_TEXTUREFORMAT_R16_UINT,
#     SDL_GPU_TEXTUREFORMAT_R16G16_UINT,
#     SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UINT,
#     SDL_GPU_TEXTUREFORMAT_R32_UINT,
#     SDL_GPU_TEXTUREFORMAT_R32G32_UINT,
#     SDL_GPU_TEXTUREFORMAT_R32G32B32A32_UINT,
#     /* Signed Integer Color Formats */
#     SDL_GPU_TEXTUREFORMAT_R8_INT,
#     SDL_GPU_TEXTUREFORMAT_R8G8_INT,
#     SDL_GPU_TEXTUREFORMAT_R8G8B8A8_INT,
#     SDL_GPU_TEXTUREFORMAT_R16_INT,
#     SDL_GPU_TEXTUREFORMAT_R16G16_INT,
#     SDL_GPU_TEXTUREFORMAT_R16G16B16A16_INT,
#     SDL_GPU_TEXTUREFORMAT_R32_INT,
#     SDL_GPU_TEXTUREFORMAT_R32G32_INT,
#     SDL_GPU_TEXTUREFORMAT_R32G32B32A32_INT,
#     /* SRGB Unsigned Normalized Color Formats */
#     SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM_SRGB,
#     /* Compressed SRGB Unsigned Normalized Color Formats */
#     SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM_SRGB,
#     /* Depth Formats */
#     SDL_GPU_TEXTUREFORMAT_D16_UNORM,
#     SDL_GPU_TEXTUREFORMAT_D24_UNORM,
#     SDL_GPU_TEXTUREFORMAT_D32_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_D24_UNORM_S8_UINT,
#     SDL_GPU_TEXTUREFORMAT_D32_FLOAT_S8_UINT,
#     /* Compressed ASTC Normalized Float Color Formats*/
#     SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM,
#     /* Compressed SRGB ASTC Normalized Float Color Formats*/
#     SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM_SRGB,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM_SRGB,
#     /* Compressed ASTC Signed Float Color Formats*/
#     SDL_GPU_TEXTUREFORMAT_ASTC_4x4_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x4_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_5x5_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x5_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_6x6_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x5_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x6_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_8x8_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x5_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x6_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x8_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_10x10_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x10_FLOAT,
#     SDL_GPU_TEXTUREFORMAT_ASTC_12x12_FLOAT
# } SDL_GPUTextureFormat;
SDL_GPU_TEXTUREFORMAT_INVALID = 0
SDL_GPU_TEXTUREFORMAT_A8_UNORM = 1
SDL_GPU_TEXTUREFORMAT_R8_UNORM = 2
SDL_GPU_TEXTUREFORMAT_R8G8_UNORM = 3
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM = 4
SDL_GPU_TEXTUREFORMAT_R16_UNORM = 5
SDL_GPU_TEXTUREFORMAT_R16G16_UNORM = 6
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UNORM = 7
SDL_GPU_TEXTUREFORMAT_R10G10B10A2_UNORM = 8
SDL_GPU_TEXTUREFORMAT_B5G6R5_UNORM = 9
SDL_GPU_TEXTUREFORMAT_B5G5R5A1_UNORM = 10
SDL_GPU_TEXTUREFORMAT_B4G4R4A4_UNORM = 11
SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM = 12
SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM = 13
SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM = 14
SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM = 15
SDL_GPU_TEXTUREFORMAT_BC4_R_UNORM = 16
SDL_GPU_TEXTUREFORMAT_BC5_RG_UNORM = 17
SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM = 18
SDL_GPU_TEXTUREFORMAT_BC6H_RGB_FLOAT = 19
SDL_GPU_TEXTUREFORMAT_BC6H_RGB_UFLOAT = 20
SDL_GPU_TEXTUREFORMAT_R8_SNORM = 21
SDL_GPU_TEXTUREFORMAT_R8G8_SNORM = 22
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_SNORM = 23
SDL_GPU_TEXTUREFORMAT_R16_SNORM = 24
SDL_GPU_TEXTUREFORMAT_R16G16_SNORM = 25
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_SNORM = 26
SDL_GPU_TEXTUREFORMAT_R16_FLOAT = 27
SDL_GPU_TEXTUREFORMAT_R16G16_FLOAT = 28
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_FLOAT = 29
SDL_GPU_TEXTUREFORMAT_R32_FLOAT = 30
SDL_GPU_TEXTUREFORMAT_R32G32_FLOAT = 31
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_FLOAT = 32
SDL_GPU_TEXTUREFORMAT_R11G11B10_UFLOAT = 33
SDL_GPU_TEXTUREFORMAT_R8_UINT = 34
SDL_GPU_TEXTUREFORMAT_R8G8_UINT = 35
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UINT = 36
SDL_GPU_TEXTUREFORMAT_R16_UINT = 37
SDL_GPU_TEXTUREFORMAT_R16G16_UINT = 38
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_UINT = 39
SDL_GPU_TEXTUREFORMAT_R32_UINT = 40
SDL_GPU_TEXTUREFORMAT_R32G32_UINT = 41
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_UINT = 42
SDL_GPU_TEXTUREFORMAT_R8_INT = 43
SDL_GPU_TEXTUREFORMAT_R8G8_INT = 44
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_INT = 45
SDL_GPU_TEXTUREFORMAT_R16_INT = 46
SDL_GPU_TEXTUREFORMAT_R16G16_INT = 47
SDL_GPU_TEXTUREFORMAT_R16G16B16A16_INT = 48
SDL_GPU_TEXTUREFORMAT_R32_INT = 49
SDL_GPU_TEXTUREFORMAT_R32G32_INT = 50
SDL_GPU_TEXTUREFORMAT_R32G32B32A32_INT = 51
SDL_GPU_TEXTUREFORMAT_R8G8B8A8_UNORM_SRGB = 52
SDL_GPU_TEXTUREFORMAT_B8G8R8A8_UNORM_SRGB = 53
SDL_GPU_TEXTUREFORMAT_BC1_RGBA_UNORM_SRGB = 54
SDL_GPU_TEXTUREFORMAT_BC2_RGBA_UNORM_SRGB = 55
SDL_GPU_TEXTUREFORMAT_BC3_RGBA_UNORM_SRGB = 56
SDL_GPU_TEXTUREFORMAT_BC7_RGBA_UNORM_SRGB = 57
SDL_GPU_TEXTUREFORMAT_D16_UNORM = 58
SDL_GPU_TEXTUREFORMAT_D24_UNORM = 59
SDL_GPU_TEXTUREFORMAT_D32_FLOAT = 60
SDL_GPU_TEXTUREFORMAT_D24_UNORM_S8_UINT = 61
SDL_GPU_TEXTUREFORMAT_D32_FLOAT_S8_UINT = 62
SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM = 63
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM = 64
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM = 65
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM = 66
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM = 67
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM = 68
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM = 69
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM = 70
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM = 71
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM = 72
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM = 73
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM = 74
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM = 75
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM = 76
SDL_GPU_TEXTUREFORMAT_ASTC_4x4_UNORM_SRGB = 77
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_UNORM_SRGB = 78
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_UNORM_SRGB = 79
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_UNORM_SRGB = 80
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_UNORM_SRGB = 81
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_UNORM_SRGB = 82
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_UNORM_SRGB = 83
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_UNORM_SRGB = 84
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_UNORM_SRGB = 85
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_UNORM_SRGB = 86
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_UNORM_SRGB = 87
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_UNORM_SRGB = 88
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_UNORM_SRGB = 89
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_UNORM_SRGB = 90
SDL_GPU_TEXTUREFORMAT_ASTC_4x4_FLOAT = 91
SDL_GPU_TEXTUREFORMAT_ASTC_5x4_FLOAT = 92
SDL_GPU_TEXTUREFORMAT_ASTC_5x5_FLOAT = 93
SDL_GPU_TEXTUREFORMAT_ASTC_6x5_FLOAT = 94
SDL_GPU_TEXTUREFORMAT_ASTC_6x6_FLOAT = 95
SDL_GPU_TEXTUREFORMAT_ASTC_8x5_FLOAT = 96
SDL_GPU_TEXTUREFORMAT_ASTC_8x6_FLOAT = 97
SDL_GPU_TEXTUREFORMAT_ASTC_8x8_FLOAT = 98
SDL_GPU_TEXTUREFORMAT_ASTC_10x5_FLOAT = 99
SDL_GPU_TEXTUREFORMAT_ASTC_10x6_FLOAT = 100
SDL_GPU_TEXTUREFORMAT_ASTC_10x8_FLOAT = 101
SDL_GPU_TEXTUREFORMAT_ASTC_10x10_FLOAT = 102
SDL_GPU_TEXTUREFORMAT_ASTC_12x10_FLOAT = 103
SDL_GPU_TEXTUREFORMAT_ASTC_12x12_FLOAT = 104
# typedef enum SDL_GPUTextureType
# {
#     SDL_GPU_TEXTURETYPE_2D,         /**< The texture is a 2-dimensional image. */
#     SDL_GPU_TEXTURETYPE_2D_ARRAY,   /**< The texture is a 2-dimensional array image. */
#     SDL_GPU_TEXTURETYPE_3D,         /**< The texture is a 3-dimensional image. */
#     SDL_GPU_TEXTURETYPE_CUBE,       /**< The texture is a cube image. */
#     SDL_GPU_TEXTURETYPE_CUBE_ARRAY  /**< The texture is a cube array image. */
# } SDL_GPUTextureType;
SDL_GPU_TEXTURETYPE_2D = 0
SDL_GPU_TEXTURETYPE_2D_ARRAY = 1
SDL_GPU_TEXTURETYPE_3D = 2
SDL_GPU_TEXTURETYPE_CUBE = 3
SDL_GPU_TEXTURETYPE_CUBE_ARRAY = 4
# typedef enum SDL_GPUTransferBufferUsage
# {
#     SDL_GPU_TRANSFERBUFFERUSAGE_UPLOAD,
#     SDL_GPU_TRANSFERBUFFERUSAGE_DOWNLOAD
# } SDL_GPUTransferBufferUsage;
SDL_GPU_TRANSFERBUFFERUSAGE_UPLOAD = 0
SDL_GPU_TRANSFERBUFFERUSAGE_DOWNLOAD = 1
# typedef enum SDL_GPUVertexElementFormat
# {
#     SDL_GPU_VERTEXELEMENTFORMAT_INVALID,
#     /* 32-bit Signed Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_INT,
#     SDL_GPU_VERTEXELEMENTFORMAT_INT2,
#     SDL_GPU_VERTEXELEMENTFORMAT_INT3,
#     SDL_GPU_VERTEXELEMENTFORMAT_INT4,
#     /* 32-bit Unsigned Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_UINT,
#     SDL_GPU_VERTEXELEMENTFORMAT_UINT2,
#     SDL_GPU_VERTEXELEMENTFORMAT_UINT3,
#     SDL_GPU_VERTEXELEMENTFORMAT_UINT4,
#     /* 32-bit Floats */
#     SDL_GPU_VERTEXELEMENTFORMAT_FLOAT,
#     SDL_GPU_VERTEXELEMENTFORMAT_FLOAT2,
#     SDL_GPU_VERTEXELEMENTFORMAT_FLOAT3,
#     SDL_GPU_VERTEXELEMENTFORMAT_FLOAT4,
#     /* 8-bit Signed Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_BYTE2,
#     SDL_GPU_VERTEXELEMENTFORMAT_BYTE4,
#     /* 8-bit Unsigned Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2,
#     SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4,
#     /* 8-bit Signed Normalized */
#     SDL_GPU_VERTEXELEMENTFORMAT_BYTE2_NORM,
#     SDL_GPU_VERTEXELEMENTFORMAT_BYTE4_NORM,
#     /* 8-bit Unsigned Normalized */
#     SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2_NORM,
#     SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4_NORM,
#     /* 16-bit Signed Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_SHORT2,
#     SDL_GPU_VERTEXELEMENTFORMAT_SHORT4,
#     /* 16-bit Unsigned Integers */
#     SDL_GPU_VERTEXELEMENTFORMAT_USHORT2,
#     SDL_GPU_VERTEXELEMENTFORMAT_USHORT4,
#     /* 16-bit Signed Normalized */
#     SDL_GPU_VERTEXELEMENTFORMAT_SHORT2_NORM,
#     SDL_GPU_VERTEXELEMENTFORMAT_SHORT4_NORM,
#     /* 16-bit Unsigned Normalized */
#     SDL_GPU_VERTEXELEMENTFORMAT_USHORT2_NORM,
#     SDL_GPU_VERTEXELEMENTFORMAT_USHORT4_NORM,
#     /* 16-bit Floats */
#     SDL_GPU_VERTEXELEMENTFORMAT_HALF2,
#     SDL_GPU_VERTEXELEMENTFORMAT_HALF4
# } SDL_GPUVertexElementFormat;
SDL_GPU_VERTEXELEMENTFORMAT_INVALID = 0
SDL_GPU_VERTEXELEMENTFORMAT_INT = 1
SDL_GPU_VERTEXELEMENTFORMAT_INT2 = 2
SDL_GPU_VERTEXELEMENTFORMAT_INT3 = 3
SDL_GPU_VERTEXELEMENTFORMAT_INT4 = 4
SDL_GPU_VERTEXELEMENTFORMAT_UINT = 5
SDL_GPU_VERTEXELEMENTFORMAT_UINT2 = 6
SDL_GPU_VERTEXELEMENTFORMAT_UINT3 = 7
SDL_GPU_VERTEXELEMENTFORMAT_UINT4 = 8
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT = 9
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT2 = 10
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT3 = 11
SDL_GPU_VERTEXELEMENTFORMAT_FLOAT4 = 12
SDL_GPU_VERTEXELEMENTFORMAT_BYTE2 = 13
SDL_GPU_VERTEXELEMENTFORMAT_BYTE4 = 14
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2 = 15
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4 = 16
SDL_GPU_VERTEXELEMENTFORMAT_BYTE2_NORM = 17
SDL_GPU_VERTEXELEMENTFORMAT_BYTE4_NORM = 18
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE2_NORM = 19
SDL_GPU_VERTEXELEMENTFORMAT_UBYTE4_NORM = 20
SDL_GPU_VERTEXELEMENTFORMAT_SHORT2 = 21
SDL_GPU_VERTEXELEMENTFORMAT_SHORT4 = 22
SDL_GPU_VERTEXELEMENTFORMAT_USHORT2 = 23
SDL_GPU_VERTEXELEMENTFORMAT_USHORT4 = 24
SDL_GPU_VERTEXELEMENTFORMAT_SHORT2_NORM = 25
SDL_GPU_VERTEXELEMENTFORMAT_SHORT4_NORM = 26
SDL_GPU_VERTEXELEMENTFORMAT_USHORT2_NORM = 27
SDL_GPU_VERTEXELEMENTFORMAT_USHORT4_NORM = 28
SDL_GPU_VERTEXELEMENTFORMAT_HALF2 = 29
SDL_GPU_VERTEXELEMENTFORMAT_HALF4 = 30
# typedef enum SDL_GPUVertexInputRate
# {
#     SDL_GPU_VERTEXINPUTRATE_VERTEX,   /**< Attribute addressing is a function of the vertex index. */
#     SDL_GPU_VERTEXINPUTRATE_INSTANCE  /**< Attribute addressing is a function of the instance index. */
# } SDL_GPUVertexInputRate;
SDL_GPU_VERTEXINPUTRATE_VERTEX = 0
SDL_GPU_VERTEXINPUTRATE_INSTANCE = 1


# typedef struct SDL_GPUBlitRegion
# {
#     SDL_GPUTexture *texture;      /**< The texture. */
#     Uint32 mip_level;             /**< The mip level index of the region. */
#     Uint32 layer_or_depth_plane;  /**< The layer index or depth plane of the region. This value is treated as a layer index on 2D array and cube textures, and as a depth plane on 3D textures. */
#     Uint32 x;                     /**< The left offset of the region. */
#     Uint32 y;                     /**< The top offset of the region.  */
#     Uint32 w;                     /**< The width of the region. */
#     Uint32 h;                     /**< The height of the region. */
# } SDL_GPUBlitRegion;
class SDL_GPUBlitRegion(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("mip_level", ctypes.c_uint32),
        ("layer_or_depth_plane", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUColorTargetBlendState
# {
#     SDL_GPUBlendFactor src_color_blendfactor;     /**< The value to be multiplied by the source RGB value. */
#     SDL_GPUBlendFactor dst_color_blendfactor;     /**< The value to be multiplied by the destination RGB value. */
#     SDL_GPUBlendOp color_blend_op;                /**< The blend operation for the RGB components. */
#     SDL_GPUBlendFactor src_alpha_blendfactor;     /**< The value to be multiplied by the source alpha. */
#     SDL_GPUBlendFactor dst_alpha_blendfactor;     /**< The value to be multiplied by the destination alpha. */
#     SDL_GPUBlendOp alpha_blend_op;                /**< The blend operation for the alpha component. */
#     SDL_GPUColorComponentFlags color_write_mask;  /**< A bitmask specifying which of the RGBA components are enabled for writing. Writes to all channels if enable_color_write_mask is false. */
#     bool enable_blend;                            /**< Whether blending is enabled for the color target. */
#     bool enable_color_write_mask;                 /**< Whether the color write mask is enabled. */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_GPUColorTargetBlendState;
class SDL_GPUColorTargetBlendState(ctypes.Structure):
    _fields_ = [
        ("src_color_blendfactor", ctypes.c_int),
        ("dst_color_blendfactor", ctypes.c_int),
        ("color_blend_op", ctypes.c_int),
        ("src_alpha_blendfactor", ctypes.c_int),
        ("dst_alpha_blendfactor", ctypes.c_int),
        ("alpha_blend_op", ctypes.c_int),
        ("color_write_mask", ctypes.c_uint8),
        ("enable_blend", ctypes.c_bool),
        ("enable_color_write_mask", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUColorTargetDescription
# {
#     SDL_GPUTextureFormat format;               /**< The pixel format of the texture to be used as a color target. */
#     SDL_GPUColorTargetBlendState blend_state;  /**< The blend state to be used for the color target. */
# } SDL_GPUColorTargetDescription;
class SDL_GPUColorTargetDescription(ctypes.Structure):
    _fields_ = [("format", ctypes.c_int), ("blend_state", SDL_GPUColorTargetBlendState)]


# typedef struct SDL_GPUGraphicsPipelineTargetInfo
# {
#     const SDL_GPUColorTargetDescription *color_target_descriptions;  /**< A pointer to an array of color target descriptions. */
#     Uint32 num_color_targets;                                        /**< The number of color target descriptions in the above array. */
#     SDL_GPUTextureFormat depth_stencil_format;                       /**< The pixel format of the depth-stencil target. Ignored if has_depth_stencil_target is false. */
#     bool has_depth_stencil_target;                                   /**< true specifies that the pipeline uses a depth-stencil target. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUGraphicsPipelineTargetInfo;
class SDL_GPUGraphicsPipelineTargetInfo(ctypes.Structure):
    _fields_ = [
        ("color_target_descriptions", ctypes.POINTER(SDL_GPUColorTargetDescription)),
        ("num_color_targets", ctypes.c_uint32),
        ("depth_stencil_format", ctypes.c_int),
        ("has_depth_stencil_target", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUMultisampleState
# {
#     SDL_GPUSampleCount sample_count;  /**< The number of samples to be used in rasterization. */
#     Uint32 sample_mask;               /**< Reserved for future use. Must be set to 0. */
#     bool enable_mask;                 /**< Reserved for future use. Must be set to false. */
#     bool enable_alpha_to_coverage;    /**< true enables the alpha-to-coverage feature. */
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUMultisampleState;
class SDL_GPUMultisampleState(ctypes.Structure):
    _fields_ = [
        ("sample_count", ctypes.c_int),
        ("sample_mask", ctypes.c_uint32),
        ("enable_mask", ctypes.c_bool),
        ("enable_alpha_to_coverage", ctypes.c_bool),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPURasterizerState
# {
#     SDL_GPUFillMode fill_mode;         /**< Whether polygons will be filled in or drawn as lines. */
#     SDL_GPUCullMode cull_mode;         /**< The facing direction in which triangles will be culled. */
#     SDL_GPUFrontFace front_face;       /**< The vertex winding that will cause a triangle to be determined as front-facing. */
#     float depth_bias_constant_factor;  /**< A scalar factor controlling the depth value added to each fragment. */
#     float depth_bias_clamp;            /**< The maximum depth bias of a fragment. */
#     float depth_bias_slope_factor;     /**< A scalar factor applied to a fragment's slope in depth calculations. */
#     bool enable_depth_bias;            /**< true to bias fragment depth values. */
#     bool enable_depth_clip;            /**< true to enable depth clip, false to enable depth clamp. */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_GPURasterizerState;
class SDL_GPURasterizerState(ctypes.Structure):
    _fields_ = [
        ("fill_mode", ctypes.c_int),
        ("cull_mode", ctypes.c_int),
        ("front_face", ctypes.c_int),
        ("depth_bias_constant_factor", ctypes.c_float),
        ("depth_bias_clamp", ctypes.c_float),
        ("depth_bias_slope_factor", ctypes.c_float),
        ("enable_depth_bias", ctypes.c_bool),
        ("enable_depth_clip", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUStencilOpState
# {
#     SDL_GPUStencilOp fail_op;        /**< The action performed on samples that fail the stencil test. */
#     SDL_GPUStencilOp pass_op;        /**< The action performed on samples that pass the depth and stencil tests. */
#     SDL_GPUStencilOp depth_fail_op;  /**< The action performed on samples that pass the stencil test and fail the depth test. */
#     SDL_GPUCompareOp compare_op;     /**< The comparison operator used in the stencil test. */
# } SDL_GPUStencilOpState;
class SDL_GPUStencilOpState(ctypes.Structure):
    _fields_ = [
        ("fail_op", ctypes.c_int),
        ("pass_op", ctypes.c_int),
        ("depth_fail_op", ctypes.c_int),
        ("compare_op", ctypes.c_int),
    ]


# typedef struct SDL_GPUVertexAttribute
# {
#     Uint32 location;                    /**< The shader input location index. */
#     Uint32 buffer_slot;                 /**< The binding slot of the associated vertex buffer. */
#     SDL_GPUVertexElementFormat format;  /**< The size and type of the attribute data. */
#     Uint32 offset;                      /**< The byte offset of this attribute relative to the start of the vertex element. */
# } SDL_GPUVertexAttribute;
class SDL_GPUVertexAttribute(ctypes.Structure):
    _fields_ = [
        ("location", ctypes.c_uint32),
        ("buffer_slot", ctypes.c_uint32),
        ("format", ctypes.c_int),
        ("offset", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUVertexBufferDescription
# {
#     Uint32 slot;                        /**< The binding slot of the vertex buffer. */
#     Uint32 pitch;                       /**< The byte pitch between consecutive elements of the vertex buffer. */
#     SDL_GPUVertexInputRate input_rate;  /**< Whether attribute addressing is a function of the vertex index or instance index. */
#     Uint32 instance_step_rate;          /**< Reserved for future use. Must be set to 0. */
# } SDL_GPUVertexBufferDescription;
class SDL_GPUVertexBufferDescription(ctypes.Structure):
    _fields_ = [
        ("slot", ctypes.c_uint32),
        ("pitch", ctypes.c_uint32),
        ("input_rate", ctypes.c_int),
        ("instance_step_rate", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUVertexInputState
# {
#     const SDL_GPUVertexBufferDescription *vertex_buffer_descriptions; /**< A pointer to an array of vertex buffer descriptions. */
#     Uint32 num_vertex_buffers;                                        /**< The number of vertex buffer descriptions in the above array. */
#     const SDL_GPUVertexAttribute *vertex_attributes;                  /**< A pointer to an array of vertex attribute descriptions. */
#     Uint32 num_vertex_attributes;                                     /**< The number of vertex attribute descriptions in the above array. */
# } SDL_GPUVertexInputState;
class SDL_GPUVertexInputState(ctypes.Structure):
    _fields_ = [
        ("vertex_buffer_descriptions", ctypes.POINTER(SDL_GPUVertexBufferDescription)),
        ("num_vertex_buffers", ctypes.c_uint32),
        ("vertex_attributes", ctypes.POINTER(SDL_GPUVertexAttribute)),
        ("num_vertex_attributes", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUBlitInfo {
#     SDL_GPUBlitRegion source;       /**< The source region for the blit. */
#     SDL_GPUBlitRegion destination;  /**< The destination region for the blit. */
#     SDL_GPULoadOp load_op;          /**< What is done with the contents of the destination before the blit. */
#     SDL_FColor clear_color;         /**< The color to clear the destination region to before the blit. Ignored if load_op is not SDL_GPU_LOADOP_CLEAR. */
#     SDL_FlipMode flip_mode;         /**< The flip mode for the source region. */
#     SDL_GPUFilter filter;           /**< The filter mode used when blitting. */
#     bool cycle;                     /**< true cycles the destination texture if it is already bound. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUBlitInfo;
class SDL_GPUBlitInfo(ctypes.Structure):
    _fields_ = [
        ("source", SDL_GPUBlitRegion),
        ("destination", SDL_GPUBlitRegion),
        ("load_op", ctypes.c_int),
        ("clear_color", SDL_FColor),
        ("flip_mode", ctypes.c_int),
        ("filter", ctypes.c_int),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUBufferBinding
# {
#     SDL_GPUBuffer *buffer;  /**< The buffer to bind. Must have been created with SDL_GPU_BUFFERUSAGE_VERTEX for SDL_BindGPUVertexBuffers, or SDL_GPU_BUFFERUSAGE_INDEX for SDL_BindGPUIndexBuffer. */
#     Uint32 offset;          /**< The starting byte of the data to bind in the buffer. */
# } SDL_GPUBufferBinding;
class SDL_GPUBufferBinding(ctypes.Structure):
    _fields_ = [("buffer", ctypes.c_void_p), ("offset", ctypes.c_uint32)]


# typedef struct SDL_GPUBufferCreateInfo
# {
#     SDL_GPUBufferUsageFlags usage;  /**< How the buffer is intended to be used by the client. */
#     Uint32 size;                    /**< The size in bytes of the buffer. */
#     SDL_PropertiesID props;         /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUBufferCreateInfo;
class SDL_GPUBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ("usage", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUBufferLocation
# {
#     SDL_GPUBuffer *buffer;  /**< The buffer. */
#     Uint32 offset;          /**< The starting byte within the buffer. */
# } SDL_GPUBufferLocation;
class SDL_GPUBufferLocation(ctypes.Structure):
    _fields_ = [("buffer", ctypes.c_void_p), ("offset", ctypes.c_uint32)]


# typedef struct SDL_GPUBufferRegion
# {
#     SDL_GPUBuffer *buffer;  /**< The buffer. */
#     Uint32 offset;          /**< The starting byte within the buffer. */
#     Uint32 size;            /**< The size in bytes of the region. */
# } SDL_GPUBufferRegion;
class SDL_GPUBufferRegion(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.c_void_p),
        ("offset", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUColorTargetInfo
# {
#     SDL_GPUTexture *texture;         /**< The texture that will be used as a color target by a render pass. */
#     Uint32 mip_level;                /**< The mip level to use as a color target. */
#     Uint32 layer_or_depth_plane;     /**< The layer index or depth plane to use as a color target. This value is treated as a layer index on 2D array and cube textures, and as a depth plane on 3D textures. */
#     SDL_FColor clear_color;          /**< The color to clear the color target to at the start of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
#     SDL_GPULoadOp load_op;           /**< What is done with the contents of the color target at the beginning of the render pass. */
#     SDL_GPUStoreOp store_op;         /**< What is done with the results of the render pass. */
#     SDL_GPUTexture *resolve_texture; /**< The texture that will receive the results of a multisample resolve operation. Ignored if a RESOLVE* store_op is not used. */
#     Uint32 resolve_mip_level;        /**< The mip level of the resolve texture to use for the resolve operation. Ignored if a RESOLVE* store_op is not used. */
#     Uint32 resolve_layer;            /**< The layer index of the resolve texture to use for the resolve operation. Ignored if a RESOLVE* store_op is not used. */
#     bool cycle;                      /**< true cycles the texture if the texture is bound and load_op is not LOAD */
#     bool cycle_resolve_texture;      /**< true cycles the resolve texture if the resolve texture is bound. Ignored if a RESOLVE* store_op is not used. */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_GPUColorTargetInfo;
class SDL_GPUColorTargetInfo(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("mip_level", ctypes.c_uint32),
        ("layer_or_depth_plane", ctypes.c_uint32),
        ("clear_color", SDL_FColor),
        ("load_op", ctypes.c_int),
        ("store_op", ctypes.c_int),
        ("resolve_texture", ctypes.c_void_p),
        ("resolve_mip_level", ctypes.c_uint32),
        ("resolve_layer", ctypes.c_uint32),
        ("cycle", ctypes.c_bool),
        ("cycle_resolve_texture", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUComputePipelineCreateInfo
# {
#     size_t code_size;                       /**< The size in bytes of the compute shader code pointed to. */
#     const Uint8 *code;                      /**< A pointer to compute shader code. */
#     const char *entrypoint;                 /**< A pointer to a null-terminated UTF-8 string specifying the entry point function name for the shader. */
#     SDL_GPUShaderFormat format;             /**< The format of the compute shader code. */
#     Uint32 num_samplers;                    /**< The number of samplers defined in the shader. */
#     Uint32 num_readonly_storage_textures;   /**< The number of readonly storage textures defined in the shader. */
#     Uint32 num_readonly_storage_buffers;    /**< The number of readonly storage buffers defined in the shader. */
#     Uint32 num_readwrite_storage_textures;  /**< The number of read-write storage textures defined in the shader. */
#     Uint32 num_readwrite_storage_buffers;   /**< The number of read-write storage buffers defined in the shader. */
#     Uint32 num_uniform_buffers;             /**< The number of uniform buffers defined in the shader. */
#     Uint32 threadcount_x;                   /**< The number of threads in the X dimension. This should match the value in the shader. */
#     Uint32 threadcount_y;                   /**< The number of threads in the Y dimension. This should match the value in the shader. */
#     Uint32 threadcount_z;                   /**< The number of threads in the Z dimension. This should match the value in the shader. */
#     SDL_PropertiesID props;                 /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUComputePipelineCreateInfo;
class SDL_GPUComputePipelineCreateInfo(ctypes.Structure):
    _fields_ = [
        ("code_size", ctypes.c_size_t),
        ("code", ctypes.POINTER(ctypes.c_uint8)),
        ("entrypoint", ctypes.c_char_p),
        ("format", ctypes.c_uint32),
        ("num_samplers", ctypes.c_uint32),
        ("num_readonly_storage_textures", ctypes.c_uint32),
        ("num_readonly_storage_buffers", ctypes.c_uint32),
        ("num_readwrite_storage_textures", ctypes.c_uint32),
        ("num_readwrite_storage_buffers", ctypes.c_uint32),
        ("num_uniform_buffers", ctypes.c_uint32),
        ("threadcount_x", ctypes.c_uint32),
        ("threadcount_y", ctypes.c_uint32),
        ("threadcount_z", ctypes.c_uint32),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUDepthStencilState
# {
#     SDL_GPUCompareOp compare_op;                /**< The comparison operator used for depth testing. */
#     SDL_GPUStencilOpState back_stencil_state;   /**< The stencil op state for back-facing triangles. */
#     SDL_GPUStencilOpState front_stencil_state;  /**< The stencil op state for front-facing triangles. */
#     Uint8 compare_mask;                         /**< Selects the bits of the stencil values participating in the stencil test. */
#     Uint8 write_mask;                           /**< Selects the bits of the stencil values updated by the stencil test. */
#     bool enable_depth_test;                     /**< true enables the depth test. */
#     bool enable_depth_write;                    /**< true enables depth writes. Depth writes are always disabled when enable_depth_test is false. */
#     bool enable_stencil_test;                   /**< true enables the stencil test. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUDepthStencilState;
class SDL_GPUDepthStencilState(ctypes.Structure):
    _fields_ = [
        ("compare_op", ctypes.c_int),
        ("back_stencil_state", SDL_GPUStencilOpState),
        ("front_stencil_state", SDL_GPUStencilOpState),
        ("compare_mask", ctypes.c_uint8),
        ("write_mask", ctypes.c_uint8),
        ("enable_depth_test", ctypes.c_bool),
        ("enable_depth_write", ctypes.c_bool),
        ("enable_stencil_test", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUDepthStencilTargetInfo
# {
#     SDL_GPUTexture *texture;               /**< The texture that will be used as the depth stencil target by the render pass. */
#     float clear_depth;                     /**< The value to clear the depth component to at the beginning of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
#     SDL_GPULoadOp load_op;                 /**< What is done with the depth contents at the beginning of the render pass. */
#     SDL_GPUStoreOp store_op;               /**< What is done with the depth results of the render pass. */
#     SDL_GPULoadOp stencil_load_op;         /**< What is done with the stencil contents at the beginning of the render pass. */
#     SDL_GPUStoreOp stencil_store_op;       /**< What is done with the stencil results of the render pass. */
#     bool cycle;                            /**< true cycles the texture if the texture is bound and any load ops are not LOAD */
#     Uint8 clear_stencil;                   /**< The value to clear the stencil component to at the beginning of the render pass. Ignored if SDL_GPU_LOADOP_CLEAR is not used. */
#     Uint8 padding1;
#     Uint8 padding2;
# } SDL_GPUDepthStencilTargetInfo;
class SDL_GPUDepthStencilTargetInfo(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("clear_depth", ctypes.c_float),
        ("load_op", ctypes.c_int),
        ("store_op", ctypes.c_int),
        ("stencil_load_op", ctypes.c_int),
        ("stencil_store_op", ctypes.c_int),
        ("cycle", ctypes.c_bool),
        ("clear_stencil", ctypes.c_uint8),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUGraphicsPipelineCreateInfo
# {
#     SDL_GPUShader *vertex_shader;                   /**< The vertex shader used by the graphics pipeline. */
#     SDL_GPUShader *fragment_shader;                 /**< The fragment shader used by the graphics pipeline. */
#     SDL_GPUVertexInputState vertex_input_state;     /**< The vertex layout of the graphics pipeline. */
#     SDL_GPUPrimitiveType primitive_type;            /**< The primitive topology of the graphics pipeline. */
#     SDL_GPURasterizerState rasterizer_state;        /**< The rasterizer state of the graphics pipeline. */
#     SDL_GPUMultisampleState multisample_state;      /**< The multisample state of the graphics pipeline. */
#     SDL_GPUDepthStencilState depth_stencil_state;   /**< The depth-stencil state of the graphics pipeline. */
#     SDL_GPUGraphicsPipelineTargetInfo target_info;  /**< Formats and blend modes for the render targets of the graphics pipeline. */
#     SDL_PropertiesID props;                         /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUGraphicsPipelineCreateInfo;
class SDL_GPUGraphicsPipelineCreateInfo(ctypes.Structure):
    _fields_ = [
        ("vertex_shader", ctypes.c_void_p),
        ("fragment_shader", ctypes.c_void_p),
        ("vertex_input_state", SDL_GPUVertexInputState),
        ("primitive_type", ctypes.c_int),
        ("rasterizer_state", SDL_GPURasterizerState),
        ("multisample_state", SDL_GPUMultisampleState),
        ("depth_stencil_state", SDL_GPUDepthStencilState),
        ("target_info", SDL_GPUGraphicsPipelineTargetInfo),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUIndexedIndirectDrawCommand
# {
#     Uint32 num_indices;    /**< The number of indices to draw per instance. */
#     Uint32 num_instances;  /**< The number of instances to draw. */
#     Uint32 first_index;    /**< The base index within the index buffer. */
#     Sint32 vertex_offset;  /**< The value added to the vertex index before indexing into the vertex buffer. */
#     Uint32 first_instance; /**< The ID of the first instance to draw. */
# } SDL_GPUIndexedIndirectDrawCommand;
class SDL_GPUIndexedIndirectDrawCommand(ctypes.Structure):
    _fields_ = [
        ("num_indices", ctypes.c_uint32),
        ("num_instances", ctypes.c_uint32),
        ("first_index", ctypes.c_uint32),
        ("vertex_offset", ctypes.c_int32),
        ("first_instance", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUIndirectDispatchCommand
# {
#     Uint32 groupcount_x;  /**< The number of local workgroups to dispatch in the X dimension. */
#     Uint32 groupcount_y;  /**< The number of local workgroups to dispatch in the Y dimension. */
#     Uint32 groupcount_z;  /**< The number of local workgroups to dispatch in the Z dimension. */
# } SDL_GPUIndirectDispatchCommand;
class SDL_GPUIndirectDispatchCommand(ctypes.Structure):
    _fields_ = [
        ("groupcount_x", ctypes.c_uint32),
        ("groupcount_y", ctypes.c_uint32),
        ("groupcount_z", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUIndirectDrawCommand
# {
#     Uint32 num_vertices;   /**< The number of vertices to draw. */
#     Uint32 num_instances;  /**< The number of instances to draw. */
#     Uint32 first_vertex;   /**< The index of the first vertex to draw. */
#     Uint32 first_instance; /**< The ID of the first instance to draw. */
# } SDL_GPUIndirectDrawCommand;
class SDL_GPUIndirectDrawCommand(ctypes.Structure):
    _fields_ = [
        ("num_vertices", ctypes.c_uint32),
        ("num_instances", ctypes.c_uint32),
        ("first_vertex", ctypes.c_uint32),
        ("first_instance", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUSamplerCreateInfo
# {
#     SDL_GPUFilter min_filter;                  /**< The minification filter to apply to lookups. */
#     SDL_GPUFilter mag_filter;                  /**< The magnification filter to apply to lookups. */
#     SDL_GPUSamplerMipmapMode mipmap_mode;      /**< The mipmap filter to apply to lookups. */
#     SDL_GPUSamplerAddressMode address_mode_u;  /**< The addressing mode for U coordinates outside [0, 1). */
#     SDL_GPUSamplerAddressMode address_mode_v;  /**< The addressing mode for V coordinates outside [0, 1). */
#     SDL_GPUSamplerAddressMode address_mode_w;  /**< The addressing mode for W coordinates outside [0, 1). */
#     float mip_lod_bias;                        /**< The bias to be added to mipmap LOD calculation. */
#     float max_anisotropy;                      /**< The anisotropy value clamp used by the sampler. If enable_anisotropy is false, this is ignored. */
#     SDL_GPUCompareOp compare_op;               /**< The comparison operator to apply to fetched data before filtering. */
#     float min_lod;                             /**< Clamps the minimum of the computed LOD value. */
#     float max_lod;                             /**< Clamps the maximum of the computed LOD value. */
#     bool enable_anisotropy;                    /**< true to enable anisotropic filtering. */
#     bool enable_compare;                       /**< true to enable comparison against a reference value during lookups. */
#     Uint8 padding1;
#     Uint8 padding2;
#     SDL_PropertiesID props;                    /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUSamplerCreateInfo;
class SDL_GPUSamplerCreateInfo(ctypes.Structure):
    _fields_ = [
        ("min_filter", ctypes.c_int),
        ("mag_filter", ctypes.c_int),
        ("mipmap_mode", ctypes.c_int),
        ("address_mode_u", ctypes.c_int),
        ("address_mode_v", ctypes.c_int),
        ("address_mode_w", ctypes.c_int),
        ("mip_lod_bias", ctypes.c_float),
        ("max_anisotropy", ctypes.c_float),
        ("compare_op", ctypes.c_int),
        ("min_lod", ctypes.c_float),
        ("max_lod", ctypes.c_float),
        ("enable_anisotropy", ctypes.c_bool),
        ("enable_compare", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUShaderCreateInfo
# {
#     size_t code_size;             /**< The size in bytes of the code pointed to. */
#     const Uint8 *code;            /**< A pointer to shader code. */
#     const char *entrypoint;       /**< A pointer to a null-terminated UTF-8 string specifying the entry point function name for the shader. */
#     SDL_GPUShaderFormat format;   /**< The format of the shader code. */
#     SDL_GPUShaderStage stage;     /**< The stage the shader program corresponds to. */
#     Uint32 num_samplers;          /**< The number of samplers defined in the shader. */
#     Uint32 num_storage_textures;  /**< The number of storage textures defined in the shader. */
#     Uint32 num_storage_buffers;   /**< The number of storage buffers defined in the shader. */
#     Uint32 num_uniform_buffers;   /**< The number of uniform buffers defined in the shader. */
#     SDL_PropertiesID props;       /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUShaderCreateInfo;
class SDL_GPUShaderCreateInfo(ctypes.Structure):
    _fields_ = [
        ("code_size", ctypes.c_size_t),
        ("code", ctypes.POINTER(ctypes.c_uint8)),
        ("entrypoint", ctypes.c_char_p),
        ("format", ctypes.c_uint32),
        ("stage", ctypes.c_int),
        ("num_samplers", ctypes.c_uint32),
        ("num_storage_textures", ctypes.c_uint32),
        ("num_storage_buffers", ctypes.c_uint32),
        ("num_uniform_buffers", ctypes.c_uint32),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUStorageBufferReadWriteBinding
# {
#     SDL_GPUBuffer *buffer;  /**< The buffer to bind. Must have been created with SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE. */
#     bool cycle;             /**< true cycles the buffer if it is already bound. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUStorageBufferReadWriteBinding;
class SDL_GPUStorageBufferReadWriteBinding(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.c_void_p),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUStorageTextureReadWriteBinding
# {
#     SDL_GPUTexture *texture;  /**< The texture to bind. Must have been created with SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE or SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE. */
#     Uint32 mip_level;         /**< The mip level index to bind. */
#     Uint32 layer;             /**< The layer index to bind. */
#     bool cycle;               /**< true cycles the texture if it is already bound. */
#     Uint8 padding1;
#     Uint8 padding2;
#     Uint8 padding3;
# } SDL_GPUStorageTextureReadWriteBinding;
class SDL_GPUStorageTextureReadWriteBinding(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("cycle", ctypes.c_bool),
        ("padding1", ctypes.c_uint8),
        ("padding2", ctypes.c_uint8),
        ("padding3", ctypes.c_uint8),
    ]


# typedef struct SDL_GPUTextureCreateInfo
# {
#     SDL_GPUTextureType type;          /**< The base dimensionality of the texture. */
#     SDL_GPUTextureFormat format;      /**< The pixel format of the texture. */
#     SDL_GPUTextureUsageFlags usage;   /**< How the texture is intended to be used by the client. */
#     Uint32 width;                     /**< The width of the texture. */
#     Uint32 height;                    /**< The height of the texture. */
#     Uint32 layer_count_or_depth;      /**< The layer count or depth of the texture. This value is treated as a layer count on 2D array textures, and as a depth value on 3D textures. */
#     Uint32 num_levels;                /**< The number of mip levels in the texture. */
#     SDL_GPUSampleCount sample_count;  /**< The number of samples per texel. Only applies if the texture is used as a render target. */
#     SDL_PropertiesID props;           /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUTextureCreateInfo;
class SDL_GPUTextureCreateInfo(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("format", ctypes.c_int),
        ("usage", ctypes.c_uint32),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("layer_count_or_depth", ctypes.c_uint32),
        ("num_levels", ctypes.c_uint32),
        ("sample_count", ctypes.c_int),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUTextureLocation
# {
#     SDL_GPUTexture *texture;  /**< The texture used in the copy operation. */
#     Uint32 mip_level;         /**< The mip level index of the location. */
#     Uint32 layer;             /**< The layer index of the location. */
#     Uint32 x;                 /**< The left offset of the location. */
#     Uint32 y;                 /**< The top offset of the location. */
#     Uint32 z;                 /**< The front offset of the location. */
# } SDL_GPUTextureLocation;
class SDL_GPUTextureLocation(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("z", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUTextureRegion
# {
#     SDL_GPUTexture *texture;  /**< The texture used in the copy operation. */
#     Uint32 mip_level;         /**< The mip level index to transfer. */
#     Uint32 layer;             /**< The layer index to transfer. */
#     Uint32 x;                 /**< The left offset of the region. */
#     Uint32 y;                 /**< The top offset of the region. */
#     Uint32 z;                 /**< The front offset of the region. */
#     Uint32 w;                 /**< The width of the region. */
#     Uint32 h;                 /**< The height of the region. */
#     Uint32 d;                 /**< The depth of the region. */
# } SDL_GPUTextureRegion;
class SDL_GPUTextureRegion(ctypes.Structure):
    _fields_ = [
        ("texture", ctypes.c_void_p),
        ("mip_level", ctypes.c_uint32),
        ("layer", ctypes.c_uint32),
        ("x", ctypes.c_uint32),
        ("y", ctypes.c_uint32),
        ("z", ctypes.c_uint32),
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32),
        ("d", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUTextureSamplerBinding
# {
#     SDL_GPUTexture *texture;  /**< The texture to bind. Must have been created with SDL_GPU_TEXTUREUSAGE_SAMPLER. */
#     SDL_GPUSampler *sampler;  /**< The sampler to bind. */
# } SDL_GPUTextureSamplerBinding;
class SDL_GPUTextureSamplerBinding(ctypes.Structure):
    _fields_ = [("texture", ctypes.c_void_p), ("sampler", ctypes.c_void_p)]


# typedef struct SDL_GPUTextureTransferInfo
# {
#     SDL_GPUTransferBuffer *transfer_buffer;  /**< The transfer buffer used in the transfer operation. */
#     Uint32 offset;                           /**< The starting byte of the image data in the transfer buffer. */
#     Uint32 pixels_per_row;                   /**< The number of pixels from one row to the next. */
#     Uint32 rows_per_layer;                   /**< The number of rows from one layer/depth-slice to the next. */
# } SDL_GPUTextureTransferInfo;
class SDL_GPUTextureTransferInfo(ctypes.Structure):
    _fields_ = [
        ("transfer_buffer", ctypes.c_void_p),
        ("offset", ctypes.c_uint32),
        ("pixels_per_row", ctypes.c_uint32),
        ("rows_per_layer", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUTransferBufferCreateInfo
# {
#     SDL_GPUTransferBufferUsage usage;  /**< How the transfer buffer is intended to be used by the client. */
#     Uint32 size;                       /**< The size in bytes of the transfer buffer. */
#     SDL_PropertiesID props;            /**< A properties ID for extensions. Should be 0 if no extensions are needed. */
# } SDL_GPUTransferBufferCreateInfo;
class SDL_GPUTransferBufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ("usage", ctypes.c_int),
        ("size", ctypes.c_uint32),
        ("props", ctypes.c_uint32),
    ]


# typedef struct SDL_GPUTransferBufferLocation
# {
#     SDL_GPUTransferBuffer *transfer_buffer;  /**< The transfer buffer used in the transfer operation. */
#     Uint32 offset;                           /**< The starting byte of the buffer data in the transfer buffer. */
# } SDL_GPUTransferBufferLocation;
class SDL_GPUTransferBufferLocation(ctypes.Structure):
    _fields_ = [("transfer_buffer", ctypes.c_void_p), ("offset", ctypes.c_uint32)]


# typedef struct SDL_GPUViewport
# {
#     float x;          /**< The left offset of the viewport. */
#     float y;          /**< The top offset of the viewport. */
#     float w;          /**< The width of the viewport. */
#     float h;          /**< The height of the viewport. */
#     float min_depth;  /**< The minimum depth of the viewport. */
#     float max_depth;  /**< The maximum depth of the viewport. */
# } SDL_GPUViewport;
class SDL_GPUViewport(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("w", ctypes.c_float),
        ("h", ctypes.c_float),
        ("min_depth", ctypes.c_float),
        ("max_depth", ctypes.c_float),
    ]


# typedef struct SDL_GPUBuffer SDL_GPUBuffer;
# typedef Uint32 SDL_GPUBufferUsageFlags;
# #define SDL_GPU_BUFFERUSAGE_VERTEX                                  (1u << 0) /**< Buffer is a vertex buffer. */
# #define SDL_GPU_BUFFERUSAGE_INDEX                                   (1u << 1) /**< Buffer is an index buffer. */
# #define SDL_GPU_BUFFERUSAGE_INDIRECT                                (1u << 2) /**< Buffer is an indirect buffer. */
# #define SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ                   (1u << 3) /**< Buffer supports storage reads in graphics stages. */
# #define SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ                    (1u << 4) /**< Buffer supports storage reads in the compute stage. */
# #define SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE                   (1u << 5) /**< Buffer supports storage writes in the compute stage. */
SDL_GPU_BUFFERUSAGE_VERTEX = 0x1
SDL_GPU_BUFFERUSAGE_INDEX = 0x2
SDL_GPU_BUFFERUSAGE_INDIRECT = 0x4
SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ = 0x8
SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ = 0x10
SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE = 0x20
# typedef Uint8 SDL_GPUColorComponentFlags;
# #define SDL_GPU_COLORCOMPONENT_R (1u << 0) /**< the red component */
# #define SDL_GPU_COLORCOMPONENT_G (1u << 1) /**< the green component */
# #define SDL_GPU_COLORCOMPONENT_B (1u << 2) /**< the blue component */
# #define SDL_GPU_COLORCOMPONENT_A (1u << 3) /**< the alpha component */
SDL_GPU_COLORCOMPONENT_R = 0x1
SDL_GPU_COLORCOMPONENT_G = 0x2
SDL_GPU_COLORCOMPONENT_B = 0x4
SDL_GPU_COLORCOMPONENT_A = 0x8
# typedef struct SDL_GPUCommandBuffer SDL_GPUCommandBuffer;
# typedef struct SDL_GPUComputePass SDL_GPUComputePass;
# typedef struct SDL_GPUComputePipeline SDL_GPUComputePipeline;
# typedef struct SDL_GPUCopyPass SDL_GPUCopyPass;
# typedef struct SDL_GPUDevice SDL_GPUDevice;
# typedef struct SDL_GPUFence SDL_GPUFence;
# typedef struct SDL_GPUGraphicsPipeline SDL_GPUGraphicsPipeline;
# typedef struct SDL_GPURenderPass SDL_GPURenderPass;
# typedef struct SDL_GPUSampler SDL_GPUSampler;
# typedef struct SDL_GPUShader SDL_GPUShader;
# typedef Uint32 SDL_GPUShaderFormat;
# #define SDL_GPU_SHADERFORMAT_INVALID  0
# #define SDL_GPU_SHADERFORMAT_PRIVATE  (1u << 0) /**< Shaders for NDA'd platforms. */
# #define SDL_GPU_SHADERFORMAT_SPIRV    (1u << 1) /**< SPIR-V shaders for Vulkan. */
# #define SDL_GPU_SHADERFORMAT_DXBC     (1u << 2) /**< DXBC SM5_1 shaders for D3D12. */
# #define SDL_GPU_SHADERFORMAT_DXIL     (1u << 3) /**< DXIL SM6_0 shaders for D3D12. */
# #define SDL_GPU_SHADERFORMAT_MSL      (1u << 4) /**< MSL shaders for Metal. */
# #define SDL_GPU_SHADERFORMAT_METALLIB (1u << 5) /**< Precompiled metallib shaders for Metal. */
SDL_GPU_SHADERFORMAT_INVALID = 0x0
SDL_GPU_SHADERFORMAT_PRIVATE = 0x1
SDL_GPU_SHADERFORMAT_SPIRV = 0x2
SDL_GPU_SHADERFORMAT_DXBC = 0x4
SDL_GPU_SHADERFORMAT_DXIL = 0x8
SDL_GPU_SHADERFORMAT_MSL = 0x10
SDL_GPU_SHADERFORMAT_METALLIB = 0x20
# typedef struct SDL_GPUTexture SDL_GPUTexture;
# typedef Uint32 SDL_GPUTextureUsageFlags;
# #define SDL_GPU_TEXTUREUSAGE_SAMPLER                                 (1u << 0) /**< Texture supports sampling. */
# #define SDL_GPU_TEXTUREUSAGE_COLOR_TARGET                            (1u << 1) /**< Texture is a color render target. */
# #define SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET                    (1u << 2) /**< Texture is a depth stencil target. */
# #define SDL_GPU_TEXTUREUSAGE_GRAPHICS_STORAGE_READ                   (1u << 3) /**< Texture supports storage reads in graphics stages. */
# #define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ                    (1u << 4) /**< Texture supports storage reads in the compute stage. */
# #define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE                   (1u << 5) /**< Texture supports storage writes in the compute stage. */
# #define SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE (1u << 6) /**< Texture supports reads and writes in the same compute shader. This is NOT equivalent to READ | WRITE. */
SDL_GPU_TEXTUREUSAGE_SAMPLER = 0x1
SDL_GPU_TEXTUREUSAGE_COLOR_TARGET = 0x2
SDL_GPU_TEXTUREUSAGE_DEPTH_STENCIL_TARGET = 0x4
SDL_GPU_TEXTUREUSAGE_GRAPHICS_STORAGE_READ = 0x8
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_READ = 0x10
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_WRITE = 0x20
SDL_GPU_TEXTUREUSAGE_COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE = 0x40
# typedef struct SDL_GPUTransferBuffer SDL_GPUTransferBuffer;


# SDL_GPUCommandBuffer * SDL_AcquireGPUCommandBuffer(
#     SDL_GPUDevice *device);
SDL_AcquireGPUCommandBuffer = libsdl3.SDL_AcquireGPUCommandBuffer
SDL_AcquireGPUCommandBuffer.argtypes = [ctypes.c_void_p]
SDL_AcquireGPUCommandBuffer.restype = ctypes.c_void_p


# bool SDL_AcquireGPUSwapchainTexture(
#     SDL_GPUCommandBuffer *command_buffer,
#     SDL_Window *window,
#     SDL_GPUTexture **swapchain_texture,
#     Uint32 *swapchain_texture_width,
#     Uint32 *swapchain_texture_height);
SDL_AcquireGPUSwapchainTexture = libsdl3.SDL_AcquireGPUSwapchainTexture
SDL_AcquireGPUSwapchainTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.POINTER(ctypes.c_uint32),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_AcquireGPUSwapchainTexture.restype = ctypes.c_bool


# SDL_GPUComputePass * SDL_BeginGPUComputePass(
#     SDL_GPUCommandBuffer *command_buffer,
#     const SDL_GPUStorageTextureReadWriteBinding *storage_texture_bindings,
#     Uint32 num_storage_texture_bindings,
#     const SDL_GPUStorageBufferReadWriteBinding *storage_buffer_bindings,
#     Uint32 num_storage_buffer_bindings);
SDL_BeginGPUComputePass = libsdl3.SDL_BeginGPUComputePass
SDL_BeginGPUComputePass.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUStorageTextureReadWriteBinding),
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUStorageBufferReadWriteBinding),
    ctypes.c_uint32,
]
SDL_BeginGPUComputePass.restype = ctypes.c_void_p


# SDL_GPUCopyPass * SDL_BeginGPUCopyPass(
#     SDL_GPUCommandBuffer *command_buffer);
SDL_BeginGPUCopyPass = libsdl3.SDL_BeginGPUCopyPass
SDL_BeginGPUCopyPass.argtypes = [ctypes.c_void_p]
SDL_BeginGPUCopyPass.restype = ctypes.c_void_p


# SDL_GPURenderPass * SDL_BeginGPURenderPass(
#     SDL_GPUCommandBuffer *command_buffer,
#     const SDL_GPUColorTargetInfo *color_target_infos,
#     Uint32 num_color_targets,
#     const SDL_GPUDepthStencilTargetInfo *depth_stencil_target_info);
SDL_BeginGPURenderPass = libsdl3.SDL_BeginGPURenderPass
SDL_BeginGPURenderPass.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUColorTargetInfo),
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUDepthStencilTargetInfo),
]
SDL_BeginGPURenderPass.restype = ctypes.c_void_p


# void SDL_BindGPUComputePipeline(
#     SDL_GPUComputePass *compute_pass,
#     SDL_GPUComputePipeline *compute_pipeline);
SDL_BindGPUComputePipeline = libsdl3.SDL_BindGPUComputePipeline
SDL_BindGPUComputePipeline.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_BindGPUComputePipeline.restype = None


# void SDL_BindGPUComputeSamplers(
#     SDL_GPUComputePass *compute_pass,
#     Uint32 first_slot,
#     const SDL_GPUTextureSamplerBinding *texture_sampler_bindings,
#     Uint32 num_bindings);
SDL_BindGPUComputeSamplers = libsdl3.SDL_BindGPUComputeSamplers
SDL_BindGPUComputeSamplers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUTextureSamplerBinding),
    ctypes.c_uint32,
]
SDL_BindGPUComputeSamplers.restype = None


# void SDL_BindGPUComputeStorageBuffers(
#     SDL_GPUComputePass *compute_pass,
#     Uint32 first_slot,
#     SDL_GPUBuffer *const *storage_buffers,
#     Uint32 num_bindings);
SDL_BindGPUComputeStorageBuffers = libsdl3.SDL_BindGPUComputeStorageBuffers
SDL_BindGPUComputeStorageBuffers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUComputeStorageBuffers.restype = None


# void SDL_BindGPUComputeStorageTextures(
#     SDL_GPUComputePass *compute_pass,
#     Uint32 first_slot,
#     SDL_GPUTexture *const *storage_textures,
#     Uint32 num_bindings);
SDL_BindGPUComputeStorageTextures = libsdl3.SDL_BindGPUComputeStorageTextures
SDL_BindGPUComputeStorageTextures.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUComputeStorageTextures.restype = None


# void SDL_BindGPUFragmentSamplers(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     const SDL_GPUTextureSamplerBinding *texture_sampler_bindings,
#     Uint32 num_bindings);
SDL_BindGPUFragmentSamplers = libsdl3.SDL_BindGPUFragmentSamplers
SDL_BindGPUFragmentSamplers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUTextureSamplerBinding),
    ctypes.c_uint32,
]
SDL_BindGPUFragmentSamplers.restype = None


# void SDL_BindGPUFragmentStorageBuffers(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     SDL_GPUBuffer *const *storage_buffers,
#     Uint32 num_bindings);
SDL_BindGPUFragmentStorageBuffers = libsdl3.SDL_BindGPUFragmentStorageBuffers
SDL_BindGPUFragmentStorageBuffers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUFragmentStorageBuffers.restype = None


# void SDL_BindGPUFragmentStorageTextures(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     SDL_GPUTexture *const *storage_textures,
#     Uint32 num_bindings);
SDL_BindGPUFragmentStorageTextures = libsdl3.SDL_BindGPUFragmentStorageTextures
SDL_BindGPUFragmentStorageTextures.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUFragmentStorageTextures.restype = None


# void SDL_BindGPUGraphicsPipeline(
#     SDL_GPURenderPass *render_pass,
#     SDL_GPUGraphicsPipeline *graphics_pipeline);
SDL_BindGPUGraphicsPipeline = libsdl3.SDL_BindGPUGraphicsPipeline
SDL_BindGPUGraphicsPipeline.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_BindGPUGraphicsPipeline.restype = None


# void SDL_BindGPUIndexBuffer(
#     SDL_GPURenderPass *render_pass,
#     const SDL_GPUBufferBinding *binding,
#     SDL_GPUIndexElementSize index_element_size);
SDL_BindGPUIndexBuffer = libsdl3.SDL_BindGPUIndexBuffer
SDL_BindGPUIndexBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUBufferBinding),
    ctypes.c_int,
]
SDL_BindGPUIndexBuffer.restype = None


# void SDL_BindGPUVertexBuffers(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     const SDL_GPUBufferBinding *bindings,
#     Uint32 num_bindings);
SDL_BindGPUVertexBuffers = libsdl3.SDL_BindGPUVertexBuffers
SDL_BindGPUVertexBuffers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUBufferBinding),
    ctypes.c_uint32,
]
SDL_BindGPUVertexBuffers.restype = None


# void SDL_BindGPUVertexSamplers(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     const SDL_GPUTextureSamplerBinding *texture_sampler_bindings,
#     Uint32 num_bindings);
SDL_BindGPUVertexSamplers = libsdl3.SDL_BindGPUVertexSamplers
SDL_BindGPUVertexSamplers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(SDL_GPUTextureSamplerBinding),
    ctypes.c_uint32,
]
SDL_BindGPUVertexSamplers.restype = None


# void SDL_BindGPUVertexStorageBuffers(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     SDL_GPUBuffer *const *storage_buffers,
#     Uint32 num_bindings);
SDL_BindGPUVertexStorageBuffers = libsdl3.SDL_BindGPUVertexStorageBuffers
SDL_BindGPUVertexStorageBuffers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUVertexStorageBuffers.restype = None


# void SDL_BindGPUVertexStorageTextures(
#     SDL_GPURenderPass *render_pass,
#     Uint32 first_slot,
#     SDL_GPUTexture *const *storage_textures,
#     Uint32 num_bindings);
SDL_BindGPUVertexStorageTextures = libsdl3.SDL_BindGPUVertexStorageTextures
SDL_BindGPUVertexStorageTextures.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_BindGPUVertexStorageTextures.restype = None


# void SDL_BlitGPUTexture(
#     SDL_GPUCommandBuffer *command_buffer,
#     const SDL_GPUBlitInfo *info);
SDL_BlitGPUTexture = libsdl3.SDL_BlitGPUTexture
SDL_BlitGPUTexture.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_GPUBlitInfo)]
SDL_BlitGPUTexture.restype = None


# Uint32 SDL_CalculateGPUTextureFormatSize(
#     SDL_GPUTextureFormat format,
#     Uint32 width,
#     Uint32 height,
#     Uint32 depth_or_layer_count);
SDL_CalculateGPUTextureFormatSize = libsdl3.SDL_CalculateGPUTextureFormatSize
SDL_CalculateGPUTextureFormatSize.argtypes = [
    ctypes.c_int,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_CalculateGPUTextureFormatSize.restype = ctypes.c_uint32


# bool SDL_CancelGPUCommandBuffer(
#     SDL_GPUCommandBuffer *command_buffer);
SDL_CancelGPUCommandBuffer = libsdl3.SDL_CancelGPUCommandBuffer
SDL_CancelGPUCommandBuffer.argtypes = [ctypes.c_void_p]
SDL_CancelGPUCommandBuffer.restype = ctypes.c_bool


# bool SDL_ClaimWindowForGPUDevice(
#     SDL_GPUDevice *device,
#     SDL_Window *window);
SDL_ClaimWindowForGPUDevice = libsdl3.SDL_ClaimWindowForGPUDevice
SDL_ClaimWindowForGPUDevice.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ClaimWindowForGPUDevice.restype = ctypes.c_bool


# void SDL_CopyGPUBufferToBuffer(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUBufferLocation *source,
#     const SDL_GPUBufferLocation *destination,
#     Uint32 size,
#     bool cycle);
SDL_CopyGPUBufferToBuffer = libsdl3.SDL_CopyGPUBufferToBuffer
SDL_CopyGPUBufferToBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUBufferLocation),
    ctypes.POINTER(SDL_GPUBufferLocation),
    ctypes.c_uint32,
    ctypes.c_bool,
]
SDL_CopyGPUBufferToBuffer.restype = None


# void SDL_CopyGPUTextureToTexture(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUTextureLocation *source,
#     const SDL_GPUTextureLocation *destination,
#     Uint32 w,
#     Uint32 h,
#     Uint32 d,
#     bool cycle);
SDL_CopyGPUTextureToTexture = libsdl3.SDL_CopyGPUTextureToTexture
SDL_CopyGPUTextureToTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTextureLocation),
    ctypes.POINTER(SDL_GPUTextureLocation),
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_bool,
]
SDL_CopyGPUTextureToTexture.restype = None


# SDL_GPUBuffer * SDL_CreateGPUBuffer(
#     SDL_GPUDevice *device,
#     const SDL_GPUBufferCreateInfo *createinfo);
SDL_CreateGPUBuffer = libsdl3.SDL_CreateGPUBuffer
SDL_CreateGPUBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUBufferCreateInfo),
]
SDL_CreateGPUBuffer.restype = ctypes.c_void_p


# SDL_GPUComputePipeline * SDL_CreateGPUComputePipeline(
#     SDL_GPUDevice *device,
#     const SDL_GPUComputePipelineCreateInfo *createinfo);
SDL_CreateGPUComputePipeline = libsdl3.SDL_CreateGPUComputePipeline
SDL_CreateGPUComputePipeline.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUComputePipelineCreateInfo),
]
SDL_CreateGPUComputePipeline.restype = ctypes.c_void_p


# SDL_GPUDevice * SDL_CreateGPUDevice(
#     SDL_GPUShaderFormat format_flags,
#     bool debug_mode,
#     const char *name);
SDL_CreateGPUDevice = libsdl3.SDL_CreateGPUDevice
SDL_CreateGPUDevice.argtypes = [ctypes.c_uint32, ctypes.c_bool, ctypes.c_char_p]
SDL_CreateGPUDevice.restype = ctypes.c_void_p


# SDL_GPUDevice * SDL_CreateGPUDeviceWithProperties(
#     SDL_PropertiesID props);
SDL_CreateGPUDeviceWithProperties = libsdl3.SDL_CreateGPUDeviceWithProperties
SDL_CreateGPUDeviceWithProperties.argtypes = [ctypes.c_uint32]
SDL_CreateGPUDeviceWithProperties.restype = ctypes.c_void_p


# SDL_GPUGraphicsPipeline * SDL_CreateGPUGraphicsPipeline(
#     SDL_GPUDevice *device,
#     const SDL_GPUGraphicsPipelineCreateInfo *createinfo);
SDL_CreateGPUGraphicsPipeline = libsdl3.SDL_CreateGPUGraphicsPipeline
SDL_CreateGPUGraphicsPipeline.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUGraphicsPipelineCreateInfo),
]
SDL_CreateGPUGraphicsPipeline.restype = ctypes.c_void_p


# SDL_GPUSampler * SDL_CreateGPUSampler(
#     SDL_GPUDevice *device,
#     const SDL_GPUSamplerCreateInfo *createinfo);
SDL_CreateGPUSampler = libsdl3.SDL_CreateGPUSampler
SDL_CreateGPUSampler.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUSamplerCreateInfo),
]
SDL_CreateGPUSampler.restype = ctypes.c_void_p


# SDL_GPUShader * SDL_CreateGPUShader(
#     SDL_GPUDevice *device,
#     const SDL_GPUShaderCreateInfo *createinfo);
SDL_CreateGPUShader = libsdl3.SDL_CreateGPUShader
SDL_CreateGPUShader.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUShaderCreateInfo),
]
SDL_CreateGPUShader.restype = ctypes.c_void_p


# SDL_GPUTexture * SDL_CreateGPUTexture(
#     SDL_GPUDevice *device,
#     const SDL_GPUTextureCreateInfo *createinfo);
SDL_CreateGPUTexture = libsdl3.SDL_CreateGPUTexture
SDL_CreateGPUTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTextureCreateInfo),
]
SDL_CreateGPUTexture.restype = ctypes.c_void_p


# SDL_GPUTransferBuffer * SDL_CreateGPUTransferBuffer(
#     SDL_GPUDevice *device,
#     const SDL_GPUTransferBufferCreateInfo *createinfo);
SDL_CreateGPUTransferBuffer = libsdl3.SDL_CreateGPUTransferBuffer
SDL_CreateGPUTransferBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTransferBufferCreateInfo),
]
SDL_CreateGPUTransferBuffer.restype = ctypes.c_void_p


# void SDL_DestroyGPUDevice(SDL_GPUDevice *device);
SDL_DestroyGPUDevice = libsdl3.SDL_DestroyGPUDevice
SDL_DestroyGPUDevice.argtypes = [ctypes.c_void_p]
SDL_DestroyGPUDevice.restype = None


# void SDL_DispatchGPUCompute(
#     SDL_GPUComputePass *compute_pass,
#     Uint32 groupcount_x,
#     Uint32 groupcount_y,
#     Uint32 groupcount_z);
SDL_DispatchGPUCompute = libsdl3.SDL_DispatchGPUCompute
SDL_DispatchGPUCompute.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_DispatchGPUCompute.restype = None


# void SDL_DispatchGPUComputeIndirect(
#     SDL_GPUComputePass *compute_pass,
#     SDL_GPUBuffer *buffer,
#     Uint32 offset);
SDL_DispatchGPUComputeIndirect = libsdl3.SDL_DispatchGPUComputeIndirect
SDL_DispatchGPUComputeIndirect.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_DispatchGPUComputeIndirect.restype = None


# void SDL_DownloadFromGPUBuffer(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUBufferRegion *source,
#     const SDL_GPUTransferBufferLocation *destination);
SDL_DownloadFromGPUBuffer = libsdl3.SDL_DownloadFromGPUBuffer
SDL_DownloadFromGPUBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUBufferRegion),
    ctypes.POINTER(SDL_GPUTransferBufferLocation),
]
SDL_DownloadFromGPUBuffer.restype = None


# void SDL_DownloadFromGPUTexture(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUTextureRegion *source,
#     const SDL_GPUTextureTransferInfo *destination);
SDL_DownloadFromGPUTexture = libsdl3.SDL_DownloadFromGPUTexture
SDL_DownloadFromGPUTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTextureRegion),
    ctypes.POINTER(SDL_GPUTextureTransferInfo),
]
SDL_DownloadFromGPUTexture.restype = None


# void SDL_DrawGPUIndexedPrimitives(
#     SDL_GPURenderPass *render_pass,
#     Uint32 num_indices,
#     Uint32 num_instances,
#     Uint32 first_index,
#     Sint32 vertex_offset,
#     Uint32 first_instance);
SDL_DrawGPUIndexedPrimitives = libsdl3.SDL_DrawGPUIndexedPrimitives
SDL_DrawGPUIndexedPrimitives.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_int32,
    ctypes.c_uint32,
]
SDL_DrawGPUIndexedPrimitives.restype = None


# void SDL_DrawGPUIndexedPrimitivesIndirect(
#     SDL_GPURenderPass *render_pass,
#     SDL_GPUBuffer *buffer,
#     Uint32 offset,
#     Uint32 draw_count);
SDL_DrawGPUIndexedPrimitivesIndirect = libsdl3.SDL_DrawGPUIndexedPrimitivesIndirect
SDL_DrawGPUIndexedPrimitivesIndirect.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_DrawGPUIndexedPrimitivesIndirect.restype = None


# void SDL_DrawGPUPrimitives(
#     SDL_GPURenderPass *render_pass,
#     Uint32 num_vertices,
#     Uint32 num_instances,
#     Uint32 first_vertex,
#     Uint32 first_instance);
SDL_DrawGPUPrimitives = libsdl3.SDL_DrawGPUPrimitives
SDL_DrawGPUPrimitives.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_DrawGPUPrimitives.restype = None


# void SDL_DrawGPUPrimitivesIndirect(
#     SDL_GPURenderPass *render_pass,
#     SDL_GPUBuffer *buffer,
#     Uint32 offset,
#     Uint32 draw_count);
SDL_DrawGPUPrimitivesIndirect = libsdl3.SDL_DrawGPUPrimitivesIndirect
SDL_DrawGPUPrimitivesIndirect.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_uint32,
]
SDL_DrawGPUPrimitivesIndirect.restype = None


# void SDL_EndGPUComputePass(
#     SDL_GPUComputePass *compute_pass);
SDL_EndGPUComputePass = libsdl3.SDL_EndGPUComputePass
SDL_EndGPUComputePass.argtypes = [ctypes.c_void_p]
SDL_EndGPUComputePass.restype = None


# void SDL_EndGPUCopyPass(
#     SDL_GPUCopyPass *copy_pass);
SDL_EndGPUCopyPass = libsdl3.SDL_EndGPUCopyPass
SDL_EndGPUCopyPass.argtypes = [ctypes.c_void_p]
SDL_EndGPUCopyPass.restype = None


# void SDL_EndGPURenderPass(
#     SDL_GPURenderPass *render_pass);
SDL_EndGPURenderPass = libsdl3.SDL_EndGPURenderPass
SDL_EndGPURenderPass.argtypes = [ctypes.c_void_p]
SDL_EndGPURenderPass.restype = None


# void SDL_GDKResumeGPU(SDL_GPUDevice *device);
SDL_GDKResumeGPU = libsdl3.SDL_GDKResumeGPU
SDL_GDKResumeGPU.argtypes = [ctypes.c_void_p]
SDL_GDKResumeGPU.restype = None


# void SDL_GDKSuspendGPU(SDL_GPUDevice *device);
SDL_GDKSuspendGPU = libsdl3.SDL_GDKSuspendGPU
SDL_GDKSuspendGPU.argtypes = [ctypes.c_void_p]
SDL_GDKSuspendGPU.restype = None


# void SDL_GenerateMipmapsForGPUTexture(
#     SDL_GPUCommandBuffer *command_buffer,
#     SDL_GPUTexture *texture);
SDL_GenerateMipmapsForGPUTexture = libsdl3.SDL_GenerateMipmapsForGPUTexture
SDL_GenerateMipmapsForGPUTexture.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_GenerateMipmapsForGPUTexture.restype = None


# const char * SDL_GetGPUDeviceDriver(SDL_GPUDevice *device);
SDL_GetGPUDeviceDriver = libsdl3.SDL_GetGPUDeviceDriver
SDL_GetGPUDeviceDriver.argtypes = [ctypes.c_void_p]
SDL_GetGPUDeviceDriver.restype = ctypes.c_char_p


# SDL_PropertiesID SDL_GetGPUDeviceProperties(SDL_GPUDevice *device);
SDL_GetGPUDeviceProperties = libsdl3.SDL_GetGPUDeviceProperties
SDL_GetGPUDeviceProperties.argtypes = [ctypes.c_void_p]
SDL_GetGPUDeviceProperties.restype = ctypes.c_uint32


# const char * SDL_GetGPUDriver(int index);
SDL_GetGPUDriver = libsdl3.SDL_GetGPUDriver
SDL_GetGPUDriver.argtypes = [ctypes.c_int]
SDL_GetGPUDriver.restype = ctypes.c_char_p


# SDL_GPUShaderFormat SDL_GetGPUShaderFormats(SDL_GPUDevice *device);
SDL_GetGPUShaderFormats = libsdl3.SDL_GetGPUShaderFormats
SDL_GetGPUShaderFormats.argtypes = [ctypes.c_void_p]
SDL_GetGPUShaderFormats.restype = ctypes.c_uint32


# SDL_GPUTextureFormat SDL_GetGPUSwapchainTextureFormat(
#     SDL_GPUDevice *device,
#     SDL_Window *window);
SDL_GetGPUSwapchainTextureFormat = libsdl3.SDL_GetGPUSwapchainTextureFormat
SDL_GetGPUSwapchainTextureFormat.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_GetGPUSwapchainTextureFormat.restype = ctypes.c_int


# int SDL_GetNumGPUDrivers(void);
SDL_GetNumGPUDrivers = libsdl3.SDL_GetNumGPUDrivers
SDL_GetNumGPUDrivers.argtypes = []
SDL_GetNumGPUDrivers.restype = ctypes.c_int


# bool SDL_GPUSupportsProperties(
#     SDL_PropertiesID props);
SDL_GPUSupportsProperties = libsdl3.SDL_GPUSupportsProperties
SDL_GPUSupportsProperties.argtypes = [ctypes.c_uint32]
SDL_GPUSupportsProperties.restype = ctypes.c_bool


# bool SDL_GPUSupportsShaderFormats(
#     SDL_GPUShaderFormat format_flags,
#     const char *name);
SDL_GPUSupportsShaderFormats = libsdl3.SDL_GPUSupportsShaderFormats
SDL_GPUSupportsShaderFormats.argtypes = [ctypes.c_uint32, ctypes.c_char_p]
SDL_GPUSupportsShaderFormats.restype = ctypes.c_bool


# Uint32 SDL_GPUTextureFormatTexelBlockSize(
#     SDL_GPUTextureFormat format);
SDL_GPUTextureFormatTexelBlockSize = libsdl3.SDL_GPUTextureFormatTexelBlockSize
SDL_GPUTextureFormatTexelBlockSize.argtypes = [ctypes.c_int]
SDL_GPUTextureFormatTexelBlockSize.restype = ctypes.c_uint32


# bool SDL_GPUTextureSupportsFormat(
#     SDL_GPUDevice *device,
#     SDL_GPUTextureFormat format,
#     SDL_GPUTextureType type,
#     SDL_GPUTextureUsageFlags usage);
SDL_GPUTextureSupportsFormat = libsdl3.SDL_GPUTextureSupportsFormat
SDL_GPUTextureSupportsFormat.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_uint32,
]
SDL_GPUTextureSupportsFormat.restype = ctypes.c_bool


# bool SDL_GPUTextureSupportsSampleCount(
#     SDL_GPUDevice *device,
#     SDL_GPUTextureFormat format,
#     SDL_GPUSampleCount sample_count);
SDL_GPUTextureSupportsSampleCount = libsdl3.SDL_GPUTextureSupportsSampleCount
SDL_GPUTextureSupportsSampleCount.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_GPUTextureSupportsSampleCount.restype = ctypes.c_bool


# void SDL_InsertGPUDebugLabel(
#     SDL_GPUCommandBuffer *command_buffer,
#     const char *text);
SDL_InsertGPUDebugLabel = libsdl3.SDL_InsertGPUDebugLabel
SDL_InsertGPUDebugLabel.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_InsertGPUDebugLabel.restype = None


# void * SDL_MapGPUTransferBuffer(
#     SDL_GPUDevice *device,
#     SDL_GPUTransferBuffer *transfer_buffer,
#     bool cycle);
SDL_MapGPUTransferBuffer = libsdl3.SDL_MapGPUTransferBuffer
SDL_MapGPUTransferBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool]
SDL_MapGPUTransferBuffer.restype = ctypes.c_void_p


# void SDL_PopGPUDebugGroup(
#     SDL_GPUCommandBuffer *command_buffer);
SDL_PopGPUDebugGroup = libsdl3.SDL_PopGPUDebugGroup
SDL_PopGPUDebugGroup.argtypes = [ctypes.c_void_p]
SDL_PopGPUDebugGroup.restype = None


# void SDL_PushGPUComputeUniformData(
#     SDL_GPUCommandBuffer *command_buffer,
#     Uint32 slot_index,
#     const void *data,
#     Uint32 length);
SDL_PushGPUComputeUniformData = libsdl3.SDL_PushGPUComputeUniformData
SDL_PushGPUComputeUniformData.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_PushGPUComputeUniformData.restype = None


# void SDL_PushGPUDebugGroup(
#     SDL_GPUCommandBuffer *command_buffer,
#     const char *name);
SDL_PushGPUDebugGroup = libsdl3.SDL_PushGPUDebugGroup
SDL_PushGPUDebugGroup.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_PushGPUDebugGroup.restype = None


# void SDL_PushGPUFragmentUniformData(
#     SDL_GPUCommandBuffer *command_buffer,
#     Uint32 slot_index,
#     const void *data,
#     Uint32 length);
SDL_PushGPUFragmentUniformData = libsdl3.SDL_PushGPUFragmentUniformData
SDL_PushGPUFragmentUniformData.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_PushGPUFragmentUniformData.restype = None


# void SDL_PushGPUVertexUniformData(
#     SDL_GPUCommandBuffer *command_buffer,
#     Uint32 slot_index,
#     const void *data,
#     Uint32 length);
SDL_PushGPUVertexUniformData = libsdl3.SDL_PushGPUVertexUniformData
SDL_PushGPUVertexUniformData.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    ctypes.c_void_p,
    ctypes.c_uint32,
]
SDL_PushGPUVertexUniformData.restype = None


# bool SDL_QueryGPUFence(
#     SDL_GPUDevice *device,
#     SDL_GPUFence *fence);
SDL_QueryGPUFence = libsdl3.SDL_QueryGPUFence
SDL_QueryGPUFence.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_QueryGPUFence.restype = ctypes.c_bool


# void SDL_ReleaseGPUBuffer(
#     SDL_GPUDevice *device,
#     SDL_GPUBuffer *buffer);
SDL_ReleaseGPUBuffer = libsdl3.SDL_ReleaseGPUBuffer
SDL_ReleaseGPUBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUBuffer.restype = None


# void SDL_ReleaseGPUComputePipeline(
#     SDL_GPUDevice *device,
#     SDL_GPUComputePipeline *compute_pipeline);
SDL_ReleaseGPUComputePipeline = libsdl3.SDL_ReleaseGPUComputePipeline
SDL_ReleaseGPUComputePipeline.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUComputePipeline.restype = None


# void SDL_ReleaseGPUFence(
#     SDL_GPUDevice *device,
#     SDL_GPUFence *fence);
SDL_ReleaseGPUFence = libsdl3.SDL_ReleaseGPUFence
SDL_ReleaseGPUFence.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUFence.restype = None


# void SDL_ReleaseGPUGraphicsPipeline(
#     SDL_GPUDevice *device,
#     SDL_GPUGraphicsPipeline *graphics_pipeline);
SDL_ReleaseGPUGraphicsPipeline = libsdl3.SDL_ReleaseGPUGraphicsPipeline
SDL_ReleaseGPUGraphicsPipeline.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUGraphicsPipeline.restype = None


# void SDL_ReleaseGPUSampler(
#     SDL_GPUDevice *device,
#     SDL_GPUSampler *sampler);
SDL_ReleaseGPUSampler = libsdl3.SDL_ReleaseGPUSampler
SDL_ReleaseGPUSampler.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUSampler.restype = None


# void SDL_ReleaseGPUShader(
#     SDL_GPUDevice *device,
#     SDL_GPUShader *shader);
SDL_ReleaseGPUShader = libsdl3.SDL_ReleaseGPUShader
SDL_ReleaseGPUShader.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUShader.restype = None


# void SDL_ReleaseGPUTexture(
#     SDL_GPUDevice *device,
#     SDL_GPUTexture *texture);
SDL_ReleaseGPUTexture = libsdl3.SDL_ReleaseGPUTexture
SDL_ReleaseGPUTexture.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUTexture.restype = None


# void SDL_ReleaseGPUTransferBuffer(
#     SDL_GPUDevice *device,
#     SDL_GPUTransferBuffer *transfer_buffer);
SDL_ReleaseGPUTransferBuffer = libsdl3.SDL_ReleaseGPUTransferBuffer
SDL_ReleaseGPUTransferBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseGPUTransferBuffer.restype = None


# void SDL_ReleaseWindowFromGPUDevice(
#     SDL_GPUDevice *device,
#     SDL_Window *window);
SDL_ReleaseWindowFromGPUDevice = libsdl3.SDL_ReleaseWindowFromGPUDevice
SDL_ReleaseWindowFromGPUDevice.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_ReleaseWindowFromGPUDevice.restype = None


# bool SDL_SetGPUAllowedFramesInFlight(
#     SDL_GPUDevice *device,
#     Uint32 allowed_frames_in_flight);
SDL_SetGPUAllowedFramesInFlight = libsdl3.SDL_SetGPUAllowedFramesInFlight
SDL_SetGPUAllowedFramesInFlight.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
SDL_SetGPUAllowedFramesInFlight.restype = ctypes.c_bool


# void SDL_SetGPUBlendConstants(
#     SDL_GPURenderPass *render_pass,
#     SDL_FColor blend_constants);
SDL_SetGPUBlendConstants = libsdl3.SDL_SetGPUBlendConstants
SDL_SetGPUBlendConstants.argtypes = [ctypes.c_void_p, SDL_FColor]
SDL_SetGPUBlendConstants.restype = None


# void SDL_SetGPUBufferName(
#     SDL_GPUDevice *device,
#     SDL_GPUBuffer *buffer,
#     const char *text);
SDL_SetGPUBufferName = libsdl3.SDL_SetGPUBufferName
SDL_SetGPUBufferName.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
SDL_SetGPUBufferName.restype = None


# void SDL_SetGPUScissor(
#     SDL_GPURenderPass *render_pass,
#     const SDL_Rect *scissor);
SDL_SetGPUScissor = libsdl3.SDL_SetGPUScissor
SDL_SetGPUScissor.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]
SDL_SetGPUScissor.restype = None


# void SDL_SetGPUStencilReference(
#     SDL_GPURenderPass *render_pass,
#     Uint8 reference);
SDL_SetGPUStencilReference = libsdl3.SDL_SetGPUStencilReference
SDL_SetGPUStencilReference.argtypes = [ctypes.c_void_p, ctypes.c_uint8]
SDL_SetGPUStencilReference.restype = None


# bool SDL_SetGPUSwapchainParameters(
#     SDL_GPUDevice *device,
#     SDL_Window *window,
#     SDL_GPUSwapchainComposition swapchain_composition,
#     SDL_GPUPresentMode present_mode);
SDL_SetGPUSwapchainParameters = libsdl3.SDL_SetGPUSwapchainParameters
SDL_SetGPUSwapchainParameters.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
]
SDL_SetGPUSwapchainParameters.restype = ctypes.c_bool


# void SDL_SetGPUTextureName(
#     SDL_GPUDevice *device,
#     SDL_GPUTexture *texture,
#     const char *text);
SDL_SetGPUTextureName = libsdl3.SDL_SetGPUTextureName
SDL_SetGPUTextureName.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
SDL_SetGPUTextureName.restype = None


# void SDL_SetGPUViewport(
#     SDL_GPURenderPass *render_pass,
#     const SDL_GPUViewport *viewport);
SDL_SetGPUViewport = libsdl3.SDL_SetGPUViewport
SDL_SetGPUViewport.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_GPUViewport)]
SDL_SetGPUViewport.restype = None


# bool SDL_SubmitGPUCommandBuffer(
#     SDL_GPUCommandBuffer *command_buffer);
SDL_SubmitGPUCommandBuffer = libsdl3.SDL_SubmitGPUCommandBuffer
SDL_SubmitGPUCommandBuffer.argtypes = [ctypes.c_void_p]
SDL_SubmitGPUCommandBuffer.restype = ctypes.c_bool


# SDL_GPUFence * SDL_SubmitGPUCommandBufferAndAcquireFence(
#     SDL_GPUCommandBuffer *command_buffer);
SDL_SubmitGPUCommandBufferAndAcquireFence = (
    libsdl3.SDL_SubmitGPUCommandBufferAndAcquireFence
)
SDL_SubmitGPUCommandBufferAndAcquireFence.argtypes = [ctypes.c_void_p]
SDL_SubmitGPUCommandBufferAndAcquireFence.restype = ctypes.c_void_p


# void SDL_UnmapGPUTransferBuffer(
#     SDL_GPUDevice *device,
#     SDL_GPUTransferBuffer *transfer_buffer);
SDL_UnmapGPUTransferBuffer = libsdl3.SDL_UnmapGPUTransferBuffer
SDL_UnmapGPUTransferBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_UnmapGPUTransferBuffer.restype = None


# void SDL_UploadToGPUBuffer(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUTransferBufferLocation *source,
#     const SDL_GPUBufferRegion *destination,
#     bool cycle);
SDL_UploadToGPUBuffer = libsdl3.SDL_UploadToGPUBuffer
SDL_UploadToGPUBuffer.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTransferBufferLocation),
    ctypes.POINTER(SDL_GPUBufferRegion),
    ctypes.c_bool,
]
SDL_UploadToGPUBuffer.restype = None


# void SDL_UploadToGPUTexture(
#     SDL_GPUCopyPass *copy_pass,
#     const SDL_GPUTextureTransferInfo *source,
#     const SDL_GPUTextureRegion *destination,
#     bool cycle);
SDL_UploadToGPUTexture = libsdl3.SDL_UploadToGPUTexture
SDL_UploadToGPUTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(SDL_GPUTextureTransferInfo),
    ctypes.POINTER(SDL_GPUTextureRegion),
    ctypes.c_bool,
]
SDL_UploadToGPUTexture.restype = None


# bool SDL_WaitAndAcquireGPUSwapchainTexture(
#     SDL_GPUCommandBuffer *command_buffer,
#     SDL_Window *window,
#     SDL_GPUTexture **swapchain_texture,
#     Uint32 *swapchain_texture_width,
#     Uint32 *swapchain_texture_height);
SDL_WaitAndAcquireGPUSwapchainTexture = libsdl3.SDL_WaitAndAcquireGPUSwapchainTexture
SDL_WaitAndAcquireGPUSwapchainTexture.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.POINTER(ctypes.c_uint32),
    ctypes.POINTER(ctypes.c_uint32),
]
SDL_WaitAndAcquireGPUSwapchainTexture.restype = ctypes.c_bool


# bool SDL_WaitForGPUFences(
#     SDL_GPUDevice *device,
#     bool wait_all,
#     SDL_GPUFence *const *fences,
#     Uint32 num_fences);
SDL_WaitForGPUFences = libsdl3.SDL_WaitForGPUFences
SDL_WaitForGPUFences.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p)),
    ctypes.c_uint32,
]
SDL_WaitForGPUFences.restype = ctypes.c_bool


# bool SDL_WaitForGPUIdle(
#     SDL_GPUDevice *device);
SDL_WaitForGPUIdle = libsdl3.SDL_WaitForGPUIdle
SDL_WaitForGPUIdle.argtypes = [ctypes.c_void_p]
SDL_WaitForGPUIdle.restype = ctypes.c_bool


# bool SDL_WaitForGPUSwapchain(
#     SDL_GPUDevice *device,
#     SDL_Window *window);
SDL_WaitForGPUSwapchain = libsdl3.SDL_WaitForGPUSwapchain
SDL_WaitForGPUSwapchain.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
SDL_WaitForGPUSwapchain.restype = ctypes.c_bool


# bool SDL_WindowSupportsGPUPresentMode(
#     SDL_GPUDevice *device,
#     SDL_Window *window,
#     SDL_GPUPresentMode present_mode);
SDL_WindowSupportsGPUPresentMode = libsdl3.SDL_WindowSupportsGPUPresentMode
SDL_WindowSupportsGPUPresentMode.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_WindowSupportsGPUPresentMode.restype = ctypes.c_bool


# bool SDL_WindowSupportsGPUSwapchainComposition(
#     SDL_GPUDevice *device,
#     SDL_Window *window,
#     SDL_GPUSwapchainComposition swapchain_composition);
SDL_WindowSupportsGPUSwapchainComposition = (
    libsdl3.SDL_WindowSupportsGPUSwapchainComposition
)
SDL_WindowSupportsGPUSwapchainComposition.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
]
SDL_WindowSupportsGPUSwapchainComposition.restype = ctypes.c_bool
