import os
import shutil

reports_dir = "reports"

if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Created directory: {reports_dir}")
else:
    print(f"Directory already exists: {reports_dir}")

txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

for file in txt_files:
    print(f"Found .txt file: {file}")

    source_path = os.path.join(os.getcwd(), file)
    destination_path = os.path.join(os.getcwd(), reports_dir, file)
    
    shutil.move(source_path, destination_path)
    print(f"Moved '{file}' to '{reports_dir}/'")
