from os import path
import os

print("Scanning. . .")
print("Wanna_Crypt:"+str(path.exists('WannaCry.exe')))
print("MEMZ:"+str(path.exists('MEMZ-destructive.exe')))
print("MEMZ:"+str(path.exists('MEMZ-clean.exe')))
print("MEMZ:"+str(path.exists('MEMZ-destructive.bat')))
print("MEMZ:"+str(path.exists('MEMZ-clean.bat')))
print("Virus_General:"+str(path.exists('virus.sh')))
print("Virus_General:"+str(path.exists('virus.bat')))
print("Virus_General:"+str(path.exists('virus.zvz')))
print("Virus_General:"+str(path.exists('virus.exe')))
print("Keep in mind that this antivirus scans the most well-known viruses. e.g. WannaCry, MEMZ, or just virus.exe!")
