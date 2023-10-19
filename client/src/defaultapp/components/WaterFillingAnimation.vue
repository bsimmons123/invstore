<template>
  <div class="water-container">
    <div class="water"></div>
  </div>
</template>

<script>
export default {
  name: 'WaterFillingAnimation',
};
</script>

<style>
.water-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.water {
  width: 200px;
  height: 200px;
  border: 2px solid wheat;
  border-radius: 50%;
  background-size: 400px 200px;
  background: url("@/assets/water.png") repeat-x;
  transition: opacity 0.3s ease-in-out;
  animation: flow .5s linear infinite;
}

@keyframes flow {
  0% {
    background-position: -1200px 200px;
  }
  100% {
    background-position: 0 0;
  }
}
</style>
