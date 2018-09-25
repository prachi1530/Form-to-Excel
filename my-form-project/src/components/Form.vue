<template>
  <el-form ref="form" :model="form" label-width="120px">
    <el-form-item label="Email">
      <el-input v-model="form.email"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <router-link to="/Formuser"></router-link>
      <router-link to="/Nonuser"></router-link>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios'
import router from '../router'
export default {
  data () {
    return {
      form: {
      }
    }
  },
  methods: {
    onSubmit () {
      this.callBackend()
      this.form = {}
    },
    callBackend () {
      axios({
        method: 'post',
        url: 'http://localhost:777',
        data: JSON.stringify(this.form)
      })
        .then(function (response) {
          if (response.data.toString() === '1') {
            router.push({name: 'Nonuser'})
          } else if (response.data.toString() === '0') {
            router.push({name: 'Formuser'})
          }
        })
        .catch(function (response) {
          console.log(response)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
