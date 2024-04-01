from taipy.gui import Gui

content = ""
img_path = "placeholder_image.png"

index = """
<|text-center|
<|{"logo.png"}|image|>

<|{content}|file_selector|extensions=.png|>
select an image from your file system

<|{img_path}|image|>
>
"""

def on_change(state, var_name, var_val):
    if var_name == "content":
        state.img_path = var_val
    print(var_name, var_val)


app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)

