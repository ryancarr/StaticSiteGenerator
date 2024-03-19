import unittest
from block_markdown import (
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
    block_type_code,
    block_type_heading,
    block_type_ordered,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered,
    
    )

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        text1 = '# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item'
        self.assertEqual(markdown_to_blocks(text1), ['# This is a heading',
                                                     'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                                                     '* This is a list item\n* This is another list item'])
        text2 = 'This is **bolded** paragraph\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n\n\n\n\n\n* This is a list\n* with items\n\n\n'
        self.assertEqual(markdown_to_blocks(text2), ['This is **bolded** paragraph',
                                                     'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                                                     '* This is a list\n* with items'
                                                     ])
    
    def test_block_to_block_type(self):
        block = '```\ncode block\n```'
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = '# heading'
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = '1. Num 1\n2. Num 2'
        self.assertEqual(block_to_block_type(block), block_type_ordered)
        block = 'This is some text, a paragraph if you will'
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = '> This is a quote\n> spanning multiple lines'
        self.assertEqual(block_to_block_type(block), block_type_quote)        
        block = '* Num 1\n* Num 2'
        self.assertEqual(block_to_block_type(block), block_type_unordered)
        block = '- Num 1\n- Num 2'
        self.assertEqual(block_to_block_type(block), block_type_unordered)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )