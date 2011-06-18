import commands

@commands.name('trustedlogin')
def trusted_login(connection, password):
    if password in connection.protocol.trusted_passwords:
        connection.trusted = True
        return 'Logged in as trusted user.'
    return 'Invalid password.'

commands.add(airstrike)

def apply_script(protocol, connection, config):
    trusted_passwords = config.get('passwords', {}).get('trusted', [])

    class ProtectConnection(connection):
        trusted = False
    
    class ProtectProtocol(protocol):
        trusted_passwords = trusted_passwords
        
        def start_votekick(self, connection, player):
            if player.trusted:
                return 'Cannot votekick a trusted player.'
            protocol.start_votekick(self, connection, player)
        
    return ProtectProtocol, connection