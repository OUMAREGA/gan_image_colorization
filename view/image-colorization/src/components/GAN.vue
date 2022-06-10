<template>
  <div class="small">
    <div>
      <input class="form-control form-control-lg" ref="file" type="file" id="file" @input="selectImgFile">
    </div>

    <div class="mt-5" />

    <div data-aos="zoom-in" data-aos-duration="1500" v-if="filePreview && !ganImage">
      <h3>Preview uploaded image</h3>
      <div class="previewBlock" @click="chooseFile" :style="{ 'background-image': `url(${filePreview})` }" />
    </div>

    <div v-if="ganImage" >
      <h3>GAN result</h3>
      <b-container class="bv-example-row">
        <b-row>
          <b-col data-as="fade-right">
            <div class="previewBlock" @click="chooseFile" :style="{ 'background-image': `url(${filePreview})` }" />
          </b-col>
          <b-col data-aos="fade-left">
            <img class="previewBlock" :src="ganImage" />
          </b-col>
        </b-row>
      </b-container>
    </div>

    <button v-if="disabled" :disabled="disabled" class="btn mt-3 btn-dark">Go</button>
    <button v-else-if="!disabled && !loading" @click="savePredict" class="btn mt-3 btn-dark">Go</button>
    <!--<button v-if="ganImage" @click="eraseCache" class="btn mt-3 btn-dark">Again</button>-->

    <b-spinner v-if="loading" label="Loading..."></b-spinner>


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
      filePreview: null,
      loading: false
    }
  },
  computed: {
    disabled() {
      return this.filePreview ? false : true
    }
  },
  methods: {
    async savePredict() {
      this.loading = true;
      let formData = new FormData();
      formData.append('file', this.file);
      const headers = {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Content-Type': 'multipart/form-data',
        'responseType': 'blob'
      }
      await axios.post('http://127.0.0.1:5000/api/v1/save_predict', formData, {headers})
      .then(async () => {
        await this.getImage()
        this.loading = false
      }).catch(e => {
           console.log(e)
      })
    },
    eraseCache() {
      //window.history.forward(1);
      //location.reload(true);
      this.filePreview = null
      this.ganImage = false
      this.$refs.file.value = null
    },

    chooseFile () {
      this.$refs.file.click()
    },
    selectImgFile () {
      this.file = this.$refs.file.files[0];
      this.ganImage = false

      if (this.file) {
        let reader = new FileReader
        reader.onload = e => {
          this.filePreview = e.target.result
        }
        reader.readAsDataURL(this.file)
      }

    },
    getImage() {
      axios.get('http://127.0.0.1:5000/api/v1/predict', {
        responseType: 'blob'
      })
      .then((response) => {
        this.ganImage = null
        this.ganImage = window.URL.createObjectURL(response.data);
        this.$refs.file.value = null
      }).catch(e => {
           console.log(e)
      })
    },

  },
}
</script>

<style>
.small {
  max-width: 600px;
  margin:  150px auto;
}

.previewBlock {
  display: block;
  cursor: pointer;
  width: 100%;
  height: 280px;
  margin: 0 auto 20px;
  background-position: center center;
  background-size: cover;
}

</style>