// eventos

let botaoPronto = document.getElementById("pronto");

// criar lista com o nome das materias

botaoPronto.addEventListener("click", () => {
    let nomes = document.getElementsByClassName("nome-disciplina");
    let lista = new Array();
    for (var i = 0; i < nomes.length; i++) {
        lista.push(nomes[i].value);
        if (i >= 1){
            nomes[i].remove();
        }
    }
    nomes[0].value = lista;
    botaoPronto.setAttribute("type", "submit");
    botaoPronto.click();
})
// mudar as cores...



// adicionar inputs de disciplinas dinamicamente...

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
