var postgroupEl = JSON.parse(document.querySelector("#postgroup-el").textContent);
var submitTo = JSON.parse(document.querySelector("#submit-to").textContent);
var csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
var profilePic = JSON.parse(document.querySelector("#profile-pic").textContent);
console.log(profilePic)
var postLikes = {
    props: ['postResponse'],

    template: `<div
                class='post-likes'>
                    <div class="post_content">
                        <img :src="pic" class="post_pic">
                        <div class="post_info">
                            <div class="post_name_text">
                                <div class="post_author">{{postResponse.user}}</div>
                                <div class="post_body">{{postResponse.body}}</div>
                            </div>
                            <div class="mood">
                                <div class="mood_caption">Mood:</div>
                                <div class="mood_desc">Sad</div>
                                <img class="mood_icon" src="/media/images/sad_mood.gif" alt="sad_mood">
                            </div>
                        </div>
                    </div>
                    <hr>
                    <div class="post_response">
                        <img class="like_class" src="/media/images/like_icon.png" alt="thumbs_up">
                        <div class="like_numbers">{{counter}}</div>
                    </div>
                </div>`,
    data: function() {
        let counter = 0
        return {
            counter: counter,
            pic: profilePic
        }
    },
    methods: {
        increment: function() {
            this.counter = this.counter + 1
        },
    },
    mounted: function() {
        console.log(this.postResponse)
        console.log('start', this.counter)
        setInterval(() => {this.counter++}, 25)
    },
    // computed: {
    //     reverseCount: function() {
    //         return this.counter.reverse();
    //     }
    // },
}
var app = new Vue({
    el: "#app1",
    components: {
        postLikes
    },
    delimiters: ["d(", ")b"],
    data: {
        postgroups: postgroupEl,
        postSubmit: '',
        hello: 'goodbye',
        post: '',
    },
    methods: {
        submitPost: function(e) {
            console.log(e);
            e.preventDefault();
            axios({
                method: "POST",
                url: submitTo,
                data: {
                    text: this.postSubmit,
                },
                headers: {
                    "X-CSRFToken": csrftoken,
                },
            }).then(
                (response) => {
                    this.postgroups = response.data.postgroup_send;
                    this.postSubmit = '';
                },
            );
        },
    },
    computed: {
        reversePost: function() {
            return this.postgroups.reverse();
        }
    },

})


