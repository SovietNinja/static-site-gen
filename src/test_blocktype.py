import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_heading_1(self):
        md = "# First heading"
        self.assertEqual(block_to_block_type(md),BlockType.HEADING)
    def test_heading_3(self):
        md = "### First heading"
        self.assertEqual(block_to_block_type(md),BlockType.HEADING)
    def test_heading_6(self):
        md = "###### First heading"
        self.assertEqual(block_to_block_type(md),BlockType.HEADING)
    def test_code_block(self):
        md = "``` code here \n and here ```"
        self.assertEqual(block_to_block_type(md),BlockType.CODE)
    def test_quote_single(self):
        md = "> quote here"
        self.assertEqual(block_to_block_type(md),BlockType.QUOTE)
    def test_quote_multiple(self):
        md = "> quote here \n> and here"
        self.assertEqual(block_to_block_type(md),BlockType.QUOTE)
    def test_unorderd_list_single(self):
        md = "- First list"
        self.assertEqual(block_to_block_type(md),BlockType.ULIST)
    def test_uorderd_list_multiple(self):
        md = "- First list\n- Second list\n- Third list"
        self.assertEqual(block_to_block_type(md),BlockType.ULIST)
    def test_ord_list_single(self):
        md = "1. First list"
        self.assertEqual(block_to_block_type(md),BlockType.OLIST)
    def test_ord_list_multiple(self):
        md = "1. First list\n2. Second list\n3. Third list"
        self.assertEqual(block_to_block_type(md),BlockType.OLIST)
    def test_paragraph(self):
        md = "```1. First list\n2. Second list\n>3. Third list but this is not a list"
        self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()