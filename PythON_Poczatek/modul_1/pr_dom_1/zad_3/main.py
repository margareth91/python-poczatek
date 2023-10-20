
import calculations.calculator

initial_value = int(input("Jaka kwote wplacasz na lokate? "))
percentage = float(input("Jakie jest oprocentowanie lokaty? "))
years = int(input("Na ile lat chcesz wplacic pieniadze? "))

calculations.calculator.calc_investment_value(initial_value, percentage, years)
