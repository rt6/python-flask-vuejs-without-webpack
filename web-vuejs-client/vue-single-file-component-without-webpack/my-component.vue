<template>
    <div class="hello"><h1>Hello {{who}}</h1></div>
</template>

<script>
module.exports = {
    data: function() {
        return {
            who: 'world to all'
        }
    }
}
</script>

<style>
.hello {
    background-color: #74b9ff;
}
</style>
