
import csv
import random
import datetime

# Configuración
NUM_REGISTROS = 10000
REGIONES = ["Norte", "Sur", "Este", "Oeste", "Centro"]
ASESORES = [
    "Juan Perez", "Maria Gomez", "Carlos Ruiz", "LUIS TORRES", "Ana Lopez", 
    "Pedro Gil", "SOFIA RAMIREZ", "lucia fernandez", "  MIGUEL ANGEL  ", "Diana  Patricia"
]
PRODUCTOS = ["Tarjeta Gold", "Credito Libranza", "Seguro Vida", "Microcredito", "CDT"]
ESTADOS = ["Aprobado", "Rechazado", "Pendiente"]

def ensuciar_texto(texto):
    """Introduce errores de formato aleatorios"""
    caso = random.randint(1, 10)
    if caso <= 3: # Mayúsculas
        return texto.upper()
    elif caso <= 5: # Minúsculas
        return texto.lower()
    elif caso <= 7: # Espacios extra
        return f"  {texto}  "
    else:
        return texto

def fecha_aleatoria():
    """Genera fecha texto o formato variada"""
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    fecha = start_date + datetime.timedelta(days=random_number_of_days)
    
    # A veces devuelve texto
    if random.random() < 0.1:
        return fecha.strftime("%d-%b-%Y") # 01-Jan-2023
    return fecha.strftime("%d/%m/%Y")

# Generar datos
datos = []
encabezados = ["ID_Transaccion", "Fecha_Venta", "Region", "Asesor_Venta", "Producto", "Monto_Venta", "Dias_Mora"]

for i in range(1, NUM_REGISTROS + 1):
    region = random.choice(REGIONES)
    asesor = ensuciar_texto(random.choice(ASESORES))
    producto = random.choice(PRODUCTOS)
    monto = random.randint(500, 50000) * 1000 # Montos en miles
    dias_mora = 0
    
    # Lógica de mora (algunos al día, otros deudores)
    if random.random() < 0.3: # 30% tiene mora
        dias_mora = random.randint(1, 120)
    
    fecha = fecha_aleatoria()
    
    # ID sucio
    id_tx = f"{i:05d}"
    
    datos.append([id_tx, fecha, region, asesor, producto, monto, dias_mora])

# Guardar CSV
ruta = "Clase_4/ventas_anuales.csv"
try:
    with open(ruta, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';') # Punto y coma para Excel latino
        writer.writerow(encabezados)
        writer.writerows(datos)
    print(f"Archivo generado exitosamente en: {ruta}")
except Exception as e:
    print(f"Error: {e}")
