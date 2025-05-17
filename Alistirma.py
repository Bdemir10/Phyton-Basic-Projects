
firstnumber = input('enter the first number ')
secondnumber = input('enter the second number ')
question= input('''select the processing 
plus: (+) ,minus (-) ,multiplied (x) ,divided: (/)  ''')
if question == ('+'):
    print(+int(firstnumber) + int(secondnumber))
if question == ('-'):
    print(+int(firstnumber) - int(secondnumber))
if question == ('*'):
    print(int(firstnumber) * int(secondnumber))
if question == '/':
    print +(int(firstnumber) / int(secondnumber))
