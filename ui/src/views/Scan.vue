<template>
  <file-upload :allow-multiple="false" v-on:fileUploaded="handleFileUploaded" />

  <div class="form-check mt-2">
      <input class="form-check-input" type="checkbox" id="addSignatureCheck" v-model="addSignature">
      <label class="form-check-label" for="addSignatureCheck">
          <span>Dodaj pieczątkę</span>
      </label>
  </div>
  <div v-show="addSignature" class="mt-2">
      <file-upload accepted-file-types="image/png" :allow-multiple="false" v-on:fileUploaded="handleSignatureUploaded" />
      <form class="form-inline">
          <div class="form-group">
            <label for="pages">Pieczątka na stronach</label>
            <input v-model="pages" type="text" id="pages" class="form-control mx-sm-3" aria-describedby="passwordHelpInline">
            <small id="pagesHelpInline" class="text-muted">
              Numery stron oddzielone przecinkami, np. 1,3,5
            </small>
          </div>
      </form>
  </div>

  <button v-if="scanInProgress" disabled="disabled" class="btn btn-lg btn-primary mt-4">
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    <span class="ml-1">Pracuję...</span>
  </button>
  <button v-else :disabled="!scanEnabled" class="btn btn-lg btn-primary mt-4" @click="scan">Skanuj</button>
    <div v-if="errors" class="alert alert-danger mt-4" role="alert">
        {{ errorsText }}
    </div>
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
        addSignature: false,
        signaturePath: '',
        pages: '',
        scanEnabled: false,
        scanInProgress: false,
        errors: false,
        errorsText: ''
      }
  },
  methods: {
      handleFileUploaded (filePath) {
          this.scanEnabled = true
          this.filePath = filePath
      },
      handleSignatureUploaded (signaturePath) {
          this.signaturePath = signaturePath
      },
      scan () {
        this.scanInProgress = true
        this.errors = false
        var data = {path: this.filePath}
        if (this.addSignature) {
            data.signature = this.signaturePath
            let pages = this.pages.split(',')
            console.log(pages)
            pages.forEach(p => {
                console.log(parseInt(p))
                if (!parseInt(p)) {
                    this.errors = true
                    this.errorsText = 'Wprowadź poprawną listę stron do dodania pieczątek'
                    this.scanInProgress = false
                }
            })
            if (this.errors) {
                return
            }
            data.pages = pages
        }
        axios.post(`${process.env.VUE_APP_BACKEND_URL}/scan/`, data).then(response => {
            this.scanInProgress = false
            window.open(`${process.env.VUE_APP_BACKEND_URL}/${response.data}`)
        }).catch(() => {
            this.scanInProgress = false
            alert('Wystąpił problem!')
        })
      }
  }
}
</script>