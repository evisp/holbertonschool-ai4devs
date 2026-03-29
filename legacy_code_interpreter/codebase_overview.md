# Codebase Overview - jQuery

## Age
First stable release in August 2006, latest stable 3.7.1 in August 2023. Active development on 4.0.0 as of 2026, dropping IE support.

## Size
Core source ~12,000 LOC across modular JS files in src/. Minified production build 80-90 KB.

## Dependencies
Runtime: standalone library, no external deps. Build/dev: Rollup 4.x, ESLint 8.x, QUnit 2.x, Webpack 5.x, RequireJS 2.3.x, jsdom 26.x.

## Issues
- 20-year codebase with legacy browser polyfills
- v4 migration breaks old IE compatibility  
- Complex build system for new contributors