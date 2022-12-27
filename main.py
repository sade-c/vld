

from pytube import YouTube # Importing YouTube class from module pytube.
from colorama import Fore # Importing colorama

print(Fore.RED + '''
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
.              video indir             .
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
'''+ Fore.RESET)
print(Fore.YELLOW +'''
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
.               zinderud               .
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
'''+ Fore.RESET)

Link = str(input(Fore.BLUE + "video indirilecek youtube adresi " + Fore.RESET))  
yt = YouTube(Link)  
print(f"{Fore.GREEN}[MESSAGE]: yükleniyor.{Fore.RESET}")
yt.streams.first().download() 