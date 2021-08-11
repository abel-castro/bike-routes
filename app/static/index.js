new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],

    data () {
        return {
          routes: null
        }
    },
    mounted () {
        axios.get('/api/routes/').then(response => (this.routes = response.data))
    }
})