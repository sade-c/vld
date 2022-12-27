from pytubeLibrary import *
from colorama import Fore # Importing colorama

from moviepy.editor import * # Importing moviepy module.
import os # importing os module
print(Fore.RED + '''
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
.       playlist den mp3 çevir         .
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.


'''+ Fore.RESET)
print(Fore.YELLOW +'''
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.
.               zinderud               .
.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.

 
'''+ Fore.RESET)

Link = str(input(Fore.BLUE + "YouTube Video  playlist adresini yaz: " + Fore.RESET)) # Requiring Link of YouTube video from user.


download_from_playlist_mp3(Link)
 
 