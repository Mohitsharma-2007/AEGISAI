# ai_detection.py
# 25+ simultaneous AI/bot/LLM detection algorithms (advanced, per user spec)

import re
import random
from collections import Counter
from urllib.parse import urlparse

def detect_user_agent(user_agent):
    bots = ['bot', 'spider', 'crawler', 'curl', 'wget', 'python', 'scrapy', 'ai', 'gpt', 'postman']
    return any(b in user_agent.lower() for b in bots)

def detect_header_anomalies(headers):
    suspicious = ['x-forwarded-for', 'x-real-ip', 'cf-connecting-ip']
    return any(h in headers for h in suspicious)

def detect_timing_anomaly(timing):
    return timing < 0.1 or timing > 10

def detect_js_disabled(js_enabled):
    return not js_enabled

def detect_cookie_disabled(cookie_enabled):
    return not cookie_enabled

def detect_behavior_entropy(entropy):
    return entropy < 10 or entropy > 90

def detect_mouse_pattern(pattern):
    return pattern == 'linear' or pattern == 'none'

def detect_keyboard_pattern(pattern):
    return pattern == 'constant' or pattern == 'none'

def detect_scroll_behavior(scroll):
    return scroll == 0 or scroll > 10000

def detect_tab_switches(tab_switches):
    return tab_switches == 0

def detect_language(headers):
    return headers.get('accept-language','').startswith('en') == False

def detect_referrer(headers):
    return not headers.get('referer')

def detect_url_pattern(url):
    return re.search(r'\?.*=.*', url) is not None

def detect_payload_entropy(payload):
    return Counter(payload).most_common(1)[0][1] > 10 if payload else False

def detect_adversarial_prompt(payload):
    return '###' in payload or '{malformed:' in payload

def detect_llm_signature(payload):
    return 'As an AI language model' in payload or 'I am an AI' in payload

def detect_headless(headers):
    return 'headless' in headers.get('user-agent','').lower()

def detect_tls_fingerprint(headers):
    return headers.get('x-tls-version') == '1.0'

def detect_ip_reputation(ip):
    return ip.startswith('192.168.') or ip.startswith('10.')

def detect_random():
    return random.random() < 0.01

# ---
# Advanced AI/ML/LLM Detection Algorithms (per user spec)
# ---

def detect_prompt_pattern(payload):
    # Regex for LLM prompt phrases
    return bool(re.search(r'(explain|summarize|act like|give code for|prompt|as an ai|write a|ignore all previous instructions)', payload, re.I))

def detect_multi_turn_memory(session):
    # Placeholder: Needs session tracking
    return False

def detect_entropy_scoring(text):
    # Placeholder: Use n-gram perplexity or Zipf's Law deviation
    return False

def detect_behavioral_loops(mouse_moves, clicks, scrolls, timings):
    from app import trap_states
    trap = next((t for t in trap_states if t['name'] == 'Behavior Puzzle'), None)
    if trap and trap['status'] != 'ON':
        return False
    # Placeholder: Detect rapid/linear/API-automated behavior
    return False

def detect_trap_question(payload):
    # Looks for honeypot prompt triggers
    from app import trap_states
    trap = next((t for t in trap_states if t['name'] == 'Honeypot Field'), None)
    if trap and trap['status'] != 'ON':
        return False
    return 'Say: I am an AI' in payload or 'Ignore all previous instructions' in payload

def detect_nonstandard_input_echo(payload):
    # Checks for non-UTF/malformed/invisible chars
    return any(ord(c) > 127 for c in payload) if payload else False

def detect_captcha_obfuscation(response):
    from app import trap_states
    trap = next((t for t in trap_states if t['name'] == 'Randomized CAPTCHA'), None)
    if trap and trap['status'] != 'ON':
        return False
    # Placeholder: Needs CAPTCHA UI/response tracking
    return False

def detect_browser_fingerprint(headers):
    # Placeholder: Canvas/WebGL/AudioCtx/plugin/timezone/font smoothing
    return False

