# assessment


python illumio.py flow_logs.txt lookup_table.cvs output.csv

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
