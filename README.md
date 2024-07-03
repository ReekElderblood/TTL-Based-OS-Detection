# TTL-Based OS Detection Script

This script uses the TTL (Time to Live) value from a ping response to infer the operating system or device type of the target IP address. It's a simple yet effective way to gain insights into the remote system.

## Usage
1. Run the script. It will ask for IP and it will execute a ping command and analyze the TTL value in the response to determine the OS or device type.

## Supported TTL Values

- **Windows**: TTL = 128
- **Linux/FreeBSD/OSX/Juniper/HP-UX**: TTL = 64
- **Cisco Devices**: TTL = 255
- **Solaris/AIX**: TTL = 254
- **Windows Server 2003/XP**: TTL = 252
- **Novell**: TTL = 240
- **HP-UX**: TTL = 200
- **MacOS**: TTL = 190
- **MacOS (Alternate)**: TTL = 127
- **IBM OS/2**: TTL = 100
- **AIX**: TTL = 60
- **Windows 95/98/ME**: TTL = 50
- **BSDI**: TTL = 48
- **SunOS**: TTL = 30

## Example

To check the OS of Google's public DNS server:

```python
IP = "8.8.8.8"
# Run the script and it will output:
# "Running OS: Linux/FreeBSD/OSX/Juniper/HP-UX"
