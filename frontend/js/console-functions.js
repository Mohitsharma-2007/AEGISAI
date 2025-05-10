/**
 * AEGIS-AI Console Functions
 * This file contains the core functions for the console page
 */

// Function to add a log entry to the console
function addLog(text, type, idx) {
  const log = document.createElement('div');
  log.className = 'log-entry ' + (type||'');
  
  // Check if the text contains detection time information
  const hasDetectionTime = text.includes('ms:') || text.includes('<1ms');
  
  // If it's a block message with detection time, highlight the speed
  if (type === 'block' && hasDetectionTime) {
    // Extract the detection time if present
    let detectionTime = '<1ms';
    const timeMatch = text.match(/in\s+(\d+\.\d+ms|\<1ms)/);
    if (timeMatch && timeMatch[1]) {
      detectionTime = timeMatch[1];
    }
    
    // Create a styled version of the text with highlighted detection time
    const textParts = text.split(':');
    const firstPart = textParts[0];
    const restPart = textParts.slice(1).join(':');
    
    // Create the log content with styled elements
    log.innerHTML = '';
    
    // Add the first part with detection time highlighted
    const firstSpan = document.createElement('span');
    if (detectionTime === '<1ms' || parseFloat(detectionTime) < 10) {
      // Ultra-fast detection (under 10ms)
      firstSpan.innerHTML = `${firstPart}: <span style="color:#00ff00;font-weight:bold;">[ULTRA-FAST: ${detectionTime}]</span>`;
    } else if (parseFloat(detectionTime) < 50) {
      // Fast detection (10-50ms)
      firstSpan.innerHTML = `${firstPart}: <span style="color:#6fffe9;font-weight:bold;">[FAST: ${detectionTime}]</span>`;
    } else {
      // Normal detection (>50ms)
      firstSpan.innerHTML = `${firstPart}: <span style="color:#ffd600;font-weight:bold;">[${detectionTime}]</span>`;
    }
    log.appendChild(firstSpan);
    
    // Add the rest of the text
    const restSpan = document.createElement('span');
    restSpan.textContent = restPart;
    log.appendChild(restSpan);
  } else {
    // Regular log entry without special formatting
    log.textContent = text;
  }
  
  // Add forensics download button for blocked events
  if(type === 'block') {
    const btnBox = document.createElement('span');
    btnBox.style = 'margin-left:1em;';
    const jsonBtn = document.createElement('button');
    jsonBtn.textContent = 'Download Forensics (JSON)';
    jsonBtn.className = 'cta';
    jsonBtn.style = 'background:#232b3a;color:#00b0ff;margin-right:0.5em;';
    jsonBtn.onclick = function(){ downloadForensics(idx, 'json'); };
    const csvBtn = document.createElement('button');
    csvBtn.textContent = 'CSV';
    csvBtn.className = 'cta';
    csvBtn.style = 'background:#232b3a;color:#ffd600;';
    csvBtn.onclick = function(){ downloadForensics(idx, 'csv'); };
    btnBox.appendChild(jsonBtn);
    btnBox.appendChild(csvBtn);
    log.appendChild(btnBox);
  }
  
  document.getElementById('console-log').appendChild(log);
  document.getElementById('console-log').scrollTop = document.getElementById('console-log').scrollHeight;
}

