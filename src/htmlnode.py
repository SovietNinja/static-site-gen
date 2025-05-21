class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
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
