from Logic.DectectorOrchestrator import DetectorOrchestrator
from Logic.Logging.ConsoleLogger import ConsoleLogger
from Logic.Logging.LoggerInterface import LoggerInterface
import sys


def handle_command_line_args(args: list[str], orchestrator: DetectorOrchestrator, logger: LoggerInterface) -> bool:
    supported_args = ['-list']
    has_supported_args = any(map(lambda argument: argument in supported_args, args))
    if not has_supported_args:
        return False
    for arg in args:
        if arg == '-list':
            ips_and_host_names = orchestrator.get_local_ip_addresses()
            logger.log('Listing IPs and PC names ---')
            for ip in ips_and_host_names.keys():
                logger.log(ip + ' : ' + ips_and_host_names[ip])
    return True


def main(args: list[str]):
    logger = ConsoleLogger(True)
    devices = get_devices_to_alert()
    try:
        orchestrator = DetectorOrchestrator(logger, devices)
        if handle_command_line_args(args, orchestrator, logger):
            return
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
