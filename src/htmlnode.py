class HTMLNode:
    '''
    Base class that defines what a HTML Node is made up of
    '''
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None) -> object:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> str:
        '''
        Convert a HTMLNode into a string representing relavant properties
        
        Returns:
            str: A string representation of a HTMLNode object
        '''
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

    def props_to_html(self) -> str:
        '''
        Return a string containing all properties belonging to this HTMLNode
        
        Returns:
            str: A string of key value pairs
        '''
        result = ''
        if self.props == None: return result
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def to_html(self) -> NotImplementedError:
        '''
        Children must override this method
        '''
        raise NotImplementedError('to_html method not implemented')