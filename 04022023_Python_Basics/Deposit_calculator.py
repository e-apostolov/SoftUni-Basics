deposit_sum = float(input())
months = int(input())
yearly_int_rate = float(input())
yearly_int_rate_percent = yearly_int_rate / 100

total_sum = deposit_sum + months * ((deposit_sum * yearly_int_rate_percent) / 12)
print(total_sum)
