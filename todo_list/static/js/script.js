// generate note dots in resize
function addDots() {
    let bodyHight = document.querySelector(".to-do-list-body").offsetHeight;
    let dotHight = document.querySelector(".dot").offsetHeight;
    let length = bodyHight / dotHight;

    let box = "";
    for (let i = 0; i < length; i++) {
        box += `<div class="dot"></div>`;
    }
    document.querySelector(".dots").innerHTML = box;
}

// delete task
function deleted(index) {
    const form = document.getElementById("delete" + index);
    form.submit();
}

function checked(index) {
    const form = document.getElementById("change" + index);
    form.submit();
}


document.addEventListener("DOMContentLoaded", () => {
    addDots()
});
