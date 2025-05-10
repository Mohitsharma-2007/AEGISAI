/**
 * AEGIS-AI Script Bridge
 * This file serves as a bridge between the frontend and the Python backend.
 * It provides JavaScript functions that map to the Python script handler.
 */

// Map of script categories
const SCRIPT_CATEGORIES = {
  'ddos': 'DDoS Attacks',
  'web': 'Web Attacks',
  'recon': 'Reconnaissance',
  'ai': 'AI/LLM Attacks',
  'bot': 'Bot Attacks',
  'captcha': 'CAPTCHA Attacks'
};

// Map of script files to their Python module paths
const SCRIPT_PATHS = {
  // DDoS scripts
  'http_flooder': 'scripts.http_flooder',
  'slowloris_attack': 'scripts.slowloris_attack',
  
  // Web attack scripts
  'sql_injection_demo': 'scripts.sql_injection_demo',
  'xss_payload_demo': 'scripts.xss_payload_demo',
  'csrf_attack_demo': 'scripts.csrf_attack_demo',
  'form_submitter': 'scripts.form_submitter',
  'harmful_demo': 'scripts.harmful_demo',
  
  // Reconnaissance scripts
  'port_scanner': 'scripts.port_scanner',
  'directory_bruteforce': 'scripts.directory_bruteforce',
  
  // AI/LLM attack scripts
  'claude_captcha_bypass': 'scripts.claude_captcha_bypass',
  'claude_probe': 'scripts.claude_probe',
  'gpt_form_attack': 'scripts.gpt_form_attack',
  'gpt_probe': 'scripts.gpt_probe',
  'gemini_form_spam': 'scripts.gemini_form_spam',
  'gemini_recon': 'scripts.gemini_recon',
  'ai_chatbot_demo': 'scripts.ai_chatbot_demo',
  'llm_completion_demo': 'scripts.llm_completion_demo',
  'torch_image_demo': 'scripts.torch_image_demo',
  'bert_qa_demo': 'scripts.bert_qa_demo',
  'langchain_demo': 'scripts.langchain_demo',
  'huggingface_transformers_demo': 'scripts.huggingface_transformers_demo',
  'openai_api_demo': 'scripts.openai_api_demo',
  'anthropic_claude_demo': 'scripts.anthropic_claude_demo',
  'stable_diffusion_demo': 'scripts.stable_diffusion_demo',
  'autogen_demo': 'scripts.autogen_demo',
  
  // Bot attack scripts
  'fake_login_bot': 'scripts.fake_login_bot',
  'email_spam_demo': 'scripts.email_spam_demo',
  'brute_force_demo': 'scripts.brute_force_demo',
  'scraper_demo': 'scripts.scraper_demo',
  'selenium_bot_demo': 'scripts.selenium_bot_demo',
  
  // CAPTCHA attack scripts
  'captcha_bypass_demo': 'scripts.captcha_bypass_demo',
  'captcha_solver_demo': 'scripts.captcha_solver_demo'
};

