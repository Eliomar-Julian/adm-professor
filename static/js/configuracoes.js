// eventos
let botaoPronto = document.getElementById("pronto");
// criar lista com o nome das materias
botaoPronto.addEventListener("click", () => {
    let nomes = document.getElementsByClassName("nome-disciplina");
    let lista = new Array();
    for (var i = 0; i < (nomes.length); i++) {
        lista.push(nomes[i].value);
        if (i != 0){
            nomes[i].remove();
        }
    }
    nomes[0].value = lista;
    botaoPronto.setAttribute("type", "submit");
    botaoPronto.click();
})
// mudar as cores...
let botaoCor = document.querySelectorAll("input[type=color]");
botaoCor[0].addEventListener("input", (MouseEvent) => {
    document.getElementsByClassName("fundo")[0].setAttribute(
        "style", `background-color: ${botaoCor[0].value}`);
})
botaoCor[1].addEventListener("input", (MouseEvent) => {
    document.getElementsByClassName("texto")[0].setAttribute(
        "style", `color: ${botaoCor[1].value}`);
})
botaoCor[2].addEventListener("input", (MouseEvent) => {
    document.getElementsByClassName("menu")[0].setAttribute(
        "style", `background-color: ${botaoCor[2].value}`);
})

function addInput() {
    let form = document.getElementById("form-1");
    let botao = document.getElementById("pronto");
    let quebraLinha = document.createElement("br");
    let inputText = document.createElement("input");
    inputText.setAttribute("name", "nome");
    inputText.setAttribute("type", "text");
    inputText.setAttribute("class", "nome-disciplina");
    form.insertBefore(quebraLinha, botao);
    form.insertBefore(inputText, botao);
    form.insertBefore(quebraLinha, botao);
    console.log(form);
}

function verCor(){
    let cores = document.querySelectorAll("input[type=color]");
    let fundo = cores.item(0);
    console.log(fundo);
}
