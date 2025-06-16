import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_templates import get_order_confirmation_template

nombre_cliente = "Carlos"
producto = "Big Box Recargado"
cantidad = 2
precio_total = round(7.50 * cantidad, 2)

from_address = "noreply@example.com"
to_address = "carlos@localhost"
subject = "🍗 Confirmación de tu pedido en KFC"

html_template = get_order_confirmation_template(nombre_cliente, producto, cantidad, precio_total)

msg = MIMEMultipart("alternative")
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

html_part = MIMEText(html_template, "html")
msg.attach(html_part)

try:
    with smtplib.SMTP("mailhog", 1025) as server:
        server.send_message(msg)
    print("📨 Correo enviado correctamente a MailHog.")
except Exception as e:
    print("❌ Error al enviar correo:", e)
