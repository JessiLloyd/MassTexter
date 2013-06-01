#imports
import urllib

numberList = [] #insert numbers AS STRINGS here
newNumberList = []
deadNumberList = []

username #insert username here
password #insert password here

preStr = "http://rest.nexmo.com/sms/json?username=" + username + "&password=" + password + "&from=Anti-EDL&to="
midStr = "&text="
message = "Anti-EDL test message"

#pre-processing
for number in numberList:
    newNumber = ""
    for char in number:
        #weed out non-number chars
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            newNumber = newNumber + char
    #weed out too-short numbers
    if len(newNumber) < 10:
        deadNumberList.append(number)
    else:
        #cut down anything too long
        while len(newNumber) > 10:
            newNumber = newNumber[1:]
        #check we have a leading 7
        if newNumber[0] == "7":
            newNumberList.append("44" + newNumber)
        else:
            deadNumberList.append(number)

#send the texts!
for number in newNumberList:
    #this line does the dirty work. uncomment it only when necessary
    #urllib.urlopen(preStr + number + midStr + message)
    print 'Text sent to ' + number

#damage report
print "\nDead numbers:"
print deadNumberList
