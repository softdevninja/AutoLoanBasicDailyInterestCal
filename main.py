#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Script will return daily interest rate in monetary value.  This method can later be extend for a much larger purpose. 

References: 
    https://www.wikihow.com/Calculate-Daily-Interest

"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

def main() -> None:
    """
    Script will perform calculations based on provided Principal balance owed & fixed rate.
    
    Returns:
        None: N/A
    """
    daily_rate : float = None
    annual_rate : float = None
    principal : float = None
    
    annual_rate = float(input("Provide annual interest rate: "))
    principal = float(input("Provide current principal balance: "))
    
    daily_interest_rate = get_daily_interest_rate(annual_rate)
    daily_rate = get_daily_interest(principal, daily_interest_rate)
    
    print(f'{daily_rate:.2f}$ is your current daily interest rate in monetary value.')
    
    return 0

def get_daily_interest_rate(annual_rate : float) -> float:
    """
    Formula:
        Annual Interest Rate / Days = Daily Interest

    Args:
        annual_rate (float): Fixed lender provided annual rate. 

    Returns:
        float: returns daily interest rate, 
    """
    return annual_rate / 365 

def get_daily_interest(principal : float, daily_interest_rate : float) -> float:
    """
    Formula:
        Principal * Daily Interest Rate = Daily Rate

    Args:
        principal (float): Principal value given by lender. 
        daily_interest_rate (float): Daily interest provided.  
    Returns:
        float: returns daily rate in monetary value.
    """
    return (principal * daily_interest_rate) / 100
    
if __name__ == '__main__':
    main()
    