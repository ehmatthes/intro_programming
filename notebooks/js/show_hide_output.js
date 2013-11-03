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

// Show single output
$(document).ready(function(){
	 $("button.show_output").click(function(){
		  var id_num = $(this).attr('target')
		  $("#output_"+id_num).show();
		  $("button#show_output_"+id_num).hide();
		  $("button#hide_output_"+id_num).show();
	 });
});

// Hide single output
$(document).ready(function(){
	 $("button.hide_output").click(function(){
		  var id_num = $(this).attr('target')
		  $("#output_"+id_num).hide();
		  $("button#hide_output_"+id_num).hide();
		  $("button#show_output_"+id_num).show();
	 });
});