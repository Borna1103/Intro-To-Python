#Borna Hemmaty     Module 2 Assignment

#This code is made as a calculator for college tuition cost over 4 years as well as the total tuition of all 4 years by usuing anual tuition increase and starting tuition

#input estimated starting tuition
Tuition = float(input('Enter starting tuition:')) 

#input annual tuition increase into 'Percent'
Increase = float(input('Enter anual tuition increase in fraction format (ex: 0.05):'))

#Calculations for every year
Year2 = str(Tuition + Increase*Tuition)
print('-------------------------\nTuition for Year 2:' + ' ' + Year2 + '$')

Year2= float(Year2)
Year3 = str(Year2 + Increase*Year2)
print('Tuition for Year 3:' + ' ' + Year3 + '$')

Year3 = float(Year3)
Year4 = str(Year3 + Increase*Year3)
print('Tuition for Year 4:' + ' ' + Year4 + '$')

#total year calculation
Year2 = float(Year2)
Year3 = float(Year3)
Year4 = float(Year4)
Total = str(Tuition+Year2+Year3+Year4)
print('Total Tuition:' + ' ' + Total + '$')
input('-------------------------\npress enter to close')