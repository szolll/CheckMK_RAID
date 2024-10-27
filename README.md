# RAID Status Checker Plugin for Checkmk

## Description
This Python script checks the status of RAID arrays using the mdadm utility. It provides insights into the health of each RAID array on the system.

## Workflow
1. **Scan for RAID Arrays**:
   - Executes the command `mdadm --detail --scan` to identify all RAID arrays present.

2. **Check RAID Array Existence**:
   - If no arrays are found, the script returns an error code and a corresponding message.

3. **Status Check for Each Array**:
   - For each detected RAID array:
     - Retrieves detailed status with `mdadm --detail <array_name>`.
     - Assesses the health of the array based on its reported state.
     - Collects status messages indicating whether the array is clean or has issues.

4. **Return Codes**:
   - **Code 0**: All RAID arrays are clean.
   - **Code 1**: No RAID arrays found.
   - **Code 2**: Issues detected in one or more arrays, with detailed messages included.
   - **Code 3**: An unexpected error occurred during execution.

## Usage
Run this script as a standalone program. It outputs the status code and message to the console, providing a quick overview of the RAID array health.

## Author
Daniel Sol

## Git
github.com/szolll
