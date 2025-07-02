"""
SDL_tray.h
System Tray
Document: https://wiki.libsdl.org/SDL3/CategoryTray
"""

import ctypes

from sdl3_ctypes.lib import libsdl3
from sdl3_ctypes.SDL_surface import SDL_Surface

# typedef struct SDL_Tray SDL_Tray;

# typedef void (SDLCALL *SDL_TrayCallback)(void *userdata, SDL_TrayEntry *entry);
SDL_TrayCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

# typedef struct SDL_TrayEntry SDL_TrayEntry;
# typedef Uint32 SDL_TrayEntryFlags;
# #define SDL_TRAYENTRY_BUTTON      0x00000001u /**< Make the entry a simple button. Required. */
# #define SDL_TRAYENTRY_CHECKBOX    0x00000002u /**< Make the entry a checkbox. Required. */
# #define SDL_TRAYENTRY_SUBMENU     0x00000004u /**< Prepare the entry to have a submenu. Required */
# #define SDL_TRAYENTRY_DISABLED    0x80000000u /**< Make the entry disabled. Optional. */
# #define SDL_TRAYENTRY_CHECKED     0x40000000u /**< Make the entry checked. This is valid only for checkboxes. Optional. */
SDL_TRAYENTRY_BUTTON = 0x1
SDL_TRAYENTRY_CHECKBOX = 0x2
SDL_TRAYENTRY_SUBMENU = 0x4
SDL_TRAYENTRY_DISABLED = 0x80000000
SDL_TRAYENTRY_CHECKED = 0x40000000
# typedef struct SDL_TrayMenu SDL_TrayMenu;


# void SDL_ClickTrayEntry(SDL_TrayEntry *entry);
SDL_ClickTrayEntry = libsdl3.SDL_ClickTrayEntry
SDL_ClickTrayEntry.argtypes = [ctypes.c_void_p]
SDL_ClickTrayEntry.restype = None


# SDL_Tray * SDL_CreateTray(SDL_Surface *icon, const char *tooltip);
SDL_CreateTray = libsdl3.SDL_CreateTray
SDL_CreateTray.argtypes = [ctypes.POINTER(SDL_Surface), ctypes.c_char_p]
SDL_CreateTray.restype = ctypes.c_void_p


# SDL_TrayMenu * SDL_CreateTrayMenu(SDL_Tray *tray);
SDL_CreateTrayMenu = libsdl3.SDL_CreateTrayMenu
SDL_CreateTrayMenu.argtypes = [ctypes.c_void_p]
SDL_CreateTrayMenu.restype = ctypes.c_void_p


# SDL_TrayMenu * SDL_CreateTraySubmenu(SDL_TrayEntry *entry);
SDL_CreateTraySubmenu = libsdl3.SDL_CreateTraySubmenu
SDL_CreateTraySubmenu.argtypes = [ctypes.c_void_p]
SDL_CreateTraySubmenu.restype = ctypes.c_void_p


# void SDL_DestroyTray(SDL_Tray *tray);
SDL_DestroyTray = libsdl3.SDL_DestroyTray
SDL_DestroyTray.argtypes = [ctypes.c_void_p]
SDL_DestroyTray.restype = None


# const SDL_TrayEntry ** SDL_GetTrayEntries(SDL_TrayMenu *menu, int *count);
SDL_GetTrayEntries = libsdl3.SDL_GetTrayEntries
SDL_GetTrayEntries.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
SDL_GetTrayEntries.restype = ctypes.POINTER(ctypes.c_void_p)


# bool SDL_GetTrayEntryChecked(SDL_TrayEntry *entry);
SDL_GetTrayEntryChecked = libsdl3.SDL_GetTrayEntryChecked
SDL_GetTrayEntryChecked.argtypes = [ctypes.c_void_p]
SDL_GetTrayEntryChecked.restype = ctypes.c_bool


# bool SDL_GetTrayEntryEnabled(SDL_TrayEntry *entry);
SDL_GetTrayEntryEnabled = libsdl3.SDL_GetTrayEntryEnabled
SDL_GetTrayEntryEnabled.argtypes = [ctypes.c_void_p]
SDL_GetTrayEntryEnabled.restype = ctypes.c_bool


# const char * SDL_GetTrayEntryLabel(SDL_TrayEntry *entry);
SDL_GetTrayEntryLabel = libsdl3.SDL_GetTrayEntryLabel
SDL_GetTrayEntryLabel.argtypes = [ctypes.c_void_p]
SDL_GetTrayEntryLabel.restype = ctypes.c_char_p


