import nmap


def discover_hosts(network_range):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments='-sn')
    return scanner.all_hosts()


if __name__ == "__main__":
    devices = discover_hosts('192.168.1.0/24')
    print(f"Found {len(devices)} devices:")
    for d in devices:
        print(f"  {d}")
        