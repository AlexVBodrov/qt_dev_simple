def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    """
    for word in ignore:
        if word in command:
            return True
    return False
    """
    result = any(map(lambda x: x in command, ignore))
    return result






print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
"""
True
True
True
False
"""