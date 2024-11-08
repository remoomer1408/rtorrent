import tkinter as tk
from tkinter import filedialog, messagebox
from parse_torrent import parse_torrent
from tracker_client import get_peers
from peer_connection import connect_to_peer, send_handshake
import hashlib

class BitTorrentClientApp:
    def __init__(self,master):
        self.master = master
        master.title("Python BitTorrent Client")

        self.label = tk.Label(master, text="Select a .torrent file:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.start_button = tk.Button(master, text='Start Download', command=self.start_download)
        self.start_button.pack(pady=5)

        self.log_text = tk.Text(master, state='disabled', height=15, width=50)

        self.log_text.pack(pady=10)

        self.file_path = None

    def log_message(self,message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Torrent files", "*.torrent")])
        if self.file_path:
            self.log_message(f"Selected file: {self.file_path}")

    def start_download(self):
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select a .torrent file first") 
            return
        
        self.log_message("Parsing torrent file...")
        torrent_info = parse_torrent(self.file_path)
        info_dict = torrent_info[b'info']
        info_dict = hashlib.sha1(bencodepy.encode(info_dict)).digest()

        peer_id = '-PC0001-' + ''.join(str(i) for i in range(12))
        announce_url = torrent_info[b'announce'].decode()

        self.log_message("Connecting to tracker...")
        peers_data = get_peers(announce_url, info_hash, peer_id)
        if peers_data:
            self.log_message("Peers found. Connecting...")
            for i in range(0, len(peers_data), 6):
                ip = ".".join(str(b) for b in peers_data[i:i+4])
                port = int.from_bytes(peers_data[i+4:i+6], 'big')
                self.log_message(f"Attempting to connect to {ip}:{port}...")
                peer_socket = connect_to_peer(ip, port)
                if peer_socket:
                    self.log_message(f"Connected to {ip}:{port}. Sending handshake...")
                    send_handshake(peer_socket, info_hash, peer_id)
                    self.log_message(f"Handshake sent to {ip}:{port}.")
                    peer_socket.close()

                self.log_message(f"Finished communication with {ip}:{port}.")
        else:
            self.log_message("No peers found or failed to connect to tracker.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitTorrentClientApp(root)
    root.mainloop()
        

