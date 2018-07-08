<template>
  <nav class="navbar is-link">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
      </a>
      <div class="navbar-burger" @click="toggleBurger" :class="{ 'is-active': showBurger }">
        <!-- 3 horizontal lines for burger -->
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

    <div class="navbar-menu" :class="{ 'is-active': showBurger }">
      <div class="navbar-start">
        <a class="navbar-item">Home</a>
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More Pages
          </a>
        
          <div class="navbar-dropdown">
          <a class="navbar-item">Page One</a>
          <a class="navbar-item">Page Two</a>
          <hr class="navbar-divider">
          <a class="navbar-item">Admin</a>
          </div>
        </div>
      </div>

      <!-- Right hand side of nav  -->
      <div class="navbar-end">
      </div>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'NavBar',
  data: function () {
    return {
      showBurger: false,
    }
  },
  components: {
  },
  methods:{
    toggleBurger: function() {
      this.showBurger = !this.showBurger
    }
 },
}
</script>

<style>
  .bigred   {
    background-color : red;
  }
</style>
