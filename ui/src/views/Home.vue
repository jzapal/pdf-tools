<template>
  <div class="row">
    <div class="col-sm-6">
      <div class="card">
        <div class="card-body">
          <h4 class="card-title">Skan</h4>
          <p class="card-text">Modyfikuje plik PDF by wyglądał jak zeskanowany</p>
          <router-link class="btn btn-primary" to="scan">Przejdź</router-link>
        </div>
      </div>
    </div>
    <div class="col-sm-6 mt-4 mt-md-0">
      <div class="card">
        <div class="card-body">
          <h4 class="card-title">Łączenie plików PDF</h4>
          <p class="card-text">Łączy kilka plików PDF w jeden</p>
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
