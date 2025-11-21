<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js';
import { useI18n } from '../composables/useI18n';

const { t } = useI18n();

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

const shifts = ref([]);
const people = ref([]);
const stats = ref([]);

// Form state
const form = ref({
  date: '',
  shift_type: 'Day',
  person_id: '',
});

const fetchShifts = async () => {
  const res = await axios.get('http://localhost:8000/shifts/');
  shifts.value = res.data;
};

const fetchPeople = async () => {
  const res = await axios.get('http://localhost:8000/personnel/');
  people.value = res.data;
};

const fetchStats = async () => {
  const res = await axios.get('http://localhost:8000/statistics/');
  stats.value = res.data;
};

const addShift = async () => {
  if (!form.value.date || !form.value.person_id) return;

  await axios.post('http://localhost:8000/shifts/', form.value);
  // Reset form but keep date for convenience? Or reset all. Let's reset.
  // form.value = { date: '', shift_type: 'Day', person_id: '' }
  // Actually, keeping the date might be nice for adding multiple shifts. Let's just clear person.
  form.value.person_id = '';

  fetchShifts();
  fetchStats();
};

const deleteShift = async (id) => {
  await axios.delete(`http://localhost:8000/shifts/${id}`);
  fetchShifts();
  fetchStats();
};

onMounted(() => {
  fetchShifts();
  fetchPeople();
  fetchStats();
});

const chartData = computed(() => ({
  labels: stats.value.map((s) => s.name),
  datasets: [
    {
      label: t('roster.shiftsAssigned'),
      data: stats.value.map((s) => s.count),
      backgroundColor: '#6366f1',
    },
  ],
}));

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
  },
  scales: {
    y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' } },
    x: { grid: { display: false } },
  },
};
</script>

<template>
  <div>
    <div style="margin-bottom: 2rem">
      <h2>{{ t('roster.title') }}</h2>
    </div>

    <div class="grid">
      <!-- Manual Scheduling Form -->
      <div class="glass-panel">
        <h3>{{ t('roster.addShiftTitle') }}</h3>
        <form @submit.prevent="addShift">
          <div style="margin-bottom: 1rem">
            <label
              style="
                display: block;
                margin-bottom: 0.5rem;
                color: var(--text-muted);
              "
              >{{ t('roster.dateLabel') }}</label
            >
            <input v-model="form.date" type="date" required />
          </div>

          <div style="margin-bottom: 1rem">
            <label
              style="
                display: block;
                margin-bottom: 0.5rem;
                color: var(--text-muted);
              "
              >{{ t('roster.shiftTypeLabel') }}</label
            >
            <select v-model="form.shift_type" required>
              <option value="Day">{{ t('roster.dayShift') }}</option>
              <option value="Night">{{ t('roster.nightShift') }}</option>
            </select>
          </div>

          <div style="margin-bottom: 1rem">
            <label
              style="
                display: block;
                margin-bottom: 0.5rem;
                color: var(--text-muted);
              "
              >{{ t('roster.personnelLabel') }}</label
            >
            <select v-model="form.person_id" required>
              <option value="" disabled>{{ t('roster.selectPerson') }}</option>
              <option
                v-for="person in people"
                :key="person.id"
                :value="person.id"
              >
                {{ person.name }} ({{ person.position }})
              </option>
            </select>
          </div>

          <button type="submit" class="btn" style="width: 100%">
            {{ t('roster.assignButton') }}
          </button>
        </form>
      </div>

      <!-- Shift List -->
      <div class="glass-panel">
        <h3>{{ t('roster.scheduledShiftsTitle') }}</h3>
        <div style="max-height: 400px; overflow-y: auto">
          <table v-if="shifts.length > 0">
            <thead>
              <tr>
                <th>{{ t('roster.tableHeaders.date') }}</th>
                <th>{{ t('roster.tableHeaders.shift') }}</th>
                <th>{{ t('roster.tableHeaders.person') }}</th>
                <th>{{ t('roster.tableHeaders.action') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="shift in shifts" :key="shift.id">
                <td>{{ shift.date }}</td>
                <td>
                  <span
                    :style="{
                      color: shift.shift_type === 'Day' ? '#fbbf24' : '#818cf8',
                      fontWeight: 'bold',
                    }"
                  >
                    {{ shift.shift_type }}
                  </span>
                </td>
                <td>{{ shift.person_name }}</td>
                <td>
                  <button
                    @click="deleteShift(shift.id)"
                    class="btn btn-danger"
                    style="padding: 0.25rem 0.75rem; font-size: 0.875rem"
                  >
                    &times;
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <p
            v-else
            style="color: var(--text-muted); text-align: center; padding: 2rem"
          >
            {{ t('roster.noShifts') }}
          </p>
        </div>
      </div>

      <!-- Stats -->
      <div class="glass-panel" style="grid-column: 1 / -1">
        <h3>{{ t('roster.statsTitle') }}</h3>
        <div style="height: 300px">
          <Bar
            v-if="stats.length > 0"
            :data="chartData"
            :options="chartOptions"
          />
          <p v-else style="text-align: center; padding: 2rem">
            {{ t('roster.noData') }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
