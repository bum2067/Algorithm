def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))

gcd_result = gcd(num1,num2)
print("최대공약수 : ", gcd_result)