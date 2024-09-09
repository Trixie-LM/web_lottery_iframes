class AuthLocators:
    # Поле для ввода логина
    LOGIN_FIELD = ("xpath", "//*[@name='login']")

    # Поле для ввода пароля
    PASSWORD_FIELD = ("xpath", "//*[@type='password']")

    # Кнопка входа
    ENTER_BUTTON = ("xpath", "(//*[text()='Войти' or text()='Log in'])[2]")

    # Заголовок модального окна входа
    LOGIN_MODAL_TITLE = ("xpath", "//h1")
