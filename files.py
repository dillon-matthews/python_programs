# File Display
def display_file_contents():
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                print(line.strip())
    except IOError:
        print("Error: The file could not be opened.")

display_file_contents()

# Average of Numbers
def calculate_average():
    try:
        total = 0
        count = 0
        with open("numbers.txt", "r") as file:
            for line in file:
                total += int(line.strip())
                count += 1
        if count > 0:
            print(f"The average is: {total / count:.2f}")
        else:
            print("The file is empty.")
    except IOError:
        print("Error: The file could not be opened.")
    except ValueError:
        print("Error: The file contains invalid data.")

calculate_average()

# Exception Handling
def exception_handling_example():
    try:
        total = 0
        count = 0
        with open("numbers.txt", "r") as file:
            for line in file:
                total += int(line.strip())
                count += 1
        if count > 0:
            print(f"The average is: {total / count:.2f}")
        else:
            print("The file is empty.")
    except IOError:
        print("Error: The file could not be opened or found.")
    except ValueError:
        print("Error: Non-numeric data found in the file.")

exception_handling_example()

# Personal Web Page Generator
def personal_web_page_generator():
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    html_content = f"""<html>
<head>
</head>
<body>
   <center>
      <h1>{name}</h1>
   </center>
   <hr />
   {description}
   <hr />
</body>
</html>"""
    with open("personal_web_page.html", "w") as html_file:
        html_file.write(html_content)
    print("Web page created successfully as 'personal_web_page.html'.")

personal_web_page_generator()
