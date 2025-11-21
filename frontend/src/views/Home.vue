<script setup>
</script>

<template>
  <div class="home-container">
    <div class="hero glass-panel">
      <h1>Duty Roster Management System</h1>
      <p>Manage personnel, schedule shifts, and view statistics efficiently.</p>
      <div class="actions">
        <router-link to="/personnel" class="btn">Manage Personnel</router-link>
        <router-link to="/roster" class="btn">View Roster</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
  text-align: center;
}

.hero {
  max-width: 600px;
}

.actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}
</style>
