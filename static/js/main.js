function printData() {
    var divToPrint = document.getElementById("tabela");
    var nomee = document.getElementsByTagName("h1")[1];
    newWin = window.open("");
    newWin.document.write("Nome: " + nomee.innerText.toUpperCase());
    newWin.document.write(divToPrint.outerHTML);
    
    newWin.print();
    newWin.close();
  }

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
function back(){
  window.history.back();
}