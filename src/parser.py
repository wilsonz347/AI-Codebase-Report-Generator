"""
CODE PARSING & AST EXTRACTION
"""

import ast
from pathlib import Path

def parse_python_file(filepath):
    """
    Parse a Python file to extract its imports and function names.
    
    Returns:
        Dictionary with the following keys:
            - 'path': File path as a string.
            - 'imports': List of imported modules.
            - 'functions': List of function names defined in the file.
    """
    try:
        source = filepath.read_text()
        tree = ast.parse(source)
    except Exception:
        return None

    imports = []
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            for alias in node.names:
                full_name = module + '.' + alias.name if module else alias.name
                imports.append(full_name)
        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return {"path": str(filepath), "imports": imports, "functions": functions}


def walk_and_parse(root_path):
    """
    Parse all Python files, skipping files inside exclude_dirs
    
    Returns:
        List of dictionaries, each containing parsed info for a Python file.
    """
    root = Path(root_path)
    exclude_dirs = {'.venv', '__pycache__', '.git', 'node_modules'}
    parsed_files = []

    for file in root.rglob("*.py"):
        # Skip if any part of the path is in exclude_dirs
        skip = False
        for part in file.parts:
            if part in exclude_dirs:
                skip = True
                break
        if skip:
            continue

        parsed = parse_python_file(file)
        if parsed is not None:
            parsed_files.append(parsed)

    return parsed_files