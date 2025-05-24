import requests
import time

API_KEY = "1F2gy34Rb5ZzTK1eR1NjWBdyYVXaSlY2"  # Reemplaza con tu token de MapQuest
BASE_URL = 'http://www.mapquestapi.com/directions/v2/route'

def obtener_datos_ruta(origen, destino):
    parametros = {
        'key': API_KEY,
        'from': origen,
        'to': destino,
        'unit': 'k'  # 'k' para kilómetros
    }
    respuesta = requests.get(BASE_URL, params=parametros)
    return respuesta.json()

def mostrar_ruta(datos):
    if datos['info']['statuscode'] != 0:
        print("Error al obtener la ruta. Verifica las ciudades.")
        return

    ruta = datos['route']
    distancia = ruta['distance']
    duracion = ruta['formattedTime']
    combustible = ruta['fuelUsed']
    narrativa = ruta['legs'][0]['narrative']

    print(f"\n📍 Distancia total: {distancia:.2f} km")
    h, m, s = map(int, duracion.split(':'))
    print(f"🕒 Duración del viaje: {h} horas, {m} minutos, {s} segundos")
    print(f"⛽ Combustible estimado: {combustible:.2f} litros")
    print(f"🗺 Narrativa del viaje: {narrativa}")

def main():
    while True:
        print("\n🔎 Consulta de Ruta - MapQuest")
        origen = input("Ingrese ciudad de origen (o 'q' para salir): ")
        if origen.lower() == 'q':
            break
        destino = input("Ingrese ciudad de destino (o 'q' para salir): ")
        if destino.lower() == 'q':
            break

        print("\nConsultando datos de la ruta...")
        datos = obtener_datos_ruta(origen, destino)
        mostrar_ruta(datos)
        time.sleep(1)

if __name__ == '__main__':
    main()