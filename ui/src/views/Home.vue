<template>
  <div class="row">
    <div class="col-sm-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Skan</h5>
          <p class="card-text"></p>
          <router-link class="btn btn-primary" to="scan">Przejdź</router-link>
        </div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Łączenie plików PDF</h5>
          <p class="card-text"></p>
          <router-link class="btn btn-primary" to="merge">Przejdź</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
