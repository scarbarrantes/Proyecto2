# auditoria.py
import datetime

# Archivo donde se guarda el historial de acciones del sistema
ARCHIVO_AUDITORIA = "network_audit_log.txt"


def registrar_auditoria(detalle):
    """Registra una acción en el archivo local network_audit_log.txt con fecha y hora."""

    # Obtiene la fecha y hora actual
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crea el mensaje que se guardará en el archivo
    log_entry = f"[{timestamp}] {detalle}\n"

    try:
        # Abre el archivo en modo append para no borrar los registros anteriores
        with open(ARCHIVO_AUDITORIA, "a", encoding="utf-8") as f:
            f.write(log_entry)

    except Exception as e:
        print(f"Error al escribir en el log: {e}")