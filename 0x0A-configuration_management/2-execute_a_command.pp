#Kill a running process in a roundabout way
exec { 'pkill':
        command => 'pkill -f killmenow',
        path    => '/usr/bin',
        }
