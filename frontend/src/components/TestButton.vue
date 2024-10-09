<script setup>
import { ref } from "vue";
import axios from "axios";

function request() {
  const access_token = localStorage.getItem("access_token");
  const refresh_token = localStorage.getItem("refresh_token");
  var err = "";
  var resp_data;
  const data = axios.get("http://127.0.0.1:8080" + "/api/products", {
    headers: { authorization: `${access_token}` },
  });
  console.log(data);
  data.then((response) => {;
    resp_data = response.data;
    console.log(resp_data);
  });
  data.catch((err) => {
    console.log(err);
    const values = {
      refresh_token: refresh_token,
    };
    console.log(values);
    axios
      .post("http://127.0.0.1:8080" + "/api/auth/refresh", values)
      .then((response) => {
        err.value = response.data.error;
        if (err.value) {
          console.log(err.value);
        } else {
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          console.log("pivo");
        }
      });
  });
}
</script>
<template>
  <button @click="request" class="w-20 h-20 bg-main"></button>
</template>
