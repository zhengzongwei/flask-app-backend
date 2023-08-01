import io
import base64
import qrcode


def generate_qrcode(data: str) -> bytes:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.make(fit=True)
    qr.add_data(data)
    img = qr.make_image()
    buf = io.BytesIO()
    img.save(buf, format('PNG'))
    image_stream = buf.getvalue()
    heximage = base64.b64encode(image_stream)
    # print('data:image/png;base64,' + heximage.decode())
    return heximage


generate_qrcode("1234")
