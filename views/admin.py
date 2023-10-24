from flet import *

def AdminHomeView(page):

    body = Column()
    body.controls.append(Row([Text("Admin", weight = FontWeight.BOLD)], alignment = MainAxisAlignment.CENTER))
    body.controls.append(Divider())

    white_con = Container(theme=Theme(color_scheme_seed=colors.LIGHT_BLUE_600),
                          theme_mode=ThemeMode.DARK)
    white_con2 = Container(theme=Theme(color_scheme_seed=colors.LIGHT_BLUE_600),
                           theme_mode=ThemeMode.DARK)


    event_list_card = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        title=TextButton(icon=icons.FORMAT_LIST_NUMBERED,
                                         text="Список заходів")
                    ),
                ]
            ),
            width=2000,
            padding=10
        ), elevation=20
    )

    class_list_card = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        title=TextButton(icon=icons.FORMAT_LIST_BULLETED,
                                         text="Список класів", on_click=lambda _: page.go("/admin/classes"))
                    ),
                ]
            ),
            width=2000,
            padding=10,
        ), elevation=20
    )

    white_con.content = event_list_card

    white_con2.content = class_list_card

    body.controls.append(event_list_card)
    body.controls.append(class_list_card)

    return body