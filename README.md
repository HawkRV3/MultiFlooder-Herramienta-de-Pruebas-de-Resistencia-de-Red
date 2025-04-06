# 🚀 Multi-Protocol Flood Tool (ICMP, TCP, UDP)

## 📚 **Descripción**
Esta herramienta permite realizar pruebas de carga simultánea de paquetes **ICMP**, **TCP** y **UDP** contra un objetivo de forma controlada. Su objetivo es ayudar en la **evaluación de la resistencia de servidores, firewalls y configuraciones de red** bajo diferentes tipos de tráfico.

> ⚠️ **Advertencia Legal:** Este script debe usarse únicamente con fines educativos, en laboratorios de ciberseguridad controlados o en entornos con autorización explícita. El uso indebido de esta herramienta puede ser ilegal y tener consecuencias legales graves.  

---

## ⚙️ **Características**
- **Tráfico simultáneo de ICMP, TCP y UDP**.
- Personalización de la dirección IP, puertos, tamaño de carga útil y velocidad de envío.
- **Multi-hilo**: Lanza múltiples hilos de cada tipo de tráfico.
- Información en tiempo real sobre la cantidad de paquetes enviados.
- Cierre controlado de los hilos en caso de interrupciones.

---

## 📦 **Requisitos**
- **Python 3.6+**
- **Bibliotecas necesarias**: `scapy`

### 📥 **Instalación**
Clona el repositorio e instala las dependencias necesarias:
```bash
git clone https://github.com/HawkRV3/MultiFlooder-Herramienta-de-Pruebas-de-Resistencia-de-Red.git
cd MultiFlooder-Herramienta-de-Pruebas-de-Resistencia-de-Red
pip install -r requirements.txt

```
> **Nota:** El archivo `requirements.txt` debe incluir la línea:  
```
scapy
```

---

## 🚀 **Uso**
Para ejecutar la herramienta, utiliza el siguiente comando:
```bash
python3 flood_script.py -t <IP-OBJETIVO> -n <HILOS> -s <TAMAÑO> -d <DEMORA> -p <PUERTO>
```

### 🔹 **Parámetros**
| Parámetro       | Descripción                          | Valor por defecto |
|-----------------|--------------------------------------|-------------------|
| `-t, --target`  | **IP del objetivo** (obligatorio)    | -                 |
| `-n, --threads` | Número de hilos por protocolo (ICMP, TCP, UDP) | `10` |
| `-s, --size`    | Tamaño de la carga útil (en bytes)   | `14000`           |
| `-d, --delay`   | Demora entre paquetes (en segundos)  | `0.001`           |
| `-p, --port`    | Puerto de destino para TCP y UDP     | `80`              |

---

## 🔥 **Ejemplos de uso**

### 🚀 **Prueba completa**
Envía paquetes ICMP, TCP y UDP a la IP `192.168.1.1` con 10 hilos por cada protocolo, carga de 12,000 bytes por paquete, una demora de 2 ms y el puerto TCP/UDP configurado en **443**.
```bash
python3 flood_script.py -t 192.168.1.1 -n 10 -s 12000 -d 0.002 -p 443
```

---

## 📘 **Explicación del flujo**
1. **Hilos múltiples**: Se crean hilos para enviar tráfico simultáneo para cada protocolo (ICMP, TCP, UDP).  
2. **Parámetros personalizables**: Los usuarios pueden ajustar la velocidad, la cantidad de hilos, el tamaño de la carga útil y los puertos objetivo.  
3. **Monitoreo en tiempo real**: Cada 100 paquetes se muestra en la consola la cantidad de paquetes enviados por cada protocolo.  
4. **Detención manual**: El script detecta la interrupción manual (`Ctrl + C`) y cierra todos los hilos de forma segura.  

---

## 🛠️ **Personalización**
Puedes personalizar el comportamiento del script modificando los siguientes valores en el archivo:
- **Número de hilos**: Aumenta o reduce la cantidad de tráfico generado.  
- **Tamaño de la carga útil**: Modifica el tamaño de los paquetes enviados.  
- **Demora entre paquetes**: Ajusta la velocidad de envío.  

---

## 🚨 **Advertencia de Legalidad**
Este script debe utilizarse únicamente con fines **educativos y de pruebas de seguridad en entornos controlados**. No realices pruebas en sistemas sin la debida autorización, ya que esto podría violar las leyes de ciberseguridad en tu país.

**Consecuencias legales posibles**:
- **Demandas legales**: Las pruebas no autorizadas se consideran ataques.  
- **Responsabilidad financiera**: Podrías ser responsable por los daños causados.  
- **Posible encarcelamiento**: La legislación de muchos países castiga los ataques de Denegación de Servicio (DDoS).  

---

## 🔐 **Medidas de Defensa**
Para protegerte contra estos ataques, te recomendamos:  
1. **Firewalls y ACLs**: Usa un firewall (UFW, IPTables) para bloquear puertos no esenciales y limitar el tráfico.  
2. **Rate-limiting**: Implementa controles de velocidad para limitar la cantidad de paquetes ICMP, TCP y UDP permitidos por segundo.  
3. **Sistemas de detección y prevención de intrusos (IDS/IPS)**: Usa soluciones como **Snort** o **Suricata** para detectar patrones de tráfico anómalos.  
4. **Servicios de protección DDoS**: Utiliza servicios de terceros como **Cloudflare** o **AWS Shield**.  

---
