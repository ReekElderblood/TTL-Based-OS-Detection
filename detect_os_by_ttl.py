import subprocess
import re

# Define the IP address to ping.
# You can change this to any IP address you want to test.
# IP = input("Enter IP: ")
IP = "8.8.8.8"

# Regular expression pattern to capture the TTL value from the ping output.
pattern = r"TTL=(\d+)"

try:
    # Execute the ping command with the provided IP address.
    # The '-n 1' option sends only one ping request.
    # 'capture_output=True' captures the output of the command.
    # 'text=True' ensures the output is returned as a string.
    # 'check=True' raises an exception if the ping command fails.
    action = subprocess.run(['ping', IP, '-n', '1'], capture_output=True, text=True, check=True)
    
    # Store the command's output.
    result = action.stdout
    
    # Search for the TTL value in the ping output using the regular expression pattern.
    match = re.search(pattern, result)
    
    if match:
        # Extract the TTL value from the matched pattern and convert it to an integer.
        ttl_value = int(match.group(1))
        
        # Determine the operating system or device based on the TTL value.
        if ttl_value == 128:
            print("Running OS: Windows")
        elif ttl_value == 64:
            print("Running OS: Linux/FreeBSD/OSX/Juniper/HP-UX")
        elif ttl_value == 255:
            print("IP belongs to a Cisco device")
        elif ttl_value == 254:
            print("Running OS: Solaris/AIX")
        else:
            print("TTL value is not recognized, further analysis required")
    else:
        # If the TTL value is not found in the output, inform the user.
        print("Cannot detect OS, TTL value not found")
except subprocess.CalledProcessError as e:
    # Handle errors from the ping command.
    print(f"Ping failed: {e}")
