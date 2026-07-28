# Bottom Up Demo

Este proyecto es una demostración simple de arquitectura "bottom-up" en Python, donde un componente de bajo nivel (`TaxCalculator`) se integra en un servicio de nivel medio (`InvoiceService`).

## Estructura del proyecto

- `src/` Contiene la lógica de negocio principal.
  - `tax_calculator.py`: calcula impuestos según la región.
  - `invoice_service.py`: crea facturas usando el calculador de impuestos.
- `tests/` Contiene las pruebas unitarias e integración.
  - `test_layer1_tax.py`
  - `test_layer2_invoice.py`

## Requisitos

- Python 3.9 o superior
- `pytest`

## Instalación

1. Crear un entorno virtual:

```bash
python -m venv .venv
```

2. Activar el entorno virtual:

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar pruebas

```bash
pytest -v
```

## Ejemplo de uso

```python
from src.tax_calculator import TaxCalculator
from src.invoice_service import InvoiceService

calculator = TaxCalculator()
service = InvoiceService(calculator)

invoice = service.create_invoice(200.0, "EU")
print(invoice)
```

Este ejemplo devuelve una factura con subtotal, impuesto y total calculados.
