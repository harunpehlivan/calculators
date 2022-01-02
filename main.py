
print ("Hello, I am a calculator. My name is Calca. I am here to solve your mathemetiacal operations.")

name= input("Before we get started. I just want to know your name. What is your name?\n My name is ")
print ("Hello,", name,"nice to meet you.")


while True:
    Value_1 = int(input("What is your first number of the operation?\n"))
    Value_2 = int(input("Your second number?\n"))
    print("Note- ", name, "write the next operator. Write + for addition. - for subsctraction. * for multipliacation. / for division.")
    Operator = str(input("+,-,*,/: \n"))
    print(Value_1,Operator,Value_2)
    if (Operator == "+"):
        print("Answer is:", Value_1+Value_2)
    elif (Operator == "-"):
        print("Answer is:", Value_1-Value_2)
    elif (Operator == "*"):
        print("Answer is:", Value_1*Value_2)
    elif (Operator == "/"):
        print("Answer is:", Value_1/Value_2)
    else:
        print("ERROR")
    print ("Thank you, ", name, "I had lots of fun answering your question. Thank you. Did you know that I was created to help people solve their caculation. I was created by- Nmoh Deshmukh. ")
    break