
<template>
  <section class="section">
  <div class="container">
    <h1 class="title"> heading </h1>
    <p>
      introduction of this example
    </p>
    <nested-msg>
      {{ msg }}
    </nested-msg>

    <span is="tree" :node="data"></span>
  </div>
  </section>
</template>

<script>


module.exports = {
  components: {
    // 'data-table': httpVueLoader('DataTable.vue'),
  },
  data: function(){
    return {
      msg: 'hello world template',
      data: {
        name:'grand parent',
        age: 70,
        hobby: 'art',
        car: 'toyota',
        children: [
          {
            name: 'parent 1',
            age: 50,
            hobby: 'cooking',
            car: 'merc',
            children: [
              {
                name:'grand child 1',
                age: 22,
                hobby: 'sport',
                car: 'toyota',
              },
              {
                name: 'grand child 2',
                age: 24,
                hobby: 'music',
                car: 'mazda',
                children:[
                  {
                    name: 'grand grand child 2',
                    age: 12,
                    hobby: 'pizza',
                    car: 'none',
                  }
                ],
              }
            ]
          },
          {
            name: 'parent 2',
            age: 50,
            hobby: 'dancing',
            car: 'audi',
            children: [
              {
                name:'grand child 3',
                age: 20,
                hobby: 'photography',
                car: 'nissan'
              },
              {
                name: 'grand child 4',
                age: 18,
                hobby: 'art',
                car: 'ford'
              }
            ]
          },
        ]
      }
    }
  },
  methods:{
    },
}

Vue.component('tree',{
  props: ['node'],
  template:`
    <span>
      <span class="columns is-narrow is-gapless is-0">
        <span class="column is-2">{{ node.name }}</span>
        <span class="column is-2">{{ node.age }}</span>
        <span class="column is-2">{{ node.car }}</span>
        <span class="column is-2">{{ node.hobby }}</span>
      </span>
      <span v-if="isParent">
        <span is="tree" v-for="child in node.children" :node="child">
        </span>
      </span>
    </span>
  `,
  methods:{
    isParent: function(){
      console.log( this.node.name + ': '  + (this.node.children && this.node.children.length))
      return (this.node.children && this.node.children.length)
    }
  }
})

Vue.component('nested-msg',{
  template:`
    <div>
      <strong>Testing</strong></br>
      <slot></slot>
    </div>
  `

})
</script>

<style>
</style>
