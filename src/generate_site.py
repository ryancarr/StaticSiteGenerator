from block_markdown import markdown_to_html_node
import logging
from os import (
    path,
    listdir,
    makedirs,
)
from shutil import (
    copy,
    rmtree,
)

def clean_directory(target: str) -> None:
    '''
    Checks if the specified target directory exists and removes it if found
    
    Args:
        target (str): The path to check
    
    Returns:
        None
    '''
    log = logging.getLogger(f'clean_directory')
    if path.exists(target):
        log.debug(f'Removing {target} directory.')
        rmtree(target)


def copy_directory(source: str, target:str) -> None:
    '''
    Recursively copy files and folders from the source path to target path
    
    Args:
        source (str): Source location to duplicate        
        target (str): Destination location for directory structure
    
    Returns:
        None
    '''
    log = logging.getLogger(f'copy_directory')
    try:
        makedirs(target)
    except Exception as e:
        log.debug('Error creating {target}: {e}')
        
    for item in listdir(source):
        source_path = path.join(source, item)
        target_path = path.join(target, item)
        if path.isfile(f'{source_path}'):
            log.debug(f'Copying {source_path} to {target_path}')
            copy(source_path, target_path)
        elif path.isdir(f'{source}/{item}'):
            copy_directory(source_path, target_path)

            
def extract_title(markdown: str) -> str:
    '''
    Extracts the title for the website from the markdown document. Requires a H1 header to be present or the document is considered invalid.
    
    Args:
        markdown (str): A string containing the entire contents of the markdown document
    
    Returns:
        str: A string containing just the header text
    '''
    for line in markdown.split('\n'):
        if not line.startswith('# '):
            raise ValueError(f'Invalid markdown format, document must start with h1 header')
        return line[2:]


def generate_page(source_path: str, template_path: str, target_path: str) -> None:
    '''
    Helper function that builds a webpage combining the template and source document and outputing it at the target location
    
    Args:
        source_path (str): Full path of the content file to convert to html        
        template_path (str): Full path of the template file to place the content into        
        target_path (str): Full path where the output html document should be saved
        
    Returns:
        None
    '''
    log = logging.getLogger(f'generate_page')
    print(f'Generating page from {source_path} to {target_path} using {template_path}')
    log.debug(f'Generating page from {source_path} to {target_path} using {template_path}')
    
    try:
        log.debug(f'Reading markdown file')
        with open(source_path, 'r') as fh:
            markdown = fh.read()
    except Exception as e:
        log.debug(f'An exception occurred: {e}')
    
    try:
        log.debug(f'Reading template file')
        with open(template_path, 'r') as fh:
            template = fh.read()
    except Exception as e:
        log.debug(f'An exception occurred: {e}')
    
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', content)
    
    try:
        with open(f'{target_path}', 'w') as fh:
            fh.write(template)
    except Exception as e:
        log.debug(f'Unable to write to file: {e}')


def generate_pages_recursive(content_path: str, template_path: str, target_path: str) -> None:
    '''
    Iterate through all files and directorys in content path looking for markdown documents to convert to html
    
    Args:
        content_path (str): The directory to traverse looking for files        
        template_path (str): The location of the template html document        
        target_path (str): The directory to place the output html document
        
    Returns:
        None
    '''
    log = logging.getLogger(f'generate_pages_recursive')
    for item in listdir(content_path):
        source = path.join(content_path, item)
        target = path.join(target_path, item).replace('.md', '.html')
        if path.isdir(source):
            if not path.exists(target):
                log.debug(f'Creatinging {target} directory.')
                makedirs(f'{target}')
            generate_pages_recursive(source, template_path, target)
        if path.isfile(source):
            generate_page(source, template_path, target)