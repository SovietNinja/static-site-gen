import os
from pathlib import Path
import shutil
import re
import sys
from markdown_to_html_node import markdown_to_html_node

if len(sys.argv) == 1:
    basepath = "/"
else: basepath = sys.argv[1]


def main():
    target_path = "./docs"
    static_path = "./static"
    content_path = "./content"
    template_path = "./template.html"
    makedir(target_path)
    clean_dir(target_path)            
    move_contents(static_path,target_path)
    generate_pages_recursive(content_path,template_path,target_path)
    
    
def check_path(target_path):
    if os.path.exists(f'{target_path}'):
        exist = True
    else : 
        exist = False
        #print(f"folder {target_path} is absent")
    return exist

def makedir(target_path):
    if check_path(target_path):
        print("Target folder exists")
        pass
    else:
        os.mkdir(target_path)
        print("Target folder is absent, creating target folder")
    pass


def clean_dir(path):
    contents = os.listdir(path)
    for content in contents:
        print(content)
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
            print(f"copying {content} file to target")
        else:
            if not os.path.exists(target_path):
                os.mkdir(target_path)
                print(f"{content} folder absent in target, creating folder")
            move_contents(source_path,target_path)
            
            
def extract_title(markdown):
    pattern = re.compile(r"^\# .*?\n")
    heading = re.search(pattern,markdown)
    if heading != None:
        heading = heading.group(0).lstrip("# ").strip()
    else:
        raise ValueError("no title found")
    return heading
 
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")         
    md_content = from_path
    template_content = template_path
    with open(md_content) as f:
        md_content = f.read()
    with open(template_content) as f:
        template_content = f.read()
    template = template_content
    html = markdown_to_html_node(md_content)
    html = html.to_html()
    title = extract_title(md_content)
    template = template.replace('{{ Title }}',title)
    template = template.replace('{{ Content }}',html)
    template = template.replace('href="/',f'href="{basepath}')
    template = template.replace('src="/',f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
 

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content = os.path.join(dir_path_content,content)
        if os.path.isfile(content):
            dest_file = os.path.splitext(os.path.basename(content))[0] + ".html"
            dest_file = os.path.join(dest_dir_path, dest_file)
            generate_page(content,template_path,dest_file)
            #print(f"generating html from {content} into {dest_file}")
        else:
            generate_pages_recursive(content,template_path,os.path.join(dest_dir_path,os.path.basename(content)))
            #print(content + " is folder")

if __name__ == "__main__":
    main()