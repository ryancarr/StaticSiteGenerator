from re import findall

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text
)

def extract_markdown_images(text: str) -> list:
    '''
    Helper function to scan a text fragment for patterns of text matching an image
    
    Args:
        text (str): Text to be examined for patterns
    
    Returns:
        list (str): List of all instances of images found in the text
    '''
    pattern = r'!\[(.*?)\]\((.*?)\)'
    return findall(pattern, text)


def extract_markdown_links(text: str) -> list:
    '''
    Helper function to scan a text fragment for patterns of text matching a link
    
    Args:
        text (str): Text to be examined for patterns
    
    Returns:
        list (str): List of all instances of links found in the text
    '''
    pattern = r'\[(.*?)\]\((.*?)\)'
    return findall(pattern, text)


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
    '''
    Helper function used to split text on a given delimiter. Perperly formatted markdown will have the delimited before and after a section of text.
    
    Args:
        old_nodes (list): A list of TextNodes that need to be checked for the approriate delimiter
        
        delimiter (str): The delimiter to check for
        
        text_type (str): String representation of the text type being searched for
        
    Returns:
        list (TextNodes): A list of TextNodes with any matching the delimiter and type properly labeled
    
    Exceptions:
        ValueError: In the event markdown text is improperly formatted an error will be raised
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f'Invalid markdown format, {text_type} not closed')
        for i in range(len(split_text)):
            if split_text[i] == '':
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes: list) -> list:
    '''
    Check a list of TextNodes for any nodes containing images
    
    Args:
        old_nodes (list): A list of TextNodes that need to be checked for images
        
    Returns:
        list (TextNodes): An updated list of TextNodes with images properly labeled
    
    Exceptions:
        ValueError: In the event a markdown link is improperly formatted an error will be raised
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            split_text = original_text.split(f'![{image[0]}]({image[1]})', 1)
            if len(split_text) != 2:
                raise ValueError(f'Invalid markdown format, image tag not closed')
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            original_text = split_text[1]
        if original_text != '':
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_links(old_nodes: list) -> list:
    '''
    Check a list of TextNodes for any nodes containing links
    
    Args:
        old_nodes (list): A list of TextNodes that need to be checked for links
        
    Returns:
        list (TextNodes): An updated list of TextNodes with links properly labeled
    
    Exceptions:
        ValueError: In the event a markdown link is improperly formatted an error will be raised
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            split_text = original_text.split(f'[{link[0]}]({link[1]})')
            if len(split_text) != 2:
                raise ValueError(f'Invalid markdown format, link tag not closed')
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = split_text[1]
        if original_text != '':
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def text_to_textnodes(text: str) -> list:
    '''
    Convert a string into a list of TextNodes separating them into normal, bold, italic, code, image or link nodes.
    
    Args:
        text (str): A string containing the text we need to convert
        
    Returns:
        list (TextNode): A list of text nodes representing text that was passed in
    '''
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, '**', text_type_bold)
    nodes = split_nodes_delimiter(nodes, '*', text_type_italic)
    nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes