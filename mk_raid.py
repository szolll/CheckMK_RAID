#!/usr/bin/env python3
"""

Script to check the status of RAID arrays using the mdadm utility.

This script executes the following steps:

1. Uses the 'mdadm --detail --scan' command to identify all RAID arrays on the system.
2. Checks if any RAID arrays are found:
   - If none are found, returns an error code and message.
3. For each detected RAID array:
   - Retrieves detailed status using 'mdadm --detail <array_name>'.
   - Determines the health of the array based on its state.
   - Collects status messages for clean and problematic arrays.
4. Returns:
   - Code 0 with a message if all arrays are clean.
   - Code 1 if no RAID arrays are found.
   - Code 2 if there are issues with any arrays, along with detailed messages.
   - Code 3 for any unexpected errors encountered during execution.
   
Usage:
Run this script as a standalone program. It prints the status code and message to the console.
"""

import subprocess

def check_raid():
    try:
        scan_result = subprocess.run(['mdadm', '--detail', '--scan'], capture_output=True, text=True, check=True)
        raid_arrays = scan_result.stdout.strip()
        
        if not raid_arrays:
            return (1, "RAID - No RAID arrays found.")
        
        status_messages = []
        for array in raid_arrays.split('\n'):
            array_name = array.split()[1]
            detail_result = subprocess.run(['mdadm', '--detail', array_name], capture_output=True, text=True, check=True)
            detailed_status = detail_result.stdout.strip()
            
            if "State : clean" in detailed_status:
                status_messages.append(f"{array_name} is clean")
            else:
                state_line = next((line for line in detailed_status.split('\n') if "State :" in line), "State not found")
                status_messages.append(f"{array_name} has issues: {state_line.strip()}")
        
        if all("is clean" in msg for msg in status_messages):
            return (0, "RAID - All RAID arrays are clean.")
        else:
            return (2, f"RAID - Issues detected: {'; '.join(status_messages)}")
        
    except subprocess.CalledProcessError as e:
        return (2, f"RAID - Failed to check RAID status: {e}")
    except Exception as e:
        return (3, f"RAID - Unexpected error occurred: {e}")

if __name__ == "__main__":
    code, message = check_raid()
    print(f"{code} {message}")
