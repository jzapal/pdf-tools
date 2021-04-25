<template>
  <div class="container mt-4">
    <router-link v-if="$route.name != 'Home'" to="/">&lt;&lt;</router-link>
    <h1 v-if="$route.name != 'Home'">{{ $route.name }}</h1>
    <router-view/>
  </div>
</template>
<style>
  @import './assets/bootstrap.min.css';
  .spinner-border {
    position: relative;
    top: -3px;
  }
</style>