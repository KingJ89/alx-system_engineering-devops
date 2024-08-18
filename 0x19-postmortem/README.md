Postmortem Report: WordPress Outage Due to Misconfigured PHP on Apache Server

Issue Summary:

    Duration of Outage: August 19, 2024, from 07:11 AM to 07:32 AM (GMT)
    Impact: The WordPress site hosted on the Apache server was down, displaying a "500 Internal Server Error" to users. Approximately 100% of the users accessing the site during this period were affected.
    Root Cause: The root cause of the outage was a misconfiguration in the PHP settings within the wp-settings.php file, which prevented the Apache server from correctly processing PHP files.

Timeline:

    07:11 AM: The issue was detected when the monitoring system flagged a "500 Internal Server Error" on the server hosting the WordPress site.
    07:13 AM: The first response was initiated by an engineer who attempted to access the site directly and confirmed the issue.
    07:15 AM: Initial investigation began by reviewing the Apache error logs, which indicated a problem with PHP processing.
    07:18 AM: The engineer assumed the issue was related to a recent update and rolled back to the previous version of the site. This did not resolve the issue.
    07:22 AM: The issue was escalated to the web stack team, who performed a detailed review of the PHP and Apache configuration files.
    07:28 AM: It was identified that the problem was caused by a typo in the wp-settings.php file, where php was incorrectly written as phpp.
    07:30 AM: A Puppet script was executed to correct the typo in the wp-settings.php file.
    07:32 AM: The site was successfully restored, and the monitoring system confirmed that the site was back online.

Root Cause and Resolution:

    Root Cause: The issue was caused by a misconfiguration in the WordPress wp-settings.php file, where the PHP configuration directive was incorrectly spelled as phpp. This caused the Apache server to fail when attempting to process PHP files, leading to a "500 Internal Server Error" across the entire site.

    Resolution: The issue was resolved by executing a Puppet script that used the sed command to correct the typo in the wp-settings.php file. This allowed Apache to properly process PHP files, restoring the functionality of the WordPress site.

Corrective and Preventative Measures:

    Improvements:
        Implement regular audits of configuration files to catch typos and misconfigurations.
        Enhance monitoring systems to provide more detailed error messages related to server configurations.

    Tasks:
        Patch all servers to ensure they have the correct PHP configurations in place.
        Add specific monitoring alerts for PHP-related errors in Apache logs.
        Update the deployment process to include automated checks for common configuration errors in critical files like wp-settings.php.
        Provide training for the engineering team on debugging server configuration issues to reduce time to resolution.
