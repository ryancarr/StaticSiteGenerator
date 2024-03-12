import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter
    )

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text    
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode('This is text with a **bolded** word', text_type_text)
        new_nodes = split_nodes_delimiter([node], '**', text_type_bold)
        self.assertListEqual(
            [
                TextNode('This is text with a ', text_type_text),
                TextNode('bolded', text_type_bold),
                TextNode(' word', text_type_text)
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode('This is text with an *italic* word', text_type_text)
        new_nodes = split_nodes_delimiter([node], '*', text_type_italic)
        self.assertListEqual(
            [
                TextNode('This is text with an ', text_type_text),
                TextNode('italic', text_type_italic),
                TextNode(' word', text_type_text)
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            'This is text with a **bolded** word and **another**', text_type_text
        )
        new_nodes = split_nodes_delimiter([node], '**', text_type_bold)
        self.assertListEqual(
            [
                TextNode('This is text with a ', text_type_text),
                TextNode('bolded', text_type_bold),
                TextNode(' word and ', text_type_text),
                TextNode('another', text_type_bold)
            ],
            new_nodes,
        )

        def test_delim_italic_double(self):
            node = TextNode('This is text with an *italic* word and *another*', text_type_text)
            new_nodes = split_nodes_delimiter([node], '*', text_type_italic)
            self.assertListEqual(
                [
                    TextNode('This is text with an ', text_type_text),
                    TextNode('italic', text_type_italic),
                    TextNode(' word and ', text_type_text),
                    TextNode('another', text_type_italic)
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode('This is text with a `code block` word', text_type_text)
        new_nodes = split_nodes_delimiter([node], '`', text_type_code)
        self.assertListEqual(
            [
                TextNode('This is text with a ', text_type_text),
                TextNode('code block', text_type_code),
                TextNode(' word', text_type_text)
            ],
            new_nodes,
        )
    
    def test_delim_fail(self):
        node = TextNode('This is text with a **bold word', text_type_text)
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], '**', text_type_bold)

    def test_extract_images(self):
        text = 'This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)'
        self.assertListEqual(
            [('image', 'https://i.imgur.com/zjjcJKZ.png'), ('another', 'https://i.imgur.com/dfsdkjfd.png')],
            extract_markdown_images(text)                        
        )

    def test_extract_images(self):
        text = 'This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)'
        self.assertListEqual(
            [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')],
            extract_markdown_links(text)                        
        )


if __name__ == '__main__':
    unittest.main()