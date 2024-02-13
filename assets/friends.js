function unfriend(el) {
    fetch(
        window.location.origin +
            "/accounts/unfriend/" +
            el.dataset.code
    )
        .then((res) => res.json())
        .then((res) => {
            if (!res.friend_find) {
                alert("This friend not find");
            } else {
                el.parentElement.remove();
                let temp = document.createElement("template");
                temp.innerHTML = `
                    <p>
                        ${res.friend_username}
                        #${res.friend}
                        <button class="sendrequest" onclick="sendrequest()" data-code="${res.friend}">Send request</button>
                    </p>
                `;

                document
                    .querySelector("#notfriends")
                    .appendChild(temp.content.children[0]);
            }
        });
}

function accept(el) {
    fetch(
        window.location.origin +
            "/accounts/acceptrequest/" +
            el.dataset.id
    )
        .then((res) => res.json())
        .then((res) => {
            if (!res.friendrequest_find) {
                alert("Your request not find");
            } else {
                el.parentElement.remove();
                let temp = document.createElement("template");
                temp.innerHTML = `
                    <p>
                        ${res.fromuser_username}
                        #${res.fromuser}
                        <button class="unfriend" onclick="unfriend(this)" data-code="${res.fromuser}">Unfriend</button>
                    </p>
                `;

                document
                    .querySelector("#friends")
                    .appendChild(temp.content.children[0]);
            }
        });
}

function decline(el) {
    fetch(
        window.location.origin +
            "/accounts/declinerequest/" +
            el.dataset.id
    )
        .then((res) => res.json())
        .then((res) => {
            if (!res.friendrequest_find) {
                alert("Your request not find");
            } else {
                el.parentElement.remove();
                let temp = document.createElement("template");
                temp.innerHTML = `
                    <p>
                        ${res.fromuser_username}
                        #${res.fromuser}
                        <button class="sendrequest" onclick="sendrequest(this)" data-code="${res.fromuser}">Send request</button>
                    </p>
                `;

                document
                    .querySelector("#notfriends")
                    .appendChild(temp.content.children[0]);
            }
        });
}

function sendrequest(el) {
    fetch(
        window.location.origin +
            "/accounts/sendrequest/" +
            el.dataset.code
        )
        .then((res) => res.json())
        .then((res) => {
            if (!res.to_user_find) {
                alert("This user not find");
            } else if (res.alreadysended) {
                alert("You already sended this request");
            } else {
                el.setAttribute("disabled");
            }
        });
}

send_by_code_form.code.addEventListener("input", (ev) => {
    ev.target.value = ev.target.value.replace(/[^\d\w]/g, "").toUpperCase()
})

send_by_code_form.addEventListener("submit", (ev) => {
    ev.preventDefault()
    fetch(
        window.location.origin +"/accounts/sendrequest/" + ev.target.code.value)
    .then((res) => res.json())
    .then((res) => {
        if (!res.to_user_find) {
            alert("This user not find");
        } else if (res.alreadysended) {
            alert("You already sended this request");
        } else {
            send_by_code_form.reset()
        }
    });
    
})