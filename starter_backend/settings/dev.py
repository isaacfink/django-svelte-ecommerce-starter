import platform

if 'macos' in platform.platform().lower():
    from .mac_dev import *
elif 'windows' in platform.platform().lower():
    from .windows_dev import *
elif 'linux' in platform.platform().lower():
    from .linux_dev import *
