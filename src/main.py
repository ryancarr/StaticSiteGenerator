import logging
from os import (
    path,
    getcwd,
    listdir,
    makedirs,
)
from shutil import (
    copy,
    rmtree,
)
from textnode import TextNode

def setup_logging(output_file: str, level=logging.DEBUG):
    logging.basicConfig(filename=output_file, filemode='w', level=level)

def main():
    node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(node)
    setup_logging(f'output.log', logging.DEBUG)
    clean_directory(f'{getcwd()}\\static', f'{getcwd()}\\public')
    copy_directory(f'{getcwd()}\\static', f'{getcwd()}\\public')

def clean_directory(source: str, target: str):
    log = logging.getLogger(f'clean_directory')
    if path.exists(f'{getcwd()}/public'):
        log.debug(f'Removing {target} directory.')
        rmtree(target)

def copy_directory(source: str, target:str):
    log = logging.getLogger(f'copy_directory')
    makedirs(target)
    print(listdir(source))
    for item in listdir(source):
        source_path = path.join(source, item)
        target_path = path.join(target, item)
        if path.isfile(f'{source_path}'):
            log.debug(f'Copying {source_path} to {target_path}')
            copy(source_path, target_path)
        elif path.isdir(f'{source}\\{item}'):
            copy_directory(source_path, target_path)

if __name__ == '__main__':
    main()