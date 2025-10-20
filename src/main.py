"""
Main entry point for Silt project.

This module orchestrates the parsing, analysis, explanation, and reporting.
"""

import argparse
from parser import parse_file, parse_directory
from analyzer import analyze_code_structure, detect_patterns
from llm_explainer import explain_module_purpose, explain_code_patterns
from report_generator import generate_markdown_report, save_report


def main():
    """
    Main function to run the Silt application.
    """
    parser = argparse.ArgumentParser(description='Silt - Code Analysis and Explanation Tool')
    parser.add_argument('path', help='Path to file or directory to analyze')
    parser.add_argument('-o', '--output', default='report.md', help='Output report path')
    
    args = parser.parse_args()
    
    # Parse
    print(f"Parsing {args.path}...")
    parsed_data = parse_file(args.path)
    
    # Analyze
    print("Analyzing code structure...")
    analysis = analyze_code_structure(parsed_data)
    patterns = detect_patterns(parsed_data)
    
    # Explain
    print("Generating explanations...")
    explanations = {
        'purpose': explain_module_purpose(parsed_data),
        'patterns': explain_code_patterns(patterns)
    }
    
    # Report
    print("Generating report...")
    report = generate_markdown_report(analysis, explanations)
    save_report(report, args.output)
    
    print(f"Report saved to {args.output}")


if __name__ == '__main__':
    main()
