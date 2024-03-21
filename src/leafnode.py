from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> object:
        self.tag = tag
        self.value = value
        self.props = props
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('leafnode has no value')
        if self.tag == None:
            return self.value
        return f'<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>'