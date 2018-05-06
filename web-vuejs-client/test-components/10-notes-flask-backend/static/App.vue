

<template>
  <div>
  <section class="hero is-info">
    <div class="hero-body">
      <div class="container">
	<h1 class="title">
	Notes
	</h1>
	<h2 class="subtitle">
        A simple notes app using Vue Js with Flask REST API backend
	</h2>
      </div>
    </div>
  </section>

  <section class="section">
  <div class="content">
      <h3 class="title is-3">Your Notes</h3>
      <p>
        <ul>
          <li v-for="(note,index) in notes">
            {{ note.id  }} {{ note.text  }}
          </li>
        </ul>
      </p>
    </div>
    <div class="container">

      <h3 class="title is-3">New Note</h3>
      <div>
	<input class="input is-info" type="text" v-model="new_note"><br><br>
	<button class="button is-success" @click="saveNewNote()">save</button>
      </div>
      
    </div>
  </section>
  </div>
</template>

<script>


module.exports = {
  components: {
    // 'data-table': httpVueLoader('DataTable.vue'),
  },
  data: function(){
    return {
      msg: 'hello world template',
      api_host: 'http://localhost:5000',
      notes:[],
      new_note:'type new note'
    }

  },
  methods:{
    getData() {
      fetch(this.api_host + '/notes')
        .then( r => r.json() )
        .then( d => this.notes = d.data )
    },
    saveNewNote(){
      fetch(this.api_host + '/notes',
        {
          method:'POST', 
          body: JSON.stringify({'text':this.new_note})
        })
        .then(r=>r.json())
        .then(d=> this.notes = d.data)
    }
  },
  mounted(){
    console.log(this.api_host)
    this.getData()
  }
}


Vue.component('nested-msg',{
  template:`
    <div>
      <strong>Testing</strong></br>
      <slot></slot>
    </div>
  `

})

</script>
