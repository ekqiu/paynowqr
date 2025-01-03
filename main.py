import typer
from typing_extensions import Annotated
from paynow import PayNowQR


def main(
    type: Annotated[
        str,
        typer.Argument(
            help="Type of PayNow account. It can be either 'Mobile' or 'UEN' "
        ),
    ],
    identifier: Annotated[
        str,
        typer.Argument(
            help="Mobile number for personal account or UEN number for business account. For Mobile, (+65) must be included."
        ),
    ],
    name: Annotated[
        str, typer.Argument(help="Name of the account holder or business.")
    ],
    amount: Annotated[float, typer.Argument(help="Amount to be paid.")],
    description: Annotated[str, typer.Argument(help="Description of the payment.")],
    expiry_date: Annotated[
        int,
        typer.Argument(help="Expiry date of the QR code. [YYYMMDD]"),
    ] = None,
    brand_colour: Annotated[
        str,
        typer.Argument(help="Colour of the PayNow logo."),
    ] = "purple",
):
    qr = PayNowQR(type, identifier, name, amount, description, expiry_date, brand_colour)
    qr.save("paynow_qr.png")


if __name__ == "__main__":
    typer.run(main)
