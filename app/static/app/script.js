function validateForm() {
  var x = document.forms["myForm"]["pesquisa"].value;
  if (x == "") {
    alert("Inserir ao menos uma letra para pesquisar!");
    return false;
  }
}