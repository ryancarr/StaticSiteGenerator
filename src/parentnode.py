from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    '''
    Represents a parent HTML node that can contain child nodes.
    
    Attributes:
        tag (str): The HTML tag of the node.
        children (list): A list of child LeafNodes belonging to the parent node.
    
    Methods:
        __init__(tag: str, children: list) -> None:
            Initializes a new ParentNode instance.
        
        __repr__() -> str:
            Returns a string representation of the ParentNode instance.
        
        to_html() -> str:
            Converts the ParentNode and children into its HTML representation.
    '''
    
    def __init__(self, tag: str, children: list) -> None:
        '''
        Initializes a new ParentNode instance.
        
        Args:
            tag (str): The HTML tag of the node.
            children (list): The children LeafNodes belonging to the parent node
        
        Returns:
            None        
        '''
        super().__init__(tag, None, children, None)
        
    def __repr__(self):
        '''
        Returns a string represenation of the ParentNode instance.
        
        Returns:
            A string represntation of the ParentNode instance.
        '''
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
    
    def to_html(self) -> str:
        '''
        Converts the parent node instance and all children to its HTML representation.
        
        Returns:
            str: The HTML representation of the ParentNode instance and its children.
            
        Exceptions:
            ValueError: tag is not an optional attribute
            ValueError: children cannot be empty
        '''
        if self.tag is None:
            raise ValueError('tag is not optional')
        if self.children is None or self.children == []:
            raise ValueError('children cannot be empty')
        result = f'<{self.tag}>'
        for leaf in self.children:
            result += leaf.to_html()
        result += f'</{self.tag}>'
        return result