#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL + C) to print stats."""
    print_stats()
    sys.exit(0)

# Set up signal handler for graceful exit on CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read input line by line
    for line in sys.stdin:
        try:
            # Split the line into components
            parts = line.split()
            
            # Check if the line matches the required format
            if len(parts) < 7:
                continue

            # Extract status code and file size (the last two parts)
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Accumulate file size
            total_size += file_size

            # Update the status code count if it's one of the expected ones
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Increment line counter
            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines that don't conform to the expected format
            continue

except KeyboardInterrupt:
    # Handle CTRL + C by printing the stats before exiting
    print_stats()
    sys.exit(0)
