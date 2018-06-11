import staticconf

from backuppy.exceptions import UnknownProtocolError
from backuppy.stores.local_backup_store import LocalBackupStore


__all__ = [
    'LocalBackupStore',
]


def get_backup_store(backup_name):
    protocol = staticconf.read_string('protocol', namespace=backup_name)
    if protocol == 'local':
        return LocalBackupStore(backup_name)
    elif protocol == 'ssh':
        raise NotImplementedError('ssh protocol not supported')
    elif protocol == 's3':
        raise NotImplementedError('s3 protocol not supported')
    else:
        raise UnknownProtocolError(f'Protocol {protocol} is not recognized')