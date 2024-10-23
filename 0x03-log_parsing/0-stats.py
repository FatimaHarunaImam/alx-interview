#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the statistics (total file size and count of each status code)."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) to print stats and exit."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for line in sys.stdin:
        try:
            # Split the line and extract fields
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract IP address (not used), date, request (not used), status code, and file size
            ip, _, _, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]

            # Ensure valid status code and file size
            status_code = int(status_code)
            file_size = int(file_size)

            # Update the metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines that don't match the expected format
            continue

except KeyboardInterrupt:
    # Handle manual interruption (CTRL + C)
    print_stats()
    sys.exit(0)
