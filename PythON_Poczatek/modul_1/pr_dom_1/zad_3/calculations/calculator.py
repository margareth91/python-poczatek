
def calc_investment_value(initial_value, percentage, years):
    final_value = initial_value * (1 + percentage / 100) ** years
    print(f"Po {years} latach bedziesz miec na lokacie {final_value:.2f} zl.")