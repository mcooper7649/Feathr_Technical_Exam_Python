$("form[name=signup_form]").submit(function (e){
    let $form = $(this);
    let $error = $form.find(".error");
    let data = $form.serialize();

  $.ajax({
    url: "/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.assign('/me/')
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form]").submit(function(e) {

  const $form = $(this);
  const $error = $form.find(".error");
  const data = $form.serialize();

  $.ajax({
    url: "/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/me/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});
