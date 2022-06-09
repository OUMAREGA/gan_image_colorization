<template>
  <section class="mb-5">
    <nav class="navbar container shadow-lg navbar-expand-lg navbar-dark text-left fixed-top bg-dark">
      <div class="container-fluid text-white ">
        <a class="navbar-brand" to="/">4M</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse " id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link mr-lg-5 mr-md-5" :to="{name: 'gan'}">
                Generative Adversarial Networks
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </section>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.router-link-active{
  color: var(--app-primary-color) !important;
}
</style>
