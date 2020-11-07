from Logic.Helpers.Beeper import Beeper
from Logic.Helpers.HostNameResolver import HostNameResolver
from Logic.Logging.LoggerInterface import LoggerInterface
from Logic.NetworkIPAddressAccessor import NetworkIPAddressAccessor


class DetectorOrchestrator:
    def __init__(self, logger: LoggerInterface, devices_to_alert_on: list[str] = None):
        self.__devices_to_alert_on = devices_to_alert_on
        self.__logger = logger
        self.__network_devices: dict = None
        self.__existing_devices: dict = dict()

    def set_devices_to_alert_on(self, devices_to_alert_on: list[str]) -> None:
         self.__devices_to_alert_on = devices_to_alert_on

    def get_local_ip_addresses(self) -> dict[str, str]:
        device_ips = NetworkIPAddressAccessor.get_network_ip_addresses()
        self.__network_devices = dict()
        for ip in device_ips:
            self.__network_devices[ip] = HostNameResolver.resolve_host_name_from_ipv4(ip)
        return self.__network_devices

    def detect(self):
        if self.__network_devices is None:
            list_of_ips: list[str] = NetworkIPAddressAccessor.get_network_ip_addresses()
            host_names: list[str] = list(map(HostNameResolver.resolve_host_name_from_ipv4, list_of_ips))
        else:
            host_names = list(self.__network_devices.values())

        devices_to_alert_dict = dict.fromkeys(self.__devices_to_alert_on, True)
        for host_name in host_names:
            if host_name in devices_to_alert_dict and host_name not in self.__existing_devices:
                Beeper.beep()
                self.__logger.log(host_name + ' found and beeped!')
            else:
                self.__logger.log(host_name + ' found but did not alert')
        self.__existing_devices = dict.fromkeys(host_names, True)
