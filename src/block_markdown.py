block_type_code      = 'code'
block_type_heading   = 'heading'
block_type_ordered   = 'ordered_list'
block_type_paragraph = 'paragraph'
block_type_quote     = 'quote'
block_type_unordered = 'unordered_list'

def markdown_to_blocks(markdown: str) -> list:
    working_text = markdown.strip().split('\n\n')
    return [block.strip() for block in working_text if block != '']

def block_to_block_type(block: str) -> str:
    lines = block.split('\n')
    if (block.startswith('# ')
        or block.startswith('## ')
        or block.startswith('### ')
        or block.startswith('#### ')
        or block.startswith('##### ')
        or block.startswith('###### ')
        ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endswith('```'):
        return block_type_code
    if len(lines) > 1 and block.startswith('> '):
        for line in lines:
            if not line.startswith('> '):
                return block_type_paragraph
        return block_type_quote
    if len(lines) > 1 and block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_unordered
    if len(lines) > 1 and block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        return block_type_unordered
    if len(lines) > 1 and block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_ordered
    return block_type_paragraph