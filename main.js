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
     * URL of a site-wide data file. The build version changes when the book is rebuilt
     * from different inputs, so browsers can cache these files between deployments.
     */
    function dataUrl(name) {
        const meta = document.querySelector('meta[name="build-version"]');
        const version = meta && meta.content ? '?v=' + meta.content : '';
        return getBasePath() + name + version;
    }

    /**
     * Load the navigation manifest JSON file
     */
    async function loadNavigation() {
        try {
            const response = await fetch(dataUrl('navigation.json'));
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
        html += `<li class="nav-item nav-home">
            <a href="${basePath}index.html">Preface</a>
        </li>`;

        navigationData.chapters.forEach((chapter, chapterIdx) => {
            const isChapterActive = chapter.sections.some(s => s.path === currentPath);
            const isExpanded = isChapterActive || !chapter.collapsed;

            // Chapter header with title on left (link), toggle arrow on right (button)
            // If chapter has its own index page (chapter.path), title links there. Otherwise, links to first section.
            const firstSection = chapter.sections[0];
            const chapterUrl = chapter.path ? (basePath + chapter.path) : (firstSection ? (basePath + firstSection.path) : '#');

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

        let html = '<h2>Table of contents</h2><ul class="toc-list">';

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

    let theoremManifest = {};
    let manifestLoaded = false;

    /**
     * Load the theorem manifest JSON file
     */
    async function loadManifest() {
        try {
            const response = await fetch(dataUrl('theorems.json'));
            if (response.ok) {
                theoremManifest = await response.json();
                manifestLoaded = true;
                console.log(`Loaded ${Object.keys(theoremManifest).length} theorem definitions`);
            }
        } catch (error) {
            console.warn('Could not load theorem manifest:', error);
        }
    }

    /**
     * Generate tooltip HTML content for a theorem reference
     */
    function generateTooltipContent(refId) {
        const info = theoremManifest[refId];

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

        return `
            <div class="tooltip-theorem ${info.type}">
                <div class="tooltip-title">${title}</div>
                <div class="tooltip-content">${info.html || 'Content not available'}</div>
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

        xrefLinks.forEach(link => {
            const refId = link.dataset.ref;

            tippy(link, {
                ...TOOLTIP_CONFIG,
                content: createLoadingContent(),
                onShow(instance) {
                    // Update content when tooltip is shown
                    if (manifestLoaded) {
                        instance.setContent(generateTooltipContent(refId));
                        // Trigger MathJax to process the tooltip content
                        if (window.MathJax && window.MathJax.typesetPromise) {
                            const tooltipEl = instance.popper.querySelector('.tippy-content');
                            if (tooltipEl) {
                                MathJax.typesetPromise([tooltipEl]).catch(err => {
                                    console.warn('MathJax typeset error:', err);
                                });
                            }
                        }
                    } else {
                        // Manifest not loaded yet, try to load
                        loadManifest().then(() => {
                            instance.setContent(generateTooltipContent(refId));
                        });
                    }
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
                const targetId = this.getAttribute('href').slice(1);
                const target = document.getElementById(targetId);

                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });

                    // Update URL without jumping
                    history.pushState(null, null, `#${targetId}`);
                }
            });
        });
    }

    // ==========================================================================
    // Mobile Menu Toggle
    // ==========================================================================

    function setupMobileMenu() {
        // Add mobile menu button if it doesn't exist
        const sidebar = document.getElementById('quarto-sidebar');
        if (!sidebar) return;

        // Create overlay
        const overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);

        // Toggle on overlay click
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('show');
            overlay.classList.remove('show');
        });
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
            const response = await fetch(dataUrl('search.json'));
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

    /**
     * Perform search
     */
    function search(query) {
        if (!searchIndex || !query) return [];
        
        const normalizedQuery = query.toLowerCase();
        const results = [];
        
        for (const entry of searchIndex) {
            const title = entry.title || '';
            const content = entry.content || '';
            
            const titleMatch = title.toLowerCase().includes(normalizedQuery);
            const contentMatch = content.toLowerCase().includes(normalizedQuery);
            
            if (titleMatch || contentMatch) {
                let score = 0;
                if (titleMatch) score += 10;
                if (contentMatch) score += 1;
                if (title.toLowerCase() === normalizedQuery) score += 20;
                
                // Create snippet
                let snippet = '';
                if (contentMatch) {
                    const idx = content.toLowerCase().indexOf(normalizedQuery);
                    const start = Math.max(0, idx - 40);
                    const end = Math.min(content.length, idx + 80);
                    snippet = (start > 0 ? '...' : '') + 
                              content.substring(start, end) + 
                              (end < content.length ? '...' : '');
                } else {
                    snippet = content.substring(0, 100) + '...';
                }
                
                results.push({
                    title: entry.title,
                    url: entry.url,
                    snippet: snippet,
                    score: score
                });
            }
        }
        
        return results.sort((a, b) => b.score - a.score).slice(0, 10);
    }

    function setupSearch() {
        const searchInput = document.getElementById('search-input');
        if (!searchInput) return;
        
        // Create results container
        const resultsContainer = document.createElement('div');
        resultsContainer.className = 'search-results';
        searchInput.parentElement.appendChild(resultsContainer);
        
        let debounceTimer;
        
        // Load index on focus
        searchInput.addEventListener('focus', () => {
            loadSearchIndex();
        });
        
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(async () => {
                if (query.length < 2) {
                    resultsContainer.classList.remove('active');
                    return;
                }
                
                await loadSearchIndex();
                const results = search(query);
                
                if (results.length > 0) {
                    resultsContainer.innerHTML = results.map(result => `
                        <div class="search-result-item" onclick="window.location.href='${getBasePath()}${result.url}'">
                            <a href="${getBasePath()}${result.url}">
                                <div class="search-result-title">${result.title}</div>
                                <div class="search-result-preview">${result.snippet}</div>
                            </a>
                        </div>
                    `).join('');
                } else {
                    resultsContainer.innerHTML = `<div class="search-no-results">No results found for "${query}"</div>`;
                }
                
                resultsContainer.classList.add('active');
            }, 300);
        });
        
        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
                resultsContainer.classList.remove('active');
            }
        });
    }

    // ==========================================================================
    // Initialization
    // ==========================================================================

    async function init() {
        console.log('Initializing book navigation...');

        // Load navigation and build sidebar
        const navLoaded = await loadNavigation();
        if (navLoaded) {
            buildSidebarNav();
            updateSidebarHeader();
        }

        // Build table of contents
        buildTableOfContents();

        // Load theorem manifest
        await loadManifest();

        // Attach tooltips
        attachTooltips();

        // Setup smooth scrolling
        setupSmoothScrolling();

        // Setup mobile menu
        setupMobileMenu();

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
