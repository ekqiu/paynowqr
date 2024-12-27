# PayNow QR Library
This library is a simple library to generate PayNow QR code for Singapore banks. It is written in Python and can be used to generate PayNow QR code for both personal and business accounts.

## Installation

```bash
pip install paynowqr
```

## Usage

```python
from paynowqr import PayNowQR

# Personal Account (mobile number)
qr = PayNowQR("Mobile", "+6591234567", "John Lim", 2.00, "Bubble Tea")
qr.save("paynow_personal.png")

# Business Account (UEN number)
qr = PayNowQR("UEN", "S12345678W", "Running Bananas", 1000.00, "Machine Maintainance")
qr.save("paynow_business.png")
```

## Parameters
1. **Type**: Type of PayNow account. It can be either "Mobile" or "UEN".
2. **Identifier**: Mobile number for personal account or UEN number for business account.
3. **Name**: Name of the account holder or business.
4. **Amount**: Amount to be paid.
5. **Description**: Description of the payment.

## Output
The above code will generate two QR codes, one for personal account and one for business account. The QR code will be saved as `paynow_personal.png` and `paynow_business.png` respectively.

## License
This library is released under the MIT License.