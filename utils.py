import socket
import time

def connect_with_retry(peer_ip, peer_port, retries=3, delay=5):
    """
    Attempt to connect to a peer with retries.
    """
    attempt = 0
    while attempt < retries:
        try:
            peer_socket = connect_to_peer(peer_ip, peer_port)
            if peer_socket:
                return peer_socket
        except socket.timeout:
            print(f"Connection attempt {attempt+1} failed. Retrying..")
            time.sleep(delay)
        attempt += 1
    print(f"Failed to connect after {retries} retries.")
    return None