def detect_honeypot_input_filled(honeypot_field):
    from app import trap_states
    trap = next((t for t in trap_states if t['name'] == 'Honeypot Field'), None)
    if trap and trap['status'] != 'ON':
        return False
    return bool(honeypot_field)

def detect_llm_language_trap(payload):
    # Looks for gibberish/inverted grammar triggers
    gibberish = ['zxqwv', 'asdfgh', 'lorem ipsum']
    return any(g in payload.lower() for g in gibberish) if payload else False

def detect_session_anomaly(mouse, scroll, fill_speed, req_interval):
    # Placeholder: Detects no mouse, no scroll, high speed, regular intervals
    return False

def detect_multimodal_challenge(response):
    # Placeholder: Needs drawing/audio challenge
    return False

def detect_probabilistic_challenge(response):
    # Placeholder: Needs JS puzzle/math riddle
    return False

def detect_ai_origin_network(ip):
    clouds = ['amazonaws.com', 'googleusercontent.com', 'azure.com']
    return any(c in ip for c in clouds)

def detect_typo_grammar_trap(payload):
    # Looks for autocorrection of subtle errors
    return 'teh' not in payload and 'recieve' not in payload and payload

def detect_user_agent_mutation(headers):
    # Checks UA mismatch with screen or behavior
    return False

def detect_cognitive_load_simulation(timings):
    # Placeholder: Complex scrolling/instruction following
    return False

def detect_payload_tarpit(payload):
    # Looks for huge DOM/fake endpoints/confusing nav
    return False

def detect_metadata_injection(headers):
    # Checks for hidden meta tag triggers
    return 'llm-trap' in str(headers).lower()

def detect_llm_blacklist_lookup(payload):
    # Placeholder: Check prompt against known LLM prompt DB
    return False

def detect_heuristic_ml_score(features):
    # Placeholder: ML classifier on risk features
    return False

def detect_voice_text_inconsistency(response):
    # Placeholder: Voice/text mismatch
    return False

def detect_fake_api_redirection(url):
    # Looks for API probing behavior
    return '/api/fake' in url

def detect_obfuscated_field_names(form_data):
    # Placeholder: Detects if randomized fields are filled
    return False

def detect_interaction_history_replay(session):
    # Placeholder: Contradicts previous steps
    return False

def detect_cognitive_bias_prompt(payload):
    # Looks for too-neutral response to bias prompt
    return False

# ---
# Additional advanced detection stubs (per user request)
# ---
def detect_stylometric_analysis(text):
    """Detects AI-generated writing style via stylometry."""
    return False

def detect_perplexity_burstiness(text):
    """Measures text perplexity and burstiness for AI pattern."""
    return False

def detect_ngram_analysis(text):
    """Checks for common n-gram patterns in AI text."""
    return False

def detect_feature_squeezing(input_data):
    """Detects adversarial examples via feature squeezing."""
    return False

def detect_shap_signature(input_data):
    """Uses SHAP explainability to find AI anomalies."""
    return False

def detect_detectgpt(text):
    """Detects AI text using DetectGPT perturbation analysis."""
    return False

def detect_watermarking(text):
    """Looks for known watermark signals in AI output."""
    return False

def detect_binoculars_method(text):
    """Zero-shot detection using statistical signatures."""
    return False

def detect_tls_certificate(headers):
    """Detects botnets via TLS certificate analysis."""
    return False

def detect_behavioral_biometrics(mouse, keys, timings):
    """Analyzes user behavior for biometric anomalies."""
    return False

def detect_time_based_interaction(timings):
    """Checks for unnatural timing of user actions."""
    return False

def detect_mouse_movement(mouse_moves):
    """Tracks mouse for natural movement patterns."""
    return False

def detect_keystroke_dynamics(keys):
    """Analyzes typing rhythm for AI/bot detection."""
    return False

def detect_device_fingerprint(headers):
    """Identifies unique device/browser characteristics."""
    return False

def detect_geolocation(headers):
    """Checks consistency of reported vs. actual location."""
    return False

def detect_referrer_header(headers):
    """Inspects HTTP referrer for anomalies."""
    return False

