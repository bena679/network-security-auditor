import nmap 

scanner = nmap.PortScanner()
scanner.scan('scanme.nmap.org', arguments='-sV')

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        ports = scanner[host][proto].keys()
        for port in ports:
            state = scanner[host][proto][port]['state']
            name = scanner[host][proto][port]['name']
            print(f"  Port {port}: {state} ({name})")
            