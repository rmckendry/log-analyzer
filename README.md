# Log Analyzer
A Python script that parses log files, filters entries by timestamp, log level, or message content, and summarizes errors. Designed to demonstrate troubleshooting and log analysis skills for IT operations roles.

## Setup
1. Ensure Python 3.6+ is installed.
2. Save `test.log` with sample log entries (provided in this repository).
3. Run the script with optional arguments:
   - Filter by log level: `python analyzer.py test.log --level=ERROR`
   - Filter by timestamp: `python analyzer.py test.log --start="2025-07-14 10:00:00" --end="2025-07-14 10:02:00"`
   - Filter by message: `python analyzer.py test.log --message="timeout"`
4. Output includes filtered logs and error count; a `summary.txt` file is generated with the error count.

## Purpose
This project showcases:
- Log parsing and filtering to identify critical issues (e.g., ERROR logs).
- Command-line argument handling for flexible analysis.
- Summarization of operational issues, useful for incident reporting and documentation.
- Skills in Python programming and troubleshooting for IT operations environments.

## Code Overview
- **Language**: Python
- **Libraries**: `argparse` for command-line arguments, `datetime` for timestamp parsing
- **Functionality**:
  - Reads log files in format: `YYYY-MM-DD HH:MM:SS - LEVEL - Message`
  - Filters logs based on optional parameters (start/end time, level, message)
  - Outputs filtered logs and counts errors
  - Writes error count to `summary.txt`

## Output Example
Running `python analyzer.py test.log --level=ERROR` with the provided `test.log`:  
Filtered logs (2):  
2025-07-14 10:00:00 - ERROR - Server timeout occurred  
2025-07-14 10:02:00 - ERROR - Database connection failed  
Errors found: 2  

Generates `summary.txt` with content:  
Errors: 2  

## Job Relevance
Aligns with IT operations needs for:
- Troubleshooting system issues through log analysis
- Managing and documenting operational incidents
- Supporting tools like Jira/Confluence for knowledge base updates
