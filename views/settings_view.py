import flet as ft
user = []

def set_u(a):
    user.append(a)
    return user

def get_u():

    return user
def SettingsView(page):

    def toggle_dark_mode(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else:
            page.theme_mode = "dark"
            page.update()


    a = ft.TextField(label = "Login")

    def jj(k):
        set_u(a.value)
        print(user)
        page.client_storage.set("user", a.value)
        page.go("/profile")

    content = ft.Column(

            [
                ft.Row(
                [
                    ft.Text("My Settings", size=30),
                    ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30, on_click = lambda _ : jj(_)),

                    ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.TextButton("Light/Dark Mode", icon=ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_dark_mode)
                    ],
                )
            ], data = a.value
        )
    content.controls.append(a)

    return ft.View("/", controls = [content])
