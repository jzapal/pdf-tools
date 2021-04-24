<template>
  <file-upload :allow-multiple="false" v-on:fileUploaded="handleFileUploaded" />
  <button v-if="scanInProgress" disabled="disabled" class="btn btn-lg btn-primary">Pracuję...</button>
  <button v-else :disabled="!scanEnabled" class="btn btn-lg btn-primary" @click="scan">Skanuj</button>
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
        scanEnabled: false,
        scanInProgress: false
      }
  },
  methods: {
      handleFileUploaded (filePath) {
          this.scanEnabled = true
          this.filePath = filePath
      },
      scan () {
        this.scanInProgress = true
        axios.post(`${process.env.VUE_APP_BACKEND_URL}/scan/`, {path: this.filePath}).then(response => {
            this.scanInProgress = false
            window.open(`${process.env.VUE_APP_BACKEND_URL}/${response.data}`)
        }).catch(error => {
            this.scanInProgress = false
            alert('Wystąpił problem!')
        })
      }
  }
}
</script>