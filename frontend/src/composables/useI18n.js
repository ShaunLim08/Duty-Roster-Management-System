import { ref, computed } from 'vue';

const currentLanguage = ref(localStorage.getItem('language') || 'en');

const translations = {
  en: {
    // Navigation
    nav: {
      home: 'Home',
      personnel: 'Personnel',
      roster: 'Roster & Stats',
    },
    // Home page
    home: {
      title: 'Duty Roster Management System',
      subtitle:
        'Manage personnel, schedule shifts, and view statistics efficiently.',
      managePersonnel: 'Manage Personnel',
      viewRoster: 'View Roster',
    },
    // Personnel page
    personnel: {
      addTitle: 'Add Personnel',
      listTitle: 'Personnel List',
      namePlaceholder: 'Name',
      agePlaceholder: 'Age',
      positionPlaceholder: 'Position',
      addButton: 'Add Person',
      deleteButton: 'Delete',
      tableHeaders: {
        name: 'Name',
        age: 'Age',
        position: 'Position',
        action: 'Action',
      },
    },
    // Roster page
    roster: {
      title: 'Manage Roster',
      addShiftTitle: 'Add Shift',
      scheduledShiftsTitle: 'Scheduled Shifts',
      statsTitle: 'Workload Statistics',
      dateLabel: 'Date',
      shiftTypeLabel: 'Shift Type',
      personnelLabel: 'Personnel',
      dayShift: 'Day Shift',
      nightShift: 'Night Shift',
      selectPerson: 'Select Person',
      assignButton: 'Assign Shift',
      noShifts: 'No shifts scheduled yet.',
      noData: 'No data available.',
      shiftsAssigned: 'Shifts Assigned',
      tableHeaders: {
        date: 'Date',
        shift: 'Shift',
        person: 'Person',
        action: 'Action',
      },
    },
  },
  zh: {
    // Navigation
    nav: {
      home: '首页',
      personnel: '人员管理',
      roster: '排班与统计',
    },
    // Home page
    home: {
      title: '值班排班管理系统',
      subtitle: '高效管理人员、安排班次和查看统计数据。',
      managePersonnel: '管理人员',
      viewRoster: '查看排班',
    },
    // Personnel page
    personnel: {
      addTitle: '添加人员',
      listTitle: '人员列表',
      namePlaceholder: '姓名',
      agePlaceholder: '年龄',
      positionPlaceholder: '职位',
      addButton: '添加人员',
      deleteButton: '删除',
      tableHeaders: {
        name: '姓名',
        age: '年龄',
        position: '职位',
        action: '操作',
      },
    },
    // Roster page
    roster: {
      title: '管理排班',
      addShiftTitle: '添加班次',
      scheduledShiftsTitle: '已排班次',
      statsTitle: '工作量统计',
      dateLabel: '日期',
      shiftTypeLabel: '班次类型',
      personnelLabel: '人员',
      dayShift: '白班',
      nightShift: '夜班',
      selectPerson: '选择人员',
      assignButton: '分配班次',
      noShifts: '暂无排班。',
      noData: '暂无数据。',
      shiftsAssigned: '分配班次',
      tableHeaders: {
        date: '日期',
        shift: '班次',
        person: '人员',
        action: '操作',
      },
    },
  },
};

export function useI18n() {
  const setLanguage = (lang) => {
    currentLanguage.value = lang;
    localStorage.setItem('language', lang);
  };

  const t = (key) => {
    const keys = key.split('.');
    let value = translations[currentLanguage.value];

    for (const k of keys) {
      if (value && value[k]) {
        value = value[k];
      } else {
        return key; // Fallback to key if translation not found
      }
    }

    return value;
  };

  const locale = computed(() => currentLanguage.value);

  return {
    t,
    locale,
    setLanguage,
  };
}
