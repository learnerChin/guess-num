import random
number = random.randint(1,100)
while True:
	guess = int(input("請輸入1個整數"))
	if guess == number:
		print("終於猜對了")
		break
	elif guess < number:
		print("太小了")
	else:
		print("太大了")
 	 