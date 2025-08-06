import os

input_folder = "data_input"
output_folder = "data_output"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print("✅ 'data_input' folder created. Please add .txt files to it and run the script again.")
    exit()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

summary_lines = []

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

        summary_lines.append(f"Filename: {filename}")
        summary_lines.append(f"Line count (excluding comments): {line_count}")
        summary_lines.append(f"Word count (excluding comments): {word_count}")
        summary_lines.append("")

summary_path = os.path.join(output_folder, "summary.txt")
with open(summary_path, 'w', encoding='utf-8') as summary_file:
    summary_file.write("\n".join(summary_lines))

print("✅ Processing complete. Check the 'data_output' folder for results and summary.")
