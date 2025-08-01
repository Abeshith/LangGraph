from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class ExpenseCalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.expense_calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night:str, total_days:float) -> float:
            """Calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_days)
        
        @tool
        def calculate_total_expense(*costs: float) -> float:
            """Calculate total expense of the trip"""
            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        @tool
        def format_currency(amount: float, currency_code: str = "USD") -> str:
            """Format amount with currency symbol. Supports USD ($), EUR (€), GBP (£), THB (฿), INR (₹), JPY (¥)"""
            currency_symbols = {
                "USD": "$",
                "EUR": "€", 
                "GBP": "£",
                "THB": "฿",
                "INR": "₹",
                "JPY": "¥",
                "SGD": "S$",
                "AUD": "A$",
                "CAD": "C$"
            }
            symbol = currency_symbols.get(currency_code.upper(), currency_code)
            return f"{symbol}{amount:,.2f}"
        
        @tool
        def format_expense_range(min_amount: float, max_amount: float, currency_code: str = "USD") -> str:
            """Format expense range with currency symbols (e.g., $50-$100)"""
            currency_symbols = {
                "USD": "$",
                "EUR": "€", 
                "GBP": "£",
                "THB": "฿",
                "INR": "₹",
                "JPY": "¥",
                "SGD": "S$",
                "AUD": "A$",
                "CAD": "C$"
            }
            symbol = currency_symbols.get(currency_code.upper(), currency_code)
            return f"{symbol}{min_amount:,.0f}-{symbol}{max_amount:,.0f}"
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget, format_currency, format_expense_range]