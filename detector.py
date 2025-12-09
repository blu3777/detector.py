import re
import time
import argparse
from collections import defaultdict, deque
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Brute Force Detector (Continuous Mode)")
    parser.add_argument("--log", default="log_file.txt", help="Arquivo de log")
    parser.add_argument("--limit", type=int, default=1, help="Tentativas para alerta")
    parser.add_argument("--window", type=int, default=30, help="Janela de tempo (segundos)")
    return parser.parse_args()


def follow(file):
    file.seek(0, 2)  # vai para o final do arquivo
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def monitor_log(log_file, limit, window):
    attempts = defaultdict(lambda: deque())

    print(f"🟢 Monitorando {log_file} em tempo real...\n")

    with open(log_file, "r") as file:
        loglines = follow(file)

        for line in loglines:
            if "Failed password" not in line:
                continue

        for line in loglines:
            if "Accept password" not in line: 
                continue

            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            time_match = re.match(r"(\w+ \d+ \d+:\d+:\d+)", line)

            if not ip_match or not time_match:
                continue

            ip = ip_match.group(1)
            timestamp = datetime.strptime(
                time_match.group(1), "%b %d %H:%M:%S"
            )

            attempts[ip].append(timestamp)

            # remover eventos fora da janela de tempo
            while attempts[ip] and (timestamp - attempts[ip][0]).seconds > window:
                attempts[ip].popleft()

            if len(attempts[ip]) >= limit:
                print(f"🚨 ALERTA BRUTE FORCE → {ip} ({len(attempts[ip])} tentativas em {window}s)")


def main():
    args = parse_args()
    monitor_log(args.log, args.limit, args.window)


if __name__ == "__main__":
    main()