import requests
import hashlib
import urllib.parse

def get_peers(announce_url, info_hash, peer_id, port=6681):
    params = {
        'info_hash': info_hash,
        'peer_id': peer_id.encode(),
        'port': port,
        'uploaded': 0,
        'downloaded': 0,
        'left': 0,
        'compact': 1,
    }

    response = requests.get(announce_url, params=params)
    if response.status_code == 200:
        return response.content
    else:
        print('Failed to connect to tracker')
        return None

#Usage
#peers = get_peers(announce_url, info_hash, '-PC0001-' + ''.join(str(i) for i in range(12))) 