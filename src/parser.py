"""
CODE PARSING & AST EXTRACTION
Extract structural information from codebases across multiple languages.
"""

import ast
from pathlib import Path

def parse_python_file(filepath):
    try:
        source = filepath.read_text()
        tree = ast.parse(source)
    except Exception:
        return None
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return {"path": str(filepath), "imports": imports, "functions": functions}

def walk_and_parse(root_path):
    root = Path(root_path)
    exclude_dirs = {'.venv', '__pycache__', '.git'}
    parsed_files = []
    for file in root.rglob("*.py"):
        if any(part in exclude_dirs for part in file.parts):
            continue
        parsed = simple_parse_python_file(file)
        if parsed:
            parsed_files.append(parsed)
    return parsed_files
