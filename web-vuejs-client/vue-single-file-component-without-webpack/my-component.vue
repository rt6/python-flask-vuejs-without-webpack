<template>
    <div class="hello"><h1>Hello {{who}}</h1>
    <component1></component1>
    </div>
</template>

<script>
module.exports = {
    components:{
      'component1': httpVueLoader('component1.vue')
    },
    data: function() {
        return {
            who: 'Michael'
        }
    }
}
</script>

<style>
.hello {
    background-color: #74b9ff;
}
</style>
