"""
Locking constants

Lock types:

- `EXCLUSIVE` exclusive lock
- `SHARED` shared lock

Lock flags:

- `NON_BLOCKING` non-blocking

Manually unlock, only needed internally

- `UNBLOCK` unlock
"""
import enum
import os
if os.name == 'nt':
    import msvcrt
    LOCK_EX = 1
    LOCK_SH = 2
    LOCK_NB = 4
    LOCK_UN = msvcrt.LK_UNLCK
elif os.name == 'posix':
    import fcntl
    LOCK_EX = fcntl.LOCK_EX
    LOCK_SH = fcntl.LOCK_SH
    LOCK_NB = fcntl.LOCK_NB
    LOCK_UN = fcntl.LOCK_UN
else:
    raise RuntimeError('PortaLocker only defined for nt and posix platforms')

class LockFlags(enum.IntFlag):
    EXCLUSIVE = LOCK_EX
    SHARED = LOCK_SH
    NON_BLOCKING = LOCK_NB
    UNBLOCK = LOCK_UN