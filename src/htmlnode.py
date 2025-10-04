

def text_node_to_html_node(text_node):
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

class HTMLNode:
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            attrs = ""
            if self.props != None and self.props != {}:
                attrs = " "+" ".join(f'{key}="{value}"' for key, value in self.props.items())
            return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
  
    def props_to_html(self):
        result = ""
        if self.props != None:
            for prop in self.props:
                 result += f' {prop}="{self.props[prop]}"'
        return result 
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
          
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


