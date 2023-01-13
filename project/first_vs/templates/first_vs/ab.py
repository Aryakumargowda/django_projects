from cryptography.fernet import Fernet

key="Fb'goFprpjsiOoXOKMBr8T256NQjTlbwh_4gCXT11ys8DA='"
key1=key.encode()
# print(key)
fernet=Fernet(key1)
mes="aryapass"
enmes=fernet.encrypt(mes)
print(enmes)