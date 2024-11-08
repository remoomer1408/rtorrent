def save_pieces_to_disk(piece_data, file_path, offset):
    """
    Saves a downloaded piece to disk at the correct offset.
    """

with open(file_path, 'r+b') as file:
    file.seek(offset)
    file.write(piece_data)
print(f"Piece saved to {file_path} at offset{offset}.")