const VERSION = 29;
// disclaimer: My semicolons aren't consistent
// I should use camel case but don't

/*
Show DOM by adding and removing stuff
Get input
Events
use Node.querySelector
*/


if (VERSION === 1) {
	alert("Hello");
	console.log("Goodbye");
}

else if (VERSION === 2) {
	if (true) { var a = 0;
	}
	console.log(a);
}

else if (VERSION === 3) {
    if (true) { let a = 0;
	}
	console.log(a);
}

else if (VERSION === 4) {
	if (true) { const a = 0;
	}
	console.log(a);
}

else if (VERSION === 5) {
    var a = 0;
    a = 1;
	console.log(a);
    let b = 0;
    b = 1;
	console.log(b);
}

else if (VERSION === 6) {
	const a = 0;
	a = 1;
	console.log(a);
  console.log('hello')
}

else if (VERSION === 7) {
    let data_arr = [5, 5.5, "hi 5 times", true, null, undefined, NaN];
    for (let i=0; i<data_arr.length; i++) {
        console.log(data_arr[i], typeof data_arr[i]);
    }
}

else if (VERSION === 8) {
    let my_arr = ['a', 'b', 'c'];
    my_arr.push('d');
    console.log(my_arr, my_arr.length, my_arr[1]);
}

else if (VERSION === 9) {
    let my_obj = {'July': 'sunny', 'October': 'rainy', 'January': 'snowy'};
    my_obj.July += '!';
    console.log(my_obj);
}

else if (VERSION === 10) {
    let my_num = 3;
    // my_num += 1;
    /*
    my_num = 5;
    my_num = 0;
    */
    console.log(my_num);
}

else if (VERSION === 11) {
    let user_name = prompt('give your name ');
    alert(`Your name is ${user_name}`);
}

else if (VERSION === 12) {
    let str_num = '5';
    console.log(str_num == 5, str_num === 5);
}

else if (VERSION === 13) {
    str_arr = ['a', 'b', 'c'];
    for (let i=0; i<str_arr.length; i++) {
        console.log(i);
        if (str_arr[i] == 'a') {
            console.log('it\'s a');
        } else if (str_arr[i] == 'b') {
            console.log('it\'s b');
        } else {
            console.log('it\'s neither');
        }
    }
}

else if (VERSION === 14) {
    let num = 5;
    if (num) {
        console.log('truthy');
    } else {
        console.log('falsy');
    }
}

else if (VERSION === 15) {
    let num1 = 7;
    let num2 = 12;
    console.log(num1 > 10? 'num1 is big': 'num1 is small');
    console.log(num2 > 10? 'num2 is big': 'num2 is small');
}
else if (VERSION === 16) {
    console.log(add(21, 6));
    function add(a, b) {
        return a + b;
    }

}

else if (VERSION === 17) {
    console.log(add3(2, 6, 4));
    let add3 = function(a, b, c) {
        return a + b + c;
    }
}

else if (VERSION === 18) {
    let mult3 = (a, b, c=1) => a * b * c;
    console.log(mult3(2, 6, 4));
    console.log(mult3(2, 6));
}

else if (VERSION === 19) {
    function args_example() {
        for (let i=0; i<arguments.length; i++) {
            console.log(arguments[i]);
        }
    }
    args_example(1, 2, 'a', true, [])
}

else if (VERSION === 20) {
    let blue_div = document.querySelector('#blue-div');
    blue_div.innerText = 'hi';
}

else if (VERSION === 21) {
    window.onload = function() {
        let blue_div = document.querySelector('#blue-div');
        blue_div.innerText = 'hi';
    }
}

else if (VERSION === 22) {
    window.onload = function() {
        let blue_div = document.querySelector('#blue-div');
        blue_div.innerHTML = '<button>pushme</button>';
    }
}

else if (VERSION === 23) {
	window.onload = function() {
		let reds = document.querySelectorAll('.red-div');
        console.log(reds);
		reds[0].style.backgroundColor = 'green';
	}
}

else if (VERSION === 24) {
	window.onload = function() {
		let main_body = document.querySelector('body');
		for (let i=0; i < 50; i++) {
			let new_div = document.createElement('div');
			new_div.style.backgroundColor = 'green';
			main_body.appendChild(new_div);
		}
	}
}

else if (VERSION === 25) {
	window.onload = function() {
    let blue_div = document.querySelector('#blue-div');
    let color_input = document.querySelector('#color-input');
    color_input.addEventListener('input', function() {
      blue_div.style.backgroundColor = color_input.value;
    });
	}
}

else if (VERSION === 26) {
	window.onload = function() {
		let main_body = document.querySelector('body');
		let main_ol = document.createElement('ol');
		main_body.appendChild(main_ol);
		for (let i=100; i <= 200; i=i+10) {
			let new_li = document.createElement('li');
			new_li.innerText = `(${i}) ${Date.now()}`;
			main_ol.insertBefore(new_li, main_ol.childNodes[0]);
		}
	}
}

else if (VERSION === 27) {
	window.onload = function() {
		let main_body = document.querySelector('body');
		let main_ol = document.createElement('ol');
		main_body.appendChild(main_ol);
		for (let i=100; i <= 200; i=i+10) {
			let new_li = document.createElement('li');
			new_li.innerText = `(${i}) ${Date.now()}`;
			main_ol.insertBefore(new_li, main_ol.childNodes[0]);
		}
	}
}

else if (VERSION === 28) {
	window.onload = function() {
		let reds = document.querySelectorAll('.red-div');
		reds[0].onclick = () => (this.style.backgroundColor = 'green');
		function clickFun() {
			this.style.backgroundColor = 'orange';
		}
		reds[1].onclick = clickFun;
	}
}

else if (VERSION === 29) {
	window.onload = function() {
		let reds = document.querySelectorAll('.red-div');
		reds[0].onclick = () => (console.log(this));
		function clickFun() {
			console.log(this);
		}
		reds[1].onclick = clickFun;
	}
}
