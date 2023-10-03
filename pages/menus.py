from django.contrib.auth import get_user_model
from django.urls import reverse
from simple_menu import Menu, MenuItem

User = get_user_model()
def profile_title(request):
    """Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return f"{name}'s Profile"

Menu.add_item("menu", MenuItem("Главная",
                               reverse('home'),
                               icon="menu-app",))

Menu.add_item("menu", MenuItem("О нас",
                               reverse('about'),
                               icon="menu-app",))

Menu.add_item("menu", MenuItem('Личный кабинет',
                               url=lambda request: request.user.get_absolute_url,
                               check=lambda request: request.user.is_authenticated,
                               icon='menu-app'))

Menu.add_item("menu", MenuItem('Мои автомобили',
                               url=lambda request: request.user.get_absolute_url,
                               check=lambda request: request.user.is_authenticated,
                               icon='menu-app'))

Menu.add_item("menu", MenuItem('Выйти',
                               reverse('account_logout'),
                               check=lambda request: request.user.is_authenticated,
                               icon='menu-app'))

Menu.add_item("menu", MenuItem('Войти',
                               reverse('account_login'),
                               check=lambda request: not request.user.is_authenticated,
                               icon='menu-app'))

Menu.add_item("menu", MenuItem('Регистрация',
                               reverse('account_signup'),
                               check=lambda request: not  request.user.is_authenticated,
                               icon='menu-app'))