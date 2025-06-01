import unittest
from extract_markdown import extract_markdown_images,extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([('to boot dev', 'https://www.boot.dev'),
                              ('to youtube', 'https://www.youtube.com/@bootdotdev')],
                             matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
                              ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')],
                             matches)
    def test_extract_markdown_images_multiple_images(self):
        matches = extract_markdown_images(
            "![image1](https://example.com/image1.jpg) and ![image2](https://example.com/image2.png)"
        )
        self.assertListEqual([('image1', 'https://example.com/image1.jpg'),
                              ('image2', 'https://example.com/image2.png')],
                             matches)

    def test_extract_markdown_images_complex_text(self):
        matches = extract_markdown_images(
            "Here is some text with [links](https://example.com) and images: ![first](https://example.com/first.jpg), ![second](https://example.com/second.png)"
        )
        self.assertListEqual([('first', 'https://example.com/first.jpg'),
                              ('second', 'https://example.com/second.png')],
                             matches)

if __name__ == "__main__":
    unittest.main()