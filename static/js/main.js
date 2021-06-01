// calcula a media no front end da pagina de perfil individual..............

function calculaMedia(){
  let tds = document.getElementsByTagName("td");
  let semestres = document.getElementsByClassName("tri");
  let pegaSemestre = new Array();
  let nota = tds[tds.length - 1].innerText;
  let notaElemento = tds[tds.length - 1];
  for (var i = 0; i<semestres.length;i++){
    pegaSemestre.push(semestres[i].innerText);
  }
  let filtraSemestre = pegaSemestre.filter(function(valor, indice) {
    return pegaSemestre.indexOf(valor) === indice;
  })
  let media = nota / filtraSemestre.length;
  if (media > 5 && media < 7){
      notaElemento.innerHTML = `${media.toFixed(1)} <br>Aprovando`;
      notaElemento.setAttribute("style", "color: orange");
  }else if (media > 7){
    notaElemento.innerHTML = `${media.toFixed(1)} <br>Aprovando`;
    notaElemento.setAttribute("style", "color: teal");
  }else if (media < 5 ){
    notaElemento.innerHTML = `${media.toFixed(1)} <br> <strong>Reprovando!</strong>`;
    notaElemento.setAttribute("style", "color: red");
  }
  rolarParaFormulario();
}

// gera o PDF da funcao de perfil individual....................................

function printData() {
    let divToPrint = document.getElementById("tabela");
    let total = document.getElementById("total");
    let media = document.getElementById("media");
    let th = document.getElementsByTagName("th");
    let td = document.getElementsByTagName("td");
    let nomee = document.getElementsByTagName("h1")[1];
    let newWin = window.open("");
    for (var i = 0; i < th.length; i++) {
      th[i].style = `padding: 1%; color: red; margin: 1%; border: 1px solid black; 
                      font-size: 15pt; font-family: Arial, sans-serif; margin: 1%;`
    }
    for (var i = 0; i < td.length; i++) {
      td[i].style = `padding: 1%; color: black; margin: 1%; border-right: 1px solid black; 
        font-size: 11pt; font-family: Arial, sans-serif; margin: 1%;border-bottom: 1px solid black`
    }
    divToPrint.setAttribute("style", "margin:auto");
    divToPrint.setAttribute("style", "width:80vw");
    newWin.document.write("Nome: " + nomee.innerText.toUpperCase());
    newWin.document.write(divToPrint.outerHTML);
    newWin.document.write("TOTAL:&nbsp;&nbsp;&nbsp;" + total.outerHTML + "<br>");
    newWin.document.write("MÉDIA:&nbsp;&nbsp;&nbsp;" + media.outerHTML);
    newWin.print();
    newWin.close();
    atualizar();
  }


// faz reload da pagna sem fazer post no banco de dados ..............................

function atualizar() {
  let nome = document.getElementsByTagName("h1")[1];
  let perfil = nome.innerText;
  document.location.href = `/perfil/${perfil}`;
}


function filtrar(radioButton, filtro) {
  let busca = document.getElementById("busca");
  let radio = document.getElementsByName("radio")[radioButton];
  let botao = document.getElementById("submit");

  busca.value = filtro;
  radio.checked = true;
  botao.click();
}

// validando form de cadastros de alunos ...................................

function validar() {
  let inputs = document.querySelectorAll(".inputs");
  let nome = inputs[0];
  let turma = inputs[1];
  let rg = inputs[2];
  let cpf = inputs[3];
  let mensagem = document.getElementsByClassName("mensagem-erro");
  let botao = document.getElementById("submeter")
  if( (nome.value).length < 1) {
    erro = mensagem[0];
    console.log("erro");
    erro.setAttribute("style", "display: block");
    return;
  }
  if( (turma.value).length < 1) {
    erro = mensagem[1];
    erro.setAttribute("style", "display: block");
    return;
  }
  if ((rg.value).length == 0) {
    rg.value = "000000"
  }
  if ((cpf.value).length == 0) {
    cpf.value = "00000000000"
  }
  botao.setAttribute("type", "submit");
  botao.click();
}

// voltar xD..

function back(){
  window.history.back();
}

// interaçoes da tela de cadastro......................------------------//

let notificacao = document.querySelectorAll(".h1");
let formulario = document.getElementById("formulario-perfil");
let filhos = formulario.childNodes;
let alerta = document.createElement("h3");
let botaoNotas = document.getElementById("insereNotas");
formulario.addEventListener("click", mudanca);
alerta.innerText = `* Os campos de notas não podem ficar vazios *`;
alerta.style = `color: #F9C743;`;

function mudanca(){
  notificacao[2].innerHTML = `Clique em <strong style="color: red; background: white;">
      Atualizar tabela</strong> caso queira limpar os campos.`;
  notificacao[2].style = "font-size: 10pt; color: #F9C743; background-color: #60371E; padding: 1%;"
}
function checarNotas(){
  if (!filhos[8].value || !filhos[12].value){
    formulario.insertBefore(alerta, filhos[14]);
    return;
  }
  alerta.remove();
  botaoNotas.setAttribute("type", "submit");
}

function rolarParaFormulario(){
  formulario.scrollIntoView(false);
}

//----------------------------------------------------------------------------------//