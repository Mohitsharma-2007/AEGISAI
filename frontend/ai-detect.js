// AI/LLM/Bot Detection & Redirect
(function(){
  // Only run on main pages (not on fake pages or dashboard)
  const FAKE_PAGES = ['fake-llm.html','fake-404.html','fake-admin.html','fake-login.html'];
  if (FAKE_PAGES.some(f => window.location.pathname.endsWith(f))) return;

  // Gather data for detection
  function getDetectionPayload() {
    return {
      user_agent: navigator.userAgent,
      js_enabled: true,
      cookie_enabled: navigator.cookieEnabled,
      url: window.location.href,
      timing: performance.now() / 1000,
      entropy: window.mouseEntropy || 42,
      mouse_pattern: 'random', // stub
      keyboard_pattern: 'random', // stub
      scroll: window.scrollY,
      tab_switches: (window.tabSwitches || 1),
      payload: '',
    };
  }

  fetch('http://localhost:5050/api/detect', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(getDetectionPayload())
  })
    .then(r=>r.json())
    .then(resp => {
      if (resp && resp.redirect) {
        // Redirect to a random fake page
        const pages = ['fake-llm.html','fake-404.html','fake-admin.html','fake-login.html'];
        window.location.href = pages[Math.floor(Math.random()*pages.length)];
      }
    })
    .catch(()=>{});
})();
