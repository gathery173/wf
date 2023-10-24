import flet as ft
def NavBar(page):

    NavBar = ft.AppBar(
            leading_width=40,
            title=ft.Text("Gathery"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT
        )

    return NavBar
