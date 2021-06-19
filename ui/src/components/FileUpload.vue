<template>
    <div>
        <file-pond
                url="http://localhost:8000"
                name="file"
                ref="pond"
                label-idle="Upuść plik tutaj..."
                :allow-multiple="allowMultiple"
                :accepted-file-types="acceptedFileTypes"
                :server=server
                v-bind:files="myFiles"
                v-on:init="handleFilePondInit"
                v-on:processfile="handleFileProcessed"
                v-on:removefile="handleFileRemoved"
        />
    </div>
</template>

<script>
    // Import Vue FilePond
    import vueFilePond from "vue-filepond";

    // Import FilePond styles
    import "filepond/dist/filepond.min.css";

    // Import FilePond plugins
    // Please note that you need to install these plugins separately

    // Import image preview plugin styles
    import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";

    // Import image preview and file type validation plugins
    import FilePondPluginFileValidateType from "filepond-plugin-file-validate-type";
    import FilePondPluginImagePreview from "filepond-plugin-image-preview";

    // Create component
    const FilePond = vueFilePond(
        FilePondPluginFileValidateType,
        FilePondPluginImagePreview
    );

    export default {
        name: "FileUpload",
        props: {
          endpoint: {
            type: String,
            required: true
          },
          allowMultiple: {
            type: Boolean,
            required: true
          },
          acceptedFileTypes: {
             type: String,
             default: "application/pdf"
          }
        },
        data: function () {
            return {
              myFiles: []
            };
        },
        computed: {
          server() {
              return `${process.env.VUE_APP_BACKEND_URL}/upload/`
          }
        },
        methods: {
            handleFilePondInit: function () {
                console.log("FilePond has initialized");

                // FilePond instance methods are available on `this.$refs.pond`
            },
            handleFileProcessed: function(e, t) {
                this.$emit('fileUploaded', t.serverId.substr(1, t.serverId.length - 2), t.id);
            },
            handleFileRemoved: function(e, t) {
                this.$emit('fileRemoved', t.id);
            }
        },
        components: {
            FilePond,
        },
    };
</script>