# SDL_TrayMenu * SDL_GetTrayEntryParent(SDL_TrayEntry *entry);
SDL_GetTrayEntryParent = libsdl3.SDL_GetTrayEntryParent
SDL_GetTrayEntryParent.argtypes = [ctypes.c_void_p]
SDL_GetTrayEntryParent.restype = ctypes.c_void_p


# SDL_TrayMenu * SDL_GetTrayMenu(SDL_Tray *tray);
SDL_GetTrayMenu = libsdl3.SDL_GetTrayMenu
SDL_GetTrayMenu.argtypes = [ctypes.c_void_p]
SDL_GetTrayMenu.restype = ctypes.c_void_p


# SDL_TrayEntry * SDL_GetTrayMenuParentEntry(SDL_TrayMenu *menu);
SDL_GetTrayMenuParentEntry = libsdl3.SDL_GetTrayMenuParentEntry
SDL_GetTrayMenuParentEntry.argtypes = [ctypes.c_void_p]
SDL_GetTrayMenuParentEntry.restype = ctypes.c_void_p


# SDL_Tray * SDL_GetTrayMenuParentTray(SDL_TrayMenu *menu);
SDL_GetTrayMenuParentTray = libsdl3.SDL_GetTrayMenuParentTray
SDL_GetTrayMenuParentTray.argtypes = [ctypes.c_void_p]
SDL_GetTrayMenuParentTray.restype = ctypes.c_void_p


# SDL_TrayMenu * SDL_GetTraySubmenu(SDL_TrayEntry *entry);
SDL_GetTraySubmenu = libsdl3.SDL_GetTraySubmenu
SDL_GetTraySubmenu.argtypes = [ctypes.c_void_p]
SDL_GetTraySubmenu.restype = ctypes.c_void_p


# SDL_TrayEntry * SDL_InsertTrayEntryAt(SDL_TrayMenu *menu, int pos, const char *label, SDL_TrayEntryFlags flags);
SDL_InsertTrayEntryAt = libsdl3.SDL_InsertTrayEntryAt
SDL_InsertTrayEntryAt.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_uint32,
]
SDL_InsertTrayEntryAt.restype = ctypes.c_void_p


# void SDL_RemoveTrayEntry(SDL_TrayEntry *entry);
SDL_RemoveTrayEntry = libsdl3.SDL_RemoveTrayEntry
SDL_RemoveTrayEntry.argtypes = [ctypes.c_void_p]
SDL_RemoveTrayEntry.restype = None


# void SDL_SetTrayEntryCallback(SDL_TrayEntry *entry, SDL_TrayCallback callback, void *userdata);
SDL_SetTrayEntryCallback = libsdl3.SDL_SetTrayEntryCallback
SDL_SetTrayEntryCallback.argtypes = [ctypes.c_void_p, SDL_TrayCallback, ctypes.c_void_p]
SDL_SetTrayEntryCallback.restype = None


# void SDL_SetTrayEntryChecked(SDL_TrayEntry *entry, bool checked);
SDL_SetTrayEntryChecked = libsdl3.SDL_SetTrayEntryChecked
SDL_SetTrayEntryChecked.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetTrayEntryChecked.restype = None


# void SDL_SetTrayEntryEnabled(SDL_TrayEntry *entry, bool enabled);
SDL_SetTrayEntryEnabled = libsdl3.SDL_SetTrayEntryEnabled
SDL_SetTrayEntryEnabled.argtypes = [ctypes.c_void_p, ctypes.c_bool]
SDL_SetTrayEntryEnabled.restype = None


# void SDL_SetTrayEntryLabel(SDL_TrayEntry *entry, const char *label);
SDL_SetTrayEntryLabel = libsdl3.SDL_SetTrayEntryLabel
SDL_SetTrayEntryLabel.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_SetTrayEntryLabel.restype = None


# void SDL_SetTrayIcon(SDL_Tray *tray, SDL_Surface *icon);
SDL_SetTrayIcon = libsdl3.SDL_SetTrayIcon
SDL_SetTrayIcon.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)]
SDL_SetTrayIcon.restype = None


# void SDL_SetTrayTooltip(SDL_Tray *tray, const char *tooltip);
SDL_SetTrayTooltip = libsdl3.SDL_SetTrayTooltip
SDL_SetTrayTooltip.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
SDL_SetTrayTooltip.restype = None


# void SDL_UpdateTrays(void);
SDL_UpdateTrays = libsdl3.SDL_UpdateTrays
SDL_UpdateTrays.argtypes = []
SDL_UpdateTrays.restype = None
