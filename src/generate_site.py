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

def clean_directory(source: str, target: str) -> None:
    log = logging.getLogger(f'clean_directory')
    if path.exists(target):
        log.debug(f'Removing {target} directory.')
        rmtree(target)

def copy_directory(source: str, target:str) -> None:
    log = logging.getLogger(f'copy_directory')
    makedirs(target)
    for item in listdir(source):
        source_path = path.join(source, item)
        target_path = path.join(target, item)
        if path.isfile(f'{source_path}'):
            log.debug(f'Copying {source_path} to {target_path}')
            copy(source_path, target_path)
        elif path.isdir(f'{source}/{item}'):
            copy_directory(source_path, target_path)
            
def extract_title(markdown: str) -> str:
    for line in markdown.split('\n'):
        if not line.startswith('# '):
            raise ValueError(f'Invalid markdown format, document must start with h1 header')
        return line[2:]

def generate_page(source_path: str, template_path: str, target_path: str) -> None:
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