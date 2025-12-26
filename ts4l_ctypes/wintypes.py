# The most useful windows datatypes
import ts4l_ctypes

BYTE = ts4l_ctypes.c_byte
WORD = ts4l_ctypes.c_ushort
DWORD = ts4l_ctypes.c_ulong

#UCHAR = ts4l_ctypes.c_uchar
CHAR = ts4l_ctypes.c_char
WCHAR = ts4l_ctypes.c_wchar
UINT = ts4l_ctypes.c_uint
INT = ts4l_ctypes.c_int

DOUBLE = ts4l_ctypes.c_double
FLOAT = ts4l_ctypes.c_float

BOOLEAN = BYTE
BOOL = ts4l_ctypes.c_long

class VARIANT_BOOL(ts4l_ctypes._SimpleCData):
    _type_ = "v"
    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.value)

ULONG = ts4l_ctypes.c_ulong
LONG = ts4l_ctypes.c_long

USHORT = ts4l_ctypes.c_ushort
SHORT = ts4l_ctypes.c_short

# in the windows header files, these are structures.
_LARGE_INTEGER = LARGE_INTEGER = ts4l_ctypes.c_longlong
_ULARGE_INTEGER = ULARGE_INTEGER = ts4l_ctypes.c_ulonglong

LPCOLESTR = LPOLESTR = OLESTR = ts4l_ctypes.c_wchar_p
LPCWSTR = LPWSTR = ts4l_ctypes.c_wchar_p
LPCSTR = LPSTR = ts4l_ctypes.c_char_p
LPCVOID = LPVOID = ts4l_ctypes.c_void_p

# WPARAM is defined as UINT_PTR (unsigned type)
# LPARAM is defined as LONG_PTR (signed type)
if ts4l_ctypes.sizeof(ts4l_ctypes.c_long) == ts4l_ctypes.sizeof(ts4l_ctypes.c_void_p):
    WPARAM = ts4l_ctypes.c_ulong
    LPARAM = ts4l_ctypes.c_long
elif ts4l_ctypes.sizeof(ts4l_ctypes.c_longlong) == ts4l_ctypes.sizeof(ts4l_ctypes.c_void_p):
    WPARAM = ts4l_ctypes.c_ulonglong
    LPARAM = ts4l_ctypes.c_longlong

ATOM = WORD
LANGID = WORD

COLORREF = DWORD
LGRPID = DWORD
LCTYPE = DWORD

LCID = DWORD

################################################################
# HANDLE types
HANDLE = ts4l_ctypes.c_void_p # in the header files: void *

HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HDC = HANDLE
HDESK = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

################################################################
# Some important structure definitions

class RECT(ts4l_ctypes.Structure):
    _fields_ = [("left", LONG),
                ("top", LONG),
                ("right", LONG),
                ("bottom", LONG)]
tagRECT = _RECTL = RECTL = RECT

class _SMALL_RECT(ts4l_ctypes.Structure):
    _fields_ = [('Left', SHORT),
                ('Top', SHORT),
                ('Right', SHORT),
                ('Bottom', SHORT)]
SMALL_RECT = _SMALL_RECT

class _COORD(ts4l_ctypes.Structure):
    _fields_ = [('X', SHORT),
                ('Y', SHORT)]

class POINT(ts4l_ctypes.Structure):
    _fields_ = [("x", LONG),
                ("y", LONG)]
tagPOINT = _POINTL = POINTL = POINT

class SIZE(ts4l_ctypes.Structure):
    _fields_ = [("cx", LONG),
                ("cy", LONG)]
tagSIZE = SIZEL = SIZE

def RGB(red, green, blue):
    return red + (green << 8) + (blue << 16)

class FILETIME(ts4l_ctypes.Structure):
    _fields_ = [("dwLowDateTime", DWORD),
                ("dwHighDateTime", DWORD)]
_FILETIME = FILETIME

class MSG(ts4l_ctypes.Structure):
    _fields_ = [("hWnd", HWND),
                ("message", UINT),
                ("wParam", WPARAM),
                ("lParam", LPARAM),
                ("time", DWORD),
                ("pt", POINT)]
