from leafnode import LeafNode

text_type_bold   = 'bold'
text_type_code   = 'code'
text_type_image  = 'image'
text_type_italic = 'italic'
text_type_link   = 'link'
text_type_text   = 'text'

class TextNode:
    '''
    Represents a node of text in a markdown document
    
    Attributes:
        text (str): The content of the text node.
        text_type (str): the type of the text node. Can be bold, code, image, italic, link or text.
        url (str, optional): The URL associated with the text node, only applies to images and links.
    '''
    
    def __init__(self, text: str, text_type: str, url:str =None) -> None:
        '''
        Creates TextNode instance
        
        Args:
            text (str): The content of the text node.
            text_type (str): The type of teh text node. Can be 'bold', 'code', 'image', 'italic', 'link' or 'text'.
            url (str, optional): The URL associated with the text node. Only applies to images or links.
        '''
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self) -> str:
        '''
        Returns representation of the instance as a string.
        '''
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def __eq__(self, other: object) -> bool:
        '''
        Test if two TextNodes are equal.
        
        Args:
            other (TextNode): The TextNode being compared to this instance.
        
        Returns:
            bool: True if the other node is equal to this instance.
        '''
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)
    
def text_node_to_html_node(text_node: object) -> LeafNode:
    '''
    Converts a TextNode to a corresponding LeftNode for HTML represenation.
    
    Args:
        text_node (TextNode): The text node to convert.
    
    Returns:
        LeafNode: The corresponding HTML representation of the text node.
        
    Exceptions:
        ValueError: If an invalid text type is provided.
    '''
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode('b', text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode('i', text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode('code', text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode('a', text_node.text, {'href':text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode('img', '', {'src':text_node.url, 'alt':text_node.text})
    else:
        raise ValueError(f'Invalid text type: {text_node.text}')