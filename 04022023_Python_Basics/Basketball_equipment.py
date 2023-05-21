yearly_tax_fixed_price = int(input())

basketball_sneakers_price = yearly_tax_fixed_price - (yearly_tax_fixed_price * 40 / 100)
basketball_kit_price = basketball_sneakers_price - (basketball_sneakers_price * 20 / 100)
basketball_ball_price = basketball_kit_price / 4
basketball_accessories_price = basketball_ball_price / 5

total_price = yearly_tax_fixed_price + basketball_sneakers_price + basketball_kit_price + basketball_ball_price + basketball_accessories_price
print(total_price)