class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

    def props_to_html(self):
        result = ''
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def to_html(self):
        raise NotImplementedError('to_html method not implemented')