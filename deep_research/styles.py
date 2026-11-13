EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<div class="dr-brand">
    <div class="dr-mark">
        <span class="dr-bar dr-bar-1"></span>
        <span class="dr-bar dr-bar-2"></span>
        <span class="dr-bar dr-bar-3"></span>
    </div>
    <div class="dr-titles">
        <h1>Deep<span class="dr-sep">/</span>Research</h1>
        <p>Multi-search web investigation</p>
    </div>
</div>
"""

# Gradio omits the app stylesheet before authentication. Include these scoped
# styles in auth_message so the native login form can share the app's identity.
LOGIN_CSS = """
body:has(#dr-login-brand) {
    --dr-bg: #fafaf7;
    --dr-surface: #ffffff;
    --dr-line: #0c0c0d;
    --dr-line-soft: #e1e1da;
    --dr-text: #0c0c0d;
    --dr-muted: #6f6f72;
    --dr-amber: #ecad0a;
    --dr-blue: #209dd7;
    --dr-purple: #753991;
    background: var(--dr-bg) !important;
}

body:has(.dark #dr-login-brand),
body.dark:has(#dr-login-brand),
html.dark body:has(#dr-login-brand) {
    --dr-bg: #0b0b0c;
    --dr-surface: #161618;
    --dr-line: #f1f1ec;
    --dr-line-soft: #2a2a2d;
    --dr-text: #f1f1ec;
    --dr-muted: #8a8a8e;
}

.gradio-container:has(#dr-login-brand) {
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important;
}

.wrap:has(#dr-login-brand) {
    box-sizing: border-box;
    min-height: 100svh !important;
    margin: 0 !important;
    padding: 2rem 1.25rem !important;
    background: var(--dr-bg) !important;
}

/* The panel is the native login wrapper; keep its form and handlers intact. */
.wrap:has(#dr-login-brand) > div {
    box-sizing: border-box !important;
    width: 100% !important;
    max-width: 440px !important;
    min-width: 0 !important;
    padding: 2rem !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    background: var(--dr-surface) !important;
    box-shadow: 8px 8px 0 var(--dr-line-soft) !important;
    gap: 1.25rem !important;
}

.wrap:has(#dr-login-brand) h2 { display: none; }
.wrap:has(#dr-login-brand) .auth { margin: 0 !important; }

#dr-login-brand {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding-bottom: 1.25rem;
    border-bottom: 3px solid var(--dr-line);
    color: var(--dr-text);
    font-size: clamp(1.4rem, 6vw, 1.9rem);
    font-weight: 900;
    letter-spacing: -0.045em;
    line-height: 1;
    text-transform: uppercase;
    white-space: nowrap;
}

.dr-login-mark { display: flex; flex-direction: column; gap: 4px; width: 30px; flex-shrink: 0; }
.dr-login-mark span { display: block; height: 6px; }
.dr-login-mark span:nth-child(1) { background: var(--dr-amber); width: 100%; }
.dr-login-mark span:nth-child(2) { background: var(--dr-blue); width: 70%; }
.dr-login-mark span:nth-child(3) { background: var(--dr-purple); width: 45%; }
.dr-login-sep { color: var(--dr-amber); font-weight: 300; margin: 0 0.04em; }
.dr-login-caption {
    display: block;
    margin-top: 1rem;
    color: var(--dr-muted);
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.wrap:has(#dr-login-brand) .form {
    gap: 1.25rem !important;
    padding: 0 !important;
    border: 0 !important;
    border-radius: 0 !important;
    background: transparent !important;
}
.wrap:has(#dr-login-brand) .form .block {
    padding: 0 !important;
    border: 0 !important;
    border-radius: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
}
.wrap:has(#dr-login-brand) label > span {
    color: var(--dr-muted) !important;
    font-family: ui-monospace, SFMono-Regular, monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.wrap:has(#dr-login-brand) input,
.wrap:has(#dr-login-brand) textarea {
    box-sizing: border-box !important;
    width: 100% !important;
    min-height: 52px !important;
    padding: 0.85rem 1rem !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    background: var(--dr-surface) !important;
    color: var(--dr-text) !important;
    font-family: inherit !important;
    font-size: 1rem !important;
    box-shadow: none !important;
}
.wrap:has(#dr-login-brand) input:focus,
.wrap:has(#dr-login-brand) textarea:focus {
    outline: none !important;
    border-color: var(--dr-blue) !important;
    box-shadow: 4px 4px 0 var(--dr-blue) !important;
}
.wrap:has(#dr-login-brand) button.primary {
    width: 100% !important;
    min-height: 52px !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    background: var(--dr-amber) !important;
    color: #0c0c0d !important;
    font-weight: 800 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    transition: background 0.15s, color 0.15s;
}
.wrap:has(#dr-login-brand) button.primary:hover {
    background: var(--dr-purple) !important;
    color: #ffffff !important;
}
.wrap:has(#dr-login-brand) button:focus-visible {
    outline: 3px solid var(--dr-blue) !important;
    outline-offset: 3px;
}
.wrap:has(#dr-login-brand) .creds {
    color: #c43c30 !important;
    font-size: 0.9rem;
    margin: 0 !important;
}
body:has(.dark #dr-login-brand) .creds { color: #ff9086 !important; }

@media (max-width: 480px) {
    .wrap:has(#dr-login-brand) { padding: 1.25rem !important; }
    .wrap:has(#dr-login-brand) > div { padding: 1.5rem 1rem !important; }
    #dr-login-brand { gap: 0.75rem; }
}
"""

LOGIN_HTML = f"""
<style>{LOGIN_CSS}</style>
<span id="dr-login-brand" role="heading" aria-level="1">
    <span class="dr-login-mark" aria-hidden="true"><span></span><span></span><span></span></span>
    <span>Deep<span class="dr-login-sep">/</span>Research</span>
</span>
<span class="dr-login-caption">Sign in to continue</span>
"""

CSS = """
.gradio-container {
    --dr-bg: #fafaf7;
    --dr-surface: #ffffff;
    --dr-line: #0c0c0d;
    --dr-line-soft: #e1e1da;
    --dr-text: #0c0c0d;
    --dr-muted: #6f6f72;
    --dr-amber: #ecad0a;
    --dr-blue: #209dd7;
    --dr-purple: #753991;

    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 4rem !important;
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important;
}

.gradio-container.dark,
.dark .gradio-container,
body.dark .gradio-container,
html.dark .gradio-container {
    --dr-bg: #0b0b0c;
    --dr-surface: #161618;
    --dr-line: #f1f1ec;
    --dr-line-soft: #2a2a2d;
    --dr-text: #f1f1ec;
    --dr-muted: #8a8a8e;
}

body { background: var(--dr-bg, #fafaf7); }

/* === HEADER === */
.dr-brand {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 1.4rem;
    padding-bottom: 1.25rem;
    border-bottom: 3px solid var(--dr-line);
    margin-bottom: 2.5rem;
}

.dr-mark {
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 38px;
}

.dr-bar { height: 7px; display: block; }
.dr-bar-1 { background: var(--dr-amber);  width: 100%; }
.dr-bar-2 { background: var(--dr-blue);   width: 70%;  }
.dr-bar-3 { background: var(--dr-purple); width: 45%;  }

.dr-titles h1 {
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    font-weight: 900;
    letter-spacing: -0.045em;
    margin: 0;
    line-height: 0.95;
    text-transform: uppercase;
    color: var(--dr-text);
}

.dr-sep {
    color: var(--dr-amber);
    font-weight: 300;
    margin: 0 0.04em;
}

.dr-titles p {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    font-size: 0.7rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0.55rem 0 0;
    color: var(--dr-muted);
}

/* === QUERY ROW === */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: var(--dr-surface) !important;
    color: var(--dr-text) !important;
    border: 2px solid var(--dr-line) !important;
    border-radius: 0 !important;
    padding: 1.05rem 1.2rem !important;
    font-size: 1.05rem !important;
    font-family: inherit !important;
    box-shadow: none !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: var(--dr-blue) !important;
    box-shadow: 6px 6px 0 0 var(--dr-blue) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 1 !important;
}

#dr-run {
    background: var(--dr-amber) !important;
    color: #0c0c0d !important;
    border: 2px solid var(--dr-line) !important;
    border-left: none !important;
    border-radius: 0 !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    font-size: 0.85rem !important;
    box-shadow: none !important;
    transition: background 0.15s, color 0.15s, transform 0.08s !important;
    min-width: 150px !important;
    padding: 1rem 1.5rem !important;
}

#dr-run:hover {
    background: var(--dr-purple) !important;
    color: #ffffff !important;
}

#dr-run:active { transform: translate(2px, 2px) !important; }

/* === EXAMPLES === */
.dr-examples-label {
    font-family: ui-monospace, SFMono-Regular, monospace;
    font-size: 0.65rem;
    letter-spacing: 0.28em;
    color: var(--dr-muted);
    text-transform: uppercase;
    margin: 2rem 0 0.85rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-line-soft);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }

#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: var(--dr-surface) !important;
    border: 1.5px solid var(--dr-line-soft) !important;
    padding: 0.7rem 1.05rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s, color 0.15s, transform 0.1s !important;
    font-size: 0.9rem !important;
    color: var(--dr-text) !important;
    border-radius: 0 !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: none !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    border-color: var(--dr-purple) !important;
    color: var(--dr-purple) !important;
    transform: translateY(-1px);
}

/* === REPORT === */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--dr-text) !important;
    min-height: 40px;
}

#dr-report > div, #dr-report .prose {
    background: transparent !important;
    color: var(--dr-text) !important;
}

#dr-report:not(:empty) {
    border-top: 1px solid var(--dr-line-soft) !important;
    padding-top: 1.75rem !important;
}

#dr-report h1 {
    font-size: 1.85rem;
    font-weight: 900;
    color: var(--dr-blue);
    border-bottom: 2px solid var(--dr-line);
    padding-bottom: 0.45rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.025em;
}

#dr-report h2 {
    font-size: 1.35rem;
    color: var(--dr-purple);
    font-weight: 800;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}

#dr-report h3 {
    font-size: 1.1rem;
    color: var(--dr-text);
    font-weight: 800;
    margin-top: 1.5rem;
}

