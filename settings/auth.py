from cryptography.fernet import Fernet
#import os
from decouple import config

KEY= bytes(config('KEY'),'utf-8')
fernet= Fernet(KEY)