# Resolve Apache 500 Internal Server Error for WordPress

# Define a custom Puppet resource to update the wp-settings.php file
exec { 'update-wordpress-settings':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin',
  logoutput => true,  # Ensures that output is logged for debugging
  unless  => '/bin/grep -q "php" /var/www/html/wp-settings.php', # Checks if the change is already applied
}
