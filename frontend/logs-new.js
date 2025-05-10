// Delete functionality
document.addEventListener('DOMContentLoaded', function() {
  // Variables
  let logsData = [];
  let selectedLogs = new Set();
  let deleteMode = null;
  
  // DOM Elements
  const modal = document.getElementById('delete-modal');
  const modalMessage = document.getElementById('modal-message');
  const modalCancel = document.getElementById('modal-cancel');
  const modalConfirm = document.getElementById('modal-confirm');
  const deleteFilteredBtn = document.getElementById('delete-filtered-logs');
  const deleteAllBtn = document.getElementById('delete-all-logs');
  const deleteSelectedBtn = document.getElementById('delete-selected');
  const searchInput = document.getElementById('log-search');
  const filterSelect = document.getElementById('log-filter');
  const selectAllCheckbox = document.getElementById('select-all-logs');
  const selectedCount = document.getElementById('selected-count');
  const selectedActions = document.getElementById('selected-actions');
  const logsTable = document.getElementById('logs-table');
  const logsTbody = document.getElementById('logs-tbody');
  
  // Initial data load
  fetch('http://localhost:5050/api/logs')
    .then(response => response.json())
    .then(data => {
      logsData = data;
      renderLogs();
      updateLogSummary();
    })
    .catch(error => {
      console.error('Error fetching logs:', error);
      logsTbody.innerHTML = '<tr><td colspan="6">Error loading logs. Please try again later.</td></tr>';
    });
  
  // Render logs function
  function renderLogs(filterText = '', filterStatus = 'All') {
    const tbody = document.getElementById('logs-tbody');
    let filtered = logsData.filter(log => {
      let match = true;
      if (filterText) {
        match = log.ip.includes(filterText) || log.type.toLowerCase().includes(filterText.toLowerCase());
      }
      if (filterStatus !== 'All') {
        match = match && log.status === filterStatus;
      }
      return match;
    });
    
    if (filtered.length) {
      tbody.innerHTML = filtered.map((log, index) => {
        // Create a unique ID for each log based on its properties
        const logId = `log-${log.timestamp.replace(/[^a-zA-Z0-9]/g, '')}-${log.ip.replace(/\./g, '-')}-${index}`;
        
        // Check if this log is selected
        const isChecked = selectedLogs.has(logId) ? 'checked' : '';
        const isSelected = selectedLogs.has(logId) ? 'selected' : '';
        
        return `
          <tr data-log-id="${logId}" class="${isSelected}">
            <td><input type="checkbox" class="log-checkbox" ${isChecked}></td>
            <td>${log.timestamp}</td>
            <td>${log.ip}</td>
            <td>${log.type}</td>
            <td>${log.status}</td>
            <td>${log.summary || ''}</td>
          </tr>
        `;
      }).join('');
      
      // Add event listeners to checkboxes
      document.querySelectorAll('.log-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
          const row = this.closest('tr');
          const logId = row.dataset.logId;
          
          if (this.checked) {
            selectedLogs.add(logId);
            row.classList.add('selected');
          } else {
            selectedLogs.delete(logId);
            row.classList.remove('selected');
          }
          
          updateSelectedCount();
        });
      });
      
      // Add event listeners to rows for clicking to select
      document.querySelectorAll('#logs-tbody tr').forEach(row => {
        if (!row.dataset.logId) return; // Skip if no log ID (like "No results" row)
        
        row.addEventListener('click', function(e) {
          // Don't toggle if clicking on the checkbox itself (let the checkbox handler handle it)
          if (e.target.type === 'checkbox') return;
          
          const checkbox = this.querySelector('.log-checkbox');
          const logId = this.dataset.logId;
          
          // Toggle checkbox
          checkbox.checked = !checkbox.checked;
          
          // Update selection
          if (checkbox.checked) {
            selectedLogs.add(logId);
            this.classList.add('selected');
          } else {
            selectedLogs.delete(logId);
            this.classList.remove('selected');
          }
          
          updateSelectedCount();
        });
      });
      
    } else {
      tbody.innerHTML = '<tr><td colspan="6">No results</td></tr>';
    }
    
    // Update the select all checkbox
    updateSelectAllCheckbox();
    
    // Update selected count
    updateSelectedCount();
  }
  
  // Update log summary
  function updateLogSummary() {
    let total = logsData.length;
    let blocked = logsData.filter(l => l.status === 'Blocked').length;
    let confused = logsData.filter(l => l.status === 'Confused').length;
    let escaped = logsData.filter(l => l.status === 'Escaped').length;
    
    document.getElementById('log-total').textContent = total;
    document.getElementById('log-blocked').textContent = blocked;
    document.getElementById('log-confused').textContent = confused;
    document.getElementById('log-escaped').textContent = escaped;
  }
  
  // Update selected count
  function updateSelectedCount() {
    const count = selectedLogs.size;
    selectedCount.textContent = count;
    
    // Show/hide the selected actions bar
    selectedActions.style.display = count > 0 ? 'block' : 'none';
  }
  
  // Update select all checkbox
  function updateSelectAllCheckbox() {
    const checkboxes = document.querySelectorAll('.log-checkbox');
    
    if (checkboxes.length === 0) {
      selectAllCheckbox.checked = false;
      selectAllCheckbox.indeterminate = false;
      return;
    }
    
    const checkedCount = document.querySelectorAll('.log-checkbox:checked').length;
    
    if (checkedCount === 0) {
      selectAllCheckbox.checked = false;
      selectAllCheckbox.indeterminate = false;
    } else if (checkedCount === checkboxes.length) {
      selectAllCheckbox.checked = true;
      selectAllCheckbox.indeterminate = false;
    } else {
      selectAllCheckbox.checked = false;
      selectAllCheckbox.indeterminate = true;
    }
  }
  
  // Show notification
  function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.style = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: rgba(24, 31, 42, 0.9);
      border-left: 4px solid ${type === 'success' ? '#00e676' : '#ff1744'};
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
      z-index: 1000;
      color: #e0e0e0;
      max-width: 300px;
    `;
    
    notification.innerHTML = `
      <div style="font-weight: bold; margin-bottom: 5px; color: ${type === 'success' ? '#00e676' : '#ff1744'}">
        ${type === 'success' ? 'Success' : 'Error'}
      </div>
      <div>${message}</div>
    `;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
      notification.style.opacity = '0';
      notification.style.transition = 'opacity 0.5s';
      setTimeout(() => notification.remove(), 500);
    }, 3000);
  }
  
  // Event Listeners
  
  // Search input
  searchInput.addEventListener('input', function() {
    renderLogs(this.value, filterSelect.value);
  });
  
  // Filter select
  filterSelect.addEventListener('change', function() {
    renderLogs(searchInput.value, this.value);
  });
  
  // Select all checkbox
  selectAllCheckbox.addEventListener('click', function() {
    const checkboxes = document.querySelectorAll('.log-checkbox');
    
    checkboxes.forEach(checkbox => {
      checkbox.checked = this.checked;
      
      const row = checkbox.closest('tr');
      if (!row || !row.dataset.logId) return;
      
      const logId = row.dataset.logId;
      if (this.checked) {
        selectedLogs.add(logId);
        row.classList.add('selected');
      } else {
        selectedLogs.delete(logId);
        row.classList.remove('selected');
      }
    });
    
    updateSelectedCount();
  });
  
  // Delete All button
  deleteAllBtn.addEventListener('click', function() {
    console.log('Delete All button clicked');
    if (logsData.length === 0) {
      alert('There are no logs to delete.');
      return;
    }
    
    deleteMode = 'all';
    modalMessage.textContent = `Are you sure you want to delete ALL ${logsData.length} logs? This action cannot be undone.`;
    modal.style.display = 'flex';
  });
  
  // Delete Filtered button
  deleteFilteredBtn.addEventListener('click', function() {
    console.log('Delete Filtered button clicked');
    const filterText = searchInput.value;
    const filterStatus = filterSelect.value;
    
    // Get count of filtered logs
    let filtered = logsData.filter(log => {
      let match = true;
      if (filterText) {
        match = log.ip.includes(filterText) || log.type.toLowerCase().includes(filterText.toLowerCase());
      }
      if (filterStatus !== 'All') {
        match = match && log.status === filterStatus;
      }
      return match;
    });
    
    const count = filtered.length;
    
    if (count === 0) {
      alert('No logs match the current filter criteria.');
      return;
    }
    
    deleteMode = 'filtered';
    modalMessage.textContent = `Are you sure you want to delete ${count} filtered logs? This action cannot be undone.`;
    modal.style.display = 'flex';
  });
  
  // Delete Selected button
  deleteSelectedBtn.addEventListener('click', function() {
    console.log('Delete Selected button clicked');
    if (selectedLogs.size === 0) {
      alert('No logs are selected.');
      return;
    }
    
    deleteMode = 'selected';
    modalMessage.textContent = `Are you sure you want to delete ${selectedLogs.size} selected logs? This action cannot be undone.`;
    modal.style.display = 'flex';
  });
  
  // Modal Cancel button
  modalCancel.addEventListener('click', function() {
    console.log('Modal cancel button clicked');
    modal.style.display = 'none';
    deleteMode = null;
  });
  
  // Modal Confirm button
  modalConfirm.addEventListener('click', function() {
    console.log('Modal confirm button clicked, deleteMode:', deleteMode);
    
    if (deleteMode === 'all') {
      // Delete all logs
      logsData = [];
      selectedLogs.clear();
      
      // Show success notification
      showNotification('All logs have been deleted successfully.');
    } 
    else if (deleteMode === 'filtered') {
      const filterText = searchInput.value;
      const filterStatus = filterSelect.value;
      
      // Count before deletion
      const countBefore = logsData.length;
      
      // Filter logs to keep only non-matching ones
      logsData = logsData.filter(log => {
        let match = true;
        if (filterText) {
          match = log.ip.includes(filterText) || log.type.toLowerCase().includes(filterText.toLowerCase());
        }
        if (filterStatus !== 'All') {
          match = match && log.status === filterStatus;
        }
        return !match; // Keep logs that DON'T match the filter
      });
      
      // Count after deletion
      const countDeleted = countBefore - logsData.length;
      
      // Clear selected logs that might have been deleted
      selectedLogs.clear();
      
      // Show success notification
      showNotification(`${countDeleted} filtered logs have been deleted successfully.`);
    }
    else if (deleteMode === 'selected') {
      // Count selected logs
      const countSelected = selectedLogs.size;
      
      // Filter out the selected logs
      logsData = logsData.filter((log, index) => {
        const logId = `log-${log.timestamp.replace(/[^a-zA-Z0-9]/g, '')}-${log.ip.replace(/\./g, '-')}-${index}`;
        return !selectedLogs.has(logId);
      });
      
      // Clear the selected logs set
      selectedLogs.clear();
      
      // Show success notification
      showNotification(`${countSelected} selected logs have been deleted successfully.`);
    }
    
    // Update UI
    renderLogs(searchInput.value, filterSelect.value);
    updateLogSummary();
    
    // Close modal
    modal.style.display = 'none';
    deleteMode = null;
  });
  
  // Close modal when clicking outside
  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      modal.style.display = 'none';
      deleteMode = null;
    }
  });
  
  // Theme toggle
  document.getElementById('theme-toggle').addEventListener('click', function() {
    document.body.classList.toggle('light-theme');
  });
});