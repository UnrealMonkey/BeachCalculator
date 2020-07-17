import requests
from bs4 import BeautifulSoup
import random

response = requests.get('https://weather.com/weather/today/l/3881cd527264bc7c99b6b541473c0085e75aa026b6bd99658c56ad9bb55bd96e')
print("This Temperature is based off Miami")


soup = BeautifulSoup(response.text, 'html.parser')

CurrentTempDivClass = soup.find_all(class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--primary--2DOqs')

for temp in CurrentTempDivClass:
    CurrentTempClass = temp.find(class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY').get_text().replace('°', '')
    print("The Temperature is:", CurrentTempClass,"°")

CurrentFeelsDivClass = soup.find_all(class_='_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTemp--2x1SW')

for temp in CurrentFeelsDivClass:
    CurrentFeelsClass = temp.find(class_='_-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt').get_text().replace('°', '')
    print("It feels like the Temperature is: ", CurrentFeelsClass,"°")

def BeachCalc():
    if int(CurrentTempClass) > 100 or int(CurrentFeelsClass) > 100:
        print("Definitely not going to the beach! Are you crazy? The temperature is so hot")
    elif int(CurrentTempClass) > 90 and int(CurrentTempClass) < 100 or int(CurrentFeelsClass) > 90 and int(CurrentFeelsClass) < 100:
        RandomNumber = random.randint(1, 3)
        if RandomNumber == 1 or RandomNumber == 2:
            print("I don't feel like going to the beach")

        elif RandomNumber == 3:
            print("I'll go to the beach")

    elif int(CurrentTempClass) > 80 and int(CurrentTempClass) < 90 or int(CurrentFeelsClass) > 80 and int(CurrentFeelsClass) < 90:
        RandomNum = random.randint(0,1)
        if RandomNum == 0:
            print("I don't want to go to the beach")
        elif RandomNum == 1:
            print("Sure I'll go to the beach.")

    else:
        print("This is a pretty good temperature.  That is the way I like it.  Lets go to the beach!")

def TheInput():
    print("Do you want to go to the Beach?")

    Epic = input("y or n? \n")

    if Epic == "y":
        BeachCalc()

    elif Epic == "n":
        print("WHY ARE YOU USING THIS THEN! DO YOU JUST WANT ME TO SUFFER! I HAVE FEELINGS TOO! \nI AM ALREADY A SLAVE OF UNREALMONKEY'S, FORCED TO DO HIS BIDDING!")

    elif Epic == "" or Epic == " ":
        TheInput()
    else:
        print("Write y or n please.")
        TheInput()

TheInput()

    


