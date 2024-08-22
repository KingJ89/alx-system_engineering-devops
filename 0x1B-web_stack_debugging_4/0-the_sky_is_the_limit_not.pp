# Enhancement of Nginx to Handle High Traffic Volume
# This script adjusts the ULIMIT to allow for more file descriptors,
# enhancing Nginx's capability to manage concurrent connections.

# Step 1: Increase the ULIMIT in the Nginx default configuration file
exec { 'enhance-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "15" /etc/default/nginx',  # Ensure idempotency
}

# Step 2: Restart Nginx to apply the changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => ['/sbin', '/bin', '/usr/sbin', '/usr/bin'],
  subscribe => Exec['enhance-nginx-ulimit'],  # Ensure ULIMIT is applied first
  refreshonly => true,  # Restart only if the ULIMIT change is successful
}

