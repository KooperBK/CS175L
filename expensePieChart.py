#CS175L
#Kooper Kaney
#expensePieChart

import matplotlib.pyplot as plt

def main():
    slice_labels = []
    slice_prices = []
    try:
        with open('expenses.txt', 'r') as infile:
            for line in infile:
                expense, price = line.strip().split('\t')
                try:
                    price = int(price)
                    slice_labels.append(expense)
                    slice_prices.append(price)
                except ValueError as baddata:
                    print(baddata)
    except IOError as bad:
        print(bad)
    
    plt.pie(slice_prices, labels=slice_labels)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
            
    