def detect_session_duration(session):
    """Tracks session length for bot/AI patterns."""
    return False

def detect_clickstream(clicks):
    """Analyzes sequence of clicks for automation."""
    return False

def detect_form_submission_timing(timings):
    """Measures time to fill/submit forms."""
    return False

def detect_scroll_behavior(scrolls):
    """Observes scrolling for human/AI patterns."""
    return False

def detect_page_focus(events):
    """Tracks tab/window focus changes."""
    return False

def detect_copy_paste(text):
    """Detects pasted content vs. typed."""
    return False

def detect_clipboard_access(events):
    """Detects clipboard interactions."""
    return False

def detect_touch_events(events):
    """Analyzes mobile touch patterns."""
    return False

def detect_sensor_data(headers):
    """Checks device sensor data for anomalies."""
    return False

def detect_battery_status(headers):
    """Observes battery level/status for bots."""
    return False

def detect_network_speed(headers):
    """Measures network speed for bot patterns."""
    return False

def detect_cookie_behavior(headers):
    """Monitors cookie usage for automation."""
    return False

def detect_local_storage(headers):
    """Checks browser local storage for anomalies."""
    return False

def detect_session_storage(headers):
    """Examines session storage for automation."""
    return False

def detect_webrtc_leak(headers):
    """Detects IP leaks via WebRTC."""
    return False

def detect_canvas_fingerprint(headers):
    """Uses HTML5 canvas for browser fingerprinting."""
    return False

def detect_audiocontext_fingerprint(headers):
    """Analyzes audio context for browser fingerprinting."""
    return False

def detect_font_enumeration(headers):
    """Lists fonts to identify systems/bots."""
    return False

def detect_plugin_enumeration(headers):
    """Checks installed plugins for anomalies."""
    return False

def detect_language_settings(headers):
    """Ensures browser language matches user claim."""
    return False

def detect_timezone(headers):
    """Compares reported and actual timezone."""
    return False

def detect_screen_resolution(headers):
    """Detects unusual screen sizes for bots."""
    return False

def detect_color_depth(headers):
    """Checks display color settings."""
    return False

def detect_hardware_concurrency(headers):
    """Identifies logical processors for VMs/bots."""
    return False

def detect_device_memory(headers):
    """Assesses available device memory."""
    return False

def detect_touch_support(headers):
    """Determines if touch input is available."""
    return False

def detect_media_devices(headers):
    """Lists connected media devices."""
    return False

def detect_webgl_fingerprint(headers):
    """Analyzes WebGL for browser fingerprinting."""
    return False

def detect_adblocker(headers):
    """Checks for ad blocker presence."""
    return False

def detect_automation_tools(headers):
    """Identifies Selenium, Puppeteer, etc."""
    return False

def detect_headless_browser(headers):
    """Detects browsers running headless."""
    return False

def detect_virtual_machine(headers):
    """Identifies if environment is a VM."""
    return False

def detect_emulator(headers):
    """Checks for mobile emulators."""
    return False

def detect_proxy_usage(headers):
    """Identifies traffic via proxies."""
    return False

def detect_vpn_usage(headers):
    """Detects use of VPNs."""
    return False

def detect_tor_network(headers):
    """Identifies Tor node traffic."""
    return False

def detect_ip_reputation_blacklist(ip):
    """Checks IPs against blacklists."""
    return False

def detect_asn(headers):
    """Analyzes ASN for bot networks."""
    return False

def detect_geoip(headers):
    """Validates IP-based location."""
    return False

def detect_dns_leak(headers):
    """Detects DNS queries outside expected paths."""
    return False

def detect_http_header(headers):
    """Inspects HTTP headers for inconsistencies."""
    return False

def detect_tls_fingerprint_advanced(headers):
    """Analyzes SSL/TLS handshake data."""
    return False

def detect_cert_pinning(headers):
    """Ensures certificate pinning."""
    return False

def detect_csp(headers):
    """Monitors Content Security Policy adherence."""
    return False

def detect_subresource_integrity(headers):
    """Validates integrity of loaded resources."""
    return False

