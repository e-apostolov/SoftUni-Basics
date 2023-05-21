from math import floor, ceil

m_count = int(input())
z_count = int(input())
r_count = int(input())
c_count = int(input())
present_price = float(input())

m_total_price = m_count * 3.25
z_total_price = z_count * 4.00
r_total_price = r_count * 3.50
c_total_price = c_count * 8.00

total_income = (m_total_price + z_total_price + r_total_price + c_total_price) * 0.95

diff = abs(total_income - present_price)

if total_income >= present_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f"She will have to borrow {ceil(diff)} leva.")