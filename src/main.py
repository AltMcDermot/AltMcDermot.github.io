import sys
import os
import shutil

from textnode import *
from htmlnode import *
from inline_markdown import *
from build import copy_static_files, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
basepath = "/"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public+'')
    os.makedirs(dir_path_public)

    print("starting build...")

    copy_static_files(dir_path_static, dir_path_public)
    generate_page(dir_path_content, template_path, dir_path_public, basepath)

    print("build complete")

main()