import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode('a', 'href', props={'href':'https://www.google.com', 'target':'_blank'})
        self.assertIsInstance(node, HTMLNode)

    def test_props_to_html(self):
        node = HTMLNode('a', 'href', props={'href':'https://www.google.com', 'target':'_blank'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_to_html(self):
        node = HTMLNode('a', 'href', props={'href':'https://www.google.com', 'target':'_blank'})
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()