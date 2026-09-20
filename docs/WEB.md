# 알고리즘 학습 웹

원본 개념·문제·대회 기록을 읽는 Astro 정적 사이트입니다. 공개 주소는
[Algorithm Learning Lab](https://10o0o.github.io/algorithm-solutions/)입니다.
화면 구성과 검색·다크 모드는 LLM lab의 웹을 바탕으로 이 저장소에 맞췄습니다.

## 로컬 실행

Node 22.12 이상과 npm 9.6.5 이상에서 실행합니다.

```bash
cd web
npm ci
npm run dev
```

문서를 수정하며 화면을 볼 때 개발 서버를 사용합니다. 본문 검색은 Pagefind 인덱스가
필요하므로 빌드 후 미리보기에서 확인합니다.

```bash
SITE_BASE=/algorithm-solutions/ npm run build
SITE_BASE=/algorithm-solutions/ npm run preview
```

기본 미리보기 주소는 `http://127.0.0.1:4321/algorithm-solutions/`입니다.
상세한 테스트 명령과 콘텐츠 처리는 [웹 README](../web/README.md)를 참고합니다.

## 콘텐츠 연결

개념은 `knowledge/`, 문제 설명은 플랫폼 코드 옆 Markdown, 대회 복기는 `contests/`에서
직접 읽습니다. 별도의 웹용 문서 복사본은 만들지 않습니다. 복기 문서가 있는 문제만
웹에 표시하고, 연결된 Python 코드는 원문 그대로 읽어 보여 줍니다. 나머지 코드는
[GitHub 저장소](https://github.com/10o0o/algorithm-solutions)에서 볼 수 있습니다.

문서의 상대 링크를 통해 관련 개념·문제·대회와 역방향 링크를 만듭니다.
파일 경로가 웹 주소를 결정하므로 제목을 바꿔도 주소는 유지됩니다.
메타데이터와 링크 규칙은 기존 [기록 작성법](USAGE.md)을 따릅니다.
공개 노트에서 raw HTML과 템플릿 안내 주석은 제거하고 Markdown·수식·코드 블록을 사용합니다.

검색은 제목과 노트 본문을 색인하며 문서 유형·분야·플랫폼·태그로 좁힐 수 있습니다.
긴 원본 풀이 코드는 검색 색인에서 제외합니다. 한국어 용어로 검색할 수 있지만
활용형·동의어가 자동으로 일치한다고 가정하지 않습니다.

## 검증과 배포

`main`에 push하거나 Actions의 `validate-and-deploy`를 수동 실행하면 Python 검사와
웹 빌드·브라우저 검사를 거쳐 GitHub Pages로 배포합니다. PR에서는 검사만 수행합니다.
수정한 Markdown과 코드를 커밋하면 동일한 파이프라인으로 사이트에 반영됩니다.

문서 작성 스킬은 파일 저장까지 수행합니다. 커밋·push는 별도로 명시해 요청합니다.
실패하면 Actions의 `check`, `frontend`, `deploy` 중 실패한 job을 확인합니다.
자동 검증을 통과하지 못한 새 빌드는 배포하지 않으며, 이전 배포가 유지됩니다.
초기 배포를 포함한 실제 확인 결과는 [검증 기록](VALIDATION.md)에 구분해 남깁니다.

## 구현 참고

- [Astro 콘텐츠 로더](https://docs.astro.build/en/reference/content-loader-reference/)
- [Pagefind 한국어 검색](https://pagefind.app/docs/multilingual/)
- [KaTeX](https://katex.org/docs/)
- [GitHub Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
