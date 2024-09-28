import os
import typing
from . import constants, exceptions
LockFlags = constants.LockFlags

class HasFileno(typing.Protocol):
    pass
LOCKER: typing.Optional[typing.Callable[[typing.Union[int, HasFileno], int], typing.Any]] = None
if os.name == 'nt':
    import msvcrt
    import pywintypes
    import win32con
    import win32file
    import winerror
    __overlapped = pywintypes.OVERLAPPED()
elif os.name == 'posix':
    import errno
    import fcntl
    LOCKER = fcntl.flock
else:
    raise RuntimeError('PortaLocker only defined for nt and posix platforms')