# Module to create a file
file {'/tmp/holberton':
	ensure  => file,
        path    => '/tmp/holberton',
        mode    => '0744',
        group   => 'www-data',
        owner   => 'www-data',
        content => 'I love Puppet',
        }