#dr-report p { line-height: 1.7; }

#dr-report a {
    color: var(--dr-blue);
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 3px;
}

#dr-report a:hover { color: var(--dr-amber); }

#dr-report code {
    background: var(--dr-surface);
    border: 1px solid var(--dr-line-soft);
    padding: 0.1rem 0.4rem;
    font-size: 0.92em;
    border-radius: 0;
}

#dr-report pre {
    background: var(--dr-surface);
    border: 1.5px solid var(--dr-line-soft);
    border-radius: 0;
    padding: 1rem 1.25rem;
}

#dr-report blockquote {
    border-left: none !important;
    background: var(--dr-surface);
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    color: var(--dr-text);
}

#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.3rem 0; line-height: 1.6; }

#dr-report table {
    border-collapse: collapse;
    border: 1.5px solid var(--dr-line);
}

#dr-report th, #dr-report td {
    border: 1px solid var(--dr-line-soft);
    padding: 0.5rem 0.85rem;
    text-align: left;
}

#dr-report th {
    background: var(--dr-surface);
    font-weight: 800;
    color: var(--dr-blue);
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-query-row { flex-direction: column !important; }
    #dr-run {
        border-left: 2px solid var(--dr-line) !important;
        border-top: none !important;
        width: 100% !important;
    }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focus()) {
        let tries = 0;
        const i = setInterval(() => {
            if (focus() || ++tries > 20) clearInterval(i);
        }, 100);
    }
}
"""
