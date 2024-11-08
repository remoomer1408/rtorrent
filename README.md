# rtorrent
A simple BitTorrent client built in Python with a GUI interface for practicing Python and exploring how peer-to-peer (P2P) file sharing works.


  Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

Introduction
This project is a Python-based BitTorrent client developed to understand the fundamentals of the BitTorrent protocol. It enables users to connect to peers, perform the BitTorrent handshake, and download pieces of a file through the protocol. The client also comes with a GUI for better interaction.

Features
- Connects to peers and performs BitTorrent handshakes.
- Downloads and saves pieces of a file from multiple peers.
- Displays download progress through a graphical user interface (GUI).
- Error handling for peer connection issues.

Requirements
- Python 3.7 or higher
- `bencodepy` for reading and decoding torrent files
- `tkinter` for the graphical user interface
- Basic knowledge of Python and networking concepts

Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/remoomer1408/rtorrent.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install bencodepy
   ```

Usage
1. Run the client:
   ```bash
   python gui_client.py
   ```

2. Select a `.torrent` file** and start the download process.

How It Works
- Torrent Parsing: The client reads a `.torrent` file using `bencodepy` to extract metadata such as `info_hash`, file name, and piece length.
- Peer Connection: The client connects to peers using the extracted information and performs the handshake.
- Download: Pieces of the file are requested and downloaded concurrently from different peers using threads.
- Progress Update: A `tkinter`-based GUI displays the progress of the download.

Future Enhancements
- Implement support for magnet links.
- Add peer exchange (PEX) for improved peer discovery.
- Enhance the GUI with more detailed statistics and controls.

Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. See the(LICENSE) file for more details.
