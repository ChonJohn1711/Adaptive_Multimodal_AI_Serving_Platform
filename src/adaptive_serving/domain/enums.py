from enum import Enum

class WorkerState(str, Enum):
    IDLE = 'idle'
    BUSY = 'busy'
    OFFLINE = 'offline'
