<template>
  <div class="container mt-4">
    <h1 v-if="$route.name != 'Home'">{{ $route.name }}</h1>
    <router-view/>
  </div>
</template>

