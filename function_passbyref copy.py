def hello(reg_name):            #here reg_name that isused in function definition is called formal argument
	print("memory location after call within function ",id(reg_name))
	print(reg_name)
	return
student="vivek"
print("memory location before call i,e before passing variable to function  ",id(student))
hello(student)          #here student that is used in function call is called actual argument
