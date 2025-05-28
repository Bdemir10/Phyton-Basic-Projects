print('Enter the like rate of the video')
like = int (input())
print('Enter the disslike rate of the video')
disslike =  int (input())

rating =like / (like+disslike)
rating_percentage = rating*100
print ('like rate of this video', rating_percentage)

if rating_percentage>90:
    print('this video liked')
elif rating_percentage <50:
    print('this video was not liked')
else:
    print('bu videodan nefret edildi')
