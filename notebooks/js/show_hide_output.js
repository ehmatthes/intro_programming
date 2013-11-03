$(document).ready(function(){
  $("button.hide_output_all").click(function(){
    $("div.output").hide();
    $("button.show_output_all").show();
    $("button.hide_output_all").hide();
  });
});

$(document).ready(function(){
  $("button.show_output_all").click(function(){
    $("div.output").show();
    $("button.show_output_all").hide();
    $("button.hide_output_all").show();
  });
});


$(document).ready(function(){
  $("button#hide_output_0").click(function(){
    $("div#output_0").hide();
    $("button#show_output_0").show();
    $("button#hide_output_0").hide();
  });
});

$(document).ready(function(){
  $("button#show_output_0").click(function(){
    $("div#output_0").show();
    $("button#show_output_0").hide();
    $("button#hide_output_0").show();
  });
});