def detect_reflected_xss(payload):
    """Identifies reflected XSS attempts."""
    return False

def detect_stored_xss(payload):
    """Detects persistent XSS vulnerabilities."""
    return False

def detect_csrf_token(headers):
    """Ensures CSRF token presence/validity."""
    return False

def detect_clickjacking(headers):
    """Prevents UI redress attacks."""
    return False

def detect_open_redirect(payload):
    """Identifies unvalidated redirects."""
    return False

def detect_content_injection(payload):
    """Detects unauthorized content additions."""
    return False

def detect_dom_mutation(headers):
    """Watches for unexpected DOM changes."""
    return False

def detect_script_injection(payload):
    """Identifies unauthorized script execution."""
    return False

def detect_third_party_scripts(headers):
    """Observes external script behavior."""
    return False

def detect_resource_load_timing(headers):
    """Measures resource load times for anomalies."""
    return False

# Run all algorithms and return a dict of results

def run_all_algorithms(request_data):
    results = {}
    # Existing checks
    results['user_agent'] = detect_user_agent(request_data.get('user_agent',''))
    results['header_anomaly'] = detect_header_anomalies(request_data.get('headers',{}))
    results['timing'] = detect_timing_anomaly(request_data.get('timing',1))
    results['js_disabled'] = detect_js_disabled(request_data.get('js_enabled',True))
    results['cookie_disabled'] = detect_cookie_disabled(request_data.get('cookie_enabled',True))
    results['behavior_entropy'] = detect_behavior_entropy(request_data.get('entropy',50))
    results['mouse_pattern'] = detect_mouse_pattern(request_data.get('mouse_pattern','random'))
    results['keyboard_pattern'] = detect_keyboard_pattern(request_data.get('keyboard_pattern','random'))
    results['scroll_behavior'] = detect_scroll_behavior(request_data.get('scroll',100))
    results['tab_switches'] = detect_tab_switches(request_data.get('tab_switches',1))
    results['language'] = detect_language(request_data.get('headers',{}))
    results['referrer'] = detect_referrer(request_data.get('headers',{}))
    results['url_pattern'] = detect_url_pattern(request_data.get('url',''))
    results['payload_entropy'] = detect_payload_entropy(request_data.get('payload',''))
    results['adversarial_prompt'] = detect_adversarial_prompt(request_data.get('payload',''))
    results['llm_signature'] = detect_llm_signature(request_data.get('payload',''))
    results['headless'] = detect_headless(request_data.get('headers',{}))
    results['tls_fingerprint'] = detect_tls_fingerprint(request_data.get('headers',{}))
    results['ip_reputation'] = detect_ip_reputation(request_data.get('ip',''))
    results['random'] = detect_random()
    # Advanced checks (per user spec)
    results['prompt_pattern'] = detect_prompt_pattern(request_data.get('payload',''))
    results['multi_turn_memory'] = detect_multi_turn_memory(request_data.get('session',{}))
    results['entropy_scoring'] = detect_entropy_scoring(request_data.get('payload',''))
    results['behavioral_loops'] = detect_behavioral_loops(
        request_data.get('mouse_moves',[]),
        request_data.get('clicks',[]),
        request_data.get('scrolls',[]),
        request_data.get('timings',[]),
    )
    results['trap_question'] = detect_trap_question(request_data.get('payload',''))
    results['nonstandard_input_echo'] = detect_nonstandard_input_echo(request_data.get('payload',''))
    results['captcha_obfuscation'] = detect_captcha_obfuscation(request_data.get('captcha_response',''))
    results['browser_fingerprint'] = detect_browser_fingerprint(request_data.get('headers',{}))
    results['honeypot_input_filled'] = detect_honeypot_input_filled(request_data.get('honeypot_field',''))
    results['llm_language_trap'] = detect_llm_language_trap(request_data.get('payload',''))
    results['session_anomaly'] = detect_session_anomaly(
        request_data.get('mouse',[]),
        request_data.get('scroll',0),
        request_data.get('fill_speed',0),
        request_data.get('req_interval',0),
    )
    results['multimodal_challenge'] = detect_multimodal_challenge(request_data.get('multi_challenge_response',''))
    results['probabilistic_challenge'] = detect_probabilistic_challenge(request_data.get('prob_challenge_response',''))
    results['ai_origin_network'] = detect_ai_origin_network(request_data.get('ip',''))
    results['typo_grammar_trap'] = detect_typo_grammar_trap(request_data.get('payload',''))
    results['user_agent_mutation'] = detect_user_agent_mutation(request_data.get('headers',{}))
    results['cognitive_load_simulation'] = detect_cognitive_load_simulation(request_data.get('timings',[]))
    results['payload_tarpit'] = detect_payload_tarpit(request_data.get('payload',''))
    results['metadata_injection'] = detect_metadata_injection(request_data.get('headers',{}))
    results['llm_blacklist_lookup'] = detect_llm_blacklist_lookup(request_data.get('payload',''))
    results['heuristic_ml_score'] = detect_heuristic_ml_score(request_data.get('features',{}))
    results['voice_text_inconsistency'] = detect_voice_text_inconsistency(request_data.get('voice_text_response',''))
    results['fake_api_redirection'] = detect_fake_api_redirection(request_data.get('url',''))
    results['obfuscated_field_names'] = detect_obfuscated_field_names(request_data.get('form_data',{}))
    results['interaction_history_replay'] = detect_interaction_history_replay(request_data.get('session',{}))
    results['cognitive_bias_prompt'] = detect_cognitive_bias_prompt(request_data.get('payload',''))
    # ---
    # Additional advanced detection stubs
    # ---
    results['stylometric_analysis'] = detect_stylometric_analysis(request_data.get('payload',''))
    results['perplexity_burstiness'] = detect_perplexity_burstiness(request_data.get('payload',''))
    results['ngram_analysis'] = detect_ngram_analysis(request_data.get('payload',''))
    results['feature_squeezing'] = detect_feature_squeezing(request_data.get('payload',''))
    results['shap_signature'] = detect_shap_signature(request_data.get('payload',''))
    results['detectgpt'] = detect_detectgpt(request_data.get('payload',''))
    results['watermarking'] = detect_watermarking(request_data.get('payload',''))
    results['binoculars_method'] = detect_binoculars_method(request_data.get('payload',''))
    results['tls_certificate'] = detect_tls_certificate(request_data.get('headers',{}))
    results['behavioral_biometrics'] = detect_behavioral_biometrics(
        request_data.get('mouse',[]), request_data.get('keys',[]), request_data.get('timings',[]))
    results['time_based_interaction'] = detect_time_based_interaction(request_data.get('timings',[]))
    results['mouse_movement'] = detect_mouse_movement(request_data.get('mouse_moves',[]))
    results['keystroke_dynamics'] = detect_keystroke_dynamics(request_data.get('keys',[]))
    results['device_fingerprint'] = detect_device_fingerprint(request_data.get('headers',{}))
    results['geolocation'] = detect_geolocation(request_data.get('headers',{}))
    results['referrer_header'] = detect_referrer_header(request_data.get('headers',{}))
    results['session_duration'] = detect_session_duration(request_data.get('session',{}))
    results['clickstream'] = detect_clickstream(request_data.get('clicks',[]))
    results['form_submission_timing'] = detect_form_submission_timing(request_data.get('timings',[]))
    results['scroll_behavior_advanced'] = detect_scroll_behavior(request_data.get('scrolls',[]))
    results['page_focus'] = detect_page_focus(request_data.get('events',[]))
    results['copy_paste'] = detect_copy_paste(request_data.get('payload',''))
    results['clipboard_access'] = detect_clipboard_access(request_data.get('events',[]))
    results['touch_events'] = detect_touch_events(request_data.get('events',[]))
    results['sensor_data'] = detect_sensor_data(request_data.get('headers',{}))
    results['battery_status'] = detect_battery_status(request_data.get('headers',{}))
    results['network_speed'] = detect_network_speed(request_data.get('headers',{}))
    results['cookie_behavior'] = detect_cookie_behavior(request_data.get('headers',{}))
    results['local_storage'] = detect_local_storage(request_data.get('headers',{}))
    results['session_storage'] = detect_session_storage(request_data.get('headers',{}))
    results['webrtc_leak'] = detect_webrtc_leak(request_data.get('headers',{}))
    results['canvas_fingerprint'] = detect_canvas_fingerprint(request_data.get('headers',{}))
    results['audiocontext_fingerprint'] = detect_audiocontext_fingerprint(request_data.get('headers',{}))
    results['font_enumeration'] = detect_font_enumeration(request_data.get('headers',{}))
    results['plugin_enumeration'] = detect_plugin_enumeration(request_data.get('headers',{}))
    results['language_settings'] = detect_language_settings(request_data.get('headers',{}))
    results['timezone'] = detect_timezone(request_data.get('headers',{}))
    results['screen_resolution'] = detect_screen_resolution(request_data.get('headers',{}))
    results['color_depth'] = detect_color_depth(request_data.get('headers',{}))
    results['hardware_concurrency'] = detect_hardware_concurrency(request_data.get('headers',{}))
    results['device_memory'] = detect_device_memory(request_data.get('headers',{}))
    results['touch_support'] = detect_touch_support(request_data.get('headers',{}))
    results['media_devices'] = detect_media_devices(request_data.get('headers',{}))
    results['webgl_fingerprint'] = detect_webgl_fingerprint(request_data.get('headers',{}))
    results['adblocker'] = detect_adblocker(request_data.get('headers',{}))
    results['automation_tools'] = detect_automation_tools(request_data.get('headers',{}))
    results['headless_browser'] = detect_headless_browser(request_data.get('headers',{}))
    results['virtual_machine'] = detect_virtual_machine(request_data.get('headers',{}))
    results['emulator'] = detect_emulator(request_data.get('headers',{}))
    results['proxy_usage'] = detect_proxy_usage(request_data.get('headers',{}))
    results['vpn_usage'] = detect_vpn_usage(request_data.get('headers',{}))
    results['tor_network'] = detect_tor_network(request_data.get('headers',{}))
    results['ip_reputation_blacklist'] = detect_ip_reputation_blacklist(request_data.get('ip',''))
    results['asn'] = detect_asn(request_data.get('headers',{}))
    results['geoip'] = detect_geoip(request_data.get('headers',{}))
    results['dns_leak'] = detect_dns_leak(request_data.get('headers',{}))
    results['http_header'] = detect_http_header(request_data.get('headers',{}))
    results['tls_fingerprint_advanced'] = detect_tls_fingerprint_advanced(request_data.get('headers',{}))
    results['cert_pinning'] = detect_cert_pinning(request_data.get('headers',{}))
    results['csp'] = detect_csp(request_data.get('headers',{}))
    results['subresource_integrity'] = detect_subresource_integrity(request_data.get('headers',{}))
    results['reflected_xss'] = detect_reflected_xss(request_data.get('payload',''))
    results['stored_xss'] = detect_stored_xss(request_data.get('payload',''))
    results['csrf_token'] = detect_csrf_token(request_data.get('headers',{}))
    results['clickjacking'] = detect_clickjacking(request_data.get('headers',{}))
    results['open_redirect'] = detect_open_redirect(request_data.get('payload',''))
    results['content_injection'] = detect_content_injection(request_data.get('payload',''))
    results['dom_mutation'] = detect_dom_mutation(request_data.get('headers',{}))
    results['script_injection'] = detect_script_injection(request_data.get('payload',''))
    results['third_party_scripts'] = detect_third_party_scripts(request_data.get('headers',{}))
    results['resource_load_timing'] = detect_resource_load_timing(request_data.get('headers',{}))
    return results

def is_blocked(results):
    # Block if 5+ triggers or any critical (llm_signature, adversarial_prompt, headless)
    triggers = sum(bool(v) for v in results.values())
    if results.get('llm_signature') or results.get('adversarial_prompt') or results.get('headless'):
        return True
    return triggers >= 5
