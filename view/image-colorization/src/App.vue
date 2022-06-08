<template>
  <div id="app" class="container" >
    <Navbar/>
    <router-view></router-view>
  </div>
</template>

<script>

import Navbar from "@/components/NavBar";
export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
:root {
  --app-primary-color: #24c8a6;
  --app-secondary-color: #232935;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
