# Currency Converter App Spec

## What We're Building

A simple local currency converter. User enters an amount, selects source and target currencies, and sees the converted result instantly.

## UI Elements

- **Input field**: Enter amount (default: 100)
- **Source currency dropdown**: Select currency to convert from (default: USD)
- **Target currency dropdown**: Select currency to convert to (default: EUR)
- **Output display**: Shows converted amount (updates automatically)

## Supported Currencies

| Code | Rate (relative to USD) |
|------|------------------------|
| USD | 1.00 |
| CNY | 7.22 |
| EUR | 0.92 |
| GBP | 0.79 |
| JPY | 155.50 |

## Tech Stack

- **Framework**: Streamlit (pure Python, no HTML needed)
- **Run command**: `streamlit run app.py`

## Files

```
currency-converter/
├── app.py        # Main app (~30 lines)
└── rates.json    # Exchange rates
```

**rates.json format:**
```json
{
  "base": "USD",
  "rates": {
    "USD": 1.00,
    "CNY": 7.22,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 155.50
  }
}
```

## Conversion Formula

```
result = amount × (target_rate / source_rate)
```