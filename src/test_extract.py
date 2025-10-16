import unittest 
from textnode import *
from inline_markdown import *
from extract_markdown import *

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        node = TextNode("These are _italic words_.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("These are ", TextType.TEXT),
            TextNode("italic words", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()