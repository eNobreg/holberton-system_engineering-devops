# Automatic Configuration
file_line {'no_auth':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => '	PasswordAuthentication no',
        }
file_line {'identity_file':
  ensure => 'present',
  path   => '~/.ssh/config'
  line   => '	IdentityFile ~/.ssh/holberton'
        }
