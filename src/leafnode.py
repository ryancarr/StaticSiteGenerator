from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    '''
    Represents a leaf HTML node, which cannot contain children.
    
    Attributes:
        tag (str): The HTML tag of the node.
        value (str): The content of the node.
        props (dict, optional): Additional properties or attributes of the node.
        
    Methods:
        __init__(tag: str, value: str, props: dict = None) --> None:
            Initialize a LeafNode instance.
        
        __repr__() -> str:
            Returns a string representation of the LeafNode instance.
            
        to_html() -> str:
            Convert the LeafNode to its HTML represenation.
    '''
    
    def __init__(self, tag: str, value: str, props: dict = None) -> object:
        '''
        Represents a leaf HTML node, which cannot contain children.
    
        Attributes:
            tag (str): The HTML tag of the node.
            value (str): The content of the node.
            props (dict, optional): Additional properties or attributes of the node.
        
        Returns:
            None
        '''
        self.tag = tag
        self.value = value
        self.props = props
    
    def __repr__(self):
        '''
        Returns a string representation of the LeafNode instance.
        
        Returns:
            str: A string represenation of the LeafNode instance.
        '''
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def to_html(self) -> str:
        '''
        Converts the LeafNode instance to its HTML representation.
        
        Returns:
            str: The HTML represenation of the LeafNode instance.
            
        Exceptions:
            ValueError: If the value of LeafNode is empty
        '''
        if self.value is None:
            raise ValueError('leafnode has no value')
        if self.tag == None:
            return self.value
        return f'<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>'