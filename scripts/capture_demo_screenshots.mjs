// Capture README screenshots from the public prototype.
// Requires Playwright available in node resolution path.
import { chromium } from 'playwright';
const url = process.env.NEIJING_DEMO_URL || 'http://127.0.0.1:33399/neijing-atlas/';
const out = new URL('../docs/assets/', import.meta.url).pathname;
const browser = await chromium.launch({ headless: true, channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
await page.goto(url, { waitUntil: 'networkidle' });
await page.addStyleTag({ content: '.nav{display:none!important}.reveal{opacity:1!important;transform:none!important}' });
await page.screenshot({ path: `${out}/neijing-demo-hero.png`, fullPage: false });
for (const [id, name] of [['signals','signals'],['lenses','lenses'],['canon','canon-evidence'],['safety','safety'],['week','weekly-report']]) {
  await page.locator(`#${id}`).scrollIntoViewIfNeeded();
  await page.waitForTimeout(500);
  await page.screenshot({ path: `${out}/neijing-demo-${name}.png`, fullPage: false });
}
await browser.close();
