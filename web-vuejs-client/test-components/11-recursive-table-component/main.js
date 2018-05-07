var vm = new Vue({
    el: 'app',
    components: {
        'App': httpVueLoader('App.vue'),
    }
})
