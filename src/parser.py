"""
CODE PARSING & AST EXTRACTION

Purpose: Extract structural information from codebases across multiple languages.

What this file should contain:
- Tree-sitter integration for parsing Python (start with Python only for MVP)
- File system traversal (walk directory tree, filter by extensions)
- AST (Abstract Syntax Tree) extraction utilities
- Extract imports/dependencies from files
- Extract function signatures, class definitions, docstrings
- Extract decorators, type hints, and annotations
- File metadata collection (LOC, complexity metrics)
- Language detection logic (if supporting multiple languages)
- Gitignore/exclusion pattern handling (skip venv, node_modules, etc.)

Key classes/functions:
- CodebaseParser class
- parse_file(filepath) -> FileAST
- extract_functions(ast_node) -> List[Function]
- extract_classes(ast_node) -> List[Class]
- extract_imports(ast_node) -> List[Import]
- get_file_tree(root_path) -> DirectoryTree
"""
