# TLS-Compatability-Checker

Prerequisites: • nmap • Python3

Working: The script lets you test the IP addresses for the compatibility with TLS v1.0, v1.1, v1.2. The IP addresses can be given in 3 ways:
• Single IP (64.124.29.1)
• IP range (64.124.29.1 - 64.124.29.100)
• File containing list of IP addresses (If this option is selected, this script will temporarily create a new file to process data from, and then delete it when the script ends)

The script will create a .txt file containing all the IP’s found compatible with TLS 1.0 in the same directory as that of the script.
