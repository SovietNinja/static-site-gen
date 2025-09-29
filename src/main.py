import os
import shutil

def main():
    # Create a TextNode object
    # Test_text = TextNode("123", TextType.LINK, "https://gratisography.com/wp-content/uploads/2023/05/gratisography-kitten-chef-free-stock-photo.jpg")
    # print(Test_text)
    makedir(current_path)
    clean_dir(public_path)            
    move_contents(static_path,public_path)


#current_path_full = os.path.abspath(os.getcwd())
current_path = os.getcwd()
public_path = current_path + "/public/"
static_path = current_path + "/static/"
def check_path(path):
    exist = {"public" : False, "static": False}
    if os.path.exists('public'):
        exist["public"] = True
    else : 
        exist["public"]  = False
        #print("folder public is absent")
    if os.path.exists('static'):
        exist["static"] = True
    else: 
        exist["static"] = False
        #print("folder static is absent")
    return exist

def makedir(path):
    if check_path(path)["static"] and check_path(path)["public"]:
        pass
    else:
        if check_path(path)["public"] == False:
            print("public folder is absent, creating public folder")
            os.mkdir("public")
        if check_path(path)["static"] == False:
            os.mkdir("static")
            print("static folder is absent, creating static folder")
    pass


def clean_dir(path):
    contents = os.listdir(path)
    for content in contents:
        content = os.path.join(path,content)
        try:
            if os.path.isdir(content):
                shutil.rmtree(content) 
            else:
                os.remove(content)
            print(f"Deleting {content}")
        except OSError as error: 
            print(error) 
            print(f"Directory {content} can not be removed")



def move_contents(source, target):
    source_contents = os.listdir(source)
    for content in source_contents:
        source_path = os.path.join(source, content) 
        target_path = os.path.join(target, content) 
        if os.path.isfile(source_path):
            if os.path.exists(target_path):
                print(f"{content} file with same name exists in target, overwriting file.")
            shutil.copy(source_path,target_path)
            print(f"coping {content} file to target")
        else:
            if not os.path.exists(target_path):
                os.mkdir(target_path)
                print(f"{content} folder absent in target, creating folder")
            move_contents(source_path,target_path)


if __name__ == "__main__":
    main()