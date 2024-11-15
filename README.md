# assessment

# Flow Log Processor
A Python-based script for processing and analyzing flow logs to generate insights by categorizing entries and aggregating counts based on predefined mappings.

# Assessment Overview
This assessment is a Python script designed to process flow log data. It applies tags to log entries using a lookup table of destination ports and protocols, generates counts for each tag, and aggregates port/protocol combination data. Results are written to an output file in a human-readable format.

# Features
1)Tag Assignment: Assigns descriptive tags to log entries based on destination port and protocol using a configurable lookup table.

2) Count Aggregation:
Tag-based counts: Displays the total number of occurrences for each tag.

Port/Protocol counts: Displays the total occurrences of each destination port and protocol combination.

Output Files: Saves the results in an easy-to-read CSV format.

Logging: Captures important runtime events and errors for debugging purposes.
Assumptions

# Assumptions

The log file (flow_logs.txt) and lookup table (lookup_table.csv) must be located in the same directory as the script.

The log file format assumes entries are space-separated and contain expected fields.

The supported protocol values in the lookup table are limited to tcp, udp, and icmp.

Only logs in version 2 are supported.

No external libraries like pandas or numpy are used, relying solely on Python's standard libraries for simplicity and portability.

# INPUT

1) Flow Logs (flow_logs.txt)
plaintext
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
   
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
...
3) Lookup Table (lookup_table.cvs)
dstport,protocol,tag

25,tcp,sv_P1

68,udp,sv_P2

23,tcp,sv_P1

443,tcp,sv_P2

110,tcp,email

993,tcp,email

143,tcp,email

# Output 
1) Tag Counts

Tag Counts:

Tag, Count

sv_P1, 2

sv_P2, 1

email, 3

Untagged, 8


2)Port/Protocol Combination Counts

Port, Protocol, Count

443, tcp, 1

23, tcp, 1

25, tcp, 1

110, tcp, 1

993, tcp, 1

143, tcp, 1

# Steps to run

1)  Clone the github.
2)  Navigate to ṭhe directory
3)  Run this command in terminal:-

python illumio.py flow_logs.txt lookup_table.cvs output.csv
