"""
MAIN ENTRY POINT & CLI INTERFACE.
"""

import typer
import os
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console

# Load environment variables from root .env
load_dotenv()

# Initialize Typer & Rich
console = Console()
app = typer.Typer()

def validate_path(path):
    """Validate if the given path exists or if URL is valid."""
    if os.path.exists(path):
        return Path(path)
    elif path.startswith("http://") or path.startswith("https://"):
        return path
    else:
        raise ValueError(f"Invalid path or URL: {path}")
    
def load_config():
    """Load the configurations (API Keys, default settings)"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[red]Error: OPENAI_API_KEY is not set in environment[/red]")
        raise typer.Exit()
    return {"api_key": api_key, "model": os.getenv("MODEL", "gpt-3.5-turbo")}

def analyze_codebase(path, config):
    """Call parser, analyzer, LLM explainer, and report generator in sequence."""
    console.print(f"[blue]Starting analysis for {path} with model {config['model']}[/blue]")
    
    # Placeholder: parse codebase
    # parser_results = parser.parse(path)
    parser_results = "parsed_data"

    # Placeholder: obtain LLM explanations
    # explanations = llm_explainer.explain(analysis_results, config)
    explanations = "explanations"

    # Placeholder: generate report
    # report_generator.generate(explanations, output_dir)
    console.print(f"[green]Report generated successfully.[/green]")

@app.command()
def analyze(
    path: str = typer.Argument(..., help="Path to the codebase or GitHub repo URL"),
    output: str = typer.Option("reports/", help="Output directory for the report"),
    model: str = typer.Option("gpt-3.5-turbo", help="LLM model to use (GPT-4, GPT-3.5, etc.)")
):
    """Analyze a codebase and generate a structured report."""
    try:
        validated_path = validate_path(path)
        config = load_config()
        analyze_codebase(validated_path, config)
        console.print(f"[green]Reports saved to {output}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
