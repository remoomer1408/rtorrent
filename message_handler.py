import struct

def request_piece(peer_socket, index, begin = 0, length=16384):
    """
    Send a request to the peer to download a specific piece.
    """
    message = struck.pack('!BIII', 6, index, begin, length) #message type 6 = request
    peer_socket.send(message)

    print(f"Requesting piece {index} from {peer_socket.getpeername()}")