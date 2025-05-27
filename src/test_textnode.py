import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_eq_img(self):
        node = TextNode("This is a image node", TextType.IMAGE,  "http://test/test.img")
        node2 = TextNode("This is a image node", TextType.IMAGE, "http://test/test.img")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a none node", TextType.LINK,  None)
        node2 = TextNode("This is url node", TextType.LINK, "http://test/test.img")
        self.assertNotEqual(node, node2)

    def test_split_middle_bald(self):
        node1 = TextNode("1 This is a text node with **bold1** text 1", TextType.TEXT)
        node2 = TextNode("2 This is a text node with **bold2** text 2", TextType.TEXT)
        node3 = TextNode("3 This is a text node with **bold3** text 3", TextType.TEXT)
        old_nodes = [node1,node2,node3]
        new_node = split_nodes_delimiter(old_nodes,"**",TextType.BOLD)
        self.assertEqual(len(new_node),9)


    def test_split_middle_italic(self):
        node1 = TextNode("1 This is a text node with _italic1_ text 1", TextType.TEXT)
        node2 = TextNode("2 This is a text node with _italic2_ text 2", TextType.TEXT)
        node3 = TextNode("3 This is a text node with _italic3_ text 3", TextType.TEXT)
        old_nodes = [node1,node2,node3]
        new_node = split_nodes_delimiter(old_nodes,"_",TextType.ITALIC)
        self.assertEqual(len(new_node),9)

    def test_split_middle_code(self):
        node1 = TextNode("1 This is a text node with `code block1` text 1", TextType.TEXT)
        node2 = TextNode("2 This is a text node with `code block2` text 2", TextType.TEXT)
        node3 = TextNode("3 This is a text node with `code block3` text 3", TextType.TEXT)
        old_nodes = [node1,node2,node3]
        new_node = split_nodes_delimiter(old_nodes,"`",TextType.CODE)
        self.assertEqual(len(new_node),9)

    def test_split_error(self):
        node1 = TextNode("1 This is a text node with `code block1 text 1", TextType.TEXT)
        node2 = TextNode("2 This is a text node with `code block2 text 2", TextType.TEXT)
        node3 = TextNode("3 This is a text node with `code block3 text 3", TextType.TEXT)
        old_nodes = [node1,node2,node3]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes,"`",TextType.CODE)

    def test_split_empty_bald(self):
        node1 = TextNode("**bold1** text 1", TextType.TEXT)
        node2 = TextNode("2 This is a text node with **bold2**", TextType.TEXT)
        node3 = TextNode("**bold3**", TextType.TEXT)
        old_nodes = [node1,node2,node3]
        new_node = split_nodes_delimiter(old_nodes,"**",TextType.BOLD)
        self.assertEqual(len(new_node),5)


if __name__ == "__main__":
    unittest.main()

    # def test_split_middle_bald(self):
    #     node1 = TextNode("1 This is a text node with **bald** text 1", TextType.TEXT),
    #     node2 = TextNode("2 This is a text node with _italic_ text 1", TextType.TEXT),
    #     node3 = TextNode("3 This is a text node with `code block` text 1", TextType.TEXT)
    #     old_nodes = [node1,node2,node3]
    #     new_node = split_nodes_delimiter(old_nodes,)