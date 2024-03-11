from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value is None:
            raise ValueError('leafnode has no value')
        if self.tag == None:
            return self.value
        return f'<{self.tag + super().props_to_html()}>{self.value}</{self.tag}>'