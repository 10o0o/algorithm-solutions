# Algorithm Learning Lab web

루트의 공개 Markdown과 Python 풀이를 읽어 만드는 Astro 정적 사이트입니다. 생성물은 `web/dist/`에만 생기며 원본 학습 기록은 루트 디렉터리에 유지됩니다.

```bash
cd web
npm ci
npx playwright install --with-deps chromium
npm run check
npm test
SITE_BASE=/algorithm-solutions/ npm run build
SITE_BASE=/algorithm-solutions/ npm run test:e2e
```

기본 배포 주소는 `https://10o0o.github.io/algorithm-solutions/`입니다.
