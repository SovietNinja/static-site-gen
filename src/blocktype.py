from enum import Enum
import re
    
BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])

def block_to_block_type(md_block):
    if re.match(r"^\#{1,6}\ ",md_block) != None:
        #print("HEAD")
        return BlockType.heading
    
    if re.match(r"(?s)(^\`{3})(.+?)(\`{3})",md_block) != None:
        #print("CODE")
        return BlockType.code
    
    if re.match(r"^\>(.+)(\n\>.+)*",md_block) != None:
        #print("QUOTE")
        return BlockType.quote

    if re.match(r"\-\ ",md_block) != None:
        regex = r"\-\ "
        block_list = md_block.splitlines()
        line = 0
        for block in block_list:
            if re.match(regex,block) != None:
                line += 1
            else: break 
        if len(block_list) == line:
            #print("UNORD")
            return BlockType.unordered_list    
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
            #print("ORDLIST")
            return BlockType.ordered_list
    #print("paragraph")     
    return BlockType.paragraph    