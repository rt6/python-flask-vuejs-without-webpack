var vm = new Vue({
    el: 'app',
    components: {
      'App': httpVueLoader('/static/App.vue'),
    }
})
