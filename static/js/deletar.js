let nomee;
document.addEventListener("dblclick", (e) => {
    autoOrganizar();
})

function abrirMsg(nome=null){
    let msg = document.getElementById('mensagem-delete');
    let frase = document.querySelector('p');
    msg.setAttribute("style", "display: block");
    if (nome) {
        nomee = nome;
        fr = `Deseja remover ${nome.value.toUpperCase()}?`;
        frase.innerText = fr;
    }
    return [msg, frase];
}

function fecharX() {
    var caixa = abrirMsg();
    caixa[0].setAttribute("style", "display: none");
    caixa[1].innerText = "";
}

function deletarNao() {
    fecharX();
}
function deletarSim() {
    let form = document.getElementById("form");
    form.setAttribute("method", "post");
    nomee.setAttribute("style", "background-color: red");
    nomee.setAttribute("type", "submit");
    nomee.click();
}
function organizar(bt) {
    let form = document.getElementById("form");
    form.setAttribute("method", "post");
    bt.setAttribute("type", "submit");
    bt.click();
}

function autoOrganizar(){
    let org = document.querySelectorAll('input[type=button]');
    org[0].click();
}

function checar() {
    let botao = document.querySelectorAll('input')[0];
    let lista = new Array();
    checando = document.getElementsByName('checado');
    for (let i = 0; i < checando.length; i++) {
        if (checando[i].checked) {
            lista.push(checando[i].value);
            checando[i].value = "";
        }
    }
    checando[0].value = lista;
    botao.setAttribute("type", "submit");
    botao.click();
}