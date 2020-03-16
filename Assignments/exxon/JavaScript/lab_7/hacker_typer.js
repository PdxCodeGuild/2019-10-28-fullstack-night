var x = 0;
	var hacktyper = document.getElementById("hacktyper");
	var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	var charLength = chars.length;
	window.onload = function() {
		the_i = setInterval(function(){
			var el = document.createElement('span');
			var rand = Math.floor(Math.random() * charLength);
			//var charText = document.createTextNode(chars[x++]);
			var charText = document.createTextNode(chars[rand]);
			if(x >= charLength) {
				x = 0;
			}else {
				hacktyper.appendChild(el).appendChild(charText);
			}
		},10);
	}
