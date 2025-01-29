# ECEN-5427-game

## Configuration

### 1. Existing Plants

In the script, you will find a list called `existing_plants`. Each entry is a dictionary with parameters like:

```python
existing_plants = [
  {
    'name': 'd1',
    'type': 'nuclear',
    'capacity_mw': 800.0,
    'reliability_pct': 93.7,
    'efficiency': 0.3353,
    'loan_payment_my_per_year': 308.1,
    'remaining_payments_yrs': 19,
    'fixed_om_my_per_year': 91.8,
    'status': 'available',
    'fuel_cost_me_per_mwh_th': 0.0,
    'variable_om_me_per_mwh': 0.0
  },
  # ... more plants ...
]
```