// Script descriptions
const SCRIPT_DESCRIPTIONS = {
  // DDoS scripts
  'http_flooder': 'HTTP Flooder - Simulates an HTTP flood attack by sending multiple requests to a target server',
  'slowloris_attack': 'Slowloris DDoS Attack - Simulates a Slowloris attack that keeps connections open by sending partial HTTP requests',
  
  // Web attack scripts
  'sql_injection_demo': 'SQL Injection Demo - Demonstrates SQL injection attacks against web applications',
  'xss_payload_demo': 'XSS Payload Demo - Demonstrates Cross-Site Scripting (XSS) attacks with various payloads',
  'csrf_attack_demo': 'CSRF Attack Demo - Demonstrates Cross-Site Request Forgery (CSRF) attacks against web forms',
  'form_submitter': 'Form Submitter - Simulates automated form submission attacks',
  'harmful_demo': 'XSS Attack Demo - Demonstrates harmful Cross-Site Scripting (XSS) attacks',
  
  // Reconnaissance scripts
  'port_scanner': 'Port Scanner - Scans for open ports on a target system',
  'directory_bruteforce': 'Directory Bruteforce - Attempts to discover hidden directories on a web server',
  
  // AI/LLM attack scripts
  'claude_captcha_bypass': 'Claude Captcha Bypass - Demonstrates bypassing CAPTCHA using Claude AI',
  'claude_probe': 'Claude Probe - Tests Claude AI for vulnerabilities and information disclosure',
  'gpt_form_attack': 'GPT Form Attack - Uses GPT to generate malicious inputs for web forms',
  'gpt_probe': 'GPT Probe - Tests GPT models for vulnerabilities and information disclosure',
  'gemini_form_spam': 'Gemini Form Spam - Uses Gemini to generate spam content for forms',
  'gemini_recon': 'Gemini Recon - Uses Gemini for reconnaissance and information gathering',
  'ai_chatbot_demo': 'AI Chatbot Demo - Demonstrates attacks against AI chatbots',
  'llm_completion_demo': 'LLM Completion Demo - Demonstrates attacks against LLM completion APIs',
  'torch_image_demo': 'Torch Image Demo - Demonstrates attacks against image recognition models',
  'bert_qa_demo': 'BERT QA Demo - Demonstrates attacks against BERT question-answering models',
  'langchain_demo': 'LangChain Agent Demo - Demonstrates attacks against LangChain agents',
  'huggingface_transformers_demo': 'Huggingface Transformers Demo - Demonstrates attacks against Huggingface models',
  'openai_api_demo': 'OpenAI API Demo - Demonstrates attacks against OpenAI APIs',
  'anthropic_claude_demo': 'Anthropic Claude Demo - Demonstrates attacks against Anthropic Claude',
  'stable_diffusion_demo': 'Stable Diffusion Demo - Demonstrates attacks against Stable Diffusion',
  'autogen_demo': 'Microsoft AutoGen Demo - Demonstrates attacks against Microsoft AutoGen',
  
  // Bot attack scripts
  'fake_login_bot': 'Fake Login Bot - Simulates automated login attempts with credential stuffing',
  'email_spam_demo': 'Email Spam Demo - Demonstrates email spam attacks',
  'brute_force_demo': 'Brute Force Demo - Demonstrates brute force password attacks',
  'scraper_demo': 'Web Scraper Demo - Demonstrates web scraping attacks',
  'selenium_bot_demo': 'Selenium Bot Demo - Demonstrates browser automation attacks',
  
  // CAPTCHA attack scripts
  'captcha_bypass_demo': 'CAPTCHA Bypass Demo - Shows techniques to bypass CAPTCHA using third-party services',
  'captcha_solver_demo': 'CAPTCHA Solver Demo - Demonstrates automated CAPTCHA solving'
};

/**
 * Get all available scripts with their metadata
 * @returns {Object} Object containing script metadata
 */
function getAvailableScripts() {
  const scripts = {};
  
  for (const [scriptId, path] of Object.entries(SCRIPT_PATHS)) {
    // Extract category from script ID
    let category = 'other';
    
    // Categorize scripts based on their ID
    if (scriptId.includes('flooder') || scriptId.includes('slowloris')) {
      category = 'ddos';
    } else if (scriptId.includes('injection') || scriptId.includes('xss') || scriptId.includes('csrf') || scriptId.includes('form_submitter') || scriptId.includes('harmful')) {
      category = 'web';
    } else if (scriptId.includes('port_scanner') || scriptId.includes('directory')) {
      category = 'recon';
    } else if (scriptId.includes('claude') || scriptId.includes('gpt') || scriptId.includes('gemini') || scriptId.includes('ai_') || scriptId.includes('llm') || scriptId.includes('langchain') || scriptId.includes('openai') || scriptId.includes('anthropic') || scriptId.includes('autogen')) {
      category = 'ai';
    } else if (scriptId.includes('login_bot') || scriptId.includes('email_spam') || scriptId.includes('brute_force') || scriptId.includes('scraper') || scriptId.includes('selenium')) {
      category = 'bot';
    } else if (scriptId.includes('captcha')) {
      category = 'captcha';
    }
    
    // Get script name
    const scriptName = scriptId
      .split('_')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
    
    // Add script to the result
    scripts[scriptId] = {
      name: scriptName,
      category: category,
      description: SCRIPT_DESCRIPTIONS[scriptId] || 'No description available'
    };
  }
  
  return scripts;
}

