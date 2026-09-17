/**
 * Book Navigation & Tooltip System
 * =================================
 * Loads navigation manifest and builds sidebar dynamically.
 * Loads theorem manifest and attaches Tippy.js tooltips to cross-references.
 */

(function () {
    'use strict';

    // ==========================================================================
    // Configuration
    // ==========================================================================

    const TOOLTIP_CONFIG = {
        theme: 'quarto',
        placement: 'top',
        animation: 'shift-away',
        interactive: true,
        allowHTML: true,
        maxWidth: 550,
        delay: [100, 0],
        appendTo: document.body,
    };

    // ==========================================================================
    // Navigation Manifest Loading
    // ==========================================================================

    let navigationData = null;

    /**
     * Get the base path to the root of the HTML output directory (set by the build)
     */
    function getBasePath() {
        const meta = document.querySelector('meta[name="asset-prefix"]');
        return meta ? meta.content : './';
    }

    /**
     * Fetch a site-wide data file. 'no-cache' revalidates with the server (a cheap 304
     * when unchanged), so edits show up without cache-busting every page on each build.
     */
    function fetchData(name) {
        return fetch(getBasePath() + name, { cache: 'no-cache' });
    }

    /**
     * Load the navigation manifest JSON file
     */
    async function loadNavigation() {
        try {
            const response = await fetchData('navigation.json');
            if (response.ok) {
                navigationData = await response.json();
                console.log(`Loaded navigation: ${navigationData.chapters.length} chapters`);
                return true;
            }
        } catch (error) {
            console.warn('Could not load navigation manifest:', error);
        }
        return false;
    }

    /**
     * Determine which page is currently active
     */
    function getCurrentPagePath() {
        const path = window.location.pathname;
        // Extract the relevant part (e.g., "ch01-vector-spaces/07-sums-and-direct-sums.html")
        const match = path.match(/([^/]+\/[^/]+\.html)$/);
        return match ? match[1] : null;
    }

    /**
     * Build the sidebar navigation HTML
     */
    function buildSidebarNav() {
        if (!navigationData) return;

        const sidebarNav = document.querySelector('.sidebar-nav');
        if (!sidebarNav) return;

        const currentPath = getCurrentPagePath();
        const basePath = getBasePath();

        let html = '<ul class="nav-list">';

        // Add Preface link
        const home = navigationData.home || { title: 'Preface', path: 'index.html' };
        html += `<li class="nav-item nav-home">
            <a href="${basePath}${home.path}">${home.title}</a>
        </li>`;
        for (const extra of navigationData.extras || []) {
            const active = currentPagePath() === extra.path ? ' active' : '';
            html += `<li class="nav-item nav-extra${active}">
                <a href="${basePath}${extra.path}"><i class="bi ${extra.icon}" aria-hidden="true"></i> ${extra.title}</a>
            </li>`;
        }

        navigationData.chapters.forEach((chapter, chapterIdx) => {
            const isChapterActive = chapter.sections.some(s => s.path === currentPath);
            const isExpanded = isChapterActive || !chapter.collapsed;

            // Chapter header with title on left (link), toggle arrow on right (button)
            // If chapter has its own index page (chapter.path), title links there. Otherwise, links to first section.
            const firstSection = chapter.sections[0];
            const chapterUrl = chapter.path ? (basePath + chapter.path) : (firstSection ? (basePath + firstSection.path) : '#');

            if (chapter.part) {
                html += `<li class="nav-part">${chapter.part}</li>`;
            }
            html += `
                <li class="nav-chapter${isChapterActive ? ' active' : ''}">
                    <div class="nav-chapter-header" data-chapter="${chapterIdx}">
                        <a href="${chapterUrl}" class="nav-chapter-title-link">
                            <span class="nav-chapter-title">${chapter.title}</span>
                        </a>
                        <span class="nav-toggle ${isExpanded ? 'expanded' : ''}">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="9 18 15 12 9 6"></polyline>
                            </svg>
                        </span>
                    </div>
                    <ul class="nav-sections ${isExpanded ? '' : 'collapsed'}">
            `;

            chapter.sections.forEach(section => {
                const isActive = section.path === currentPath;
                // Avoid duplicating if the chapter title already links to this index page
                // But user might want it in list too. Let's keep all sections in list.
                const sectionPath = basePath + section.path;

                html += `
                    <li class="nav-section-item${isActive ? ' active' : ''}">
                        <a href="${sectionPath}" title="${section.title}">
                            <span class="nav-section-number">${section.number}</span>
                            <span class="nav-section-title">${section.title}</span>
                        </a>
                    </li>
                `;
            });

            html += '</ul></li>';
        });

        html += '</ul>';
        sidebarNav.innerHTML = html;

        // Keep the current section in view in a long sidebar
        const active = sidebarNav.querySelector('.nav-section-item.active');
        const sidebar = document.getElementById('quarto-sidebar');
        if (active && sidebar) {
            const offset = active.getBoundingClientRect().top - sidebar.getBoundingClientRect().top;
            if (offset > sidebar.clientHeight * 0.7) {
                sidebar.scrollTop = offset - sidebar.clientHeight / 3;
            }
        }

        // Add click handlers for chapter expansion (ONLY on toggle arrow)
        setupChapterToggle();
    }

    /**
     * Setup chapter toggle (expand/collapse)
     */
    function setupChapterToggle() {
        document.querySelectorAll('.nav-toggle').forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const header = toggle.closest('.nav-chapter-header');
                const sections = header.nextElementSibling;

                toggle.classList.toggle('expanded');
                sections.classList.toggle('collapsed');
            });
        });
    }

    /**
     * Update the book title in sidebar header
     */
    function updateSidebarHeader() {
        if (!navigationData) return;

        const sidebarTitle = document.querySelector('.sidebar-title');
        if (sidebarTitle && navigationData.title) {
            sidebarTitle.textContent = navigationData.title;
        }
    }

    // ==========================================================================
    // Table of Contents (Right Sidebar)
    // ==========================================================================

    /**
     * Build table of contents from page headings
     */
    function buildTableOfContents() {
        const tocContainer = document.querySelector('.toc');
        if (!tocContainer) return;

        // Find all h2 and h3 headings in the main content
        const content = document.querySelector('.content');
        if (!content) return;

        const headings = content.querySelectorAll('h2, h3');
        if (headings.length === 0) return;

        let html = '<h2>On this page</h2><ul class="toc-list">';

        headings.forEach(heading => {
            const level = heading.tagName.toLowerCase();
            const id = heading.id || heading.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-');
            heading.id = id;  // Ensure heading has an ID

            const indent = level === 'h3' ? ' toc-indent' : '';
            html += `
                <li class="toc-item${indent}">
                    <a href="#${id}">${heading.textContent}</a>
                </li>
            `;
        });

        html += '</ul>';
        tocContainer.innerHTML = html;

        // Setup scroll spy
        setupScrollSpy(headings);
    }

    /**
     * Highlight the current section in the TOC as user scrolls
     */
    function setupScrollSpy(headings) {
        if (headings.length === 0) return;

        const headingArray = Array.from(headings);
        let ticking = false;

        function updateActiveHeading() {
            // Find the heading that is currently at or just above the viewport top
            const scrollY = window.scrollY;
            const offset = 100; // Offset from top to trigger

            let currentHeading = null;

            for (let i = headingArray.length - 1; i >= 0; i--) {
                const heading = headingArray[i];
                const rect = heading.getBoundingClientRect();
                const headingTop = rect.top + scrollY;

                if (headingTop <= scrollY + offset) {
                    currentHeading = heading;
                    break;
                }
            }

            // If no heading is above viewport, use the first one
            if (!currentHeading && headingArray.length > 0) {
                currentHeading = headingArray[0];
            }

            // Update TOC active state
            if (currentHeading) {
                const id = currentHeading.id;
                const tocLink = document.querySelector(`.toc a[href="#${id}"]`);

                // Only update if changed
                const currentActive = document.querySelector('.toc a.active');
                if (tocLink && tocLink !== currentActive) {
                    document.querySelectorAll('.toc a.active').forEach(a => a.classList.remove('active'));
                    tocLink.classList.add('active');
                }
            }

            ticking = false;
        }

        function onScroll() {
            if (!ticking) {
                requestAnimationFrame(updateActiveHeading);
                ticking = true;
            }
        }

        window.addEventListener('scroll', onScroll, { passive: true });

        // Initial update
        updateActiveHeading();
    }

    // ==========================================================================
    // Theorem Manifest & Tooltips
    // ==========================================================================

    // Tooltip data is split into one shard per chapter (theorems/<chapter>.json), fetched
    // the first time a reference into that chapter is hovered.
    const theoremShards = new Map();  // shard name -> Promise of { labelId: info }

    function loadShard(shard) {
        if (!theoremShards.has(shard)) {
            theoremShards.set(shard, fetchData(`theorems/${shard}.json`)
                .then(response => response.ok ? response.json() : {})
                .catch(error => {
                    console.warn(`Could not load theorem data for ${shard}:`, error);
                    return {};
                }));
        }
        return theoremShards.get(shard);
    }

    /**
     * Generate tooltip HTML content for a theorem reference
     */
    function generateTooltipContent(refId, info, goTo) {

        if (!info) {
            return `<div class="tooltip-error">Reference not found: ${refId}</div>`;
        }

        // Build title (title_html keeps math in titles typesettable)
        let title = info.type_name || (info.type.charAt(0).toUpperCase() + info.type.slice(1));
        if (info.number) {
            title += ` ${info.number}`;
        }
        if (info.title_html || info.title) {
            title += ` (${info.title_html || info.title})`;
        }

        const footer = goTo
            ? `<a class="tooltip-go" href="${goTo.href}">Go to ${goTo.label} <i class="bi bi-arrow-right-short" aria-hidden="true"></i></a>`
            : '';
        return `
            <div class="tooltip-theorem ${info.type}">
                <div class="tooltip-title">${title}</div>
                <div class="tooltip-content">${info.html || 'Content not available'}</div>
                ${footer}
            </div>
        `;
    }

    /**
     * Create loading placeholder
     */
    function createLoadingContent() {
        return `
            <div class="tooltip-loading">
                <div class="spinner"></div>
                <span>Loading...</span>
            </div>
        `;
    }

    /**
     * Attach tooltips to all cross-reference links
     */
    function attachTooltips() {
        if (typeof tippy === 'undefined') {
            console.warn('Tippy.js not loaded, skipping tooltips');
            return;
        }

        const xrefLinks = document.querySelectorAll('a.xref[data-ref]');
        // Without hover (phones, tablets) the first tap opens the preview, which has a
        // "Go to" link; with a mouse, hovering previews and clicking follows the link.
        const touch = window.matchMedia('(hover: none)').matches;

        xrefLinks.forEach(link => {
            const refId = link.dataset.ref;
            const shard = link.dataset.shard;
            const goTo = touch ? { href: link.getAttribute('href'), label: link.textContent.trim() } : null;
            if (touch) link.addEventListener('click', event => event.preventDefault());

            tippy(link, {
                ...TOOLTIP_CONFIG,
                ...(touch ? { trigger: 'click', hideOnClick: true, placement: 'bottom', maxWidth: 'calc(100vw - 24px)' } : {}),
                content: createLoadingContent(),
                onShow(instance) {
                    loadShard(shard).then(entries => {
                        instance.setContent(generateTooltipContent(refId, entries[refId], goTo));
                        // Typeset math in the tooltip
                        const tooltipEl = instance.popper.querySelector('.tippy-content');
                        if (tooltipEl && window.MathJax && window.MathJax.typesetPromise) {
                            MathJax.typesetPromise([tooltipEl]).catch(err => {
                                console.warn('MathJax typeset error:', err);
                            });
                        }
                    });
                }
            });
        });

        console.log(`Attached tooltips to ${xrefLinks.length} cross-references`);
    }

    // ==========================================================================
    // Smooth Scrolling for Internal Links
    // ==========================================================================

    function setupSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const targetId = decodeURIComponent(this.getAttribute('href').slice(1));
                const target = document.getElementById(targetId);

                if (target) {
                    e.preventDefault();
                    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                    target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });

                    // Update URL without jumping
                    history.pushState(null, null, `#${targetId}`);
                    markTarget(target);
                }
            });
        });
    }

    // ==========================================================================
    // List of Results: filters
    // ==========================================================================

    function setupResultsFilters() {
        const filters = document.querySelector('.results-filters');
        if (!filters) return;
        const checkboxes = [...filters.querySelectorAll('input[type="checkbox"]')];
        const search = filters.querySelector('.results-search');
        const empty = document.querySelector('.results-empty');

        const apply = () => {
            const groups = new Set(checkboxes.filter(c => c.checked).map(c => c.value));
            const words = search.value.toLowerCase().split(/\s+/).filter(Boolean);
            let shown = 0;
            document.querySelectorAll('.result').forEach(item => {
                const visible = groups.has(item.dataset.group)
                    && words.every(w => item.dataset.search.includes(w));
                item.hidden = !visible;
                if (visible) shown++;
            });
            document.querySelectorAll('.results-section, .results-chapter').forEach(block => {
                block.hidden = !block.querySelector('.result:not([hidden])');
            });
            empty.hidden = shown > 0;
        };
        checkboxes.forEach(c => c.addEventListener('change', apply));
        search.addEventListener('input', apply);
    }

    // ==========================================================================
    // Foldable Proofs and Solutions
    // ==========================================================================

    /**
     * Proofs can be hidden and solutions start hidden, so readers can try an example first.
     * Only outermost blocks fold (a claim's proof inside a proof stays with its proof).
     */
    function setupFolding() {
        const blocks = document.querySelectorAll('.content .proof.small-env, .content .solution.small-env');
        blocks.forEach(block => {
            if (block.parentElement.closest('.proof, .solution')) return;
            const kind = block.classList.contains('solution') ? 'solution' : 'proof';
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'fold-toggle';
            block.classList.add('foldable');
            block.dataset.foldLabel = kind === 'solution' ? 'Solution.' : 'Proof.';
            block.prepend(button);

            const set = folded => {
                block.classList.toggle('is-folded', folded);
                button.setAttribute('aria-expanded', String(!folded));
                button.innerHTML = `<i class="bi bi-chevron-${folded ? 'down' : 'up'}" aria-hidden="true"></i> ${folded ? 'Show' : 'Hide'} ${kind}`;
            };
            button.addEventListener('click', () => set(!block.classList.contains('is-folded')));
            block.addEventListener('unfold', () => set(false));
            set(kind === 'solution');
        });
    }

    /** Open any folded block containing the element. */
    function unfoldAround(element) {
        for (let block = element?.closest('.is-folded'); block; block = block.parentElement?.closest('.is-folded')) {
            block.dispatchEvent(new Event('unfold'));
        }
    }

    // ==========================================================================
    // Reading Progress and Keyboard Navigation
    // ==========================================================================

    function readJson(key, fallback) {
        try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch (e) { return fallback; }
    }

    function currentPagePath() {
        return document.querySelector('meta[name="page-path"]')?.content || '';
    }

    /** Remember visited pages and the last reading position. */
    function trackReading() {
        const path = currentPagePath();
        if (!path) return;
        const visited = new Set(readJson('book-visited', []));
        visited.add(path);
        saveSetting('book-visited', JSON.stringify([...visited]));

        if (path === 'index.html') return;  // the start page is not a reading position
        const title = document.querySelector('.quarto-title h1.title')?.textContent.replace(/\s+/g, ' ').trim() || document.title;
        const headings = [...document.querySelectorAll('.content h2[id], .content h3[id]')];
        let timer;
        const save = () => {
            let heading = null;
            for (const h of headings) {
                if (h.getBoundingClientRect().top < 120) heading = h;
            }
            saveSetting('book-last', JSON.stringify({
                path, title,
                heading: heading ? { id: heading.id, text: heading.textContent.replace(/[#\s]+$/, '').replace(/\s+/g, ' ').trim() } : null,
                time: Date.now(),
            }));
        };
        window.addEventListener('scroll', () => { clearTimeout(timer); timer = setTimeout(save, 400); }, { passive: true });
        // Also when leaving or hiding the page, so a quick scroll-then-close is not lost
        window.addEventListener('pagehide', save);
        document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') save(); });
        save();
    }

    /** Check marks next to visited sections in the sidebar. */
    function markVisitedSections() {
        const visited = new Set(readJson('book-visited', []));
        document.querySelectorAll('.sidebar-nav .nav-section-item').forEach(item => {
            const link = item.querySelector('a');
            const path = link && new URL(link.href).pathname.match(/([^/]+\/[^/]+\.html)$/)?.[1];
            if (path && visited.has(path)) {
                item.classList.add('visited');
                link.setAttribute('title', `${link.getAttribute('title') || ''} (read)`.trim());
            }
        });
    }

    /** On the start page, offer to continue where the reader left off. */
    function showContinueReading() {
        if (currentPagePath() !== 'index.html') return;
        const last = readJson('book-last', null);
        if (!last || !last.path) return;
        const header = document.querySelector('.quarto-title-block');
        if (!header) return;
        const href = getBasePath() + last.path + (last.heading ? `#${last.heading.id}` : '');
        const card = document.createElement('aside');
        card.className = 'continue-reading';
        card.innerHTML = `
            <a class="continue-reading-link" href="${href}">
                <span class="continue-reading-label">Continue reading</span>
                <span class="continue-reading-title"></span>
                <span class="continue-reading-heading"></span>
            </a>
            <button type="button" class="continue-reading-dismiss" aria-label="Dismiss">
                <i class="bi bi-x-lg" aria-hidden="true"></i>
            </button>`;
        card.querySelector('.continue-reading-title').textContent = last.title;
        card.querySelector('.continue-reading-heading').textContent = last.heading ? last.heading.text : '';
        card.querySelector('.continue-reading-dismiss').addEventListener('click', () => {
            saveSetting('book-last', null);
            card.remove();
        });
        header.after(card);
    }

    /** Left and right arrow keys go to the previous and next page. */
    function setupArrowKeys() {
        document.addEventListener('keydown', event => {
            if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
            if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
            const target = event.target;
            if (target.closest('input, textarea, select, [contenteditable="true"], .code-cell, .plot, .widget')) return;
            if (document.body.classList.contains('drawer-open')) return;
            // Leave horizontal scrolling of a focused wide equation alone
            if (target !== document.body && target.scrollWidth > target.clientWidth) return;
            const link = document.querySelector(event.key === 'ArrowLeft'
                ? '.nav-page-previous .pagination-link' : '.nav-page-next .pagination-link');
            if (link) {
                event.preventDefault();
                window.location.href = link.href;
            }
        });
    }

    // ==========================================================================
    // MathJax on Demand
    // ==========================================================================

    /**
     * On pages whose math was rendered at build time, MathJax is loaded only when text that
     * was not rendered needs it (search snippets). Resolves to MathJax, or null.
     */
    let mathjaxLoading = null;
    function ensureMathJax() {
        if (window.MathJax?.typesetPromise) return Promise.resolve(window.MathJax);
        if (mathjaxLoading) return mathjaxLoading;
        const load = src => new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.head.append(script);
        });
        mathjaxLoading = load(getBasePath() + 'mathjax-macros.js').then(() => {
            window.MathJax = {
                tex: {
                    inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']],
                    processEscapes: true, processEnvironments: true, macros: window.BOOK_MACROS || {},
                },
                options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'] },
                startup: { typeset: false },
            };
            return load('https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml-full.js');
        }).then(() => window.MathJax.startup.promise).then(() => window.MathJax).catch(() => null);
        return mathjaxLoading;
    }

    // ==========================================================================
    // Wide Inline Formulas
    // ==========================================================================

    /**
     * MathJax cannot break inline formulas across lines. On narrow screens a long one
     * overflows the column and is clipped; mark those so they scroll sideways instead.
     */
    function setupWideInlineMath() {
        const prerendered = document.querySelector('meta[name="math-prerendered"]');
        if (!prerendered && !window.MathJax) return;
        const update = () => {
            document.querySelectorAll('.content mjx-container:not([display="true"])').forEach(math => {
                math.classList.remove('wide-inline');
                const column = math.closest('li, p, .env, .small-env, .content');
                if (column && math.getBoundingClientRect().width > column.clientWidth) {
                    math.classList.add('wide-inline');
                }
            });
        };
        if (prerendered) {
            // Formulas are already in the page; measure once fonts have loaded
            document.fonts.ready.then(update);
        } else {
            const whenReady = () => MathJax.startup?.promise?.then(update);
            if (MathJax.startup?.promise) whenReady();
            else window.addEventListener('load', whenReady);
        }
        let timer;
        window.addEventListener('resize', () => { clearTimeout(timer); timer = setTimeout(update, 200); });
    }

    // ==========================================================================
    // Link Anchors and Targets
    // ==========================================================================

    /** Briefly highlight the theorem or heading a link led to. */
    function markTarget(element) {
        document.querySelectorAll('.is-target').forEach(el => el.classList.remove('is-target'));
        if (!element) return;
        unfoldAround(element);
        void element.offsetWidth;  // restart the animation when the same target is chosen again
        element.classList.add('is-target');
    }

    function markTargetFromHash() {
        if (location.hash.length > 1) {
            markTarget(document.getElementById(decodeURIComponent(location.hash.slice(1))));
        }
    }

    /**
     * A "#" link after each heading and theorem title. Clicking it goes to the element and
     * copies its address, so a result can be shared or cited.
     */
    function setupAnchorLinks() {
        const content = document.querySelector('.content');
        if (!content) return;
        content.querySelectorAll('h2[id], h3[id], .env[id]').forEach(element => {
            const host = element.classList.contains('env') ? element.querySelector('.theorem-title') : element;
            if (!host) return;
            const link = document.createElement('a');
            link.className = 'anchor-link';
            link.href = `#${element.id}`;
            link.textContent = '#';
            link.setAttribute('aria-label', 'Copy link to this ' + (element.classList.contains('env') ? 'result' : 'section'));
            link.addEventListener('click', () => {
                const url = `${location.origin}${location.pathname}#${element.id}`;
                navigator.clipboard?.writeText(url).then(() => {
                    link.dataset.copied = 'true';
                    setTimeout(() => delete link.dataset.copied, 1500);
                }).catch(() => {});
            });
            host.append(' ', link);
        });
    }

    // ==========================================================================
    // Mobile Menu Toggle
    // ==========================================================================

    /**
     * Toolbar buttons.
     * - Contents: on phones and small tablets the book sidebar is a drawer; on wider screens
     *   the button folds the sidebar away so the text column can widen.
     * - Theme: light / dark. Follows the system until the reader chooses; the choice is saved.
     * - On this page: folds the right-hand pane away.
     * Choices are saved in localStorage and applied before first paint (see template.html).
     */
    const DRAWER_QUERY = window.matchMedia('(max-width: 900px)');

    function saveSetting(key, value) {
        try {
            if (value === null) localStorage.removeItem(key);
            else localStorage.setItem(key, value);
        } catch (e) { /* private mode: the setting lasts for this page only */ }
    }

    function setButtonLabel(button, label) {
        button.setAttribute('aria-label', label);
        button.dataset.tooltip = label;
    }

    function setupLayoutControls() {
        const root = document.documentElement;
        const sidebar = document.getElementById('quarto-sidebar');
        const sidebarButton = document.querySelector('.sidebar-toggle');
        const tocButton = document.querySelector('.toc-toggle');
        const themeButton = document.querySelector('.theme-toggle');

        // --- Book contents: drawer (narrow) or collapsible pane (wide) ---
        if (sidebar && sidebarButton) {
            const overlay = document.createElement('div');
            overlay.className = 'sidebar-overlay';
            document.body.appendChild(overlay);

            const setDrawer = open => {
                sidebar.classList.toggle('show', open);
                overlay.classList.toggle('show', open);
                document.body.classList.toggle('drawer-open', open);
                sidebarButton.setAttribute('aria-expanded', String(open));
                setButtonLabel(sidebarButton, open ? 'Close book contents' : 'Open book contents');
                if (open) {
                    const current = sidebar.querySelector('.nav-section-item.active a') || sidebar.querySelector('a');
                    current?.focus({ preventScroll: true });
                    current?.scrollIntoView({ block: 'center' });
                }
            };
            const setCollapsed = collapsed => {
                if (collapsed) root.dataset.sidebar = 'collapsed';
                else delete root.dataset.sidebar;
                sidebarButton.setAttribute('aria-expanded', String(!collapsed));
                setButtonLabel(sidebarButton, collapsed ? 'Show book contents' : 'Hide book contents');
                saveSetting('book-sidebar', collapsed ? 'collapsed' : null);
            };
            const syncMode = () => {
                if (DRAWER_QUERY.matches) setDrawer(false);
                else {
                    setDrawer(false);
                    setCollapsed(root.dataset.sidebar === 'collapsed');
                }
            };

            sidebarButton.addEventListener('click', () => {
                if (DRAWER_QUERY.matches) setDrawer(!sidebar.classList.contains('show'));
                else setCollapsed(root.dataset.sidebar !== 'collapsed');
            });
            overlay.addEventListener('click', () => setDrawer(false));
            document.addEventListener('keydown', event => {
                if (event.key === 'Escape' && sidebar.classList.contains('show')) {
                    setDrawer(false);
                    sidebarButton.focus();
                }
            });
            sidebar.addEventListener('click', event => {
                if (DRAWER_QUERY.matches && event.target.closest('a')) setDrawer(false);
            });
            DRAWER_QUERY.addEventListener('change', syncMode);
            syncMode();
        }

        // --- On this page ---
        if (tocButton) {
            const setToc = collapsed => {
                if (collapsed) root.dataset.toc = 'collapsed';
                else delete root.dataset.toc;
                tocButton.setAttribute('aria-expanded', String(!collapsed));
                setButtonLabel(tocButton, collapsed ? 'Show “On this page”' : 'Hide “On this page”');
                saveSetting('book-toc', collapsed ? 'collapsed' : null);
            };
            tocButton.addEventListener('click', () => setToc(root.dataset.toc !== 'collapsed'));
            setToc(root.dataset.toc === 'collapsed');
        }

        // --- Theme ---
        if (themeButton) {
            const systemDark = window.matchMedia('(prefers-color-scheme: dark)');
            const applyTheme = theme => {
                root.dataset.theme = theme;
                const dark = theme === 'dark';
                themeButton.setAttribute('aria-pressed', String(dark));
                setButtonLabel(themeButton, dark ? 'Switch to light mode' : 'Switch to dark mode');
            };
            themeButton.addEventListener('click', () => {
                const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
                // Back to "follow the system" when the choice matches the system anyway
                saveSetting('book-theme', next === (systemDark.matches ? 'dark' : 'light') ? null : next);
                applyTheme(next);
            });
            systemDark.addEventListener('change', event => {
                let stored = null;
                try { stored = localStorage.getItem('book-theme'); } catch (e) {}
                if (!stored) applyTheme(event.matches ? 'dark' : 'light');
            });
            applyTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
        }
    }

    // ==========================================================================
    // Search Implementation
    // ==========================================================================

    let searchIndex = null;

    /**
     * Load search index
     */
    async function loadSearchIndex() {
        if (searchIndex) return true;
        
        try {
            const response = await fetchData('search.json');
            if (response.ok) {
                searchIndex = await response.json();
                console.log(`Loaded search index: ${searchIndex.length} entries`);
                return true;
            }
        } catch (error) {
            console.warn('Could not load search index:', error);
        }
        return false;
    }

    function escapeHtml(text) {
        return String(text).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    }

    /** Split text into [{math: bool, text}] at \\( ... \\) and \\[ ... \\] delimiters. */
    function splitMath(text) {
        const parts = [];
        const pattern = /\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g;
        let last = 0, match;
        while ((match = pattern.exec(text))) {
            if (match.index > last) parts.push({ math: false, text: text.slice(last, match.index) });
            parts.push({ math: true, text: match[0] });
            last = pattern.lastIndex;
        }
        if (last < text.length) parts.push({ math: false, text: text.slice(last) });
        return parts;
    }

    /** Escape text and wrap query words in <mark>, outside formulas (MathJax typesets those). */
    function highlight(text, words) {
        return splitMath(text).map(part => {
            if (part.math) return escapeHtml(part.text);
            let html = escapeHtml(part.text);
            for (const word of words) {
                const pattern = new RegExp(escapeHtml(word).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
                html = html.replace(pattern, match => `<mark>${match}</mark>`);
            }
            return html;
        }).join('');
    }

    /** A slice of `text` around `index` that never cuts through a formula. */
    function snippetAround(text, index, before = 50, after = 110) {
        let start = Math.max(0, index - before);
        let end = Math.min(text.length, index + after);
        for (const pattern of [/\\\(([\s\S]*?)\\\)/g, /\\\[([\s\S]*?)\\\]/g]) {
            let match;
            while ((match = pattern.exec(text))) {
                const mStart = match.index, mEnd = pattern.lastIndex;
                if (mStart < start && mEnd > start) start = mStart;
                if (mStart < end && mEnd > end) end = mEnd;
            }
        }
        return (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');
    }

    /**
     * Search pages and results (theorems, definitions, ...). Every word of the query must
     * appear; matches in titles rank above matches in text, and results above pages.
     */
    function search(query) {
        if (!searchIndex || !query) return [];
        const words = query.toLowerCase().split(/\s+/).filter(Boolean);
        const results = [];

        for (const entry of searchIndex) {
            const title = (entry.title || '').toLowerCase();
            const content = (entry.content || '').toLowerCase();
            if (!words.every(w => title.includes(w) || content.includes(w))) continue;

            let score = 0;
            for (const w of words) {
                if (title.includes(w)) score += 10;
                else score += 1;
            }
            if (title.includes(query.toLowerCase())) score += 15;
            if (entry.kind === 'result') score += 2;

            // Snippet around the first word found in the text
            const hit = words.map(w => content.indexOf(w)).filter(i => i >= 0).sort((a, b) => a - b)[0];
            const snippet = snippetAround(entry.content || '', hit === undefined ? 0 : hit, hit === undefined ? 0 : 50);
            results.push({ ...entry, snippet, score });
        }
        return results.sort((a, b) => b.score - a.score).slice(0, 12);
    }

    function setupSearch() {
        const searchInput = document.getElementById('search-input');
        if (!searchInput) return;

        const resultsContainer = document.createElement('div');
        resultsContainer.className = 'search-results';
        resultsContainer.id = 'search-results';
        resultsContainer.setAttribute('role', 'listbox');
        searchInput.parentElement.appendChild(resultsContainer);
        searchInput.setAttribute('aria-controls', 'search-results');

        let debounceTimer;
        let activeIndex = -1;

        const items = () => [...resultsContainer.querySelectorAll('.search-result-item')];
        const close = () => {
            resultsContainer.classList.remove('active');
            activeIndex = -1;
        };
        const setActive = index => {
            const list = items();
            if (!list.length) return;
            activeIndex = (index + list.length) % list.length;
            list.forEach((item, i) => item.classList.toggle('selected', i === activeIndex));
            list[activeIndex].scrollIntoView({ block: 'nearest' });
        };

        searchInput.addEventListener('focus', () => {
            loadSearchIndex();
            if (resultsContainer.childElementCount && searchInput.value.trim().length >= 2) {
                resultsContainer.classList.add('active');
            }
        });

        // "/" focuses search (unless the reader is typing somewhere else)
        document.addEventListener('keydown', event => {
            if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey) return;
            const target = event.target;
            if (target.closest('input, textarea, select, [contenteditable="true"]')) return;
            event.preventDefault();
            const sidebar = document.getElementById('quarto-sidebar');
            if (DRAWER_QUERY.matches && !sidebar?.classList.contains('show')) {
                document.querySelector('.sidebar-toggle')?.click();
            } else if (!DRAWER_QUERY.matches && document.documentElement.dataset.sidebar === 'collapsed') {
                document.querySelector('.sidebar-toggle')?.click();
            }
            searchInput.focus();
        });

        searchInput.addEventListener('keydown', event => {
            if (event.key === 'ArrowDown') { event.preventDefault(); setActive(activeIndex + 1); }
            else if (event.key === 'ArrowUp') { event.preventDefault(); setActive(activeIndex - 1); }
            else if (event.key === 'Enter') {
                const list = items();
                const chosen = list[activeIndex >= 0 ? activeIndex : 0];
                if (chosen) { event.preventDefault(); chosen.click(); }
            } else if (event.key === 'Escape') {
                if (resultsContainer.classList.contains('active')) {
                    event.stopPropagation();
                    close();
                } else {
                    searchInput.blur();
                }
            }
        });

        searchInput.addEventListener('input', event => {
            const query = event.target.value.trim();
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(async () => {
                if (query.length < 2) {
                    close();
                    return;
                }
                await loadSearchIndex();
                const words = query.split(/\s+/).filter(Boolean);
                const results = search(query);
                activeIndex = -1;

                if (results.length) {
                    resultsContainer.innerHTML = results.map(result => `
                        <a class="search-result-item" role="option" href="${escapeHtml(getBasePath() + result.url)}">
                            <span class="search-result-title">${highlight(result.title, words)}</span>
                            ${result.kind === 'result' ? `<span class="search-result-page">${escapeHtml(result.page)}</span>` : ''}
                            <span class="search-result-preview">${highlight(result.snippet, words)}</span>
                        </a>
                    `).join('');
                } else {
                    resultsContainer.innerHTML = `<div class="search-no-results">No results for “${escapeHtml(query)}”</div>`;
                }
                resultsContainer.classList.add('active');
                if (results.length && /\\\(|\\\[/.test(resultsContainer.textContent)) {
                    ensureMathJax().then(mj => {
                        if (!mj) return;
                        mj.typesetClear?.([resultsContainer]);
                        mj.typesetPromise([resultsContainer]).catch(() => {});
                    });
                }
            }, 150);
        });

        document.addEventListener('click', event => {
            if (!searchInput.contains(event.target) && !resultsContainer.contains(event.target)) close();
        });
    }

    // ==========================================================================
    // Initialization
    // ==========================================================================

    async function init() {
        console.log('Initializing book navigation...');

        // Toolbar first, so its buttons work while the navigation data loads
        setupLayoutControls();

        // Load navigation and build sidebar
        const navLoaded = await loadNavigation();
        if (navLoaded) {
            buildSidebarNav();
            updateSidebarHeader();
            markVisitedSections();
        }

        // Reading position, "continue reading" on the start page, arrow-key paging
        trackReading();
        showContinueReading();
        setupArrowKeys();

        // Build table of contents
        buildTableOfContents();

        setupWideInlineMath();

        // Fold solutions (and let readers fold proofs), before anchors are resolved
        setupFolding();
        setupResultsFilters();

        // Link anchors on headings and theorems; highlight the linked element
        setupAnchorLinks();
        markTargetFromHash();
        window.addEventListener('hashchange', markTargetFromHash);

        // Attach tooltips
        attachTooltips();

        // Setup smooth scrolling
        setupSmoothScrolling();


        // Setup search
        setupSearch();

        console.log('Book navigation initialized');
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
