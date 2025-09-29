import unittest
from textnode import TextNode,TextType
from extract_markdown import extract_markdown_images,extract_markdown_links



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            img_nodes = extract_markdown_images(old_node.text)
            if len(img_nodes) == 0:
                new_nodes.append(old_node)
                continue
            parsed_text = old_node.text
            for i in range(0, len(img_nodes)):
                image_alt, image_link = img_nodes[i]
                #print(image_alt, image_link)
                sections = parsed_text.split(f"![{image_alt}]({image_link})",1)
                #print(parsed_text)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                parsed_text = sections[1]
                new_nodes.append(TextNode(f"{image_alt}",TextType.IMAGE,f"{image_link}"))
            if parsed_text != "":
                new_nodes.append(TextNode(parsed_text, TextType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            link_nodes = extract_markdown_links(old_node.text)
            if len(link_nodes) == 0:
                new_nodes.append(old_node)
                continue
            parsed_text = old_node.text
            for i in range(0, len(link_nodes)):
                url_text , url = link_nodes[i]
                #print(image_alt, image_link)
                sections = parsed_text.split(f"[{url_text}]({url})",1)
                #print(parsed_text)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                parsed_text = sections[1]
                new_nodes.append(TextNode(f"{url_text}",TextType.LINK,f"{url}"))
            if parsed_text != "":
                new_nodes.append(TextNode(f"{parsed_text}", TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    input_node = [TextNode(f"{text}", TextType.TEXT),]
    output = []
    output = (split_nodes_image(input_node))
    #print("After images:", output)
    output = (split_nodes_links(output))
    #print("After links:", output)
    types_dict = {
            "**": TextType.BOLD,
            "_" : TextType.ITALIC,
            "`" : TextType.CODE
            }
    for delimiter in types_dict:
        text_type = types_dict[delimiter]
        output = (split_nodes_delimiter(output, delimiter, text_type))
    return output

if __name__ == "__main__":
    unittest.main()



