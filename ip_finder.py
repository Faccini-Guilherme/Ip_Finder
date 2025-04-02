import re

with open ("log.txt", "r") as file: #log.txt = file with log
    logs = file.read()
ips = re.findall(r'\b(?:\d{1,3}\.) {3}\d{1,3}\b',logs)
with open ("ips_encontrados.txt","w")as output: #ips_encontrados.txt = file with found IPs 
    output.write("\n".join(ips))
print(f"{len(ips)} IPs encontrados e salvos!")
