'''
Site Generation Script

This script generates a static website by copying static files from a 'static' directory,
processes markdown files in the 'content' directory into html files,
and combines them all into the 'public' directory.

Usage: python main.py

Dependancies:
    - Python 3.x
    - generate_site module (contains helper functions and modules)
    - logging module (built-in)

Configuration:
    content_dir: Directory containing markdown files for website content.
    public_dir: Directory where generated website will be placed
    static_dir: Directory containing static files (CSS, images, JavaScript)
    template_html: Path to the HTML template file for the website layout
    
Functions:
    setup_logging(output_file: str, level: int = logging.DEBUG) -> None:
        Initializes logging configuration
    
    main() -> None:
        Main entry point of script. Cleans existing public directory, copies static files,
        generates webpages from markdown files.
    
'''
from generate_site import (
    clean_directory,
    copy_directory,
    generate_pages_recursive,
)
import logging

content_dir = './content'  # The forward slash works on both *nix and Windows systems
public_dir = './public'
static_dir = './static'
template_html = './template.html'

def setup_logging(output_file: str, level: int =logging.DEBUG) -> None:
    '''
    Initializes logging configuration
    
    Arguments:
        output_file (str): Path to the output log file
        level (int): Logging level (Default: logging.DEBUG)
    
    Returns:
        None
    '''
    logging.basicConfig(filename=output_file, filemode='w', level=level)

def main():
    '''
    Main entry point of the script.
    
    Performs the following tasks:
    1. Initializes logging.
    2. Cleans the output directory
    3. Copies static files.
    4. Generates HTML pages from markdown content
    
    Returns:
        None
    '''
    setup_logging(f'output.log', logging.DEBUG)
    print('Beginning site generation process')
    clean_directory(public_dir)
    copy_directory(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_html, public_dir)
    print('Website generation complete.')

if __name__ == '__main__':
    main()