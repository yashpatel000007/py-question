import os

input_folder = "data_input"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print("✅ 'data_input' folder created.")
    print("📂 Please add .txt files to the 'data_input' folder and run the script again.")
else:
    print("📁 'data_input' folder already exists. You can add .txt files to it.")
