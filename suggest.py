script_version = '2.0'
relese_type = 'stable'
latest_supported_config = '2.0'
print('starting...')


import sys
import os


sys.path.append(
    f'{__file__}/..'
)

from init import config_create
import rich


rich.pretty.install()
config = config_create(
    latest_supported_config,
    script_version,
)


import bot


print(f'started bot v{script_version}')
bot.main()
