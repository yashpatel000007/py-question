import os

input_folder = "data_input"
output_folder = "data_output"

if not os.path.exists(input_folder):
    print("❌ 'data_input' folder not found. Please create it and add .txt files first.")
    exit()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        line_count = 0
        word_count = 0
        modified_lines = []

        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip().startswith('#'):
                    continue
                line_count += 1
                word_count += len(line.strip().split())
                modified_line = line.replace("temp", "permanent")
                modified_lines.append(modified_line)

        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.writelines(modified_lines)

        print(f"✅ Processed: {filename}")
        print(f"   → Lines (excluding comments): {line_count}")
        print(f"   → Words (excluding comments): {word_count}")
