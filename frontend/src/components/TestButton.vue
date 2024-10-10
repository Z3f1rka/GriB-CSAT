<script setup>
import { ref } from "vue";
import axios from "axios";
import { auth_get, auth_post } from "../requests.js";

function request() {
  var err = "";
  var resp_data = auth_post("/api/products", { a: "AAAAAAAAAA" });
}
</script>
<template>
  <button @click="request" class="w-20 h-20 bg-main"></button>
</template>
