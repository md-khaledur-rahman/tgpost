import os
from urllib.parse import urlparse




page_no = input("Enter Your Page Number: ")
url = input("Enter Your Post Link: ")

path = urlparse(url).path.lstrip("/")


# Define the folder and file name
folder_path = 'G:\Scholarship\scholarship'
file_name = '%s.html'%page_no

# Ensure the folder exists; create it if it doesn't
os.makedirs(folder_path, exist_ok=True)

# Define the full path for the file
file_path = os.path.join(folder_path, file_name)

# HTML content to write to the file
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
    <div class="container-fluid row mb-5">

        <!-- Side banner (Scholarship) -->
        <div class="col-3 bg-warning pt-2 d-none d-lg-block">
            <div>
                <a href="https://t.me/higher_education_scholarship" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100 my-3 fw-bold">Join Our Telegram</a>
            </div>
            <div>
                <a href="https://t.me/higher_education_scholarship" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100 my-3 fw-bold">Join Our Telegram</a>
            </div>
            <div>
                <a href="https://t.me/higher_education_scholarship" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100 my-3 fw-bold">Join Our Telegram</a>
            </div>
            <div>
                <a href="https://t.me/higher_education_scholarship" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100 my-3 fw-bold">Join Our Telegram</a>
            </div>
            
                    
        </div>


        <!-- Telegram Post -->
        <div class="col-12 col-md-7 col-lg-6">
            <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100 my-3">Higher Education Scholarships</a>
            <br>
            <script async src="https://telegram.org/js/telegram-widget.js?22" data-telegram-post="{path}" data-width="100%"></script>


            <a href="https://t.me/higher_education_scholarship" target="_blank" class="btn btn-outline-success w-100">More Scholarships</a>
            
        </div>


        <!-- Side Banner (Facebook) -->
        <div class="col-3 bg-info pt-2 d-none d-lg-block">
            <div>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank" class="btn btn-outline-light w-100 my-3 fw-bold text-dark">Follow Us on Facebook</a>
            </div>
            <div>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank" class="btn btn-outline-light w-100 my-3 fw-bold text-dark">Follow Us on Facebook</a>
            </div>
            <div>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank" class="btn btn-outline-light w-100 my-3 fw-bold text-dark">Follow Us on Facebook</a>
            </div>
            <div>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank">
                    <img src="photos/scholarship.jpg" alt="" class="img-fluid rounded-circle">
                </a>
                <a href="https://www.facebook.com/AllScholarshipNews" target="_blank" class="btn btn-outline-light w-100 my-3 fw-bold text-dark">Follow Us on Facebook</a>
            </div>
            
    
        </div>
    </div>





    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
"""

# Write the HTML content to the file
with open(file_path, 'w') as file:
    file.write(html_content)

print(f"HTML file created at: {file_path}")
