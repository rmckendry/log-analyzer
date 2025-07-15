import argparse
from datetime import datetime

def analyze_logs(file_path, start_time=None, end_time=None, level=None, message=None):
    with open(file_path, 'r') as f:
        logs = f.readlines()
    
    filtered = []
    for log in logs:
        parts = log.strip().split(' - ', 2)
        if len(parts) < 3: continue
        timestamp_str, log_level, msg = parts
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        
        if start_time and timestamp < start_time: continue
        if end_time and timestamp > end_time: continue
        if level and log_level != level: continue
        if message and message not in msg: continue
        
        filtered.append(log)
    
    print(f"Filtered logs ({len(filtered)}):")
    for log in filtered:
        print(log.strip())
    errors = sum(1 for log in filtered if 'ERROR' in log)
    print(f"Errors found: {errors}")
    with open('summary.txt', 'w') as f:
        f.write(f"Errors: {errors}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument('file', type=str)
    parser.add_argument('--start', type=str, help='YYYY-MM-DD HH:MM:SS')
    parser.add_argument('--end', type=str, help='YYYY-MM-DD HH:MM:SS')
    parser.add_argument('--level', type=str)
    parser.add_argument('--message', type=str)
    
    args = parser.parse_args()
    start = datetime.strptime(args.start, '%Y-%m-%d %H:%M:%S') if args.start else None
    end = datetime.strptime(args.end, '%Y-%m-%d %H:%M:%S') if args.end else None
    analyze_logs(args.file, start, end, args.level, args.message)