$(function() {
  // $('a#calculate').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/ajax_request', function(data) {
      console.log("Ajax Called");
      $("#result").text(data.result);
    });
    return false;

  });