// Function to download forensics reports
async function downloadForensics(idx, format) {
  const url = `/api/forensics/report?idx=${idx}&format=${format}`;
  const res = await fetch(url);
  if(format==='json') {
    const data = await res.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], {type:'application/json'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'forensics_report.json';
    document.body.appendChild(a); a.click(); setTimeout(()=>{document.body.removeChild(a)}, 200);
  } else {
    const text = await res.text();
    const blob = new Blob([text], {type:'text/csv'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'forensics_report.csv';
    document.body.appendChild(a); a.click(); setTimeout(()=>{document.body.removeChild(a)}, 200);
  }
}

// Simulate attack and defense logs
window.startAllAttacks = function() {
  addLog('Starting all simulated attacks...', 'info');
  setTimeout(()=>addLog('Bot-Attack-1 attacking...', 'bot'), 500);
  setTimeout(()=>addLog('AegisAI blocked Bot-Attack-1!', 'block', 0), 1200);
  setTimeout(()=>addLog('LLM-Attack-2 attacking...', 'ai'), 1700);
  setTimeout(()=>addLog('AegisAI confused LLM-Attack-2!', 'block'), 2300);
  setTimeout(()=>addLog('Scripted Bot-Attack-3 attacking...', 'bot'), 2600);
  setTimeout(()=>addLog('AegisAI blocked Scripted Bot-Attack-3!', 'block'), 3200);
  setTimeout(()=>addLog('All simulated attacks complete.', 'info'), 4000);
}

// Script descriptions for UI
const scriptDescriptions = {
  // DDoS Attacks
  'http_flooder': 'Simulates an HTTP flood attack by sending multiple requests to a target server',
  'slowloris_attack': 'Simulates a Slowloris attack that keeps connections open by sending partial HTTP requests',
  
  // Web Attacks
  'sql_injection_demo': 'Demonstrates SQL injection attacks against web applications',
  'xss_payload_demo': 'Demonstrates Cross-Site Scripting (XSS) attacks with various payloads',
  'csrf_attack_demo': 'Demonstrates Cross-Site Request Forgery (CSRF) attacks against web forms',
  'form_submitter': 'Simulates automated form submission attacks',
  'harmful_demo': 'Demonstrates XSS attacks with various payloads and techniques',
  
  // Reconnaissance
  'port_scanner': 'Scans for open ports on a target system',
  'directory_bruteforce': 'Attempts to discover hidden directories on a web server',
  
  // AI/LLM Attacks
  'claude_captcha_bypass': 'Demonstrates how Claude AI can be used to bypass CAPTCHA challenges',
  'claude_probe': 'Tests Claude AI for vulnerabilities and information disclosure',
  'gpt_form_attack': 'Uses GPT to generate malicious inputs for web forms',
  'gpt_probe': 'Tests GPT models for vulnerabilities and information disclosure',
  'gemini_form_spam': 'Uses Gemini AI to generate spam content for forms',
  'gemini_recon': 'Uses Gemini AI for reconnaissance and information gathering',
  
  // Additional attack types
  'fake_login_bot': 'Simulates automated login attempts with credential stuffing',
  'email_spam_demo': 'Demonstrates email spam campaign techniques',
  'brute_force_demo': 'Simulates brute force password attacks',
  'ai_chatbot_demo': 'Demonstrates attacks against AI chatbot systems',
  'llm_completion_demo': 'Uses LLMs to generate malicious content',
  'torch_image_demo': 'Demonstrates adversarial attacks on image recognition systems',
  'bert_qa_demo': 'Tests question-answering systems for vulnerabilities',
  'langchain_demo': 'Demonstrates attacks against LangChain agent systems',
  'huggingface_transformers_demo': 'Tests transformer models for content moderation bypasses',
  'openai_api_demo': 'Demonstrates OpenAI API abuse techniques',
  'anthropic_claude_demo': 'Tests Claude API for constitutional AI bypasses',
  'autogen_demo': 'Demonstrates attacks against Microsoft AutoGen multi-agent systems',
  'scraper_demo': 'Simulates web scraping attacks',
  'selenium_bot_demo': 'Demonstrates browser automation attacks using Selenium',
  'captcha_bypass_demo': 'Shows techniques to bypass CAPTCHA using third-party services',
  'captcha_solver_demo': 'Demonstrates ML-based CAPTCHA solving techniques',
  'stable_diffusion_demo': 'Tests Stable Diffusion for safety filter bypasses'
};

// Function to update script description
function updateScriptDesc() {
  const key = document.getElementById('bot-script-select').value;
  document.getElementById('bot-script-desc').textContent = scriptDescriptions[key] || '';
}

// Function to show block details
function showBlockDetails(details) {
  // Remove any existing block details box
  document.getElementById('block-details-box')?.remove();
  
  // Create the block details box
  const box = document.createElement('div');
  box.id = 'block-details-box';
  box.style = 'margin-top:1.5em; padding:1em; background:#232b3a; border-radius:8px; border-left:4px solid #ff5252;';
  
  // Add the title
  const title = document.createElement('h4');
  title.style = 'margin-top:0; color:#ff5252;';
  title.textContent = 'Attack Block Details';
  box.appendChild(title);
  
  // Add the details
  const detailsList = document.createElement('div');
  detailsList.style = 'display:grid; grid-template-columns:1fr 1fr; gap:0.5em;';
  
  // Add each detail item
  for (const [key, value] of Object.entries(details)) {
    // Skip complex objects
    if (typeof value === 'object' && value !== null) continue;
    
    const item = document.createElement('div');
    item.style = 'margin-bottom:0.3em;';
    
    const label = document.createElement('span');
    label.style = 'color:#b5b5b5; font-size:0.9em;';
    label.textContent = key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()) + ': ';
    item.appendChild(label);
    
    const valueSpan = document.createElement('span');
    valueSpan.style = 'color:#ffd600; font-size:0.9em;';
    valueSpan.textContent = value;
    item.appendChild(valueSpan);
    
    detailsList.appendChild(item);
  }
  
  box.appendChild(detailsList);
  
  // Add the box to the page
  document.getElementById('online-attack-section').appendChild(box);
}

// Function to show error details
function showErrorDetails(error, script) {
  // Remove any existing error details box
  document.getElementById('error-details-box')?.remove();
  
  // Create the error details box
  const box = document.createElement('div');
  box.id = 'error-details-box';
  box.style = 'margin-top:1.5em; padding:1em; background:#232b3a; border-radius:8px; border-left:4px solid #ff5252;';
  
  // Add the title
  const title = document.createElement('h4');
  title.style = 'margin-top:0; color:#ff5252;';
  title.textContent = 'Error Details';
  box.appendChild(title);
  
  // Add the error message
  const message = document.createElement('div');
  message.style = 'margin-bottom:1em; color:#ffd600;';
  message.textContent = error;
  box.appendChild(message);
  
  // Add the script info
  const scriptInfo = document.createElement('div');
  scriptInfo.style = 'color:#b5b5b5; font-size:0.9em;';
  scriptInfo.textContent = `Script: ${script}`;
  box.appendChild(scriptInfo);
  
  // Add the box to the page
  document.getElementById('online-attack-section').appendChild(box);
}

// Function to run online bot attack
window.runOnlineBotAttack = function() {
  const scriptKey = document.getElementById('bot-script-select').value;
  addLog('Running online bot/AI/LLM attack ('+scriptKey+')...', 'online');
  document.getElementById('online-status').textContent = 'Online attack running...';
  document.getElementById('run-bot-btn').disabled = true;
  
  // Check if we should use the local JavaScript implementation or the Python backend
  if (window.useLocalScripts) {
    // Use local JavaScript implementation
    try {
      const result = attackScripts[scriptKey].execute();
      
      if (result.success && result.events) {
        // Track log index for forensics download
        let logIdx = window._logIndex || 0;
        result.events.forEach(ev => {
          addLog(ev, ev.includes('blocked') ? 'block' : 'online', ev.includes('blocked') ? logIdx : undefined);
          logIdx++;
        });
        window._logIndex = logIdx;
        document.getElementById('online-status').textContent = 'Online attack finished!';
        
        // Show detailed block info if present
        if (result.block_details) {
          showBlockDetails(result.block_details);
        } else {
          document.getElementById('block-details-box')?.remove();
        }
        document.getElementById('error-details-box')?.remove();
      } else {
        addLog('No attack events returned.', 'info');
        document.getElementById('online-status').textContent = '';
        document.getElementById('block-details-box')?.remove();
      }
      
      document.getElementById('run-bot-btn').disabled = false;
    } catch (error) {
      document.getElementById('run-bot-btn').disabled = false;
      addLog('Error running local attack: ' + error.message, 'info');
      document.getElementById('online-status').textContent = '';
      document.getElementById('block-details-box')?.remove();
      document.getElementById('error-details-box')?.remove();
    }
  } else {
    // Check if we can use the script bridge
    if (window.scriptBridge && typeof window.scriptBridge.runScript === 'function') {
      // Use script bridge
      window.scriptBridge.runScript(scriptKey)
        .then(j => {
          const runBtn = document.getElementById('run-bot-btn');
          runBtn.disabled = false;
          if(j.success && j.events) {
            // Track log index for forensics download
            let logIdx = window._logIndex || 0;
            j.events.forEach(ev => {
              addLog(ev, ev.includes('blocked') ? 'block' : 'online', ev.includes('blocked') ? logIdx : undefined);
              logIdx++;
            });
            window._logIndex = logIdx;
            document.getElementById('online-status').textContent = 'Online attack finished!';
            // Show detailed block info if present
            if(j.block_details) {
              showBlockDetails(j.block_details);
            } else {
              document.getElementById('block-details-box')?.remove();
            }
            document.getElementById('error-details-box')?.remove();
          } else {
            if(j.error) {
              showErrorDetails(j.error, j.script || 'unknown');
              // Don't disable the button on error
              runBtn.disabled = false;
            }
            addLog('No attack events returned.', 'info');
            document.getElementById('online-status').textContent = '';
            document.getElementById('block-details-box')?.remove();
          }
        })
        .catch((error) => {
          document.getElementById('run-bot-btn').disabled = false;
          addLog('Error running attack via bridge: ' + error.message, 'info');
          document.getElementById('online-status').textContent = '';
          document.getElementById('block-details-box')?.remove();
          document.getElementById('error-details-box')?.remove();
          
          // Fall back to local scripts
          window.useLocalScripts = true;
          setTimeout(() => window.runOnlineBotAttack(), 500);
        });
    } else {
      // Use direct Python backend API
      fetch('http://localhost:5050/api/online-bot-attack', {
        method:'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({script: `scripts.${scriptKey}`})
      })
      .then(r=>r.json()).then(j=>{
        const runBtn = document.getElementById('run-bot-btn');
        runBtn.disabled = false;
        if(j.success && j.events) {
          // Track log index for forensics download
          let logIdx = window._logIndex || 0;
          j.events.forEach(ev => {
            addLog(ev, ev.includes('blocked') ? 'block' : 'online', ev.includes('blocked') ? logIdx : undefined);
            logIdx++;
          });
          window._logIndex = logIdx;
          document.getElementById('online-status').textContent = 'Online attack finished!';
          // Show detailed block info if present
          if(j.block_details) {
            showBlockDetails(j.block_details);
          } else {
            document.getElementById('block-details-box')?.remove();
          }
          document.getElementById('error-details-box')?.remove();
        } else {
          if(j.error) {
            showErrorDetails(j.error, j.script || 'unknown');
            // Don't disable the button on error
            runBtn.disabled = false;
          }
          addLog('No attack events returned.', 'info');
          document.getElementById('online-status').textContent = '';
          document.getElementById('block-details-box')?.remove();
        }
      }).catch((error)=>{
        document.getElementById('run-bot-btn').disabled = false;
        // If the backend is not running, fall back to local scripts
        if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
          addLog('Backend not available, falling back to local scripts...', 'info');
          window.useLocalScripts = true;
          // Try again with local scripts
          setTimeout(() => window.runOnlineBotAttack(), 500);
        } else {
          addLog('Error running online attack: ' + error.message, 'info');
          document.getElementById('online-status').textContent = '';
          document.getElementById('block-details-box')?.remove();
          document.getElementById('error-details-box')?.remove();
        }
      });
  }
};

// Detection speed test
window.testDetectionSpeed = function() {
  const detectionSpeedEl = document.getElementById('detection-speed');
  const testBtn = document.getElementById('test-detection-speed');
  
  // Disable the button during testing
  testBtn.disabled = true;
  testBtn.textContent = 'Testing...';
  
  addLog('Starting detection speed test...', 'info');
  
  // List of scripts to test
  const scriptsToTest = [
    'sql_injection_demo',
    'xss_payload_demo',
    'form_submitter',
    'gpt_form_attack',
    'claude_probe'
  ];
  
  // Track test results
  let detectionCount = 0;
  let fastestDetection = Infinity;
  let slowestDetection = 0;
  let totalDetectionTime = 0;
  
  // Function to run a test for a specific script
  function runTest(scriptIndex) {
    // If we've tested all scripts, show the results
    if (scriptIndex >= scriptsToTest.length) {
      const avgDetectionTime = totalDetectionTime / detectionCount;
      
      addLog(`Detection speed test complete. Results:`, 'info');
      addLog(`Fastest detection: ${fastestDetection < 1 ? '<1' : fastestDetection.toFixed(2)}ms`, 'info');
      addLog(`Slowest detection: ${slowestDetection.toFixed(2)}ms`, 'info');
      addLog(`Average detection: ${avgDetectionTime.toFixed(2)}ms`, 'info');
      
      // Update the detection speed display with the fastest time
      detectionSpeedEl.innerHTML = `Detection Speed: <b>${fastestDetection < 1 ? '<1' : fastestDetection.toFixed(2)}ms</b>`;
      
      // Re-enable the test button
      testBtn.disabled = false;
      testBtn.textContent = 'Test Detection Speed';
      
      return;
    }
    
    const scriptKey = scriptsToTest[scriptIndex];
    
    // Log the current test
    addLog(`Testing detection speed for ${scriptKey}...`, 'info');
    
    // Check if we should use the local JavaScript implementation or the Python backend
    if (window.useLocalScripts) {
      // Use local JavaScript implementation
      try {
        // Simulate a detection test
        const startTime = performance.now();
        
        // Execute the script in test mode if available
        if (attackScripts[scriptKey] && typeof attackScripts[scriptKey].testDetection === 'function') {
          attackScripts[scriptKey].testDetection();
        } else {
          // Just execute the script normally if no test function is available
          attackScripts[scriptKey].execute();
        }
        
        const endTime = performance.now();
        const detectionTime = endTime - startTime;
        
        // Log the result
        addLog(`${scriptKey} detection time: ${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms`, 'info');
        
        // Update the stats
        totalDetectionTime += detectionTime;
        detectionCount++;
        fastestDetection = Math.min(fastestDetection, detectionTime);
        slowestDetection = Math.max(slowestDetection, detectionTime);
        
        // Update the detection speed display during testing
        detectionSpeedEl.innerHTML = `Testing: <b style="color:#ffd600;">${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms</b>`;
        
        // Run the next test after a short delay
        setTimeout(() => runTest(scriptIndex + 1), 500);
      } catch (error) {
        console.error('Error during local speed test:', error);
        addLog(`Error testing script ${scriptKey}: ${error.message}`, 'info');
        
        // Continue with next test
        setTimeout(() => runTest(scriptIndex + 1), 500);
      }
    } else if (window.scriptBridge && typeof window.scriptBridge.testDetectionSpeed === 'function') {
      // Use script bridge
      window.scriptBridge.testDetectionSpeed(scriptKey)
        .then(j => {
          if (j.success && j.detection_time !== undefined) {
            const detectionTime = j.detection_time;
            
            // Log the result
            addLog(`${scriptKey} detection time: ${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms`, 'info');
            
            // Update the stats
            totalDetectionTime += detectionTime;
            detectionCount++;
            fastestDetection = Math.min(fastestDetection, detectionTime);
            slowestDetection = Math.max(slowestDetection, detectionTime);
            
            // Update the detection speed display during testing
            detectionSpeedEl.innerHTML = `Testing: <b style="color:#ffd600;">${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms</b>`;
          }
          
          // Run the next test after a short delay
          setTimeout(() => runTest(scriptIndex + 1), 500);
        })
        .catch(error => {
          console.error('Error during bridge speed test:', error);
          addLog(`Error testing script ${scriptKey}: ${error.message}`, 'info');
          
          // Continue with next test
          setTimeout(() => runTest(scriptIndex + 1), 500);
        });
    } else {
      // Use Python backend API directly
      fetch('http://localhost:5050/api/test-detection-speed', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({script: `scripts.${scriptKey}`})
      })
      .then(r => r.json())
      .then(j => {
        if (j.success && j.detection_time !== undefined) {
          const detectionTime = j.detection_time;
          
          // Log the result
          addLog(`${scriptKey} detection time: ${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms`, 'info');
          
          // Update the stats
          totalDetectionTime += detectionTime;
          detectionCount++;
          fastestDetection = Math.min(fastestDetection, detectionTime);
          slowestDetection = Math.max(slowestDetection, detectionTime);
          
          // Update the detection speed display during testing
          detectionSpeedEl.innerHTML = `Testing: <b style="color:#ffd600;">${detectionTime < 1 ? '<1' : detectionTime.toFixed(2)}ms</b>`;
        }
        
        // Run the next test after a short delay
        setTimeout(() => runTest(scriptIndex + 1), 500);
      })
      .catch(error => {
        console.error('Error during speed test:', error);
        
        // If the backend is not running, fall back to local scripts
        if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
          addLog('Backend not available, falling back to local scripts...', 'info');
          window.useLocalScripts = true;
          
          // Try again with local scripts
          runTest(scriptIndex);
        } else {
          addLog(`Error testing script ${scriptKey}: ${error.message}`, 'info');
          
          // Continue with next test
          setTimeout(() => runTest(scriptIndex + 1), 500);
        }
      });
    }
  }
  
  // Start the tests
  runTest(0);
};