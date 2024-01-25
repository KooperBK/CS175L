#CS175L
#Kooper Kaney
#Stocks

comission_rate_p = float(input('Enter comission rate percentage (ex. 0.03) on stock purchase: '))
comission_rate_s = float(input('Enter comission rate percentage (ex. 0.03) on stock sale: '))
num_shares_p = int(input('Enter number of shares purchased: '))
num_shares_s = int(input('Enter number of shares sold: '))
purchase_per_share = float(input('Enter purchase price per share: '))
sell_per_share = float(input('Enter sell price per share: '))

amount_paid_stock = (num_shares_p * purchase_per_share)
comission_paid_purchase = (comission_rate_p * amount_paid_stock)
total_paid = (amount_paid_stock + comission_paid_purchase)
stock_sold_for = (num_shares_s * sell_per_share)
comission_paid_sale = (stock_sold_for * comission_rate_s)
total_sold = (stock_sold_for - comission_paid_sale)
profit_loss = (total_sold - total_paid)


print(f'Amount paid for the stock: ${amount_paid_stock:,.2f}')
print(f'Comission paid on the purchase: ${comission_paid_purchase:,.2f}')
print(f'Amount the stock sold for: ${stock_sold_for:,.2f}')
print(f'Comission paid on the sale: ${comission_paid_sale:,.2f}')
print(f'Profit (or loss if negative): ${profit_loss:,.2f}')
