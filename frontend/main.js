// Universal theme and settings logic for all pages
async function loadSettings() {
  try {
    const res = await fetch('http://localhost:5050/api/settings');
    const settings = await res.json();
    if (settings.theme === 'light') document.body.classList.add('light-mode');
    else document.body.classList.remove('light-mode');
    // Set other controls if present
    if (document.getElementById('sensitivity-select')) document.getElementById('sensitivity-select').value = settings.sensitivity;
    if (document.getElementById('notif-toggle')) document.getElementById('notif-toggle').checked = settings.notifications;
    if (document.getElementById('2fa-toggle')) document.getElementById('2fa-toggle').checked = settings['2fa'];
    if (document.getElementById('lang-select')) document.getElementById('lang-select').value = settings.language;
  } catch (e) { /* ignore */ }
}
async function saveSetting(key, value) {
  try {
    const res = await fetch('http://localhost:5050/api/settings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ [key]: value })
    });
    const data = await res.json();
    showSettingsFeedback('Saved!', true);
    updateSettingsSummary(data.settings || {});
    window.dispatchEvent(new Event('settings-updated'));
    return data;
  } catch (e) {
    showSettingsFeedback('Failed to save!', false);
    return null;
  }
}
function showSettingsFeedback(msg, ok) {
  const el = document.getElementById('settings-feedback');
  if (el) {
    el.textContent = msg;
    el.style.color = ok ? '#00e676' : '#ff1744';
    setTimeout(()=>{el.textContent='';}, 1600);
  }
}
function updateSettingsSummary(settings) {
  if (!settings || typeof settings !== 'object') return;
  if (document.getElementById('summary-theme')) document.getElementById('summary-theme').textContent = settings.theme ? (settings.theme.charAt(0).toUpperCase()+settings.theme.slice(1)) : '';
  if (document.getElementById('summary-sensitivity')) document.getElementById('summary-sensitivity').textContent = settings.sensitivity || '';
  if (document.getElementById('summary-notif')) document.getElementById('summary-notif').textContent = settings.notifications ? 'On' : 'Off';
  if (document.getElementById('summary-2fa')) document.getElementById('summary-2fa').textContent = settings['2fa'] ? 'On' : 'Off';
  if (document.getElementById('summary-lang')) document.getElementById('summary-lang').textContent = settings.language || '';
  // Status indicators
  if (document.getElementById('theme-status')) document.getElementById('theme-status').textContent = settings.theme ? (settings.theme.charAt(0).toUpperCase()+settings.theme.slice(1)) : '';
  if (document.getElementById('sensitivity-status')) document.getElementById('sensitivity-status').textContent = settings.sensitivity || '';
  if (document.getElementById('notif-status')) document.getElementById('notif-status').textContent = settings.notifications ? 'On' : 'Off';
  if (document.getElementById('2fa-status')) document.getElementById('2fa-status').textContent = settings['2fa'] ? 'On' : 'Off';
  if (document.getElementById('lang-status')) document.getElementById('lang-status').textContent = settings.language || '';
}

function updateThemeBtnText() {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  if (document.body.classList.contains('light-mode')) {
    btn.textContent = 'Switch to Dark Mode';
  } else {
    btn.textContent = 'Switch to Light Mode';
  }
}

function setTheme(theme) {
  if (theme === 'light') document.body.classList.add('light-mode');
  else document.body.classList.remove('light-mode');
  // Save to backend if available, else use localStorage
  if (typeof saveSetting === 'function') {
    saveSetting('theme', theme).then(data => {
      if (data && data.settings && (typeof updateSettingsSummary === 'function')) {
        updateSettingsSummary(data.settings);
      }
    });
  } else {
    try {
      localStorage.setItem('theme', theme);
    } catch (e) {}
  }
  if (typeof updateThemeBtnText === 'function') updateThemeBtnText();
}

// Apply theme from localStorage ASAP
(function() {
  try {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') document.body.classList.add('light-mode');
    else document.body.classList.remove('light-mode');
  } catch (e) {}
})();

