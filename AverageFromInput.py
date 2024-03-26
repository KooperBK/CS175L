#CS175L
#Kooper Kaney
#AverageFromInput

def main():
    total = 0
    count = 0
    average = 0
    try:
        numbers = open("numbers.txt","r")
        for number in numbers:
            try:
                number = int(number.strip())
                count +=1
                total +=number
                print(f'I read in {count} number(s) Current number is:\t{number:6.2f} Total is:\t{total:6.2f}')
                if count == 3:
                    average = total / count
                    print(f'Average: {average}')
            except ValueError as baddata:
                print(f'Bad data. skipping {baddata}')

    except IOError:
        print('An error occured trying to read the file.')
        numbers.close()

if __name__ == '__main__':
    main()
    
