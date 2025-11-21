<script setup>
import { useI18n } from '../composables/useI18n';

const { t } = useI18n();
</script>

<template>
  <div class="home-container">
    <div class="hero glass-panel">
      <h1>{{ t('home.title') }}</h1>
      <p>{{ t('home.subtitle') }}</p>
      <div class="actions">
        <router-link to="/personnel" class="btn">{{
          t('home.managePersonnel')
        }}</router-link>
        <router-link to="/roster" class="btn">{{
          t('home.viewRoster')
        }}</router-link>
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
