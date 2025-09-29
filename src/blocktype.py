from enum import Enum
import re
    
BlockType = Enum('BlockType', ['PARAGRAPH', 'HEADING', 'CODE', 'QUOTE', 'ULIST', 'OLIST'])

def block_to_block_type(md_block):
    if re.match(r"^\#{1,6}\ ",md_block) != None:
        #print("HEAD")
        return BlockType.HEADING
    
    if re.match(r"(?s)(^\`{3})(.+?)(\`{3})",md_block) != None:
        #print("CODE")
        return BlockType.CODE
    
    if re.match(r"^\>(.+)(\n\>.+)*",md_block) != None:
        #print("QUOTE")
        return BlockType.QUOTE

    if re.match(r"\-\ ",md_block) != None:
        regex = r"\-\ "
        block_list = md_block.splitlines()
        line = 0
        for block in block_list:
            if re.match(regex,block) != None:
                line += 1
            else: break 
        if len(block_list) == line:
            #print("ULIST")
            return BlockType.ULIST    
    if re.match(r"(1\.\ )",md_block) != None:
        line = 0
        order = 1
        block_list = md_block.splitlines()
        for block in block_list:
            regex = re.escape(str(order)) + r"(\.\ )"
            if re.match(regex,block) != None:
                line += 1 
                order += 1
            else: break 
        if len(block_list) == line:
            #print("OLIST")
            return BlockType.OLIST
    #print("paragraph")     
    return BlockType.PARAGRAPH    