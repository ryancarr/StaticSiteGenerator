from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list):
        super().__init__(tag, None, children, None)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('tag is not optional')
        if self.children is None or self.children == []:
            raise ValueError('children cannot be empty')
        result = f'<{self.tag}>'
        for leaf in self.children:
            result += leaf.to_html()
        result += f'</{self.tag}>'
        return result