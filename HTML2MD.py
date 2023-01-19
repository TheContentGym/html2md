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
