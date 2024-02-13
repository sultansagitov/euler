document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector(".sidebar");
    const sidebarToggle = document.querySelector(".sidebar-toggle");

    sidebarToggle.addEventListener("click", () => {
        sidebar.classList.toggle("active");
    });
});

const themeSwiter = {
    init() {
        this.wrapper = document.getElementById("theme-switcher-wrapper");
        this.button = document.getElementById("theme-switcher-button");
        this.theme = this.wrapper.querySelectorAll("[data-theme]");
        this.themes = [
            "theme-orange",
            "theme-purple",
            "theme-green",
            "theme-blue",
        ];
        this.events();
        this.start();
    },

    events() {
        this.button.addEventListener("click", this.displayed.bind(this), false);
        this.theme.forEach((theme) =>
            theme.addEventListener("click", this.themed.bind(this), false)
        );
    },

    start() {
        let theme = this.themes[theme_id - 1];
        document.body.classList.add(theme);
    },

    displayed() {
        this.wrapper.classList.contains("is-open")
            ? this.wrapper.classList.remove("is-open")
            : this.wrapper.classList.add("is-open");
    },

    themed(e) {
        this.themes.forEach((theme) => {
            if (document.body.classList.contains(theme))
                document.body.classList.remove(theme);
        });

        const formData = new FormData(document.querySelector("#theme_form"));
        formData.set(
            "theme",
            this.themes.indexOf(`theme-${e.currentTarget.dataset.theme}`) + 1
        );

        fetch("/accounts/change_theme", {
            method: "POST",
            body: formData,
        })
            .then((res) => res.json())
            .then((res) => {
                if (!res.correct)
                    console.error("Произошла ошибка при загрузке темы");
            })
            .catch((error) => {
                console.error("Произошла ошибка при загрузке темы", error);
            });

        return document.body.classList.add(
            `theme-${e.currentTarget.dataset.theme}`
        );
    },
};

themeSwiter.init();

let reader = new FileReader();

document
    .querySelector("#avatar_img")
    .addEventListener("change", function (event) {
        const formData = new FormData(document.querySelector("#avatar_form"));
        reader.readAsDataURL(document.querySelector("#avatar_img").files[0]);

        reader.onload = () => {
            document.querySelector(".profile-page .content__avatar").style[
                "background-image"
            ] = `url(${reader.result})`;
        };

        fetch("/accounts/upload_avatar", {
            method: "POST",
            body: formData,
        })
            .then((res) => res.json())
            .then((res) => {
                if (!res.correct)
                    console.error("Произошла ошибка при загрузке аватара");
            })
            .catch((error) =>
                console.error("Произошла ошибка при загрузке аватара", error)
            );
    });
