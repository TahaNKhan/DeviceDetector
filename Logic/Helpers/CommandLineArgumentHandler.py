from ..DectectorOrchestrator import DetectorOrchestrator
from ..Logging.LoggerInterface import LoggerInterface

class CommandLineArgumentHandler:
    __SUPPORTED_ARGS = ['-list']
    def __init__(self, orchestrator: DetectorOrchestrator, logger: LoggerInterface) -> bool:
        self.__orchestrator = orchestrator
        self.__logger = logger
        
    def handle_arguments(self, args: list[str]):
        has_supported_args = any(map(lambda argument: argument in self.__SUPPORTED_ARGS, args))
        if not has_supported_args:
            return False
        for arg in args:
            if arg == '-list':
                ips_and_host_names = self.__orchestrator.get_local_ip_addresses()
                self.__logger.log('Listing IPs and PC names ---')
                for ip in ips_and_host_names.keys():
                    self.__logger.log(ip + ' : ' + ips_and_host_names[ip])
        return True
