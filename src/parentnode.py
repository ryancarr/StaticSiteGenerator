from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list) -> object:
        super().__init__(tag, None, children, None)
        
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
    
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError('tag is not optional')
        if self.children is None or self.children == []:
            raise ValueError('children cannot be empty')
        result = f'<{self.tag}>'
        for leaf in self.children:
            result += leaf.to_html()
        result += f'</{self.tag}>'
        return result