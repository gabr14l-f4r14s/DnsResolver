#!/usr/bin/python3
import socket,sys

VERDE = "\033[92m"
RESET = "\033[0m"

if len(sys.argv) <2:
	print("Modo de uso: python3 dnsResolver.py www.exemplo.com")
	sys.exit(1)

host = sys.argv[1]

while True:
	try:
		print(f"{VERDE}{host},--->, {socket.gethostbyname(host)}{RESET}")
	except socket.gaierror:
		print("Não foi possível resolver o host:", host)

	confirma = input("Deseja fazer outra resolução? (y/n): ").lower()

	if confirma == "y":
		host = input("Digite o novo host: ")
	else:
		break
		
