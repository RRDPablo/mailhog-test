import os
import qrcode
import pdfkit
from jinja2 import Environment, FileSystemLoader

def create_pdf(datos_pedido):
    # Generar QR
    qr_text = f"{datos_pedido['numero_pedido']} - {datos_pedido['nombre_cliente']} - ${datos_pedido['total']}"
    qr = qrcode.make(qr_text)

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    os.makedirs(static_dir, exist_ok=True)
    qr_path = os.path.join(static_dir, "qr.png")
    qr.save(qr_path)

    # Renderizar plantilla HTML
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("factura.html")

    html = template.render(datos=datos_pedido, qr_path=qr_path)

    # Generar PDF
    output_path = os.path.join(os.path.dirname(__file__), "pedido.pdf")
    options = { "enable-local-file-access": None }
    pdfkit.from_string(html, output_path, options=options)

    return output_path
