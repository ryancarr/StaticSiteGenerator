from inline_markdown import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node

block_type_code      = 'code'
block_type_heading   = 'heading'
block_type_ordered   = 'ordered_list'
block_type_paragraph = 'paragraph'
block_type_quote     = 'quote'
block_type_unordered = 'unordered_list'

def block_to_block_type(block: str) -> str:
    '''
    Helper function that determines what type of data a block contains.
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns: 
        str: A string representing the block type ie, code for a code block
    '''
    lines = block.split('\n')
    if (block.startswith('# ')
        or block.startswith('## ')
        or block.startswith('### ')
        or block.startswith('#### ')
        or block.startswith('##### ')
        or block.startswith('###### ')
        ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endswith('```'):
        return block_type_code
    if len(lines) > 1 and block.startswith('> '):
        for line in lines:
            if not line.startswith('> '):
                return block_type_paragraph
        return block_type_quote
    if len(lines) > 1 and block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_unordered
    if len(lines) > 1 and block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        return block_type_unordered
    if len(lines) > 1 and block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_ordered
    return block_type_paragraph


def block_to_html_node(block: str) -> ParentNode:
    '''
    This function determines which helper function to call to convert the block into the correct type of ParentNode.
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns:
        ParentNode: A ParentNode containing the contents of the block
    '''
    block_type = block_to_block_type(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_ordered:
        return ordered_to_html_node(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_unordered:
        return unordered_to_html_node(block)


def code_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts a code block into a code block inside a preformatted ParentNode
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A preformatted ParentNode with a code child node
    '''
    if not block.startswith('```') and block.endswith('```'):
        raise ValueError(f'Invalid code block')
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode('code', children)
    return ParentNode('pre', [code])


def heading_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts a markdown header into the proper h level ParentNode
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A ParentNode containing the header
    '''
    level = len(block) - len(block.lstrip('#'))
    if level == 0 or level > 6:
        raise ValueError(f'Invalid heading level: {level}')
    text = block[level + 1: ].lstrip()
    children = text_to_children(text)
    return ParentNode(f'h{level}', children)


def markdown_to_blocks(markdown: str) -> list:
    '''
    Breaks a markdown document into individual blocks of content
    
    Args: 
        markdown (str): A string containing the markdown document
    
    Returns: 
        list (str): A list of strings for easier processing of each block
    '''
    working_text = markdown.strip().split('\n\n')
    return [block.strip() for block in working_text if block != '']


def markdown_to_html_node(markdown: str) -> ParentNode:
    '''
    Helper function that starts the process of converting markdown into HTMLNodes
    
    Args: 
        markdown (str): Contents of an entire markdown document
    
    Returns:
        ParentNode: A ParentNode containing the entire markdown document as children nodes
    '''
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode('div', children)


def ordered_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts an ordered list block into the appropriate ParentNode
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A ParentNode containing the entire ordered list
    '''
    items = block.split('\n')
    li_items = []
    for item in items:
        text = item.split(' ', maxsplit=1)[1]
        children = text_to_children(text)
        li_items.append(ParentNode('li', children))
    return ParentNode('ol', li_items)


def paragraph_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts a block of unlabeled content as a paragraph ParentNode
    
    Args: 
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A ParentNode containing the paragraph text
    '''
    lines = block.split('\n')
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)


def quote_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts a block of quote blocks into a quote ParentNode
    
    Args:
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A ParentNode containing the entire quote block
    '''
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError(f'Invalid quote block')
        new_lines.append(line.lstrip('>').strip())
    text = ' '.join(new_lines)
    children = text_to_children(text)
    return ParentNode('blockquote', children)


def text_to_children(text: str) -> list:
    '''
    Helper function that converts raw markdown and converts it into individual html nodes, nesting children nodes as necessary
    
    Args: 
        text (str): The text to convert to HTMLNodes
    
    Returns:
        list (LeafNode): A list of children nodes representing the text that was passed in
    '''
    children = []
    text_nodes = text_to_textnodes(text)    
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def unordered_to_html_node(block: str) -> ParentNode:
    '''
    Helper function that converts an unordered list block into the appropriate ParentNode
    
    Args:
        block (str): String of content representing a single block of markdown
    
    Returns: 
        ParentNode: A ParentNode containing the entire unordered list
    '''
    items = block.split('\n')
    li_items = []
    for item in items:
        text = item.split(' ', maxsplit=1)[1]
        children = text_to_children(text)
        li_items.append(ParentNode('li', children))
    return ParentNode('ul', li_items)