<template>
<div>
  <my-component></my-component>
</div>
</template>

<script type="text/javascript">
module.exports = {
  components: {
    'my-component': httpVueLoader('my-component.vue')
  }
}
</script>
