block_type_code      = 'code'
block_type_heading   = 'heading'
block_type_ordered   = 'ordered_list'
block_type_paragraph = 'paragraph'
block_type_quote     = 'quote'
block_type_unordered = 'unordered_list'

def markdown_to_blocks(markdown: str) -> list:
    working_text = markdown.strip().split('\n\n')
    return [block.strip() for block in working_text if block != '']
