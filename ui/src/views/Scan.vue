<template>
  <file-upload :allow-multiple="false" v-on:fileUploaded="handleFileUploaded" />
  <button :disabled="!scanEnabled" class="btn btn-lg btn-primary" @click="scan">Skanuj</button>
</template>
<script>
import FileUpload from "../components/FileUpload";
import axios from 'axios'

export default {
  name: 'Scan',
  components: {FileUpload},
  data () {
      return {
        filePath: '',
        scanEnabled: false
      }
  },
  methods: {
      handleFileUploaded (filePath) {
          this.scanEnabled = true
          this.filePath = filePath
      },
      scan () {
        axios.post(`${process.env.VUE_APP_BACKEND_URL}/scan/`, {path: this.filePath}).then(response => {
            window.open(`${process.env.VUE_APP_BACKEND_URL}/${response.data}`)
        })
      }
  }
}
</script>