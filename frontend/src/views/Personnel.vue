<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const people = ref([])
const form = ref({ name: '', age: '', position: '' })

const fetchPeople = async () => {
  const res = await axios.get('http://localhost:8000/personnel/')
  people.value = res.data
}

const addPerson = async () => {
  await axios.post('http://localhost:8000/personnel/', form.value)
  form.value = { name: '', age: '', position: '' }
  fetchPeople()
}

const deletePerson = async (id) => {
  await axios.delete(`http://localhost:8000/personnel/${id}`)
  fetchPeople()
}

onMounted(fetchPeople)
</script>

<template>
  <div class="grid">
    <div class="glass-panel">
      <h2>Add Personnel</h2>
      <form @submit.prevent="addPerson">
        <input v-model="form.name" placeholder="Name" required />
        <input v-model="form.age" type="number" placeholder="Age" required />
        <input v-model="form.position" placeholder="Position" required />
        <button type="submit" class="btn">Add Person</button>
      </form>
    </div>

    <div class="glass-panel">
      <h2>Personnel List</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Position</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="person in people" :key="person.id">
            <td>{{ person.name }}</td>
            <td>{{ person.age }}</td>
            <td>{{ person.position }}</td>
            <td>
              <button @click="deletePerson(person.id)" class="btn btn-danger" style="padding: 0.5rem;">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
