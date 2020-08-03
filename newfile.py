def backAndForthNumbers (x): 

	number = 23 #Assigned number 
	checker = number #Chekcer for reverse of the number 
	reverse = 0  
	while number > 0: 
		digit = number % 10  #Extracting last digit of the number 
		reverse = reverse*10 + digit  #appending the digit to the reverse 
		number = number // 10  #Leave behind the last digit from the number 
	if checker == reverse:  
		# Comparing reverse to oroginal 
		print True 
	else: 
		print False  #Results 

print backAndForthNumbers(223)