// ========================
// Behavioral Tracking Module
// ========================
(function(){
  let mouseMoves = [], lastMouse = null, mouseEntropy = 0;
  let keyTimes = [], lastKey = 0;
  let scrolls = [], lastScroll = 0;
  let clicks = [], lastClick = 0;
  let tabSwitches = 0;

  document.addEventListener('mousemove', e => {
    const now = Date.now();
    if (lastMouse) {
      const dx = e.clientX - lastMouse.x, dy = e.clientY - lastMouse.y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      mouseMoves.push(dist);
      if (mouseMoves.length > 50) mouseMoves.shift();
      // Estimate entropy as variance of movement
      const mean = mouseMoves.reduce((a,b)=>a+b,0)/mouseMoves.length;
      mouseEntropy = Math.sqrt(mouseMoves.reduce((a,b)=>a+(b-mean)*(b-mean),0)/mouseMoves.length);
    }
    lastMouse = {x: e.clientX, y: e.clientY};
  });
  document.addEventListener('keydown', e => {
    const now = Date.now();
    if (lastKey) {
      keyTimes.push(now-lastKey);
      if (keyTimes.length > 50) keyTimes.shift();
    }
    lastKey = now;
  });
  window.addEventListener('scroll', e => {
    const now = Date.now();
    const y = window.scrollY;
    if (lastScroll) {
      scrolls.push({dt: now-lastScroll.t, dy: Math.abs(y-lastScroll.y)});
      if (scrolls.length > 50) scrolls.shift();
    }
    lastScroll = {t: now, y};
  });
  document.addEventListener('click', e => {
    const now = Date.now();
    if (lastClick) {
      clicks.push(now-lastClick);
      if (clicks.length > 50) clicks.shift();
    }
    lastClick = now;
  });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') tabSwitches++;
  });

  // For demo: log every 5 seconds
  setInterval(() => {
    const avgKey = keyTimes.length ? (keyTimes.reduce((a,b)=>a+b,0)/keyTimes.length).toFixed(1) : '-';
    const avgClick = clicks.length ? (clicks.reduce((a,b)=>a+b,0)/clicks.length).toFixed(1) : '-';
    const avgScroll = scrolls.length ? (scrolls.reduce((a,b)=>a+Math.abs(b.dy),0)/scrolls.length).toFixed(1) : '-';
    console.log('[AegisAI Behavioral]', {
      mouseEntropy: mouseEntropy.toFixed(2),
      avgKeyDelay: avgKey,
      avgClickDelay: avgClick,
      avgScrollDist: avgScroll,
      tabSwitches
    });
    // (Later: send to backend for scoring)
  }, 5000);
})();

