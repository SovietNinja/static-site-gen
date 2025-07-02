import unittest
from split_nodes import split_nodes_image,split_nodes_links,text_to_textnodes
from textnode import TextNode,TextType

class TestSplit(unittest.TestCase):
    def test_split_nodes_image(self):
        node1 = TextNode(
            "This is text with an ![image_node1](https://i.imgur.com/zjjcJKZ.png) and another ![second image_node1](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with an ![image_node2](https://i.imgur.com/zjjcJKZ.png) and another ![second image_node2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        nodes = [node1,node2]
        matches = split_nodes_image(nodes)
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT, None),
                            TextNode("image_node1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode(" and another ", TextType.TEXT, None), 
                            TextNode("second image_node1", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"), 
                            TextNode("This is text with an ", TextType.TEXT, None),
                            TextNode("image_node2",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode(" and another ", TextType.TEXT, None),
                            TextNode("second image_node2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")]
                            , matches)
        
    def test_split_nodes_only_image(self):
        node1 = TextNode(
            "![image_node1](https://i.imgur.com/zjjcJKZ.png)![second image_node1](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "![image_node2](https://i.imgur.com/zjjcJKZ.png)![second image_node2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        nodes = [node1,node2]
        matches = split_nodes_image(nodes)
        self.assertListEqual([TextNode("image_node1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode("second image_node1", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"), 
                            TextNode("image_node2",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode("second image_node2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")]
                            , matches)
    
        
        
        
    def test_split_nodes_link(self):
        node1 = TextNode(
            "This is text with an [first link 1](https://i.imgur.com/zjjcJKZ.png) and another [second link 1](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with an [first link 2](https://i.imgur.com/zjjcJKZ.png) and another [second link 2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        nodes = [node1,node2]
        matches = split_nodes_links(nodes)
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT, None),
                            TextNode("first link 1", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode(" and another ", TextType.TEXT, None), 
                            TextNode("second link 1", TextType.LINK, "https://i.imgur.com/3elNhQu.png"), 
                            TextNode("This is text with an ", TextType.TEXT, None),
                            TextNode("first link 2", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode(" and another ", TextType.TEXT, None),
                            TextNode("second link 2", TextType.LINK, "https://i.imgur.com/3elNhQu.png")]
                            , matches)
        
    def test_split_nodes_only_link(self):
        node1 = TextNode(
            "[first link 1](https://i.imgur.com/zjjcJKZ.png)[second link 1](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[first link 2](https://i.imgur.com/zjjcJKZ.png)[second link 2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        nodes = [node1,node2]
        matches = split_nodes_links(nodes)
        self.assertListEqual([TextNode("first link 1", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode("second link 1", TextType.LINK, "https://i.imgur.com/3elNhQu.png"), 
                            TextNode("first link 2", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"), 
                            TextNode("second link 2", TextType.LINK, "https://i.imgur.com/3elNhQu.png")]
                            , matches)   
        
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        matches = text_to_textnodes(text)
        self.assertListEqual([
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with an ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" word and a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" and an ", TextType.TEXT),
                            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            TextNode(" and a ", TextType.TEXT),
                            TextNode("link", TextType.LINK, "https://boot.dev"),
                            ],matches)
        
    def test2_text_to_textnodes(self):
        text = "This is **bold** and ![image](url) has **more bold**"
        matches = text_to_textnodes(text)
        self.assertListEqual([
                    TextNode("This is ", TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url"),
                    TextNode(" has ", TextType.TEXT),
                    TextNode("more bold", TextType.BOLD),
                    ],matches)
        
if __name__ == "__main__":
    unittest.main()