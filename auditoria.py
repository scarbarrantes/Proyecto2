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
        
        def leer_auditoria():
    """
    Vuelca el contenido completo del archivo de auditoría en consola.
    Cumple con el requisito del proyecto: opción de menú para ver el log en vivo.
    """
    if not os.path.exists(ARCHIVO_AUDITORIA):
        print("\n[Auditoría] El archivo aún no existe. No hay registros.")
        return

    with open(ARCHIVO_AUDITORIA, "r", encoding="utf-8") as f:
        contenido = f.read()

    print("\n===== HISTORIAL DE AUDITORÍA =====")
    if not contenido.strip():
        print("(El archivo está vacío)")
    else:
        print(contenido, end="")
    print("==================================")


def limpiar_auditoria():
    """Elimina el archivo de auditoría. Útil para pruebas y demostraciones."""
    if os.path.exists(ARCHIVO_AUDITORIA):
        os.remove(ARCHIVO_AUDITORIA)
        print("[Auditoría] Historial eliminado.")
    else:
        print("[Auditoría] No existe archivo para eliminar.")


# Alias para compatibilidad con módulos que importen 'log_evento'
log_evento = registrar_auditoria