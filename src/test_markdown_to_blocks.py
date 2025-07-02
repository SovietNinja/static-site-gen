import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_one_word(self):
        md = """
**bolded**

_italic_
`code`
italic_code

- List1
- List2
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "**bolded**",
                "_italic_\n`code`\nitalic_code",
                "- List1\n- List2",
            ],
        )
        
if __name__ == "__main__":
    unittest.main()