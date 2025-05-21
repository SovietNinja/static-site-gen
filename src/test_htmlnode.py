import unittest
from htmlnode import HTMLNode,LeafNode


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
    


if __name__ == "__main__":
    unittest.main()