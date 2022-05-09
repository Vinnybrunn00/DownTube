from rich.console import Console
from pyfiglet import figlet_format
from rich import print
from pytube import *
import sys
import os

if sys.platform != 'linux':
    os.system('clear')
    print('\n\nYour system is not Linux\n\n\n\n Bye!!!')
    sys.exit()

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

console = Console()
banner = figlet_format('DownTube')
style = f'[italic][bold]{banner}[/]'
style2 = f'[italic]{banner}[/]'
style3 = f'[bold]{banner}[/]'

class Downtube:
    def __init__(self):
        print(style)
        self.link = input('Video link: ')
        if len(self.link) != 28:
            os.system(limpar)
            print('[?] - [red]Your link is in trouble[/]')
            sys.exit()
        self.yt = YouTube(self.link)
        os.system(limpar)
        print(style2)
        print(
            f'[cyan][-] {self.yt.title}\n\n[/]'
            '1 - [yellow]Video quality at 360p[/]\n'
            '2 - [yellow]Video quality at 720p[/]\n'
            '3 - [yellow]Video quality at 1080 ((Without audio))[/]\n'
            '4 - [yellow]Audio in 128kbps\n'
            )
        self.option = int(input('Choose an option: '))

    def Limpar(self):
        os.system(limpar)

    def Download(self):
        if self.option == 1:     
            try:
                self.Limpar()
                print(style3)
                with console.status("Downloading...") as void:
                    baixar = self.yt.streams.get_by_itag(18)
                    baixar.download("DownTube360p")
                    check = os.system('ls | grep DownTube360p')
                    if check == 0:
                        self.Limpar()
                        print(style3)
                        print('[+] [green]Successfully downloaded :heavy_check_mark:[/]')
                    else:
                        print('Unable to complete download')
            except:
                print('Unexpected error')

        elif self.option == 2:
            try:
                self.Limpar()
                print(style3)
                with console.status("Downloading...") as void:
                    baixar = self.yt.streams.get_by_itag(22)
                    baixar.download('DownTube720p')
                    check = os.system('ls | grep DownTube720p')
                    if check == 0:
                        self.Limpar()
                        print(style3)
                        print('[+] [green]Successfully downloaded :heavy_check_mark:[/]')
                    else:
                        print('Unable to complete download')
                        
            except:
                print('Unexpected error')

        elif self.option == 3:
            try:
                self.Limpar()
                print(style3)
                with console.status("Downloading...") as void:
                    baixar = self.yt.streams.get_by_itag(137)
                    baixar.download('DownTube1080p')
                    check = os.system('ls | grep DownTube1080p')
                    if check == 0:
                        self.Limpar()
                        print(style3)
                        print('[+] [green]Successfully downloaded :heavy_check_mark:[/]')
                    else:
                        print('Unable to complete download')

            except:
                print('Unexpected error')

        elif self.option == 4:
            try:
                self.Limpar()
                print(style3)
                with console.status("Downloading...") as void:
                    baixar = self.yt.streams.get_by_itag(140)
                    baixar.download('DownTubeAUDIO')
                    check = os.system('ls | grep DownTubeAUDIO')
                    if check == 0:
                        self.Limpar()
                        print(style3)
                        print('[+] [green]Successfully downloaded :heavy_check_mark:[/]')
                    else:
                        print('Unable to complete download')
                        
            except:
                print('Unexpected error')

vini = Downtube()
vini.Limpar()
vini.Download()