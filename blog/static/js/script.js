$(document).ready(function() {
	$('.sqrt').click(function() {
		var num = $('#num1').val();
		var result = Math.sqrt(num);
		alert('Квадратный корень из ' + num + ' = ' +result);
	})

	$('.power').click(function() {
		var num = $('#num2').val();
		var pow = $('#power').val();
		var result = Math.pow(num, pow);
		alert(num+ ' в степени ' + pow + ' = ' + result);
	})

})