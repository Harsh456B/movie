# import gzip
import bz2
import os
import shutil

# File path
file_path = r'C:\Users\VICTUS\Movie_project\similarity.pkl'
compressed_gzip_path = r'C:\Users\VICTUS\Movie_project\similarity_compressed.pkl.gz'
compressed_bz2_path = r'C:\Users\VICTUS\Movie_project\similarity_compressed.pkl.bz2'

# # Compressing with gzip
# with open(file_path, 'rb') as f_in:
#     with gzip.open(compressed_gzip_path, 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# Compressing with bz2
with open(file_path, 'rb') as f_in:
    with bz2.open(compressed_bz2_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# File size comparison
original_size = os.path.getsize(file_path)
# gzip_size = os.path.getsize(compressed_gzip_path)
bz2_size = os.path.getsize(compressed_bz2_path)

original_size,bz2_size
