# This
exec { 'Install':
    command  => 'sudo apt-get update && sudo apt-get install -y nginx && sudo sed -i "17i\ \tadd_header X-Served-By \ $HOSTNAME;\n" /etc/nginx/nginx.conf && sudo service nginx restart',
    provider => shell,
}
