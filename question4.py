import os

txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]
print(".txt files:", txt_files)
