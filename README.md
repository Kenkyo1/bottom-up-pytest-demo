# Bottom Up Demo

This project is a simple demonstration of a "bottom-up" architecture in Python, where a low-level component (`TaxCalculator`) is integrated into a mid-level service (`InvoiceService`).

## Project structure

- `src/` contains the main business logic.
  - `tax_calculator.py`: calculates taxes based on the region.
  - `invoice_service.py`: creates invoices using the tax calculator.
- `tests/` contains unit and integration tests.
  - `test_layer1_tax.py`
  - `test_layer2_invoice.py`

## Requirements

- Python 3.9 or higher
- `pytest`

## Installation

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

In Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest -v
```

## Usage example

```python
from src.tax_calculator import TaxCalculator
from src.invoice_service import InvoiceService

calculator = TaxCalculator()
service = InvoiceService(calculator)

invoice = service.create_invoice(200.0, "EU")
print(invoice)
```

This example returns an invoice with subtotal, tax, and total calculated.
