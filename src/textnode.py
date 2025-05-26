from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

    def __eq__(self, other):
        # Check if the other object is a TextNode
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )
        return False
    
    def text_node_to_html_node(self,text_node):
        if not isinstance(text_node,TextNode):
            raise Exception("node is not TextNode instance")
        match text_node.text_type:
            case (text_node.text_type.TEXT):
                return LeafNode(None,text_node.text)
            case (text_node.text_type.BOLD):
                return LeafNode("b",text_node.text)
            case (text_node.text_type.ITALIC):
                return LeafNode("i",text_node.text)
            case (text_node.text_type.CODE):
                return LeafNode("code",text_node.text)
            case (text_node.text_type.LINK):
                return LeafNode("a",text_node.text,{"href":f"{text_node.url}"})
            case (text_node.text_type.IMAGE):
                return LeafNode("img","",{"src":f"{text_node.url}",f"alt":f"{text_node.text}"}) 
            case _:
                raise Exception("Node type is not supported")
        
        


