import { defineConfig, devices } from '@playwright/test';

const base = `/${(process.env.SITE_BASE || '/algorithm-solutions/').split('/').filter(Boolean).join('/')}/`;
const origin = 'http://127.0.0.1:4321';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI ? 'line' : 'list',
  use: { baseURL: origin, trace: 'retain-on-failure', screenshot: 'only-on-failure' },
  webServer: {
    command: 'npm run preview -- --port 4321',
    env: { SITE_BASE: base, ASTRO_PREVIEW_BACKGROUND: '1' },
    url: `${origin}${base}`,
    reuseExistingServer: false,
    timeout: 120_000,
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'], viewport: { width: 1280, height: 900 } } },
    { name: 'mobile-chromium', use: { ...devices['Pixel 5'], viewport: { width: 390, height: 844 } } },
  ],
});
