import socket

host_name = socket.gethostname()
ip_hostname = socket.gethostbyname(host_name)

ip = ip_hostname.split('.')
bits = ''.join(ip)

bits_bin = bin(int(bits))

print("\nAdres IP:", ip_hostname)
print('Do zapisu adresu IP w systemie binarnym użyto', len(bits_bin[2:]), 'bitów.')

