# Puppet script to adjust the OS file descriptor limits for better handling of open files
# This script:
# 1. Increases the soft and hard limits for the maximum number of open files.
# 2. Ensures the PAM limits module is loaded to enforce these limits in user sessions.
# 3. Restarts the Nginx service to apply any changes related to file descriptor limits if necessary.

# Increase the maximum number of open files (soft limit)
file_line { 'increase-open-files-soft-limit':
  path  => '/etc/security/limits.conf',
  line  => '* soft nofile 4096',
  match => '^\\*\\s+soft\\s+nofile',
  notify => Exec['restart-nginx'],  # Notify to restart Nginx if this change is made
}

# Increase the maximum number of open files (hard limit)
file_line { 'increase-open-files-hard-limit':
  path  => '/etc/security/limits.conf',
  line  => '* hard nofile 8192',
  match => '^\\*\\s+hard\\s+nofile',
  notify => Exec['restart-nginx'],  # Notify to restart Nginx if this change is made
}

# Ensure the PAM limits module is loaded for user sessions
file_line { 'enable-pam-limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session required pam_limits.so',
}

file_line { 'enable-pam-limits-account':
  path  => '/etc/pam.d/common-account',
  line  => 'session required pam_limits.so',
  match => '^session required pam_limits.so',
}

# Restart Nginx to apply new system limits if needed
exec { 'restart-nginx':
  command     => '/etc/init.d/nginx restart',
  path        => ['/sbin', '/bin', '/usr/sbin', '/usr/bin'],
  refreshonly => true,  # Only run if notified by file_line resources
}