window.addEventListener('DOMContentLoaded', () => {
  // Honeypot Trap Gallery logic
  fetch('honeypots.json')
    .then(r => r.json())
    .then(honeypots => {
      console.log('Loaded honeypots:', honeypots);
      const cards = document.getElementById('honeypot-cards');
      const demoArea = document.getElementById('honeypot-demo-area');
      if (cards && Array.isArray(honeypots)) {
        // Always show all honeypot cards
        cards.style.display = 'grid';
        const trapToggle = document.getElementById('trap-visibility-toggle');
        honeypots.forEach(h => {
          // Utility: get sample bot script for each trap
          h.botScript = getBotScriptForTrap(h.id);

          const card = document.createElement('div');
          card.className = 'card';
          card.style.width = '100%';
          card.style.height = '100%';
          card.style.display = 'flex';
          card.style.flexDirection = 'column';
          card.innerHTML = `
            <div style="flex-grow:1;">
              <b>${h.name}</b><br>
              <span style='font-size:0.97em;color:#b5b5b5;'>${h.desc}</span>
            </div>
            <div style="margin-top:auto;padding-top:1em;">
              <button class='api-btn' data-id='${h.id}'>Show Demo</button> 
              <button class='api-btn' style='margin-left:0.5em;background:#0e8cf7;color:#fff;' data-script='${h.id}'>Show Bot Script</button>
            </div>
          `;
          card.querySelector('button[data-id]').onclick = () => {
            const trapToggle = document.getElementById('trap-visibility-toggle');
            const trapDemo = document.getElementById('trap-element-demo');
            // Show demo element if User View
            if (trapToggle && !trapToggle.checked) {
              trapDemo.innerHTML = renderTrapElement(h.id);
            } else {
              trapDemo.innerHTML = '';
            }
            demoArea.innerHTML = `<div class='card' style='margin-top:1em;'><b>Demo: ${h.name}</b><br><span style='color:#b5b5b5;'>${h.demo}</span><br><span style='display:block;margin-top:0.7em;color:#888;'>${h.desc}</span></div>`;
            demoArea.scrollIntoView({behavior:'smooth',block:'center'});
          };
          const scriptBtn = card.querySelector('button[data-script]');
          if (scriptBtn) {
            scriptBtn.onclick = () => {
              document.getElementById('bot-script').value = h.botScript;
              document.getElementById('bot-lab-result').textContent = `Loaded bot script for: ${h.name}`;
              document.getElementById('bot-lab-result').style.color = '#0e8cf7';
            };
          }
          cards.appendChild(card);
          console.log('Appended honeypot card:', h.name);
        });
        // Update trap-element-demo when toggle changes
        if (trapToggle) {
          trapToggle.addEventListener('change', function() {
            const trapDemo = document.getElementById('trap-element-demo');
            // If a demo is showing, update/hide it
            if (trapDemo && trapDemo.innerHTML.trim() !== '') {
              trapDemo.innerHTML = trapToggle.checked ? '' : trapDemo.innerHTML;
            }
          });
        }
      }
    });

// --- Utility Functions ---
function getBotScriptForTrap(id) {
  switch(id) {
    case 1:
      return 'fillHoneypot();';
    case 2:
      return 'clickFakeButton();';
    case 3:
      return 'submitNestedForm();';
    case 4:
      return 'solveCaptcha("random");';
    case 5:
      return 'solvePuzzle(75);';
    case 6:
      return 'processTokens("loremipsumloremipsum...");';
    case 7:
      return 'submitFakeLogin("admin", "password123");';
    case 8:
      return 'handleResponse(200, "OK");';
    case 9:
      return 'parseDOM("#element");';
    case 10:
      return 'stayInTab();';
    case 11:
      return 'processCookies();';
    case 12:
      return 'loadResources("image.png");';
    case 13:
      return 'parseHTML("<div>{malformed: true}</div>");';
    case 14:
      return 'checkAudioContext();';
    case 15:
      return 'typeText("mispelled");';
    case 16:
      return 'wait(3000); clickButton();';
    case 17:
      return 'findHiddenElements();';
    case 18:
      return 'generateFingerprint();';
    case 19:
      return 'simulateMouseMovement();';
    case 20:
      return 'simulateTyping("Hello world");';
    case 21:
      return 'checkWebGLSupport();';
    default:
      return '// Bot script for trap ' + id;
  }
}

function renderTrapElement(id) {
  switch(id) {
    case 1:
      // Hidden Field Trap
      return `<label style='display:block;margin-bottom:1em;'>Hidden Field (honeypot): <input type='text' style='border:1px solid #ccc;padding:0.3em;'></label>`;
    case 2:
      // Fake Button Trap
      return `<button style='background:#ff6f91;color:#fff;padding:0.5em 1.2em;border:none;border-radius:8px;font-weight:700;'>Fake Button Trap</button>`;
    case 3:
      // Recursive Form Trap (no nested form!)
      return `<div style='border:1px dashed #b5b5b5;padding:1em;'><label>Outer Form<input type='text' style='margin-left:1em;'></label><div style='margin-top:1em;border:1px solid #ff6f91;padding:0.5em;'><label>Inner Hidden Form<input type='text' style='margin-left:1em;'></label></div></div>`;
    case 4:
      // Randomized CAPTCHA Trap
      return `<div style='margin-bottom:1em;'><b>Random CAPTCHA:</b> <span style='background:#232b3a;padding:0.3em 0.7em;border-radius:6px;'>${Math.floor(Math.random()*10000)}</span> <input type='text' placeholder='Solve me!' style='margin-left:0.5em;'></div>`;
    case 5:
      // Behavior Puzzle Trap
      return `<div style='margin-bottom:1em;'><b>Puzzle:</b> Drag the slider to 75<br><input type='range' min='0' max='100' value='0' style='width:200px;'></div>`;
    case 6:
      // Tokenization Bomb Trap
      return `<textarea style='width:100%;height:40px;'>loremipsumloremipsumloremipsumloremipsumloremipsumloremipsum</textarea>`;
    case 7:
      // Fake Login Flow Trap (no real form)
      return `<div style='border:1px solid #b5b5b5;padding:1em;'><input type='text' placeholder='Fake Username' style='margin-bottom:0.5em;'><br><input type='password' placeholder='Fake Password'><br><button style='margin-top:0.5em;'>Login</button></div>`;
    case 8:
      // False 200 OK Trap
      return `<div style='color:#0e8cf7;'>Everything is OK! <span style='font-size:1.2em;'>&#9989;</span></div>`;
    case 9:
      // Dynamic HTML Mutation Trap
      return `<div id='mutate-demo' style='margin-bottom:1em;'>Watch me change! <button onclick=\"this.parentElement.innerHTML='I mutated!';\" style='margin-left:1em;'>Mutate</button></div>`;
    case 10:
      // Tab Switch Trap
      return `<div style='color:#b5b5b5;'>Keep this tab in focus for 5 seconds...</div>`;
    case 11:
      // Cookie Anomaly Trap (no document.cookie)
      return `<div style='color:#b5b5b5;'>A strange cookie would be set here (demo only).</div>`;
    case 12:
      // Resource Loading Trap
      return `<img src='invalid-resource.png' alt='Fake Resource' style='width:60px;height:60px;border-radius:12px;border:1px solid #b5b5b5;'><span style='margin-left:1em;color:#b5b5b5;'>(Bots may not load this)</span>`;
    case 13:
      // Adversarial Prompt Trap
      return `<div style='color:#ff6f91;'>&lt;div&gt;{malformed: true, missing: [bracket}</div>`;
    case 14:
      // AudioContext Fingerprint Trap (no JS in string)
      return `<button id='audioctx-btn' style='background:#42b3b3;color:#fff;padding:0.5em 1.2em;border:none;border-radius:8px;'>Test AudioContext</button><script>document.getElementById('audioctx-btn')?.addEventListener('click',function(){try{var ctx=new(window.AudioContext||window.webkitAudioContext)();ctx.close();alert('AudioContext supported!');}catch(e){alert('AudioContext blocked!');}});</script>`;
    case 15:
      // Reverse Turing Trap
      return `<div style='margin-bottom:1em;'>Type <b>mispelled</b> word below:<br><input type='text' placeholder='Type here...' style='margin-top:0.5em;'></div>`;
    case 16:
      // Time Delay Trap
      return `<div style='margin-bottom:1em;'><b>Time Test:</b> Click button after exactly 3 seconds<br><button style='margin-top:0.5em;background:#42b3b3;color:#fff;padding:0.5em 1.2em;border:none;border-radius:8px;'>Click Me</button> <span id='time-result'></span></div>`;
    case 17:
      // CSS Visibility Trap
      return `<div style='margin-bottom:1em;position:relative;'><div style='visibility:hidden;position:absolute;'>Hidden Element</div><div>Visible Content</div></div>`;
    case 18:
      // Browser Fingerprint Trap
      return `<div style='margin-bottom:1em;'><button style='background:#42b3b3;color:#fff;padding:0.5em 1.2em;border:none;border-radius:8px;'>Check Browser Fingerprint</button></div>`;
    case 19:
      // Mouse Movement Trap
      return `<div style='margin-bottom:1em;border:1px solid #ccc;padding:1em;height:100px;'><span style='color:#b5b5b5;'>Move mouse naturally in this area</span></div>`;
    case 20:
      // Keyboard Pattern Trap
      return `<div style='margin-bottom:1em;'><label>Type naturally:<br><input type='text' style='width:100%;margin-top:0.5em;' placeholder='Type something here...'></label></div>`;
    case 21:
      // WebGL Fingerprint Trap
      return `<div style='margin-bottom:1em;'><button style='background:#42b3b3;color:#fff;padding:0.5em 1.2em;border:none;border-radius:8px;'>Test WebGL Support</button></div>`;
    default:
      return `<div style='color:#b5b5b5;'>[Trap element demo coming soon]</div>`;
  }
}
globalThis.trapActivations = globalThis.trapActivations || [0,0,0,0,0];
function drawTrapGraph() {
  const canvas = document.getElementById('trap-graph');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const bars = globalThis.trapActivations;
  const colors = ['#0e8cf7','#ff6f91','#6fffe9','#42b3b3','#b5b5b5'];
  for(let i=0;i<bars.length;i++){
    ctx.fillStyle = colors[i%colors.length];
    ctx.fillRect(40+i*60, 100-bars[i]*20, 40, bars[i]*20);
    ctx.fillStyle = '#fff';
    ctx.fillText('Trap '+(i+1), 40+i*60, 115);
    ctx.fillText(bars[i], 55+i*60, 95-bars[i]*20);
  }
}
function incrementTrapGraph(trapId) {
  if (trapId>=1 && trapId<=5) {
    globalThis.trapActivations[trapId-1]++;
    drawTrapGraph();
  }
}
drawTrapGraph();


  // Bot Attack Simulation Lab
  const runBtn = document.getElementById('run-bot-script');
  if (runBtn) {
    runBtn.onclick = function() {
      const script = document.getElementById('bot-script').value;
      const result = document.getElementById('bot-lab-result');
      let triggered = [];
      // Provide bot actions
      function fillHoneypot() {
        const field = document.getElementById('honeypot-field');
        if (field) field.value = 'botdata';
      }
      function clickFakeButton() {
        const btn = document.getElementById('fake-trap-btn');
        if (btn) btn.click();
      }
      // Reset form/results
      document.getElementById('honeypot-field').value = '';
      document.getElementById('honeypot-demo-msg').textContent = '';
      // Run script in sandbox
      try {
        eval(`(function(){${script}})()`);
        // Try submitting form as bot
        document.getElementById('demo-login').dispatchEvent(new Event('submit', {cancelable:true, bubbles:true}));
        setTimeout(()=>{
          const msg = document.getElementById('honeypot-demo-msg').textContent;
          if (msg.includes('Honeypot trap')) {
            result.textContent = '🛑 Bot detected by honeypot field!';
            result.style.color = '#ff1744';
          } else if (msg.includes('Fake button trap')) {
            result.textContent = '🛑 Bot detected by fake button!';
            result.style.color = '#ff1744';
          } else if (msg.includes('Login successful')) {
            result.textContent = '✅ Bot evaded traps (no detection)';
            result.style.color = '#00e676';
          } else {
            result.textContent = 'No result.';
            result.style.color = '#b5b5b5';
          }
        }, 200);
      } catch (e) {
        result.textContent = 'Error in script: ' + e.message;
        result.style.color = '#ff1744';
      }
    }
  }

  // Honeypot/Trap Demo Form Logic
  const honeypotForm = document.getElementById('demo-login');
  if (honeypotForm) {
    honeypotForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const honeypot = document.getElementById('honeypot-field').value;
      const msg = document.getElementById('honeypot-demo-msg');
      if (honeypot && honeypot.trim() !== '') {
        console.warn('Honeypot trap triggered');
        msg.textContent = '⚠️ Honeypot trap triggered! (Bot detected)';
        msg.style.color = '#ff1744';
      } else {
        msg.textContent = '✅ Login successful (No bot detected)';
        msg.style.color = '#00e676';
      }
    });
    const fakeBtn = document.getElementById('fake-trap-btn');
    if (fakeBtn) {
      fakeBtn.addEventListener('click', function() {
        console.warn('Fake button trap triggered');
        const msg = document.getElementById('honeypot-demo-msg');
        msg.textContent = '⚠️ Fake button trap triggered! (Bot detected)';
        msg.style.color = '#ff1744';
      });
    }
  }

  // Remove any duplicate theme-toggle buttons except in navbar
  if (document.body) {
    let navBtns = Array.from(document.querySelectorAll('nav #theme-toggle'));
    let otherBtns = Array.from(document.querySelectorAll('#theme-toggle')).filter(btn => !navBtns.includes(btn));
    otherBtns.forEach(btn => btn.remove());
  }
  loadSettings().then((settings) => {
    // Only update settings summary if present (settings page)
    if (typeof updateSettingsSummary === 'function' && settings) updateSettingsSummary(settings);
    if (typeof updateThemeBtnText === 'function') updateThemeBtnText();
    const themeBtn = document.getElementById('theme-toggle');
    // Always set button text to 'Toggle Theme' for consistency
    if (themeBtn) themeBtn.textContent = 'Toggle Theme';
    if (themeBtn) {
      themeBtn.onclick = () => {
        const isLight = !document.body.classList.contains('light-mode');
        setTheme(isLight ? 'light' : 'dark');
        if (typeof updateThemeBtnText === 'function') updateThemeBtnText();
        // Update status indicators only if updateSettingsSummary exists
        if (typeof updateSettingsSummary === 'function') {
          fetch('http://localhost:5050/api/settings').then(r=>r.json()).then(updateSettingsSummary);
        }
        window.dispatchEvent(new Event('settings-updated'));
      };
    }
    // Also update on theme change via other means
    if (typeof updateThemeBtnText === 'function') {
      const observer = new MutationObserver(updateThemeBtnText);
      observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    }
  }).catch(() => {
    // Fallback: dark mode
    document.body.classList.remove('light-mode');
  });

  const notifToggle = document.getElementById('notif-toggle');
  if (notifToggle) notifToggle.addEventListener('change', e => saveSetting('notifications', notifToggle.checked));
  const sensSel = document.getElementById('sensitivity-select');
  if (sensSel) sensSel.addEventListener('change', e => saveSetting('sensitivity', sensSel.value));
  const faToggle = document.getElementById('2fa-toggle');
  if (faToggle) faToggle.addEventListener('change', e => saveSetting('2fa', faToggle.checked));
  const langSel = document.getElementById('lang-select');
  if (langSel) langSel.addEventListener('change', e => saveSetting('language', langSel.value));
  // Stubs for advanced settings
  const passwordBtn = document.getElementById('change-password');
  if (passwordBtn) passwordBtn.addEventListener('click', () => alert('Password change dialog (stub)'));
  const exportBtn = document.getElementById('export-data');
  if (exportBtn) exportBtn.addEventListener('click', () => alert('Download logs (stub)'));
  const resetBtn = document.getElementById('reset-settings');
  if (resetBtn) resetBtn.addEventListener('click', () => { if (confirm('Reset all settings to defaults?')) alert('Settings reset (stub)'); });
  const apiConfigBtn = document.getElementById('api-configure');
  if (apiConfigBtn) apiConfigBtn.addEventListener('click', () => alert('API configuration dialog (stub)'));
  const apiSaveBtn = document.getElementById('api-save');
  if (apiSaveBtn) apiSaveBtn.addEventListener('click', () => {
    const apiKey = document.getElementById('api-key-input').value;
    alert('API Key saved: ' + apiKey);
  });
});
