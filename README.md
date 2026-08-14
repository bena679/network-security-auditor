# network-security-auditor
Scans network to identify every device connected, checks open ports 
## Learned from Nmap (Phase 1)
- Port scans check what ports are open and listening for connections 
- Common ports like 22(SSH) and 80 (HTTP) are expected on most servers 
- Unusual ports need investigation with -sV (version detection) 
- "tcpwrapped" = something listening but not responding in identifiable way (ambiguous result)