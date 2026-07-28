from src.tax_calculator import TaxCalculator

class InvoiceService:
    """Mid-level component: Integrates TaxCalculator to generate total invoice."""

    def __init__(self, tax_calculator: TaxCalculator):
        self.tax_calc = tax_calculator

    def create_invoice(self, subtotal: float, region: str) -> dict:
        tax = self.tax_calc.calculate_tax(subtotal, region)
        total = round(subtotal + tax, 2)
        return {
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
            "region": region
        }