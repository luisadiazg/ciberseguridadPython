import socket

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tiempo de espera para la conexión en segundos
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        sock.close()

    except KeyboardInterrupt:
        print("Scanning stopped by user.")
        exit()
    except socket.error:
        print("Could not connect to server.")
        exit()

def main():
    target_ip = input("Enter target IP address: ")
    ports = [int(p) for p in input("Enter ports to scan (comma-separated): ").split(",")]

    for port in ports:
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()
