import socket


class HostNameResolver:
    @staticmethod
    def resolve_host_name_from_ipv4(ip_address: str) -> str:
        """
        Attempt to resolve a host name from IP address.
        :param ip_address: IP address to resolve the host name for
        :return: Host name if found else the IP address
        """
        return socket.getfqdn(ip_address)
