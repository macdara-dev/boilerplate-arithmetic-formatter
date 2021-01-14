def arithmetic_arranger(problems, display_results = False):
	# return an error if more than 5 problems are supplied
	if len(problems) > 5:
		return "Error: Too many problems."

	num1 = []
	num2 = []
	operator = ""
	num_len = []
  
	for probs in problems:
		n1, op, n2 = probs.split()

    # return an error if supplied operands are not digits
		if not n1.isdigit() or not n2.isdigit():
			return "Error: Numbers must only contain digits."

    # return an error if supplied operands are greater in length than 4 digits
    # for i in n1:
    #     if len(i) > 4:
    #     return "Error: Numbers cannot be more than four digits."

    # for i in n2:
    #     if len(i) > 4:
    #     return "Error: Numbers cannot be more than four digits."

		num1.append(n1)
		operator += op
		num2.append(n2)
		# Return the largest item in an iterable or the largest of two or more arguments.
		num_len.append(max(map(len, [n1, n2]))) 

	for i in num_len:
		if i > 4: return "Error: Numbers cannot be more than four digits."	

	# return an error if supplied operators are 'divide' or 'multiply'
	if "/" in op or "*" in op:
		return "Error: Operator must be '+' or '-'."

	for i in range(len(num1)):
		arranged_problems = ("\t".join([num1[i].rjust(num_len[i] + 2)]))

	for i in range(len(num2)):
  		arranged_problems += ("\t".join([operator[i] + " " + num2[i].rjust(num_len[i])]))

	for i in range (len(num_len)):
  		arranged_problems += ("\t".join(["-" * (num_len[i] + 2) ]))
    

    # print(ret)
	if display_results:
		arranged_problems += "\n" + "\t".join([str(eval(problems[i])).rjust(num_len[i] + 2)for i in range(len(num1))])

		return arranged_problems

    


      
   
        

  
