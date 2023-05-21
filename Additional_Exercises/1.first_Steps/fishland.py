price_mackerel = float(input())
price_sprinkle = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

price_bonito = price_mackerel + (price_mackerel * 0.6)
price_safrid = price_sprinkle + (price_sprinkle * 0.8)

total_price = (price_bonito * bonito_kg) + (price_safrid * safrid_kg) + (7.50 * mussels_kg)

print(f"{total_price:.2f}")

