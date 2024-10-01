import os
import re

def extract_code_description_and_titles(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Trova tutti i blocchi di codice
    code_blocks = re.findall(r'(```.*?```)', content, re.DOTALL)
    
    # Trova le descrizioni e i titoli immediati prima di ogni blocco di codice
    result_content = ""
    remaining_content = content

    for code in code_blocks:
        pattern = r'([\s\S]*?)(```.*?```)'  # Cattura il testo prima del blocco di codice
        match = re.search(pattern, remaining_content, re.DOTALL)
        if match:
            pre_code_text = match.group(1).strip()
            
            # Raccogli i titoli e la descrizione
            lines = pre_code_text.split("\n")
            description = ""
            for line in lines:
                if line.startswith("#"):  # Mantieni i titoli
                    result_content += f"{line}\n"
                else:
                    description = line
            
            result_content += f"{description}\n{code}\n\n"
            remaining_content = remaining_content.replace(match.group(0), '', 1)

    # Salva il risultato filtrato
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result_content)

    print(f"File filtrato salvato come: {output_file}")

def process_all_markdown_files(directory):
    # Trova tutti i file markdown nella cartella
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"filtrato_{filename}")
            print(f"Processando il file: {input_path}")
            extract_code_description_and_titles(input_path, output_path)

# Esegui la funzione sulla cartella desiderata
directory_path = './docs_tools'  # Specifica la tua cartella con i file markdown
process_all_markdown_files(directory_path)
