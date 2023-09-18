from django.urls import reverse

from simple_menu import Menu, MenuItem


def profile_title(request):
    """Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return f"{name}'s Profile"

Menu.add_item("menu", MenuItem("Subpages",
                               reverse('about'),
                               icon="menu-app",))
