import requests 
import colorama 
from colorama import Fore
import os 
colorama.init()

os.system("title InstaChecker ~ [ Instagram Username Availability Checker ] ~ By: Biscuits")

a = f"""
{Fore.LIGHTCYAN_EX}
	██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
	██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
	██║██╔██╗ ██║███████╗   ██║   ███████║██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
	██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
	██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
	╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

		                 {Fore.LIGHTRED_EX}Made By Biscuits / @netuser on Insta{Fore.RESET}
	"""
print(a)

def checker():
	Fore.LIGHTYELLOW_EX
	username = input(f'{Fore.LIGHTYELLOW_EX} Username > ')

	req = requests.get("https://www.instagram.com/"+username)
	if req.status_code == 404:
		print(f'\n{Fore.LIGHTGREEN_EX} [+] {username.upper()} IS AVAILABLE OR BANNED{Fore.RESET}')
		again = input(f'\n{Fore.LIGHTYELLOW_EX} Do You want to test another username? [y/n]{Fore.RESET} ')
		if again == 'y':
			os.system("cls")
			print(a)
			checker()
		else:
			os.system('exit')
	elif req.status_code == 200:
		print(f'\n{Fore.LIGHTRED_EX} [-] {username.upper()} IS NOT AVAILABLE{Fore.RESET}')
		again2 = input(f'\n{Fore.LIGHTYELLOW_EX} Do You want to test another username? [y/n]{Fore.RESET} ')
		if again2 == 'y':
			os.system("cls")
			print(a)
			checker()
		else:
			os.system("exit")

checker()



