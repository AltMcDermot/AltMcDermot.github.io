import os
import shutil
from block_markdown import markdown_to_html_node


def buildSite():
    print("starting build...")
    path = "./public/"

    if os.path.exists(path):
        shutil.rmtree(path+'')
    os.makedirs(path)
    copy_static_files("./static/", path)

    generate_page("./content/", "./template.html", "./public/")
    
    print("build complete")

def copy_static_files(src,dest):
    # print("=====Copy==Start=====")
    if not src.endswith("/"):
        src=src+"/"
    if not dest.endswith("/"):
        dest=dest+"/"
    
    for item in os.listdir(src):
        if  os.path.isfile(src+item):
            if os.path.exists(dest):
                shutil.copy(src+item,dest)
                pass
        else:
            destination = dest+item
            source = src+item
            os.makedirs(destination)
            copy_static_files(source, destination)

def extract_title(markdown):
    file = open(markdown, 'r')
    lines = file.readlines()
    header = None
    for line in lines:
        if line.startswith("# "):
            header = line[2:]
    return header

def generate_page(from_path, template_path, dest_path):
    if not from_path.endswith("/"):
        from_path=from_path+"/"
    if not dest_path.endswith("/"):
        dest_path=dest_path+"/"
    
    if os.path.isdir(from_path):
        for item in os.listdir(from_path):
            if os.path.isdir(from_path+item):
                os.makedirs(dest_path+item, exist_ok=True)
                generate_page(from_path+item+'/', template_path, dest_path+item)

            else:
                print(f"generating page from {item} to {dest_path} using {template_path}")

                header = extract_title(from_path+item)
                markdownfile = open(from_path+item, 'r')
                lines = markdownfile.read()

                template_file = open(template_path, 'r')
                template_lines = template_file.readlines()
        
                nodes = markdown_to_html_node(lines)
                markup = ""
                html = nodes.to_html()

                for line in template_lines:
                    if line.find("{{ Content }}") != -1:
                        line = line.replace("{{ Content }}", html)
                    if line.find("{{ Title }}") != -1:
                        line = line.replace("{{ Title }}", header.strip())
                    markup += line


                if os.path.exists(dest_path+item):
                    os.remove(dest_path+item)
                    
                with open(dest_path+item[:-2]+"html", 'w') as f:
                    f.write(markup)
                    f.close()
