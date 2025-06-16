import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os

# Datos del cliente y del pedido
nombre_cliente = "Carlos"
producto = "Big Box Recargado"
cantidad = 3
precio_total = round(7.50 * cantidad, 3)

# Configuración del correo
from_address = "noreply@example.com"
to_address = "carlos@localhost"
subject = "🍗 Confirmación de tu pedido en KFC"

# Configurar Jinja2 para cargar la plantilla desde la carpeta 'templates'
template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("order_confirmation.html")

# Renderizar la plantilla con datos
html_template = template.render(
    nombre_cliente=nombre_cliente,
    producto=producto,
    cantidad=cantidad,
    precio_total=precio_total,
)

# Construcción del mensaje MIME
msg = MIMEMultipart("alternative")
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

# Adjuntar la parte HTML
html_part = MIMEText(html_template, "html")
msg.attach(html_part)

# Enviar correo usando MailHog (servicio docker llamado 'mailhog')
try:
    with smtplib.SMTP("mailhog", 1025) as server:
        server.send_message(msg)
    print("📨 Correo enviado correctamente a MailHog.")
except Exception as e:
    print("❌ Error al enviar correo:", e)
