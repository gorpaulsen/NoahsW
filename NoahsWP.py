import webbrowser

# Lag vebside
import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>NoahsW</title>
</head>
<body>
    <h1>Welcome to Noahs webpage!</h1>
    <p>Her kan du skrive hva du vil, Noah!.</p>
    <p>Tullball</p>
</body>
</html>
"""

file_path = os.path.abspath("Index.html")
with open(file_path, "w") as file:
    file.write(html_content)

webbrowser.open(f"file://{file_path}")
