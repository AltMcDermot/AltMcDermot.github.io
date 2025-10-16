import unittest 
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple_attrs(self):
        node = HTMLnode("a","a link is here", None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html().strip(), "href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_props_to_html_no_attrs(self):
        node = HTMLnode("p","lorem Ipsum")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_no_attrs(self):
        node = HTMLnode("p","lorem Ipsum", None, {})
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Link to Google", {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Link to Google</a>")

class TestParentNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()