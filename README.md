## Static-site generator.

### Description

Designed and implemented a simple static-site generator in Python.

The generator takes a directory of Markdown files and converts them into a static website. 
The generator also supports templates, which allows for the creation of a consistent layout across all pages.


### Usage

To use the generator, run the following command:

    python3 generator.py <input-directory> <output-directory>

The generator will then convert all Markdown files in the input directory into HTML files in the output directory.

To use the flask server, run the following command:

    python3 app.py

The flask server will then run on `http://localhost:5000/`
and will display the generated website.
The site allows a user to upload a Markdown file and navigate to the generated HTML pages.

### Features

The generator supports the following features:

* Markdown to HTML conversion
* Templates
* CSS styling
* Flask server
* File upload
* Navigation



### Dependencies

The generator requires the following dependencies:

* Python 3
* Python Markdown
* Python Jinja2
* Flask

Install dependencies using the following command:

    pip3 install -r requirements.txt



### License

The generator is licensed under the MIT License. See the LICENSE file for more information.

### Author
TERRY MOCHIRE, FEB 2023.