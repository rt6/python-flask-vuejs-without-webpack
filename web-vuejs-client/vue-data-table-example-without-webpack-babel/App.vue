

<template>
<div>
  <data-table></data-table>
</div>
</template>

<script>
const getters = {
  getMessage(state) {
    return (state.message).toUpperCase();
  },
  getCounter(state) {
    return state.counter;
  },
  getData(state){
    return state.data
  },
  getTableName(state){
    return state.table_name;
  }
}

const mutations = {
  changeMessage(state, msg) {
    console.log('changeMessage:' + msg)
    state.message = msg;
  },
  incrementCounter(state){
    state.counter++;
  }
}

const actions ={
    changeMessage(store,msg){
      store.commit('changeMessage', msg)
  },
    incrementCounter(store){
      store.commit('incrementCounter')
  },
    handleMessageChange(store,msg){
      store.commit('changeMessage', msg)
      store.commit('incrementCounter')
  },
}

// initial state
const state = {
  table_name: 'Hello Vue!',
  counter: 0,
  data: {
    'series 1': [1,2,3,4,5],
    'series 2': [1,2,3,4,5],
  }
}


store = new Vuex.Store({
  state: state,
  mutations: mutations,
  actions: actions,
  getters: getters
});

module.exports = {
  components: {
    'data-table': httpVueLoader('DataTable.vue'),
  },
  'store': store
}
</script>
