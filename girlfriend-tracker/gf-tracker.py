import sys, subprocess


linux_terminal_code = str(subprocess.run(['ifconfig'],  capture_output=True))

linux_code_to_python_string = linux_terminal_code.split()

for single_string in linux_code_to_python_string:
    if '.' in single_string:
        if len(single_string) == 14:
            ip_adress = single_string[:12] + '0/24'
    else:
        pass

nmap_with_ip_adress = str(subprocess.run(['nmap', '-sn' , ip_adress ], capture_output=True))

nmap_and_ip = nmap_with_ip_adress.split()

print(nmap_and_ip)

for nmap_output in nmap_and_ip:
    if 'Cierras-iPhone.home' in nmap_output:
        print('cierra is home')
    else:
        pass
