import csv
import qrcode
import qrcode.image.svg


def generate_svg_barcode(url, filename):
    # Create QR code instance
    qr = qrcode.QRCode(version=None, box_size=10, border=4)

    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an SVG image
    img = qr.make_image(
        fill_color="black",
        back_color="transparent",
        image_factory=qrcode.image.svg.SvgImage,
    )

    # Save the image
    img.save(filename)

def generate_png_barcode(url, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create a PNG image
    img = qr.make_image(fill_color="black", back_color="transparent")
    
    # Save the image
    img.save(filename)

# generate qr-codes for certificate's validation link for all students
endpoint = "https://cc.elouardy.com/certificate/"
csv_file = "../data/students.csv"
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        url = f"{endpoint}{row.get("code")}"
        output_file = f"../static/img/qr-codes/{row.get("name")}.png"
        generate_png_barcode(url, output_file)
        print(f"qr-code generated for {row.get("name")}")
