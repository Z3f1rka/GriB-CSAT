<script setup>
</script>

<template>
    <div style="background-color: #01BB72;">
        <header class="box" ref="header_height">
            <div>
                <img class='logo' src="/logo.png" />
            </div>
        </header>
    </div>
</template>
<style scoped>  
header {
  background-color: #01BB72;
  top: 0;
  z-index: 999;
  width: 100%;
  position: sticky;
  padding: 0.4%;
  padding-left: 2%;
}
.logo {
    width: 135px;
    height: 72px;
    
}
</style>