from .Helpers.CommandRunner import CommandRunner
import re

class NetworkIPAddressAccessor:
    @staticmethod
    def __get_ip_v4_regex():
        return r'192+\.[0-9]+[0-9]*[0-9]*\.[0-9]+[0-9]*[0-9]*\.[0-9]+[0-9]*[0-9]*'

    @staticmethod
    def get_network_ip_addresses() -> list:
        command_runner = CommandRunner('arp -a')
        command_runner.run_and_wait()
        arp_output = command_runner.get_output()
        ip_addresses = re.findall(NetworkIPAddressAccessor.__get_ip_v4_regex(), arp_output)
        return ip_addresses