#CS175L
#Kooper Kaney
#TemperatureConversions

def main():
    controlLoop()

def convertToKelvin(Fahrenheit):
    Kelvin = (Fahrenheit - 32) * (5/9) + 273.15
    return Kelvin
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    #return Kelvin
    pass

def convertToCentigrade(Fahrenheit):
    Centigrade = (Fahrenheit - 32) * (5/9)
    return Centigrade
    #Convert Fahrenheit to Centigrade
    #return Centigrade
    pass

def doConversion():
    Fahrenheit = getFahrenheit()#getFahrenheit(), get back Fahrenheit
    Kelvin = convertToKelvin(Fahrenheit)#convertToKelvin(), send Fahrenheit get back Kelvin
    Centigrade = convertToCentigrade(Fahrenheit)#ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    print(f'Fahrenheit: {Fahrenheit:.2f} Kelvin: {Kelvin:.2f}, Centigrade: {Centigrade:.2f}')#prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'

def repeat():
    conversions = int(input('How many conversions would you like to do this time? '))#Inputs How many conversions would you like to do this time?
    for x in range (conversions):
        doConversion()

def controlLoop():
    looper = input('Do you want to do some conversions (Yes or No)?: ')#Inputs 'Do you want to do some conversions(Yes or No)?'
    if looper == 'yes' or looper == 'Yes' or looper == 'YES':
        repeat()

def getFahrenheit():
    while True:
        try:
            Fahrenheit = float(input('Enter Fahrenheit temperature (must be between -50 to 130): '))
            if -50.0 <= Fahrenheit <= 130.0:
                return Fahrenheit
            else:
                print('Error. Please enter a temperature from -50 through 130.')
        except ValueError:
            print('Invalid input')
        


# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
