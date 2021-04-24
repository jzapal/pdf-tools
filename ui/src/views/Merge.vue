<template>
  <file-upload :allow-multiple="true" v-on:fileUploaded="handleFileUploaded" />
  <button v-if="mergeInProgress" disabled="disabled" class="btn btn-lg btn-primary">
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    <span class="ml-1">Pracuję...</span>
  </button>
  <button v-else :disabled="!mergeEnabled" class="btn btn-lg btn-primary" @click="merge">Połącz</button>
</template>
<script>
    import FileUpload from "../components/FileUpload";
    import axios from 'axios'

    export default {
        name: 'merge',
        components: {FileUpload},
        data () {
            return {
                filePath: '',
                mergeEnabled: false,
                mergeInProgress: false
            }
        },
        methods: {
            handleFileUploaded (filePath) {
                this.mergeEnabled = true
                this.filePath = filePath
            },
            merge () {
                this.mergeInProgress = true
                axios.post(`${process.env.VUE_APP_BACKEND_URL}/merge/`, {path: this.filePath}).then(response => {
                    this.mergeInProgress = false
                    window.open(`${process.env.VUE_APP_BACKEND_URL}/${response.data}`)
                }).catch(() => {
                    this.mergeInProgress = false
                    alert('Wystąpił problem!')
                })
            }
        }
    }
</script>