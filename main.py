def read_input_csv():
    with open("./input/2024.csv", "r") as f:
        lines = f.readlines()
    create_html_boilerplate(lines, "tada.html")


def create_html_boilerplate(lines, filename="index.html"):
    """Creates a basic HTML boilerplate file."""
    html_content = (
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>"""
        + "".join(lines)
        + """</p>
</body>
</html>"""
    )
    with open(filename, "w") as f:
        f.write(html_content)


if __name__ == "__main__":
    read_input_csv()
