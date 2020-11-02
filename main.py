from Logic.DectectorOrchestrator import DetectorOrchestrator
from Logic.Logging.ConsoleLogger import ConsoleLogger
from Logic.Logging.LoggerInterface import LoggerInterface
from Logic.Helpers.CommandLineArgumentHandler import CommandLineArgumentHandler
import sys

def main(args: list[str]) -> None:
    logger = ConsoleLogger(True)
    orchestrator = DetectorOrchestrator(logger)
    command_line_helper = CommandLineArgumentHandler(orchestrator, logger)
    if command_line_helper.handle_arguments(args):
        return
    devices = get_devices_to_alert()
    orchestrator.set_devices_to_alert_on(devices)
    while True:
        try:
            orchestrator.start()
        finally:
            logger.publish()

def get_devices_to_alert() -> list[str]:
    try:
        file = open('./AlertOnDeviceConnectedList.txt')
        lines = file.readlines()
        # Remove lines that start with `#`
        filtered_lines = filter(lambda line: not line.startswith('#'), lines)
        return list(filtered_lines)
    except IOError:
        # File doesn't exist
        return []


if __name__ == '__main__':
    main(sys.argv)
