import os

# Define the folder and file name
folder_path = 'path/to/your/folder'
file_name = 'example.html'

# Ensure the folder exists; create it if it doesn't
os.makedirs(folder_path, exist_ok=True)

# Define the full path for the file
file_path = os.path.join(folder_path, file_name)

# HTML content to write to the file
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a simple HTML page created with Python.</p>
</body>
</html>
"""

# Write the HTML content to the file
with open(file_path, 'w') as file:
    file.write(html_content)

print(f"HTML file created at: {file_path}")
