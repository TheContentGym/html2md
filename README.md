# HTML to Markdown Converter
This is a simple script that converts an HTML webpage to a markdown file.

## Requirements
- html2text
- requests
- io
## How it Works
1. The script sends a GET request to the provided URL using the requests module.
2. The HTML content of the URL is then obtained using the response.text method.
3. The html2text module is used to convert the HTML to markdown format.
4. The ignore_images and ignore_links options are set to True, so that images and links are ignored in the final markdown output.
5. The markdown content is then written to a file using the io module, with the file name provided as an argument.

```
import html2text
import requests
import io

def html_to_markdown(url, file_name):
    response = requests.get(url)
    html = response.text
    h = html2text.HTML2Text()
    h.ignore_images = True
    h.ignore_links = True
    markdown = h.handle(html)
    
    with io.open(file_name, "w", encoding="utf-8") as file:
        file.write(markdown)

url = "https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-c-api-porting"
file_name = "markdownOutput.md"
html_to_markdown(url, file_name)
```

In the example above, the url variable is set to a specific URL, and the file_name variable is set to "markdownOutput.md". When the script is run, the markdown content of the URL will be saved in a file named "markdownOutput.md".

You can modify the URL and file name to your desired values.
