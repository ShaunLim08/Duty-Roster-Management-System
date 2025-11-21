<script setup>
import { useI18n } from './composables/useI18n';

const { t, locale, setLanguage } = useI18n();

const toggleLanguage = () => {
  setLanguage(locale.value === 'en' ? 'zh' : 'en');
};
</script>

<template>
  <div>
    <nav class="nav">
      <div class="nav-links">
        <router-link to="/">{{ t('nav.home') }}</router-link>
        <router-link to="/personnel">{{ t('nav.personnel') }}</router-link>
        <router-link to="/roster">{{ t('nav.roster') }}</router-link>
      </div>
      <button @click="toggleLanguage" class="language-toggle">
        {{ locale === 'en' ? '中文' : 'English' }}
      </button>
    </nav>
    <router-view></router-view>
  </div>
</template>

<style>
/* Global styles are imported in main.js via style.css */

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.language-toggle {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: var(--text);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.language-toggle:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}
</style>
