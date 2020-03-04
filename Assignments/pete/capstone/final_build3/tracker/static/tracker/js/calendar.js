var dateTime = JSON.parse(document.querySelector('#date_time').textContent);
var monthStart = JSON.parse(document.querySelector('#month_start').textContent);
var monthLength = JSON.parse(document.querySelector('#month_length').textContent);
var loggedDays = JSON.parse(document.querySelector('#logged_days').textContent);

if (monthStart===6) {
    var dayCounter = 0
} else {
    var dayCounter = monthStart + 1;
}

// let dayArr = document.querySelectorAll('.day');

// for (let i=0; i<monthLength; i++) {
//     dayArr[dayCounter].innerText = i+1;
//     for (let j=0; j<loggedDays.length; j++) {
//         if (dayArr[dayCounter].innerText == parseInt(loggedDays[j].day)) {
//             dayArr[dayCounter].style.color = 'red';
//             console.log('red')
//         }
//     }
//     dayCounter ++;
// }

// let changeCal = false
// function al() {
//     if (changeCal) {
//         for (let i=0; i<7;i++) {
//             dayArr.slice(dayArr.length-7)[i].style.display = changeCal?'none':'block';
//             document.querySelector("#calendar-container").style.gridTemplate = `7% repeat(${rows}, 1fr) / repeat(7, 1fr)`
//         }
//     }
// }
var monthDay = {
    props: ['day', 'loggedDays',],
    template: `<a :href="href"><div class="day">
            <div class="upper-day">{{ day }}</div>
            <div class="lower-day">{{ trainOrRest }}</div>
        </div></a>`,
    computed: {
        trainOrRest: function() {
            for (let i=0; i<loggedDays.length; i++) {
                if (loggedDays[i].day == this.day) {
                    console.log(this.day);
                    if (loggedDays[i].train) {
                        return 'Training Day'
                    } else {
                        return 'Rest Day'
                    }
                }
            }
        },
        paddedDay: function() {
            return String(this.day).padStart(2, '0');
        },
        dateString: function() {
            return `${loggedDays[0].year}-${loggedDays[0].month}-${this.paddedDay}`
        },
        href: function() {
            return `{% url 'tracker:day2' date=${this.dateString} %}`
        }
    },
}

var app = new Vue({
    el: '#app',
    data: {
        monthStart,
        monthLength,
        loggedDays,
        // monthDays: [],
    },
    components: {
        monthDay,
    },
    computed: {
        monthDays: function() {
            monthDaysArr = []
            for (let i=0; i<monthLength; i++) {
                monthDaysArr.push(i+1);
            }
            return monthDaysArr
        }
    }
})