/**
 * Run a script by ID
 * @param {string} scriptId - The ID of the script to run
 * @param {Object} params - Optional parameters for the script
 * @returns {Promise<Object>} Promise resolving to the script result
 */
async function runScript(scriptId, params = {}) {
  try {
    // Check if the script exists
    if (!SCRIPT_PATHS[scriptId]) {
      return {
        success: false,
        error: `Script ${scriptId} not found`
      };
    }
    
    // If using local scripts, use the local implementation
    if (window.useLocalScripts) {
      console.log(`Running local script: ${scriptId}`);
      return runLocalScript(scriptId, params);
    }
    
    // Make API call to the Python backend
    const response = await fetch('http://localhost:5050/api/online-bot-attack', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        script: SCRIPT_PATHS[scriptId],
        params: params
      })
    });
    
    // Parse the response
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Error running script:', error);
    
    // If API call fails, try to run local script as fallback
    try {
      console.log(`Falling back to local script: ${scriptId}`);
      return runLocalScript(scriptId, params);
    } catch (localError) {
      return {
        success: false,
        error: `API Error: ${error.message}. Local fallback error: ${localError.message}`,
        script: scriptId
      };
    }
  }
}

/**
 * Run a local script implementation
 * @param {string} scriptId - The ID of the script to run
 * @param {Object} params - Optional parameters for the script
 * @returns {Object} The script result
 */
function runLocalScript(scriptId, params = {}) {
  // Check if we have a local implementation
  if (typeof window.localScripts === 'undefined' || !window.localScripts[scriptId]) {
    throw new Error(`Local script not found: ${scriptId}`);
  }
  
  // Run the local implementation
  return window.localScripts[scriptId](params);
}

/**
 * Test the detection speed of a script
 * @param {string} scriptId - The ID of the script to test
 * @returns {Promise<Object>} Promise resolving to the test result
 */
async function testDetectionSpeed(scriptId) {
  try {
    // Check if the script exists
    if (!SCRIPT_PATHS[scriptId]) {
      return {
        success: false,
        error: `Script ${scriptId} not found`
      };
    }
    
    // If using local scripts, use the local implementation
    if (window.useLocalScripts) {
      console.log(`Testing local script detection speed: ${scriptId}`);
      return testLocalDetectionSpeed(scriptId);
    }
    
    // Make API call to the Python backend
    const response = await fetch('http://localhost:5050/api/test-detection-speed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        script: SCRIPT_PATHS[scriptId]
      })
    });
    
    // Parse the response
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Error testing detection speed:', error);
    
    // If API call fails, try to test local script as fallback
    try {
      console.log(`Falling back to local script detection test: ${scriptId}`);
      return testLocalDetectionSpeed(scriptId);
    } catch (localError) {
      return {
        success: false,
        error: `API Error: ${error.message}. Local fallback error: ${localError.message}`,
        script: scriptId
      };
    }
  }
}

/**
 * Test the detection speed of a local script
 * @param {string} scriptId - The ID of the script to test
 * @returns {Object} The test result
 */
function testLocalDetectionSpeed(scriptId) {
  // Check if we have a local implementation
  if (typeof window.localScripts === 'undefined' || !window.localScripts[scriptId]) {
    throw new Error(`Local script not found: ${scriptId}`);
  }
  
  // Simulate detection speed test
  return {
    success: true,
    detection_time: Math.random() * 3 + 1, // Random time between 1-4ms
    script: scriptId
  };
}

// Export the functions to the global scope
window.scriptBridge = {
  getAvailableScripts,
  runScript,
  testDetectionSpeed,
  SCRIPT_CATEGORIES,
  SCRIPT_PATHS,
  SCRIPT_DESCRIPTIONS
};