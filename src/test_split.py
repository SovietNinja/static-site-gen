import unittest
from split_nodes import split_nodes_image,split_nodes_links
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
if __name__ == "__main__":
    unittest.main()