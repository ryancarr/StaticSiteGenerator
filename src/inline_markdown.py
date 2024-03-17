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

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list:
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

def extract_markdown_images(text: str) -> list:
    pattern = r'!\[(.*?)\]\((.*?)\)'
    return findall(pattern, text)

def extract_markdown_links(text: str) -> list:
    pattern = r'\[(.*?)\]\((.*?)\)'
    return findall(pattern, text)

def split_nodes_image(old_nodes: list) -> list:
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