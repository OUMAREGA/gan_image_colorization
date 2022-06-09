<template>
  <div class="small">
    <!--<div>
      <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
    </div>-->


    <div>
      <input class="form-control form-control-lg" ref="file" type="file" id="file" @input="selectImgFile">
    </div>

    <div class="mt-5" />

    <div v-if="filePreview && !ganImage">
      <h3>Previem uploaded image</h3>
      <div class="previewBlock" @click="chooseFile" :style="{ 'background-image': `url(${filePreview})` }" />
    </div>

    <div v-if="ganImage" >
      <h3>GAN result</h3>
      <b-container class="bv-example-row">
        <b-row>
          <b-col>1 of 3</b-col>
          <b-col>2 of 3</b-col>
        </b-row>
      </b-container>
    </div>

    <button @click="predict" class="btn mt-3 btn-dark">Go</button>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  components: {
  },
  data () {
    return {
      datacollection: null,
      file: null,
      ganImage: false,
      filePreview: null
    }
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    predict() {
      let formData = new FormData();
      formData.append('file', this.file);
      const headers = {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Content-Type': 'multipart/form-data'
      }

      axios.post('http://127.0.0.1:5000/api/v1/predict', formData, {headers})
      .then((response) => {
        console.log(response)
        this.predict_class = response.data.class
      }).catch(e => {
           console.log(e)
      })
    },

    chooseFile () {
      this.$refs.fileInput.click()
    },
    selectImgFile () {
      this.file = this.$refs.file.files[0];

      if (this.file) {
        let reader = new FileReader
        reader.onload = e => {
          this.filePreview = e.target.result
        }
        reader.readAsDataURL(this.file)
      }
    }
  },
}
</script>

<style>
.small {
  max-width: 600px;
  margin:  150px auto;
}
.container {
  max-width: 600px;
}
.previewBlock {
  display: block;
  cursor: pointer;
  width: 300px;
  height: 280px;
  margin: 0 auto 20px;
  background-position: center center;
  background-size: cover;
}

</style>