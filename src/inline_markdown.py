from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
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