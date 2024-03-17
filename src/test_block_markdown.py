import unittest
from block_markdown import (
    markdown_to_blocks,
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
