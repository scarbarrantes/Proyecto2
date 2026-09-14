# auditoria.py
import datetime

def registrar_auditoria(detalle):
    """Registra una acción en el archivo local network_audit_log.txt con fecha y hora."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {detalle}\n"
    try:
        with open("network_audit_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error al escribir en el log: {e}")
