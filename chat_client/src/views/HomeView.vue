<script setup lang="ts">
import apiClient from '@/services/apiClient';
import {onMounted} from "vue";


function getData() {
  apiClient.get('/account/whoami')
    .then((res) => {
      console.log(res.data);  // Log the response from whoami
    })
    .catch((error) => {
      console.error('Failed to fetch whoami:', error);
    });
}

onMounted(()=>{
    getData();
})
</script>

<template>
  <main>
    asdasdasd
  </main>
</template>
