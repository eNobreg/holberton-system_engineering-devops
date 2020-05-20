# Fixes the bug
exec{ 'Install':
  command  => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
