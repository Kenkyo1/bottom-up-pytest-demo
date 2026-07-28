import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.tax_calculator import TaxCalculator

@pytest.fixture
def tax_calc():
    return TaxCalculator()

def test_tax_calculation_valid_region(tax_calc):
    result = tax_calc.calculate_tax(100.0, "US")
    assert result == 8.0

def test_tax_calculation_negative_amount_raises_error(tax_calc):
    with pytest.raises(ValueError):
        tax_calc.calculate_tax(-50.0, "EU")