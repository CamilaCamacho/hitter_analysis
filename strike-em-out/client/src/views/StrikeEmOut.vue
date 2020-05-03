<template>
  <div class="container">
    <h1>This is the Strike Em Out page</h1>
    <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'StrikeEmOut',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/strikeemout';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>

</style>
