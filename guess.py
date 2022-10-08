import random
number = random.randint(1,100)
i = 0
while True:
	guess = int(input("請輸入1個整數"))
	i += 1
	if guess == number:
		print(f"終於猜對了,總共猜了{i}次")
		break
	elif guess < number:
		print(f"太小了, 猜了{i}次")
	else:
		print(f"太大了, 猜了{i}次")
 	#print(f"這是你猜的第{i}次")