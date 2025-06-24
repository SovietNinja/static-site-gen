import unittest
import re
from textnode import TextNode,TextType
from extract_markdown import extract_markdown_images,extract_markdown_links

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

if __name__ == "__main__":
    unittest.main()



