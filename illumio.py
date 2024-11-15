
import csv
from collections import defaultdict
import logging

# Configure logging
logging.basicConfig(
    filename='illumio.log',  # Log file name
    level=logging.INFO,            # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def load_tag_mapping():
    """
    Loads a tag mapping from a CSV file, creating a dictionary with (dstport, protocol) as the key.
    Returns: Dictionary mapping (dstport, protocol) to tags.
    """
    tag_map = {}
    filename = 'lookup_table.cvs'
    try:
        with open(filename, mode='r', newline='', encoding='ascii') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['dstport'], row['protocol'].lower())
                tag_map[key] = row['tag']
        logging.info(f"Successfully loaded tag mapping from '{filename}'.")
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
        raise
    except KeyError as e:
        logging.warning(f"Missing expected column: {e}")
    except Exception as e:
        logging.error(f"Error loading tag mapping: {e}")
        raise
    return tag_map

def read_log_file(filename):
    """
    Generator that reads the log file line by line, stripping each line.
    """
    try:
        with open(filename, mode='r', newline='', encoding='ascii') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
        raise
    except Exception as e:
        logging.error(f"Error reading log file: {e}")
        raise

def process_logs(log_lines, tag_map):
    """
    Parses each log line to extract the destination port and protocol.
    Uses the tag mapping to categorize each log entry by tag and counts occurrences.
    Returns: Two dictionaries - one with tag counts and one with port/protocol counts.
    """
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    protocol_lookup = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp'
    }
    
    try:
        for line in log_lines:
            fields = line.split()
            if len(fields) < 11:
                continue  # Skip malformed lines

            dst_port = fields[6]
            protocol = protocol_lookup.get(fields[7], 'icmp')
            if protocol == 'icmp':
                dst_port = '0'  # ICMP typically uses port 0

            key = (dst_port, protocol)

            # Increment port/protocol counts
            port_protocol_counts[key] += 1

            # Determine tag or mark as untagged if not in mapping
            tag = tag_map.get(key, 'Untagged')
            tag_counts[tag] += 1

    except ValueError as e:
        logging.error(f"ValueError: {e} on line: {line.strip()}")
        raise
    return tag_counts, port_protocol_counts

def write_results(tag_counts, port_protocol_counts, output_filename):
    """
    Writes the results to a file, displaying counts for each tag and each port/protocol pair.
    """
    try:
        with open(output_filename, mode='w', newline='', encoding='ascii') as output_file:
            # Write tag counts
            output_file.write("Tag Counts:\nTag, Count\n")
            for tag, count in tag_counts.items():
                output_file.write(f"{tag},{count}\n")
            
            # Write port/protocol combination counts
            output_file.write("\nPort/Protocol Combination Counts:\nPort, Protocol, Count\n")
            for (port, protocol), count in port_protocol_counts.items():
                output_file.write(f"{port},{protocol},{count}\n")
                
    except Exception as e:
        logging.error(f"Failed to write to output file: {e}")

def main():
    tag_map = load_tag_mapping()
    log_lines = read_log_file('flow_logs.txt')
    tag_counts, port_protocol_counts = process_logs(log_lines, tag_map)
    write_results(tag_counts, port_protocol_counts, 'output_counts.txt')

if __name__ == "__main__":
    main()




