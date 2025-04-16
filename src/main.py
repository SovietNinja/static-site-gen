from textnode import TextNode, TextType

# Print the TextNode object; __repr__ will be called automatically
def main():
    # Create a TextNode object
    Test_text = TextNode("ZOV", TextType.LINK, "https://rusatribut.ru/products/flag-zov")
    print(Test_text)

if __name__ == "__main__":
    main()