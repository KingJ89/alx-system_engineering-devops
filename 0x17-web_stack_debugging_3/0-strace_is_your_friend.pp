# Ensure proper PHP configuration for WordPress by updating wp-settings.php

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
  unless    => '/bin/grep -q "php" /var/www/html/wp-settings.php'
}
