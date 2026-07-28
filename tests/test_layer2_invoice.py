import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.tax_calculator import TaxCalculator
from src.invoice_service import InvoiceService


@pytest.fixture
def invoice_service():
    real_tax_calc = TaxCalculator()
    return InvoiceService(tax_calculator=real_tax_calc)

def test_bottom_up_invoice_integration(invoice_service):
    invoice = invoice_service.create_invoice(200.0, "EU")
    
    assert invoice["subtotal"] == 200.0
    assert invoice["tax"] == 40.0
    assert invoice["total"] == 240.0