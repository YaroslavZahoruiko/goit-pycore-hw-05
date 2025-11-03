from collections import Counter
from pathlib import Path
from helpers.create_path import create_path
import sys


### Handle logs logic
class LogParseError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split()

    if not date or not time or not level:
        raise LogParseError("Invalid file forman")

    return {"date": date, "time": time, "level": level, "message": " ".join(message)}


def load_logs(path: Path) -> list:
    with open(path, "r") as fh:
        return [parse_log_line(line.strip()) for line in fh]


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    level = level.upper()
    return list(filter(lambda log_dict: log_dict["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict[str, int]:
    return dict(Counter(log["level"] for log in logs))


### Styling output logic
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def print_table(logs):
    columns = [f" {'Log level':<10} ", f" {'count':<5} "]
    print(columns[0] + "|" + columns[1])
    print("-" * len(columns[0]) + "|" + "-" * len(columns[1]))

    for key, value in logs.items():
        print(f" {key:<10} | {value:< 5} ")


def print_logs_details(logs):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def exit_with_error(error):
    print(error)
    sys.exit(1)


def main():
    try:
        if len(sys.argv) < 2:
            exit_with_error("Please provide file path")

        logs = load_logs(create_path(sys.argv[1]))
    except Exception as e:
        exit_with_error(e)

    print("Welcome to log helper")
    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "help":
            print("Available command:\n\r- show_count \n\r- logs_details <error level>")
        elif command == "show_count":
            print_table(count_logs_by_level(logs))
        elif command == "logs_details":
            print_logs_details(filter_logs_by_level(logs, args[0]))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
