let disabled = false;
let answerIsCorrect = false;

function answer(button) {
    if (!disabled) {
        fetch(
            window.location.origin +
                "/level/getanswer/" +
                level +
                "/" +
                question +
                "/" +
                button.getAttribute("data-answer")
        )
            .then((res) => res.json())
            .then((res) => {
                disabled = true;

                document.querySelector(".popup-bg").style.display = "flex";
                if (!res.levelfind) {
                    document.querySelector(".popup-text").textContent =
                        "Уровень не найден";
                } else if (!res.questionfind) {
                    document.querySelector(".popup-text").textContent =
                        "Вопрос не найден";
                } else if (res.answered) {
                    document.querySelector(".popup-text").textContent =
                        "Ты уже ответил на этот вопрос";
                } else if ((answerIsCorrect = res.correct)) {
                    document.querySelector(".popup-text").textContent =
                        "Правильно";
                } else {
                    document.querySelector(".popup-text").textContent =
                        "Не правильно";
                }
            });
    }
}
