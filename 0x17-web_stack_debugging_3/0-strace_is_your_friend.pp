# Ensure proper PHP configuration for WordPress by updating wp-settings.php

exec { 'correct-wordpress-config':
  command   => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path      => ['/usr/local/bin', '/bin'],
  unless    => '/bin/grep -q "php" /var/www/html/wp-settings.php', # Run only if 'php' is not found
  logoutput => true,  # Log command output for debugging
  require   => File['/var/www/html/wp-settings.php'], # Ensure the file exists before running
}

