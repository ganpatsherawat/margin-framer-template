import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://hoox-advisory.edgecompute.app',
  output: 'static',
  build: {
    format: 'directory'
  }
});
