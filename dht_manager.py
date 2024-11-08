def get_peers_from_multiple_trackers(trackers, info_hash, peer_id):
    all_peers = []
    for trackers in trackers: 
        peers_data = get_peers(tracker, info_hash, peer_id)
        if peers_data:
            all_peers.append(peers_data)
    return all_peers
