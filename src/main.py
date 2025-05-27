from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

# Print the TextNode object; __repr__ will be called automatically
def main():
    # Create a TextNode object
    Test_text = TextNode("ZOV", TextType.LINK, "https://rusatribut.ru/files/products/Flag-ZOV_1.1000x1000w.jpg")
    print(Test_text)

if __name__ == "__main__":
    main()