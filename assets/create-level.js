let questionCount = 0;
let questionCountEl = document.querySelector("#question-count")

document.querySelector("#addquestion").addEventListener("click", (ev) => {
    ev.preventDefault()
    let que = questionCount++;
    questionCountEl.value = questionCount
    let temp = document.createElement("template")
    
    temp.innerHTML = `
        <ul>
            <li>
                <b>Вопрос:</b>
                <input type="text" name="question-${que}" />
            </li>
            <li>
                <b>Выбор:</b>
                <ul>
                    <li><input type="radio" name="question-${que}-correct" value="1"> <input type="text" name="question-${que}-choise-1"></li>
                    <li><input type="radio" name="question-${que}-correct" value="2"> <input type="text" name="question-${que}-choise-2"></li>
                    <li><input type="radio" name="question-${que}-correct" value="3"> <input type="text" name="question-${que}-choise-3"></li>
                    <li><input type="radio" name="question-${que}-correct" value="4"> <input type="text" name="question-${que}-choise-4"></li>
                </ul>
            </li>
        </ul>
    `;

    document.querySelector("#questions").appendChild(temp.content.children[0])
});
