import threading
import hashlib

def download_piece(peer_socket, piece_index):
    """
    This function will be responsible for downloading a specific piece from a peer.
    You can send requests to the peer and receive the data here.
    """
# Simulate sending request for a piece and receiving data
print(f"Downloading piece {piece_index} from peer")
# You would typically send the appropriate message to request a specific piece
# For simplicity, just simulate download with a placeholder
# peer_socket.send(piece_request_message)
# data = peer_socket.recv(1024)

print(f"Piece {piece_index} downloaded.")
# After downloading, you would need to save it to a file and validate it using SHA1.

def start_download_with_threads(peers):
    """
    This function downloads pieces concurrently from multiple peers.
    """
    threads = []
    for i, peer in enumerate(peers):
    #Create a new thread for each peer connection to download pieces concurrently
    thread = threading.Thread(target=download_piece, args=(peer, i))

    threads.append(thread)
    thread.start()

    #Wait for all threads to finish
    for thread in threads:
        thread.join()
    print("Download complete.")

def verify_piece(piece_data, expected_hash):
    """
    Verifies the downloaded piece by comparing its hash with the expected hash.
    """
    piece_hash = hashlib.sha1(piece_data).hexdigest()
    if piece_hash == expected_hash:
        print("Piece verified successfully!")
        return True
    else:
        print("Piece Verification Failed!")
        return False



# Usage
# start_download_with_threads(peer_sockets)
# Usage
# Assume `downloaded_piece` is the data received from the peer
# and `expected_piece_hash` is the expected hash of that piece.
# if verify_piece(downloaded_piece, expected_piece_hash):
# save_piece_to_disk(downloaded_piece)
