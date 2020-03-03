var todosEl = JSON.parse(document.querySelector("#todos-el").textContent);
var submitTo = JSON.parse(document.querySelector("#submit-to").textContent); // new
var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value; // new
var app = new Vue({
	el: "#app",
	delimiters: ["d(", ")b"],
	data: {
		todos: todosEl,
		todoSubmit: '', // new
	},
	methods: { // new
		submitToDo: function() {
			axios({
				method: "POST",
				url: submitTo,
				data: {
					text: this.todoSubmit,
				},
				headers: {
					"X-CSRFToken": csrftoken,
				},
			}).then(
				(response) => {
					this.todos = response.data.todos;
					this.todoSubmit = '';
				}

			);
		},
	},
	
})
