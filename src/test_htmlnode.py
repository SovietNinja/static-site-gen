import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode,text_node_to_html_node
from textnode import TextType,TextNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_one_prop(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_multiple_props(self):
        node = HTMLNode("a", "Click me", None, {
            "href": "https://example.com",
            "target": "_blank"
        })
        # The order of properties might vary, so we need to check for both possibilities
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://example.com" target="_blank"' or 
            result == ' target="_blank" href="https://example.com"'
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_wtih_href(self):
        node = LeafNode("a", "Look at this cats!", {"href": "https://cat.com"}) 
        self.assertEqual(node.to_html(), '<a href="https://cat.com">Look at this cats!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_no_child(self):
        with self.assertRaises(TypeError):
            parent_node = ParentNode("div") # type: ignore
        # try:
        #     parent_node = ParentNode("div")
        # except TypeError:
        #     self.res = True
        # self.assertTrue(self.res)

        
    def test_to_html_with_no_tag(self):
        with self.assertRaises(TypeError):
            parent_node = ParentNode() # type: ignore
        # except TypeError:
        #     self.res = True
        # self.assertTrue(self.res)
        
    def test_parent_to_html_empty_tag_raises_exception(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(None, [LeafNode("span", "child")])
            parent.to_html()

    def test_parent_to_html_no_children_raises_exception(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("div", [])
            parent.to_html()

    def test_parent_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent_node = ParentNode("section", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<section><p>First paragraph</p><p>Second paragraph</p></section>")
        
    def test_parent_to_html_with_attributes(self):
        child_node = LeafNode("a", "Link to site", {"href": "https://example.com"})
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><a href="https://example.com">Link to site</a></div>')
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_link(self):
        node = TextNode("This is url node", TextType.LINK, "http://test/test.img")  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is url node")
        self.assertEqual(html_node.props, {'href': 'http://test/test.img'})
    
    def test_img(self):
        node = TextNode("This is image node", TextType.IMAGE, "http://test/test.img")  
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'alt': 'This is image node', 'src': 'http://test/test.img'})



    # def test_print(self):
    #     node = TextNode("This is url node", TextType.LINK, "http://test/test.img")  
    #     html_node = text_node_to_html_node(node)
    #     print(html_node.__repr__)

if __name__ == "__main__":
    unittest.main()