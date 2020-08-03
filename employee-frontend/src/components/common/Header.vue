<template>
  <div class="hero is-info header-container">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">{{ title }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Header',
    props: {
      title: String
    }
  }
</script>

<style scoped>
.header-container {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
