from flet import *
from data import check_login

def IndexPage(page):

    page.title = "Gathery"

    body = Column()

    def login_(a):
        try:
            if check_login(login.value, password.value) == "admin-login-true":

                page.go("/admin")
                page.update()

            if check_login(login.value, password.value) == "admin-login-false":
                snack = SnackBar(content=Text("Неправильний пароль!"))
                page.snack_bar = snack
                page.snack_bar.open = True
                page.update()
            if check_login(login.value, password.value) == "teacher-login-true":
                user = login.value[:login.value.index('@')]
                page.go(f"/home/{user}")
                page.update()

            if check_login(login.value, password.value) == "teacher-login-false":
                snack = SnackBar(content=Text("Неправильний пароль!"))
                page.snack_bar = snack
                page.snack_bar.open = True
                page.update()
            if check_login(login.value, password.value) == "unregistered":
                snack = SnackBar(content=Text("Незареєстрований користувач!"))
                page.snack_bar = snack
                page.snack_bar.open = True
                page.update()

        except:
            snack = SnackBar(content=Text("Сталася помилка! Перевірте правильність введених данних!"))
            page.snack_bar = snack
            page.snack_bar.open = True
            page.update()

    title_text = Row(controls=[Text("Вхід", size=30, weight=FontWeight.W_900)],
                     alignment=MainAxisAlignment.CENTER)

    text_under = Row(controls=[
        Text("до системи організації шкільних заходів", text_align=TextAlign.CENTER, color=colors.GREY)],
        alignment=MainAxisAlignment.CENTER)

    but = FilledTonalButton("Увійти в систему", width=300, on_click = lambda _ : login_(_))

    con = Container(height=80)

    login = TextField(label="Ім'я користувача", border=InputBorder.UNDERLINE)
    password = TextField(label="Пароль", border=InputBorder.UNDERLINE, password=True,
                         can_reveal_password=True)

    body_ = Row([Card(content=Container(Column([
        login,
        password,
        Container(height=20),
        but

    ]), padding=40), elevation=20)], alignment=MainAxisAlignment.CENTER)

    body.controls.append(con)

    body.controls.append(title_text)
    body.controls.append(text_under)
    body.controls.append(body_)
    appbar = AppBar(title = Text("Gathery"))

    return View("/", controls = [appbar, body])
