# TTL-Based OS Detection Script

This script uses the TTL (Time to Live) value from a ping response to infer the operating system or device type of the target IP address. It's a simple yet effective way to gain insights into the remote system.

## Usage

1. Replace the `IP` variable in `detect_os_by_ttl.py` with the target IP address you want to check.
2. Run the script. It will execute a ping command and analyze the TTL value in the response to determine the OS or device type.

## Supported TTL Values

- **Windows**: TTL = 128
- **Linux/FreeBSD/OSX/Juniper/HP-UX**: TTL = 64
- **Cisco Devices**: TTL = 255
- **Solaris/AIX**: TTL = 254

## Example

To check the OS of Google's public DNS server:

```python
IP = "8.8.8.8"
# Run the script and it will output:
# "Running OS: Linux/FreeBSD/OSX/Juniper/HP-UX"
