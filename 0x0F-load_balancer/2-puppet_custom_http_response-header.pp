# Install
exec { 'Install':
    command  => 'sudo apt-get update && sudo apt-get install -y nginx && sudo sed -i "35i\\n\tadd_header X-Served-By $HOSTNAME;\n" /etc/nginx/sites-available/default && sudo service nginx restart',
    provider => shell,
}
