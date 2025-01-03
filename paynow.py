import qrcode
from utils import calculate_crc
from PIL import Image, ImageOps


class PayNowQR:
    def __init__(self, recipient_type, recipient_id, recipient_name, amount, reference, expiry_date="", brand_colour="purple"):
        """
        Initialize the PayNowQR object.
        :param recipient_type: 'UEN' or 'MOBILE'
        :param recipient_id: UEN or mobile number
        :param recipient_name: Name of recipient
        :param amount: Transaction amount
        :param reference: Reference number
        :param exipiry_date: Expiry date of the QR code [YYYYMMDD] (optional)
        :param brand_colour: Colour of the PayNow logo (optional)
        """
        self.recipient_type = recipient_type
        self.recipient_id = recipient_id
        self.recipient_name = recipient_name
        self.amount = "{:.2f}".format(float(amount))
        self.reference = reference
        self.expiry_date = "{:08d}".format(int(expiry_date)) if expiry_date else "20991230"
        self.brand_colour = brand_colour

    def generate_payload(self):
        """
        Generate EMVCo-compliant payload for the PayNow QR code.
        """

        recipient_type_id = "2" if self.recipient_type == "UEN" else "0"

        recipient_type_id_length = f"{len(recipient_type_id):02}"
        recipient_id_length = f"{len(self.recipient_id):02}"
        amount_length = f"{len(self.amount):02}"
        reference_length = f"{len(self.reference):02}"
        recipient_name_length = f"{len(self.recipient_name):02}"
        additional_data_field_length = f"{int(reference_length) + 4:02}"
        expiry_date_length = f"{len(self.expiry_date):02}"
        print(f"Expiry Date Length: {expiry_date_length} {self.expiry_date}")
        

        merchant_account_info = (
            "0009SG.PAYNOW"
            "01"
            + recipient_type_id_length
            + recipient_type_id
            + "02"
            + recipient_id_length
            + self.recipient_id
            + "03010"
            + "04"
            + expiry_date_length
            + self.expiry_date
        )
        merchant_account_info_length = f"{len(merchant_account_info):02}"

        payload = (
            "000201"
            "010212"
            "26"
            + merchant_account_info_length
            + merchant_account_info
            + "52040000"
            + "5303702"
            + "54"
            + amount_length
            + self.amount
            + "5802SG"
            + "59"
            + recipient_name_length
            + self.recipient_name
            + "6009Singapore"
            + "62"
            + additional_data_field_length
            + "01"
            + reference_length
            + self.reference
        )
        checksum = calculate_crc(payload + "6304")

        return payload + "6304" + checksum

    def save(self, output_file="paynow_qr.png"):
        """
        Generate the PayNow QR code image.
        :param output_file: Output file name
        """
        payload = self.generate_payload()
        print(f"Payload: {payload}")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.brand_colour, back_color="white").convert("RGB")

        logo = Image.open("paynow-logo.png")
        logo = logo.resize((1000, 450), Image.LANCZOS)

        img_w, img_h = img.size
        expanded_img = ImageOps.expand(
            img, border=(img_w // 5, img_h // 5), fill="white"
        )

        pos = ((expanded_img.size[0] - logo.size[0]) // 2, expanded_img.size[1] - 320)
        expanded_img.paste(logo, pos, logo)

        expanded_img.save(output_file)
        print(f"QR code saved as {output_file}")
