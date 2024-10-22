import os
import re

def is_valid_code_block(code):
    # Rigetta blocchi che sembrano contenere diagrammi
    diagram_pattern = r'[─│┌┐└┘→←↑↓]'
    if re.search(diagram_pattern, code):
        return False

    # Rigetta blocchi che sembrano YAML (chiavi seguite da due punti ":")
    yaml_pattern = r'^\s*\w+:\s*.*$'
    if re.search(yaml_pattern, code, re.MULTILINE):
        return False

    # Accetta blocchi che contengono prompt di shell, msf, sliver, output o comandi PHP e Windows/Powershell
    valid_prompt_pattern = r'^(sliver|msf\d+|>>|[*\[\]+]|\.\/|php|use|generate|Payload options)'
    if re.search(valid_prompt_pattern, code, re.MULTILINE):
        return True

    # Se nessun pattern corrisponde, rigetta il blocco
    return False

def extract_code_description_and_titles(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Trova tutti i blocchi di codice multi-line
    code_blocks = re.findall(r'(```.*?```)', content, re.DOTALL)
    
    # Trova tutti i blocchi di codice inline
    inline_code_blocks = re.findall(r'`([^`]+)`', content)

    result_content = ""
    remaining_content = content

    # Elabora i blocchi di codice multi-line
    for code in code_blocks:
        # Verifica se il blocco di codice è valido
        if not is_valid_code_block(code):
            continue
        
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

    # Elabora i blocchi di codice inline (con verifica della validità)
    for inline_code in inline_code_blocks:
        # Verifica se il blocco inline è valido
        if is_valid_code_block(inline_code):
            result_content += f"`{inline_code}`\n\n"

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
directory_path = './docs_tools_back'  # Specifica la tua cartella con i file markdown
process_all_markdown_files(directory_path)
