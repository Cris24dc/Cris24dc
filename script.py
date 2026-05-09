import os
import requests
import cairosvg
from PIL import Image
from io import BytesIO

urls = {
    "c": "https://github.com/Matoka26/Matoka26/assets/106425405/3281fd3e-d8cd-4943-9ab7-20f3fa4effe2",
    "cpp": "https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg",
    "python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "git": "https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg",
    "linux": "https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg",
    "docker": "https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg",
    "scrapy": "https://i0.wp.com/www.craigperler.com/blog/wp-content/uploads/2016/11/scrapy.webp?fit=300%2C300&ssl=1",
    "numpy": "https://img.icons8.com/color/512/numpy.png",
    "pandas": "https://img.icons8.com/color/512/pandas.png",
    "matplotlib": "https://img.icons8.com/color/600/matplotlib.png",
    "scikitlearn": "https://icon.icepanel.io/Technology/svg/scikit-learn.svg",
    "pytorch": "https://blog.christianperone.com/wp-content/uploads/2018/10/pytorch-logo.png",
    "javascript": "https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg",
    "nodejs": "https://www.svgrepo.com/show/354119/nodejs-icon.svg",
    "react": "https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg",
    "css3": "https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg",
    "dotnetcore": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg",
    "mysql": "https://cdn.prod.website-files.com/66754aa69a5d872183713f9c/672dfced5422c158fb5a6002_mysql%20logo.png"
}

os.makedirs("img", exist_ok=True)

for name, url in urls.items():
    response = requests.get(url)
    output_path = f"img/{name}.png"

    if "svg" in url or b"<svg" in response.content[:100].lower():
        cairosvg.svg2png(bytestring=response.content, write_to=output_path)
    else:
        img = Image.open(BytesIO(response.content))
        img.convert("RGBA").save(output_path, "PNG")