<template>
  <nav class="navbar " style="background-color:#74b9ff">
    <div class="navbar-brand">
        <a class="navbar-item" style="width:135px;font-color:#fff">&nbsp;</a>
    </div>
    <div class="navbar-brand">
        <a class="navbar-item">Admin</a>
    </div>

    <div class="navbar-menu" :class="{ 'is-active': showBurger }">
      <div class="navbar-start">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Users
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
  name: 'NavBarSecondary',
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
