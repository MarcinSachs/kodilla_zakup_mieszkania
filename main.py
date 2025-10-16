import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


def calculate_future_price(flat_price, annual_price_increase, years):
    """Oblicza orientacyjną cenę mieszkania za określoną liczbę lat przy założeniu liniowego wzrostu."""
    return flat_price * (1 + annual_price_increase * years)


def calculate_monthly_savings(future_price, annual_deposit_rate, years):
    """Oblicza kwotę, którą trzeba odkładać co miesiąc, aby uzbierać na mieszkanie."""
    return npf.pmt(annual_deposit_rate / 12, years * 12, 0, -future_price)


def calculate_deposit_value(monthly_savings, annual_deposit_rate, months):
    """Oblicza wartość lokaty po określonej liczbie miesięcy, uwzględniając kapitalizację."""
    deposit_values = [0]  # Początkowa wartość lokaty
    for i in range(1, months + 1):
        deposit_values.append(
            deposit_values[i-1] * (1 + annual_deposit_rate / 12) + monthly_savings)
    return deposit_values


# Variables
flat_price = 120000
annual_price_increase = 0.05
annual_deposit_rate = 0.12
years = 5
months = years * 12

# 1 - Orientacyjna cena mieszkania za 5 lat
future_price = calculate_future_price(flat_price, annual_price_increase, years)
print(
    f"Orientacyjna cena mieszkania za {years} lat (liniowy wzrost): {future_price:.2f} PLN")
# output: Orientacyjna cena mieszkania za 5 lat (liniowy wzrost): 150000.00 PLN

# 2 - Kwota, którą trzeba odłożyć co miesiąc, aby za 5 lat kupić mieszkanie
monthly_savings = calculate_monthly_savings(
    future_price, annual_deposit_rate, years)
print(
    f"Kwota, którą trzeba odłożyć co miesiąc, aby za {years} lat kupić mieszkanie: {monthly_savings:.2f} PLN")
# output: Kwota, którą trzeba odłożyć co miesiąc, aby za 5 lat kupić mieszkanie: 1836.67 PLN

# 3a - Cena mieszkania co miesiąc przez 5 lat (liniowy wzrost)
monthly_price_increase = flat_price * \
    annual_price_increase / 12  # miesieczny wzrost ceny
monthly_prices = [flat_price + i *
                  monthly_price_increase for i in range(months + 1)]

# 3b - Wartość lokaty co miesiąc
deposit_values = calculate_deposit_value(
    monthly_savings, annual_deposit_rate, months)


print("Miesiąc | Cena mieszkania (PLN) | Wartość lokaty (PLN)")
for month in range(months + 1):
    print(
        f"{month:6} | {monthly_prices[month]:20.2f} | {deposit_values[month]:17.2f}")

# Wykres
plt.figure(figsize=(12, 6))
plt.plot(monthly_prices, label='Cena mieszkania (liniowy wzrost)')
plt.plot(deposit_values, label='Wartość lokaty', linestyle='--')
plt.title('Cena mieszkania vs Wartość lokaty przez 5 lat')
plt.xlabel('Miesiące')
plt.ylabel('Kwota (PLN)')
plt.legend()
plt.grid(True)
plt.show()
# output:
