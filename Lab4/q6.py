hrs, mins= 13, 32
secs = (hrs*3600) + (mins*60)
print('Equivalent number of seconds:', secs)

seconds=int(input('Enter the number of seconds: '))
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print("Hours:Minutes:Seconds = ",hour,minutes,seconds)
