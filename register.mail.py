email_list = []

for i in range(20):
    print('Welcome to the email subscription system')
    mail = input('Enter your email address that you would like to register with. ')
    email_list.append(mail)
    print('Congratulations, your email has been registered to the system.')

    registerlist = input('Do you want to see all registered emails in the system? E/N ')

    if registerlist.upper() == 'E':
        print('\n All Registered email addresses:')
        for index, email in enumerate(email_list):
            print(f'{index + 1 }.{email}')
    else:
        print('Thank you for registering')

input('You have seen all saved e-mails, press enter to exit.')

