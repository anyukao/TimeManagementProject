document.getElementById("logincheck").addEventListener("click", function () {

  var pass1 = document.getElementById("pass1").value;
  var pass2 = document.getElementById("pass2").value;

  if (pass1=="" && pass2==""){
    alert("Заполните поля. Введите пароль");
  }
  else if(pass1 === pass2) {
      var form = document.querySelector("form");
      form.submit(); // Отправляем форму, если пароли совпадают
      // console.log("")
  } else {
      alert("Пароли не совпадают. Пожалуйста, введите одинаковые пароли.");
  }
});
