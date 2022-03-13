function newElement() {
    let li = document.createElement("li");
    let inputValue = document.getElementById("input").value;
    let t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must write something!");
    }
    else {
        document.getElementById("box_list").appendChild(li);
    }
    document.getElementById("input").value = "";

    let remove_btn = document.createElement("button");
    let remove_text = document.createTextNode("\u00D7");
    let copy_btn = document.createElement("button");
    let copy_text = document.createTextNode("Copy");

    remove_btn.className = "close";
    copy_btn.className = "copy";

    remove_btn.appendChild(remove_text);
    copy_btn.appendChild(copy_text);

    li.appendChild(remove_btn);
    li.appendChild(copy_btn);

    let copy = document.getElementsByClassName("copy");

    for (let i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            let div = this.parentElement;
            div.style.display = "none";
        }
    }
    for(let i = 0; i < copy.length; i++){
        copy[i].onclick = function (){
            copy = li.cloneNode(true);
            li.appendChild(copy);
        }
    }
}

let close = document.getElementsByClassName("close");
for (let i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        let div = this.parentElement;
        div.style.display = "none";
    }
}
