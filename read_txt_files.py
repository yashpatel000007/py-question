import os

input_folder = "data_input"

if not os.path.exists(input_folder):
    print("❌ 'data_input' folder does not exist. Please create it first.")
    exit()

txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

if txt_files:
    print("📄 .txt files found in 'data_input':")
    for file in txt_files:
        print(f" - {file}")
else:
    print("⚠️ No .txt files found in 'data_input'.")
