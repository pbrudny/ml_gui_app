from taipy.gui import Gui

content = ""
img_path = "logo.png"

index = """
<|text-center|
<|{img_path}|image|>

<|{content}|file_selector|>
select an image from your file system
>
"""

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)

