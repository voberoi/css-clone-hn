import json
from urlparse import urlparse
import random
from jinja2 import Template
import codecs


def get_posts():
    fd = open("front-page.json")
    hn_data = json.loads(fd.read())

    rank = 1
    posts = []
    for item in hn_data["hits"]:
        url = item["url"]

        domain = urlparse(url).netloc
        domain = ".".join(domain.rsplit(".", 2)[-2:])
        
        post = {
            "rank": rank,
            "author": item["author"],
            "votes": item["points"],
            "comments": item["num_comments"],
            "url": url,
            "domain": domain,
            "title": item["title"],
            "time_ago": str(random.randint(1, 10)) + " hours ago",
        }
        
        posts.append(post)
        
        rank += 1

    return posts

def main():
    fd = codecs.open('index.html.jnj', encoding='utf-8')
    template = Template(fd.read())
    rendered = template.render(posts=get_posts())
    fd.close()

    print rendered.encode("utf-8")

main()
    




    
