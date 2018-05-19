i = 1
d_sum = 0#定义偶数和
s_sum = 0#定义奇数和
while i <= 100:
	if i%2 == 0:
		d_sum+=i
	else:
		s_sum+=i
	i+=1


print("偶数的和是%d"%d_sum)
print("奇数和是%d"%s_sum)
