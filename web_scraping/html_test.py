from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]")
print(d)

print(soup.head)
print(soup.find_all(class_="special"))
print(soup.find_all(attrs={"data-example": "yes"}))

print("------------------")
print(soup.find_all(id="first"))
d2 = soup.select("#first")
print(d2)

print("------------------")
# find an element with an id of foo
soup.find(id="foo")
soup.select("#foo")

# find all elements wit a class of bar
# careful! "class" is a reserver word in python
soup.find_all(class_="bar")
soup.select(".bar")

# find all elements wit a data
# attribute of "baz"
# using the general attrs kwarg
soup.find_all(attrs={"data-baz": True})
soup.select("[data-baz]")
