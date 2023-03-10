#!/usr/bin/env python3
import os
import shutil
import sys

import markdown
from jinja2 import FileSystemLoader, Environment


# Convert markdown to html
def markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(output_file, 'w') as f:
        f.write(html)


# Render Jinja2 template with data
def render_template(template_file, output_file, context):
    if not os.path.exists('templates/'):
        os.makedirs('templates/')

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    try:
        template = env.get_template(template_file)
        html = template.render(context)

        with open(output_file, 'w') as f:
            f.write(html)
    except:
        print("Template not found")


# Generate the site
def generate_site(input_directory, output_directory):
    # Create the output directory
    if not os.path.exists(output_directory + '/templates/'):
        os.makedirs(output_directory + '/templates/')

    if not os.path.exists('html/'):
        os.makedirs('html/')
    # Convert markdown to html

    markdown_files = [f for f in os.listdir(input_directory) if f.endswith('.md')]
    for markdown_file in markdown_files:
        input_file = os.path.join(input_directory, markdown_file)
        output_file = os.path.join('html', markdown_file.replace('.md', '.html'))
        markdown_to_html(input_file, output_file)

    # Render Jinja2 template with data
    pages = []
    for html_file in os.listdir('html'):
        if html_file.endswith('.html'):
            pages.append(html_file)

    for page in pages:
        template_file = page
        output_file = os.path.join(output_directory, 'templates', page)
        title = page.replace('.html', '')
        values = open('html/' + page).read()
        context = {'title': title, 'content': values}
        render_template(template_file, output_file, context)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 generator.py input_directory output_directory')
        sys.exit(1)

    markdown_directory = sys.argv[1]
    output = sys.argv[2]
    generate_site(markdown_directory, output)
