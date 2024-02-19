import random

print("Şifre Oluşturucuya Hoş Geldiniz.\n")

parolaicer = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = 0
parola = ""

uzunluk = int(input("Oluşturacağımız parolanın uzunluğunu integer cinsinden girin : "))

for i in range(uzunluk):
    parola += random.choice(parolaicer)

print("Parolanız", parola, "'dır.")
                                                       
