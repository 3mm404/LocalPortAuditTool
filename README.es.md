# LocalPortAuditTool

Una herramienta de Python para auditar puertos TCP en máquinas locales y redes privadas. Diseñada para ayudar en auditorías de seguridad básicas y pruebas de servicios personalizados.

## Descripción

LocalPortAuditTool es un script en Python que:
- Realiza conexiones TCP a puertos específicos
- Recibe y muestra banners o respuestas iniciales de servicios
- Envía comandos de prueba como "help" y muestra las respuestas
- Ayuda a identificar servicios y versiones en máquinas locales o redes privadas

## Uso

```bash
python check_port.py [IP] [PUERTO]
```

Ejemplo:
```bash
python check_port.py 127.0.0.1 80
```

## Requisitos

- Python 3.x
- Biblioteca estándar de Python (no requiere instalaciones adicionales)

## Advertencias Legales

⚠️ Este script está diseñado únicamente para uso ético y legal. No debe usarse para:
- Acceder a sistemas sin autorización
- Realizar ataques o actividades maliciosas
- Violar términos de servicio o leyes locales

El uso indebido de esta herramienta puede ser ilegal. El autor no se hace responsable del uso indebido del script.

## Ejemplo de Salida

```
[*] Conectando a 127.0.0.1 en el puerto 80...
[*] Banner recibido:
HTTP/1.1 400 Bad Request
Server: Apache/2.4.41 (Ubuntu)
Date: Mon, 17 Jul 2024 04:43:01 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: 300
Connection: close

[*] Enviando comando 'help'...
[*] Respuesta recibida:
400 Bad Request
Your browser sent a request that this server could not understand.
```

## Experiencia Personal

Durante el desarrollo de esta herramienta, se descubrió un comportamiento interesante en Windows:
- MMSSHOST.exe, un servicio de Microsoft, responde a conexiones en el puerto 135 con un banner específico
- Esta herramienta puede ayudar a identificar servicios similares que podrían pasarse por alto en auditorías tradicionales

## Contribución

¡Tu contribución es bienvenida! Si encuentras bugs, tienes mejoras o quieres agregar nuevas funcionalidades:

1. Abre un issue describiendo el problema o sugerencia
2. Haz un fork del repositorio
3. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
4. Realiza tus cambios
5. Envía un pull request

## Licencia

MIT License - Copyright (c) 2025 3mm404
