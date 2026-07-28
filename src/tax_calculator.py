class TaxCalculator:
    """Lowest level component: Calculates sales tax based on region."""
    
    TAX_RATES = {
        "US": 0.08,
        "EU": 0.20,
        "LATAM": 0.15
    }

    def calculate_tax(self, amount: float, region: str) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        rate = self.TAX_RATES.get(region, 0.10)
        return round(amount * rate, 2)