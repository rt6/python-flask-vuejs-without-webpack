<template>
  <div>
    <NavBar></NavBar>
    <NavBarSecondary></NavBarSecondary>
    <Body></Body>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import NavBarSecondary from './components/NavBarSecondary.vue'
import Body from './components/Body.vue'

export default {
  name: 'app',
  components:{
    NavBar,
    NavBarSecondary,
    Body,
  },
  data: function () {
    return {
    }
  },
  methods:{
 },
}
</script>

<style>
</style>
