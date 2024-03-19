#CS175L
#Kooper Kaney
#AverageFromInput

numbers = open("numbers.txt","r")

def main():
    total = 0
    count = 0
    average = 0
    try: 
        for number in numbers:
            number = int(number.strip())
            count +=1
            total +=number
            print(f'I read in {count} number(s) Current number is:\t{number:6.2f} Total is:\t{total:6.2f}')
            if count == 3:
                average = total / count
                print(f'Average: {average}')
    except IOError:
        print('An error occured trying to read the file.')

if __name__ == '__main__':
    main()
    
