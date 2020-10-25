from Logic.NetworkIPAddressAccessor import NetworkIPAddressAccessor
from Logic.Helpers.HostNameResolver import HostNameResolver
from Logic.Helpers.Beeper import Beeper

def main():
    list_of_ips = NetworkIPAddressAccessor.get_network_ip_addresses()
    host_names = map(HostNameResolver.resolve_host_name_from_ipv4, list_of_ips)
    devices_to_alert = get_devices_to_alert()
    devices_to_alert_dict = dict()
    for device in devices_to_alert:
        devices_to_alert_dict[device] = True
    for host_name in host_names:
        if host_name in devices_to_alert_dict:
            Beeper.beep()
            print(host_name + ' found and beeped!')
        else:
            print(host_name + ' found but not in alert list')


def get_devices_to_alert() -> list:
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
    main()