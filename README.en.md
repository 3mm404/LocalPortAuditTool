# LocalPortAuditTool

A Python tool for auditing TCP ports on local machines and private networks. Designed to assist in basic security audits and testing of custom services.

## Description

LocalPortAuditTool is a Python script that:
- Makes TCP connections to specific ports
- Receives and displays service banners or initial responses
- Sends test commands like "help" and shows the responses
- Helps identify services and versions on local machines or private networks

## Usage

```bash
python check_port.py [IP] [PORT]
```

Example:
```bash
python check_port.py 127.0.0.1 80
```

## Requirements

- Python 3.x
- Python standard library (no additional installations required)

## Legal Warnings

⚠️ This script is designed for ethical and legal use only. It should not be used to:
- Access systems without authorization
- Perform attacks or malicious activities
- Violate terms of service or local laws

Improper use of this tool may be illegal. The author is not responsible for misuse of the script.

## Example Output

```
[*] Connecting to 127.0.0.1 on port 80...
[*] Banner received:
HTTP/1.1 400 Bad Request
Server: Apache/2.4.41 (Ubuntu)
Date: Mon, 17 Jul 2024 04:43:01 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: 300
Connection: close

[*] Sending 'help' command...
[*] Response received:
400 Bad Request
Your browser sent a request that this server could not understand.
```

## Personal Experience

During the development of this tool, an interesting behavior was discovered in Windows:
- MMSSHOST.exe, a Microsoft service, responds with a specific banner on port 135
- This tool can help identify similar services that might be overlooked in traditional audits

## Contribution

Your contributions are welcome! If you find bugs, have improvements, or want to add new features:

1. Open an issue describing the problem or suggestion
2. Fork the repository
3. Create a feature branch (`git checkout -b feature/AmazingFeature`)
4. Make your changes
5. Submit a pull request

## License

MIT License - Copyright (c) 2025 3mm404
