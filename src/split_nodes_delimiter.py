import unittest
from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            split_list = old_node.text.split(f'{delimiter}',maxsplit=3)
            if len(split_list) != 3:
                raise Exception(f"closing {delimiter} not found")
            if split_list[0] != "":
                new_nodes.append(TextNode(f'{split_list[0]}',TextType.TEXT))
            new_nodes.append(TextNode(f'{split_list[1]}',text_type))
            if split_list[2] != "":
                new_nodes.append(TextNode(f'{split_list[2]}',TextType.TEXT))
    return new_nodes

if __name__ == "__main__":
    unittest.main()