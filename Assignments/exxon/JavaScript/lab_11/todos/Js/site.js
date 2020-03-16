let app = new Vue({
    el: '#app',
    data: {
        message: 'Your Todo List',
        todos:[

        ],
        newTodo: {
            text: '',
            isCompleted: false
        },

    
},

            
            
            

methods: {
    addTodo: function() {
        this.todos.push({text: this.newTodo.text, isComplete: this.newTodo.isComplete})
    },

    eraseTodo: function(index){
        this.todos.splice(index,1);
    },

    completeTask: function(todos){
        todos.isCompleted = !todos.isCompleted;
    }
}
});


