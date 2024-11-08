import hashlib
import struct

def send_handshake(peer_socket, info_hash, peer_id):
    """
    Sends a handshake to the peer to initiate communication.
    """
    # Protocol string: BitTorrent protocol
    protocol = b'BitTorrent protocol'
    pstrlen = len(protocol)
    
    # Reserved: 8 bytes set to 0
    reserved = b'\x00' * 8
    
    # Create the handshake message
    handshake_message = struct.pack(f'B{pstrlen}s8s20s20s', pstrlen, protocol, reserved, info_hash, peer_id.encode())

    # Send handshake to the peer
    peer_socket.send(handshake_message)
    print(f"Handshake sent to {peer_socket.getpeername()}")

def connect_to_peer(ip, port):
    """
    Establishes a connection with a peer and returns the socket.
    """
    import socket

    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        peer_socket.connect((ip, port))
        return peer_socket
    except socket.error as e:
        print(f"Error connecting to peer {ip}:{port} - {e}")
        return None
