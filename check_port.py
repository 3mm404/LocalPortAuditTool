import socket

#Example: python check_port.py 192.168.171.1:6646
ip = "192.168.171.1"
port = 6646

try:
    # Crear socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print(f"[+] Conectado a {ip}:{port}")

    # Recibir datos (si el servidor envía algo al conectar)
    data = s.recv(1024)
    print(f"[<] Respuesta inicial: {data.decode(errors='ignore')}")

    # Enviar un mensaje (puedes cambiarlo por 'help', 'status', etc.)
    s.sendall(b"help\r\n")

    response = s.recv(1024)
    print(f"[<] Respuesta tras enviar 'hello': {response.decode(errors='ignore')}")

    s.close()
except Exception as e:
    print(f"[!] Error: {e}")
