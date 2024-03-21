from generate_site import (
    clean_directory,
    copy_directory,
    generate_page,
)
import logging

content_dir = './content'
static_dir = './static'  # The forward slash works on both *nix and Windows systems
public_dir = './public'
template_html = './template.html'

def setup_logging(output_file: str, level=logging.DEBUG):
    logging.basicConfig(filename=output_file, filemode='w', level=level)

def main():
    setup_logging(f'output.log', logging.DEBUG)
    print('Beginning site generation process')
    clean_directory(static_dir, public_dir)
    copy_directory(static_dir, public_dir)
    generate_page(f'{content_dir}/index.md', template_html, public_dir)

if __name__ == '__main__':
    main()