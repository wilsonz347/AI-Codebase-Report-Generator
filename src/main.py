"""
MAIN ENTRY POINT & CLI INTERFACE

Purpose: Command-line interface and orchestration layer for Silt.

What this file should contain:
- Typer/Click CLI setup with commands (analyze, configure, etc.)
- Argument parsing (--path, --repo, --output, --model selection)
- Input validation (check if path exists, GitHub URL format)
- Orchestration: call parser → analyzer → llm_explainer → report_generator
- Error handling and user-friendly error messages
- Rich console output for progress tracking (progress bars, status updates)
- Configuration loading (API keys, default settings)
- Main execution flow control

Key functions:
- main() or app = typer.Typer()
- analyze_command(path, output_dir, model_name)
- validate_inputs()
- setup_logging()
"""
