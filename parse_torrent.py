import bencodepy

def parse_torrent(file_path):
    with open(file_path, 'rb') as fr:
        torrent_data = bencodepy.decode(f.read())
    return torrent_data

# Usage
# torrent_info = parse_torrent('vengeance-essential-clubsounds-vol.-5.7z_archive.torrent')