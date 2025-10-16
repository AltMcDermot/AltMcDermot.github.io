from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue  
        split_nodes = []      
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown syntax detected")        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        delimiters = extract_markdown_images(node.text)
        if len(delimiters) == 0:
            nodes.append(node)
            continue
        current_node = node.text

        for i in range(len(delimiters)):
            d = f"![{delimiters[i][0]}]({delimiters[i][1]})"
            sections = current_node.split(d, 1)

            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))

            nodes.append(TextNode(delimiters[i][0], TextType.IMAGE, delimiters[i][1]))

            if sections[1] != "":
                if i == len(delimiters)-1:
                    nodes.append(TextNode(sections[1], TextType.TEXT))
                else:
                    current_node = sections[1]
        # print(nodes)
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        delimiters = extract_markdown_links(node.text)
        if len(delimiters) == 0:
            nodes.append(node)
            continue

        current_node = node.text

        for i in range(len(delimiters)):
            d = f"[{delimiters[i][0]}]({delimiters[i][1]})"
            sections = current_node.split(d, 1)

            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))

            nodes.append(TextNode(delimiters[i][0], TextType.LINK, delimiters[i][1]))

            if sections[1] != "":
                if i == len(delimiters)-1:
                    nodes.append(TextNode(sections[1], TextType.TEXT))
                else:
                    current_node = sections[1]
        
    return nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    return node
