document.addEventListener("DOMContentLoaded", function() {

    // Prevent closing from click inside dropdown
    document.querySelectorAll('.dropdown-menu').forEach(function(dropdown) {
        dropdown.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    });

    // Fixed menu on scroll for desktop
    if (window.innerWidth < 768) {
        const titleCategory = document.querySelector('.nav-home-aside .title-category');
        if (titleCategory) {
            titleCategory.addEventListener('click', function(e) {
                e.preventDefault();
                const menuCategory = document.querySelector('.menu-category');
                if (menuCategory) {
                    menuCategory.style.display = menuCategory.style.display === 'none' || !menuCategory.style.display ? 'block' : 'none';
                    document.querySelectorAll('.menu-category .submenu').forEach(function(submenu) {
                        submenu.style.display = 'none';
                    });
                }
            });
        }

        document.querySelectorAll('.has-submenu a').forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const submenu = this.nextElementSibling;
                if (submenu) {
                    submenu.style.display = submenu.style.display === 'none' || !submenu.style.display ? 'block' : 'none';
                }
            });
        });

    } // end if


    // Bootstrap tooltip
    if (document.querySelectorAll('[data-bs-toggle="tooltip"]').length > 0) {
        document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function(elem) {
            new bootstrap.Tooltip(elem); // Assumes Bootstrap's JS is loaded
        });
    } // end if

    // Offcanvas menu
    document.querySelectorAll("[data-trigger]").forEach(function(trigger) {
        trigger.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            const offcanvasId = this.getAttribute('data-trigger');
            const offcanvas = document.querySelector(offcanvasId);
            if (offcanvas) {
                offcanvas.classList.toggle("show");
                document.body.classList.toggle("offcanvas-active");
                const screenOverlay = document.querySelector(".screen-overlay");
                if (screenOverlay) {
                    screenOverlay.classList.toggle("show");
                }
            }
        });
    });


    // Close menu by clicking
    document.querySelectorAll(".btn-close, .screen-overlay").forEach(function(elem) {
        elem.addEventListener('click', function() {
            const screenOverlay = document.querySelector(".screen-overlay");
            if (screenOverlay) {
                screenOverlay.classList.remove("show");
            }
            document.querySelectorAll(".mobile-offcanvas").forEach(function(menu) {
                menu.classList.remove("show");
            });
            document.body.classList.remove("offcanvas-active");
        });
    });

});
