import os

def remove_empty_markdown_files(directory):
    # Scorre tutti i file nella cartella specificata
    for filename in os.listdir(directory):
        # Controlla se il file ha l'estensione .md
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            
            # Verifica se il file è vuoto o contiene solo spazi bianchi
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if len(content) == 0:
                    os.remove(file_path)
                    print(f"File vuoto rimosso: {file_path}")

# Esegui la funzione sulla cartella desiderata
directory_path = './docs_filtrato'
remove_empty_markdown_files(directory_path)
