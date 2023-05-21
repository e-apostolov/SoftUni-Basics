count_pen = int(input())
count_markers = int(input())
detergent_liters = int(input())
discount = float(input())
discount_percentage = discount/100

price_pen = 5.80
price_markers = 7.20
price_detergent = 1.20

total_price_pen = count_pen * price_pen
total_price_markers = price_markers * count_markers
total_price_detergent = price_detergent * detergent_liters

total_price = (total_price_pen + total_price_markers + total_price_detergent)
total_sum = total_price - (total_price*discount_percentage)

print(total_sum)
