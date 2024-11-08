import sys
import hashlib
from parse_torrent import parse_torrent
from tracker_client import get_peers
from peer_connection import connect_to_peer, send_handshake

def main(torrent_path):
    torrent_info = parse_torrent(torrent_path)
    info_dict = torrent_info[b'info']
    info_hash = hashlib.sha1(bencodepy.encode(info_dict)).digest()

    peer_id = '-PC-0001' + ''.join(str(i) for i in range (12))
    announce_url = torrent_info[b'announce'].decode()

    peers_data = get_peers(announce_url, info_hash, peer_id)
    if peers_data:
        #Extract IPs and ports (compact format)
        for i in range(0, len(peers_data), 6):
            ip = ".".join(str(b) for b in peers_data[i:i+4])  # Corrected line
            port = int.from_bytes(peers_data[i+4:i+6], 'big')
            peer_socket = connect_to_peer(ip, port)
            if peer_socket:
                send_handshake(peer_socket, info_hash, peer_id)
                peer_socket.close()


if __name__=="__main__":
    if len(sys.argv) !=2:
        print("Usage: python manin.py <path/to/torrent/file")
        sys.exit(1) 

    main(sys.argv[1])
    