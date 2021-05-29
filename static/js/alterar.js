function mudando(){
    // muda a legenda da tabela para o nome do aluno selecionado
    let legenda = document.querySelectorAll("legend");
    legenda[0].innerText = decodeURI(window.location.pathname).slice(9).toUpperCase();
}

function mudar(botao) {
    // muda a url para o perfil de deleção do aluno em questão
    let nome = botao.value;
    window.location.replace(`/alterar/${nome}`);
}

function voltar(){
    // volta a pagina de deleção...
    document.location.replace('/deletar');
}

function confirmar(botao) {
    let valores = document.getElementsByTagName('input');
    let oculto = document.querySelectorAll('input[type=hidden]');
    let confirmar = document.querySelectorAll('button');
    let ids = new Array();
    let trimestre = new Array();
    let atividades = new Array();
    let notas = new Array();
    let valor = new Array();

    for (var i = 0; i < valores.length; i++) {
        if (valores[i].name == "id"){
            ids.push(valores[i].value);
        }else if (valores[i].name == "tri"){
            trimestre.push(valores[i].value);
        }else if (valores[i].name == "ati"){
            atividades.push(valores[i].value);
        }else if (valores[i].name == "not") {
            notas.push(valores[i].value);
        }else if (valores[i].name == "val"){
            valor.push(valores[i].value)
        }

    }
    console.log(confirmar[0]);
    oculto[0].value = `${ids};${trimestre};${atividades};${notas};${valor}`
    confirmar[0].type = "submit";
}
function redirecionar(botao) {
    let url = decodeURI(window.location.pathname).slice(9)
    window.location.replace(`/perfil/${url}`);
}

