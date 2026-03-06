import flet as ft

def main(page: ft.Page):
    page.title = "Flet in GitHub Codespaces"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt = ft.TextField(label="Dein Name")
    output = ft.Text()

    def say_hello(e):
        output.value = f"Hallo {txt.value}!"
        page.update()

    page.add(
        txt,
        ft.ElevatedButton("Sagen", on_click=say_hello),
        output
    )

ft.app(target=main)
