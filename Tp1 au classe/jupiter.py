import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Configuration
NOTEBOOK_TITLE = "TP1 Code Files - Hachem Squalli Elhoussaini"
OUTPUT_NB_NAME = "TP1_Code_Files.ipynb"

# Find all code-[number].py files in the directory
code_files = sorted([f for f in os.listdir() 
                    if f.startswith('code-') and f.endswith('.py') and not f.startswith('~$')])

# Create a new notebook
nb = new_notebook()

# Add title
nb.cells.append(new_markdown_cell(f"# {NOTEBOOK_TITLE}"))
nb.cells.append(new_markdown_cell("## Fichiers de code du TP1"))

# Function to add a Python file to the notebook
def add_python_file(filename):
    nb.cells.append(new_markdown_cell(f"### {filename}"))
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        nb.cells.append(new_code_cell(content))
    else:
        nb.cells.append(new_markdown_cell(f"⚠️ Fichier introuvable: {filename}"))

# Add all code files to the notebook in order
for code_file in code_files:
    add_python_file(code_file)
    nb.cells.append(new_markdown_cell("---"))  # Add separator between files

# Add summary
nb.cells.append(new_markdown_cell("## Résumé"))
nb.cells.append(new_markdown_cell(f"Nombre de fichiers inclus: {len(code_files)}"))
for file in code_files:
    nb.cells.append(new_markdown_cell(f"- `{file}`"))

# Save the notebook
with open(OUTPUT_NB_NAME, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print(f"Notebook créé avec succès: {OUTPUT_NB_NAME}")
print("Fichiers inclus:")
for file in code_files:
    print(f"- {file}")