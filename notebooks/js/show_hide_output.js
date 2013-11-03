// Show all output
$(document).ready(function(){
	 $("button.show_output_all").click(function(){
		  // Make all output visible
		  $("div.output").show();
		  // Make sure all buttons toggled to 'hide output'
		  $("button.show_output").hide();
		  $("button.hide_output").show();
	 });
});

// Hide all output
$(document).ready(function(){
	 $("button.hide_output_all").click(function(){
		  // Hide all output
		  $("div.output").hide();
		  // Make sure all buttons toggled to 'show output'
		  $("button.show_output").show();
		  $("button.hide_output").hide();
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