tagMSG = MSG
MAX_PATH = 260

class WIN32_FIND_DATAA(ts4l_ctypes.Structure):
    _fields_ = [("dwFileAttributes", DWORD),
                ("ftCreationTime", FILETIME),
                ("ftLastAccessTime", FILETIME),
                ("ftLastWriteTime", FILETIME),
                ("nFileSizeHigh", DWORD),
                ("nFileSizeLow", DWORD),
                ("dwReserved0", DWORD),
                ("dwReserved1", DWORD),
                ("cFileName", CHAR * MAX_PATH),
                ("cAlternateFileName", CHAR * 14)]

class WIN32_FIND_DATAW(ts4l_ctypes.Structure):
    _fields_ = [("dwFileAttributes", DWORD),
                ("ftCreationTime", FILETIME),
                ("ftLastAccessTime", FILETIME),
                ("ftLastWriteTime", FILETIME),
                ("nFileSizeHigh", DWORD),
                ("nFileSizeLow", DWORD),
                ("dwReserved0", DWORD),
                ("dwReserved1", DWORD),
                ("cFileName", WCHAR * MAX_PATH),
                ("cAlternateFileName", WCHAR * 14)]

################################################################
# Pointer types

LPBOOL = PBOOL = ts4l_ctypes.POINTER(BOOL)
PBOOLEAN = ts4l_ctypes.POINTER(BOOLEAN)
LPBYTE = PBYTE = ts4l_ctypes.POINTER(BYTE)
PCHAR = ts4l_ctypes.POINTER(CHAR)
LPCOLORREF = ts4l_ctypes.POINTER(COLORREF)
LPDWORD = PDWORD = ts4l_ctypes.POINTER(DWORD)
LPFILETIME = PFILETIME = ts4l_ctypes.POINTER(FILETIME)
PFLOAT = ts4l_ctypes.POINTER(FLOAT)
LPHANDLE = PHANDLE = ts4l_ctypes.POINTER(HANDLE)
PHKEY = ts4l_ctypes.POINTER(HKEY)
LPHKL = ts4l_ctypes.POINTER(HKL)
LPINT = PINT = ts4l_ctypes.POINTER(INT)
PLARGE_INTEGER = ts4l_ctypes.POINTER(LARGE_INTEGER)
PLCID = ts4l_ctypes.POINTER(LCID)
LPLONG = PLONG = ts4l_ctypes.POINTER(LONG)
LPMSG = PMSG = ts4l_ctypes.POINTER(MSG)
LPPOINT = PPOINT = ts4l_ctypes.POINTER(POINT)
PPOINTL = ts4l_ctypes.POINTER(POINTL)
LPRECT = PRECT = ts4l_ctypes.POINTER(RECT)
LPRECTL = PRECTL = ts4l_ctypes.POINTER(RECTL)
LPSC_HANDLE = ts4l_ctypes.POINTER(SC_HANDLE)
PSHORT = ts4l_ctypes.POINTER(SHORT)
LPSIZE = PSIZE = ts4l_ctypes.POINTER(SIZE)
LPSIZEL = PSIZEL = ts4l_ctypes.POINTER(SIZEL)
PSMALL_RECT = ts4l_ctypes.POINTER(SMALL_RECT)
LPUINT = PUINT = ts4l_ctypes.POINTER(UINT)
PULARGE_INTEGER = ts4l_ctypes.POINTER(ULARGE_INTEGER)
PULONG = ts4l_ctypes.POINTER(ULONG)
PUSHORT = ts4l_ctypes.POINTER(USHORT)
PWCHAR = ts4l_ctypes.POINTER(WCHAR)
LPWIN32_FIND_DATAA = PWIN32_FIND_DATAA = ts4l_ctypes.POINTER(WIN32_FIND_DATAA)
LPWIN32_FIND_DATAW = PWIN32_FIND_DATAW = ts4l_ctypes.POINTER(WIN32_FIND_DATAW)
LPWORD = PWORD = ts4l_ctypes.POINTER(WORD)
