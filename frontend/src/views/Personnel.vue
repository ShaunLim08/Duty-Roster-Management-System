<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useI18n } from '../composables/useI18n';

const { t } = useI18n();

const people = ref([]);
const form = ref({ name: '', age: '', position: '' });

const fetchPeople = async () => {
  const res = await axios.get('http://localhost:8000/personnel/');
  people.value = res.data;
};

const addPerson = async () => {
  await axios.post('http://localhost:8000/personnel/', form.value);
  form.value = { name: '', age: '', position: '' };
  fetchPeople();
};

const deletePerson = async (id) => {
  await axios.delete(`http://localhost:8000/personnel/${id}`);
  fetchPeople();
};

onMounted(fetchPeople);
</script>

<template>
  <div class="grid">
    <div class="glass-panel">
      <h2>{{ t('personnel.addTitle') }}</h2>
      <form @submit.prevent="addPerson">
        <input
          v-model="form.name"
          :placeholder="t('personnel.namePlaceholder')"
          required
        />
        <input
          v-model="form.age"
          type="number"
          :placeholder="t('personnel.agePlaceholder')"
          required
        />
        <input
          v-model="form.position"
          :placeholder="t('personnel.positionPlaceholder')"
          required
        />
        <button type="submit" class="btn">
          {{ t('personnel.addButton') }}
        </button>
      </form>
    </div>

    <div class="glass-panel">
      <h2>{{ t('personnel.listTitle') }}</h2>
      <table>
        <thead>
          <tr>
            <th>{{ t('personnel.tableHeaders.name') }}</th>
            <th>{{ t('personnel.tableHeaders.age') }}</th>
            <th>{{ t('personnel.tableHeaders.position') }}</th>
            <th>{{ t('personnel.tableHeaders.action') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="person in people" :key="person.id">
            <td>{{ person.name }}</td>
            <td>{{ person.age }}</td>
            <td>{{ person.position }}</td>
            <td>
              <button
                @click="deletePerson(person.id)"
                class="btn btn-danger"
                style="padding: 0.5rem"
              >
                {{ t('personnel.deleteButton') }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
