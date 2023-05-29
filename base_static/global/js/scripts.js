(() =>{
    const forms = document.querySelectorAll('.form-delete')

    for (const form of forms) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const confirmed = confirm('Are you sure?');

            if (confirmed) {
                form.submit();
            }
        });
    }
})();


(() =>{
    const buttonCloseMenu = document.querySelector('.button-close-menu');
    const buttonShowMenu = document.querySelector('.button-show-menu');
    const menuContainer = document.querySelector('.menu-container');

    const buttonShowMenuVisibleClass = 'button-show-menu-visible';
    const menuHiddenClass = 'menu-hidden';

    const closemenu = () => {
        buttonShowMenu.classList.add(buttonShowMenuVisibleClass);
        menuContainer.classList.add(menuHiddenClass);
    };

    const showmenu = () => {
        buttonShowMenu.classList.remove(buttonShowMenuVisibleClass);
        menuContainer.classList.remove(menuHiddenClass);
    };

    if (buttonCloseMenu) {
        buttonCloseMenu.removeEventListener('click', closemenu);
        buttonCloseMenu.addEventListener('click', closemenu);
    }

    if (buttonShowMenu) {
        buttonShowMenu.removeEventListener('click', showmenu);
        buttonShowMenu.addEventListener('click', showmenu);
    }
})();

(() =>{
    const authorsLogoutLinks = document.querySelectorAll('.authors-logout-link');
    const formLogout = document.querySelector('.form-logout');

    for (const link of authorsLogoutLinks) {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            formLogout.submit();
        });
    }
})();
