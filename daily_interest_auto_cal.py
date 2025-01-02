#!/usr/bin/env python3

def main() -> int:
    daily_rate : float = None
    annual_rate : float = None
    principal : float = None
    
    annual_rate = float(input("Provide annual interest rate: "))
    principal = float(input("Provide current principal balance: "))
    
    daily_interest = get_daily_interest(annual_rate)
    daily_rate = get_daily_interest_rate(principal, daily_interest)
    
    print(f'{daily_rate:.2f}$ is your current daily interest rate in monetary value.')
    
    return 0

def get_daily_interest(annual_rate : float) -> float:
    return annual_rate / 365 

def get_daily_interest_rate(principal : float, daily_interest : float) -> float:
    return (principal * daily_interest) / 100
    
if __name__ == '__main__':
    main()
    