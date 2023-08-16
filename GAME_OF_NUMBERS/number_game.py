# Aklından bi sayı tut oyunu

import random as rnd

n = rnd.randint(1,10)
count = 0
user_data = 0 

while(True):
    user_data = input ("2 TAHMİN HAKKINIZ VAR!" "\n" "Tahmininizi giriniz: ")
    count += 1
    if (int(count) == 3 ):
        if (n == user_data):
            print ("Doğru Tahmin, Tebrikler")

        else:
            print("Tahmin haklarınız bitti, kaybettiniz :(")
        break
    
    user_data = int (user_data)
    if (user_data > n):
        print("Daha küçük bir sayı tahmin edin")
    elif (user_data < n):
        print("Daha büyük bir sayı tahmin edin")
    else:
        print("Tahmininiz doğru, tebrikler!")
        print (str(count) , ". Tahminde buldunuz :)")
        break