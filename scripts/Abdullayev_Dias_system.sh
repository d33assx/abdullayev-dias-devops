#!/bin/bash
# Displays student information and basic system information.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INFO_FILE="$SCRIPT_DIR/../Abdullayev_Dias_info.txt"

echo "=============================="
echo "Student Information"
echo "=============================="
echo
echo "Name: Dias"
echo "Surname: Abdullayev"
echo "Group: IT2-2313SE"
echo "Student ID: 37240"
echo
echo "=============================="
echo "System Information"
echo "=============================="
echo
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s) $(uname -r)"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
if command -v free >/dev/null 2>&1; then
    free -h                       # Linux
else
    vm_stat | head -6             # macOS has no 'free', use vm_stat
fi
echo

if [ -f "$INFO_FILE" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
