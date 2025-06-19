import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader
from generate_pdf import create_pdf

# Datos del pedido
datos_pedido = {
    "local_nombre": "KFC El Recreo",
    "direccion_local": "Av. Pedro Vicente Maldonado y Av. Morán Valverde",
    "telefono_local": "0991122334",
    "ruc_local": "1790011223001",
    "numero_pedido": "PED-001",
    "fecha_pedido": "2025-06-16",
    "nombre_cliente": "Carlos",
    "correo_cliente": "carlos@example.com",
    "direccion_cliente": "Quito, Ecuador",
    "productos": [
        {
            "nombre": "Big Box Recargado",
            "cantidad": 2,
            "precio_unitario": 7.50,
            "subtotal": round(2 * 7.50, 2)
        }
    ],
    "total": round(2 * 7.50, 2)
}

# Crear PDF
pdf_path = create_pdf(datos_pedido)

# Renderizar email
template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("email_template.html")
html_body = template.render(datos=datos_pedido)

# Enviar correo
msg = MIMEMultipart()
msg["From"] = "noreply@example.com"
msg["To"] = datos_pedido["correo_cliente"]
msg["Subject"] = f"🧾 Factura de tu pedido {datos_pedido['numero_pedido']}"

msg.attach(MIMEText(html_body, "html"))

with open(pdf_path, "rb") as f:
    pdf = MIMEApplication(f.read(), _subtype="pdf")
    pdf.add_header("Content-Disposition", "attachment", filename="pedido.pdf")
    msg.attach(pdf)

try:
    with smtplib.SMTP("mailhog", 1025) as server:
        server.send_message(msg)
    print("✅ Correo enviado correctamente.")
except Exception as e:
    print("❌ Error al enviar el correo:", e)
