from flet import *
from data import get_classes, edit_class, delete_class, add_class
from flet_route import Params, Basket

def AdminClassesView(page):

    content = Column(height=700, width = 2000)
    content.controls.append(Row([Text("Список Класів", weight = FontWeight.BOLD)], alignment = MainAxisAlignment.CENTER))
    content.controls.append(Divider())
    cc = Column(height=600, width = 2000, scroll=ScrollMode.ALWAYS, on_scroll_interval = 0)

    back_card = Card(
        content=Container(
            content=Column(
                [IconButton(icon=icons.ARROW_BACK, on_click = lambda _ : page.go("/admin")
                            )
                    ]
            ),
            width=60,
            padding=10
        ), elevation = 20
    )
    def add(d):
        def save(s):
            add_class(teacher.value, index.value, leader.value, room.value, login.value, pwd.value)

            cc.controls.clear()
            for i in get_classes():
                cc.controls.append(
                    Class(i["index"], i["teacher"], i["leader"], i["room"], i["pass"], i["login"]))
                page.update()
            page.update()

        index = TextField(label="Індекс")
        teacher = TextField(label="Вчитель")
        leader = TextField(label="Лідер")
        room = TextField(label="Кабінет")
        login = TextField(label="Логін")
        pwd = TextField(label = "Пароль")
        save_button = TextButton(text="Зберегти", on_click=lambda _: save(_), width=900)

        add_dialog = BottomSheet(Container(
            Column([
                index,
                teacher,
                leader,
                room,
                login,
                pwd,
                save_button
            ], scroll=ScrollMode.ALWAYS

            ), padding=15)
        )

        page.dialog = add_dialog
        add_dialog.open = True
        page.update()

    new_concert_card = Card(
        content=Container(
            content=Column(
                [IconButton(icon=icons.ADD, on_click = add
                                         )
                ]
            ),
            width = 60,
            padding=10
        ), elevation = 20
    )

    class Class(UserControl) :

        def __init__(self, id, teacher, leader, room, pwd, login) :
            super().__init__()

            self.card = None
            self.id = id
            self.login = login
            self.teacher = teacher
            self.leader = leader
            self.room = room
            self.pwd = pwd

        def build(self, dlg=None) :
            def extend(l) :

                def edit(_) :
                    action_dlg.open = False
                    page.update()

                    def save(s):
                        edit_class(self.teacher, teacher.value, index.value, leader.value, room.value, login.value, pwd.value)
                        edit_dialog.open = False
                        cc.controls.clear()
                        for i in get_classes():
                            cc.controls.append(
                                Class(i["index"], i["teacher"], i["leader"], i["room"], i["pass"], i["login"]))
                            page.update()
                        page.update()

                    index = TextField(label = "Індекс", value = self.id)
                    teacher = TextField(label = "Вчитель", value = self.teacher)
                    leader = TextField(label = "Лідер", value = self.leader)
                    room = TextField(label = "Кабінет", value = self.room)
                    login = TextField(label = "Логін", value = self.login)
                    pwd = TextField(label = "Пароль", value = self.pwd)
                    save_button = TextButton(text = "Зберегти", on_click = lambda _ : save(_), width = 900)

                    edit_dialog = BottomSheet(Container(
                        Column([
                            index,
                            teacher,
                            leader,
                            room,
                            login,
                            save_button
                        ], scroll = ScrollMode.ALWAYS

                            ), padding=15)
                        )

                    page.dialog = edit_dialog
                    edit_dialog.open = True
                    page.update()

                def delete(d):
                    delete_class(self.teacher)
                    cc.controls.clear()
                    for i in get_classes():
                        cc.controls.append(
                            Class(i["index"], i["teacher"], i["leader"], i["room"], i["pass"], i["login"]))
                        page.update()

                action_dlg = BottomSheet(Container(ResponsiveRow(controls=[
                    TextButton("Змінити", icon=icons.EDIT, on_click=edit),
                    TextButton("Видалити", icon=icons.DELETE, on_click=delete),
                    Container(height=10)],
                ), padding=15)
                )

                page.dialog = action_dlg
                action_dlg.open = True
                page.update()

            self.card = Card(
                content=Container(
                    content=Column(
                        controls=[ListTile(
                            leading=Text(f"{self.id}", size=20),
                            title=Text(f"{self.teacher}\n"
                                       , weight=FontWeight.BOLD),
                            subtitle=Text(f"Лідер        •  {self.leader}\n"
                                          f"Кабінет     •  {self.room}")
                        )]
                    ), padding=10, on_click=extend
                ),
                width=2000
            )

            return self.card


    content.controls.append(Row([back_card, new_concert_card]))
    for i in get_classes():

        cc.controls.append(Class(i["index"], i["teacher"], i["leader"], i["room"], i["pass"], i["login"]))
        page.update()

    content.controls.append(cc)

    return content
