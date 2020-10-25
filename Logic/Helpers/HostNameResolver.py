import socket

class HostNameResolver:
    @staticmethod
    def resolve_host_name_from_ipv4(ip_address: str) -> str:
        return socket.getfqdn(ip_address)
