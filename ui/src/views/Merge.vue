<template>
  <file-upload :allow-multiple="true" v-on:fileUploaded="handleFileUploaded"
               v-on:fileRemoved="handleFileRemoved"/>
  <button v-if="mergeInProgress" disabled="disabled" class="btn btn-lg btn-primary">
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    <span class="ml-1 mt-2">Pracuję...</span>
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
                files: [],
                mergeEnabled: false,
                mergeInProgress: false
            }
        },
        methods: {
            handleFileUploaded (filePath, fileId) {
                this.mergeEnabled = true
                this.files.push({path: filePath, id: fileId})
            },
            handleFileRemoved (fileId) {
                console.log(this.files, fileId)
                this.files = this.files.filter(f => f.id !== fileId)
                if (this.files.length === 0)
                    this.mergeEnabled = false
            },
            merge () {
                this.mergeInProgress = true
                var paths = []
                this.files.forEach(f => paths.push(f.path))
                axios.post(`${process.env.VUE_APP_BACKEND_URL}/merge/`, {pdfs: paths}).then(response => {
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