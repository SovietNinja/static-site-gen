def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    out = []
    for block in blocks:
        block = block.strip()
        if block != "":
            out.append(block)
    return out