---
title: "수업 운영 문서·스킬 전수 점검"
updated: "2026-10-23"
tags: ["documentation", "audit", "teaching"]
---

# 수업 운영 문서·스킬 전수 점검

2026-10-23 기준 추적 문서 78개를 점검했다. 점검 당시 기존 파일 18개를 확정 수정, 기록 스킬 2개를 행동 확인 후 결정, 58개를 유지 대상으로 분류했다. 현행 학습 스킬의 기본 흐름은 개선 설계와 맞는다. 점검에서 찾은 문제는 주변 안내의 의무 진단 문장, 오래된 현재형 표현, 과거 명세와 현행 운영의 경계, 잘못된 링크와 불명확한 반례 설명이다.

**상태: 승인된 계획의 네 작업 로컬 반영·검증 완료, 전체 변경 검토 완료.** 기준 커밋은 `bafcd820936b98135e63656e2889e15dfa85a7d8`이다. [구현 계획](superpowers/plans/2026-10-23-documentation-consistency.md)에 따라 기존 문서 18개를 수정하고 60개를 유지했다. 새 보고서·계획 2개를 더했으며 학습 중단 상태·사용자 코드·CPH·과거 본문을 보존했다. 아래 발견·제안은 점검 당시 기록이고 최종 적용 내용은 [반영 결과](#반영-결과)에 구분한다. 커밋·push·Pages 갱신은 수행하지 않았다.

## 범위와 판단 기준

대상은 Git 추적 Markdown 74개와 현행 스킬 UI YAML 4개다. 현행 스킬 4개와 퇴역 스킬 10개, 사용 안내·설계·과거 명세·복기·개념 노트·템플릿을 모두 포함한다. 다른 문서 확장자(`mdx`, `rst`, `txt`, `adoc`)의 추적 문서는 없었다. Git 제외 사용자 파일, 로컬 실행 이력, 복구본, 의존성·빌드 산출물과 저장소 밖 설정은 변경 대상이 아니다.

전문을 읽고, 같은 대화에서 이미 읽은 20개는 바이트 해시가 그대로임을 확인해 재사용했다. 나머지 58개는 이번 점검에서 읽었다. 파일별 역할과 조치는 [전수 목록](#전수-목록)에 남긴다. 관련 코드·설정·검사기는 문서의 설명과 명령을 대조하는 근거로 확인했으며, 문서 78개 집계에는 포함하지 않는다.

채택된 기준은 [수업 개선 설계](TEACHING_DESIGN.md)다. 새 기법의 필요한 설명, 충분한 독립 설계·구현·실행, 최신 코드·출력에 대한 리뷰, 기존 증거 재사용, 요청형 모범 코드와 다음 이동, 학습자 소유권을 유지한다. 독립 해결·숙달·학습 효과는 파일 존재나 로컬 통과만으로 인정하지 않는다. 복습·혼합·대회는 기존 주 5–7시간 안에서 다른 활동을 대체한다.

## 기준 위치

| 정보 | 기준 문서 | 다른 문서의 역할 |
| --- | --- | --- |
| 작업·파일 보존, 검증, 저장·게시 범위 | [AGENTS](../AGENTS.md) | 모든 작업에 필요한 경계를 짧게 유지한다. |
| 회차 진행·힌트·WA 리뷰·이동·대회 중 도움 경계 | [study-algorithms](../.agents/skills/study-algorithms/SKILL.md) | 안내서는 진입 방법과 링크만 설명한다. |
| 목표·선수·주제 순서·주간 예산 | [ROADMAP](../ROADMAP.md) | 별도 진도표나 의무 과제를 추가하지 않는다. |
| 중단 상태·현재 근거·재개 선택 | [STATE](../STATE.md) | 오래된 다음 행동으로 최신 재개 위치를 덮어쓰지 않는다. |
| 기록 작성·도움·판정의 근거 | [개념 기록](../.agents/skills/record-algorithm-knowledge/SKILL.md), [문제 복기](../.agents/skills/review-algorithm-problem/SKILL.md), [대회 복기](../.agents/skills/review-algorithm-contest/SKILL.md) | 요청받은 기록과 실제로 확인한 사실만 저장한다. |
| 환경 사용·웹·과거 검증 | [USAGE](USAGE.md), [WEB](WEB.md), [VALIDATION](VALIDATION.md) | 현재 사용법과 날짜가 있는 과거 결과를 구분한다. |
| 채택 근거와 지난 설계·실행 | [TEACHING_DESIGN](TEACHING_DESIGN.md), [이전 구현 결과](TEACHING_IMPLEMENTATION_PLAN.md#실행-결과), [과거 명세](../specs/001-redesign-learning-system/spec.md) | 과거 상태·승인·검증을 보존하되 현행 지시로 취급하지 않는다. |

## 확인한 수정 사항

위치는 기준 커밋의 줄 번호다. `높음`은 수업 행동이 달라질 수 있는 충돌, `보통`은 사용·해석 오류, `낮음`은 중복·표현 정리다.

| ID | 우선순위·위치 | 확인한 문제 | 최소 수정과 완료 기준 |
| --- | --- | --- | --- |
| F01 | 낮음 · `AGENTS.md:41–44`, `:35` | 시작 절과 스킬에 있는 회차 설명을 다시 싣고, 예전 생성기 전용 검사까지 루트에 둔다. | 반복 설명은 스킬 링크로 줄이고 호환 도구의 집중 검사만 USAGE의 기존 호환 절로 옮긴다. 학습자 소유권·파일 보존·기록·게시 경계와 기본 검사 명령은 유지한다. |
| F02 | 높음 · `docs/USAGE.md:194–198` | 익숙한 주제는 대표 통합 문제를 먼저 풀게 한다. 충분한 현재 증거를 재사용한다는 조건이 빠졌다. 혼합 연습의 태그 비공개도 원문 제목까지 바꾸는 뜻으로 읽힐 수 있다. | 현재 코드·설명·실행을 먼저 활용하고 부족할 때만 확인 과제를 고른다. 혼합 연습에서는 강사가 추가하는 기법 힌트만 감추며 원문을 보존한다. |
| F03 | 보통 · `cses/README.md:4` | 설정·사용법만 준비됐다는 저장소 전체 상태 설명이 실제 풀이·Array Division 복기와 맞지 않는다. | README가 환경 사용 안내임을 설명하고 표는 파일명 예시로 둔다. 예시·파일 존재를 AC나 진도로 바꾸지 않는다. |
| F04 | 보통 · `docs/VALIDATION.md:69–75`, `docs/USAGE.md:86`, `README.md:76` | 예전 플랫폼 워크스페이스의 미완료 첫 사용 절차와 당시 클라우드 상태가 현재 안내처럼 남아 있다. | VALIDATION의 9월 20일·10월 2일 결과와 수치는 보존한다. 옛 첫 사용 절차는 당시 미확인으로 표시하고 현재 단일 루트 흐름에 연결한다. USAGE의 장치 상태도 당시 확인 범위로 한정하고 README 링크 설명을 맞춘다. |
| F05 | 보통 · `docs/LEARNING_REVIEW.md:15`, 다음 행동 표 | ABC277E 재현 우선 제안이 문서 전체에서는 현행 필수 과제로 읽힐 수 있다. 뒤쪽 한 절에만 당시 제안이라는 표시가 있다. | 서두에서 개선 전 검토임을 밝히고 현재 재개는 STATE, 운영은 학습 스킬로 연결한다. 과거 결과·제안·도움 구분은 보존한다. |
| F06 | 낮음 · `knowledge/README.md:15` | LeetCode 3개를 현재 연결 문제 노트처럼 소개하지만 다른 플랫폼 문제 복기도 14개 있다. | 작성·연결 예시임을 표시한다. 최신 진도 목록을 또 만들지 않고 STATE를 참조한다. |
| F07 | 보통 · `specs/001-redesign-learning-system/`의 10개 문서 | 일부 서두에는 당시 기록임이 있지만 계약·quickstart를 직접 열면 옛 SCC 재개 과제·Spec Kit 단계·승인 제한이 현재 지시처럼 보인다. | 각 문서 첫 제목 뒤에 짧은 과거 자료 안내와 STATE·학습 스킬·채택 설계 링크를 둔다. 본문·FR·당시 승인·체크박스·검증 수치는 바꾸지 않는다. |
| F08 | 보통 · `specs/001-redesign-learning-system/research.md:8` | 삭제된 현행 위치의 `speckit-plan/SKILL.md` 링크가 깨져 있다. | 보관된 `.specify/retired/.agents/skills/speckit-plan/SKILL.md`로 연결하고 당시 계획 스킬의 퇴역본임을 표시한다. 실행하지 않는다. |
| F09 | 보통 · `atcoder/abc325d.md:37` | 전체 끝점순 처리 결과를 `3`이라고 쓰지만 그 처리의 시간 갱신 규칙이 없다. | 기대값 `4`와 유효 시간표는 유지하고 정의되지 않은 실패 개수만 뺀다. 과거 사용자 코드 버전을 새로 추정하지 않는다. |

F09의 모호성은 합성한 두 처리 방식에서도 드러난다. 같은 네 상품을 끝점순으로 읽되 `time <= start`일 때만 선택하고 `time = end + 1`로 옮기면 1개, `time <= end`일 때 선택하고 `time = max(time, start) + 1`로 옮기면 3개다. 실행으로 두 값을 확인했고 작은 완전탐색의 최적값은 4였다. 어느 방식이 당시 사용자 코드였는지는 이 문장만으로 확정할 수 없으므로 숫자 하나를 다른 숫자로 교체하지 않는다.

## 행동 확인 후 결정할 스킬 문구

아래는 정적 문구의 위험이며 관찰된 응답 실패로 확정하지 않는다. 새 행동 규칙은 실제 비교에서 필요한 경우에만 추가한다. 현행 규칙으로 적절히 대응하면 그대로 유지한다.

| ID | 대상·근거 | 비교할 입력과 기대 행동 | 수정 조건 |
| --- | --- | --- | --- |
| R01 | `record-algorithm-knowledge/SKILL.md:9–10`은 과거 세션·Git 이력에서 경험 복원을 일괄 배제한다. | 사용자가 특정 커밋의 확인된 기록을 근거로 정리해 달라면 그 자료·날짜를 확인해 활용한다. 코드 존재만으로 독립 해결·AC·숙달을 추정하지 않는다. | 명시적 요청과 검증 가능한 근거까지 거부하는 실패가 재현될 때만 조회 금지를 근거·추정 구분으로 좁힌다. |
| R02 | `review-algorithm-problem/SKILL.md:9`의 중단 경계는 실전 대회만 명시한다. 학습·대회 스킬은 측정용 virtual도 포함한다. | 시간이 남은 측정용 virtual에서 복기라는 이름으로 WA 원인·수정 코드를 요구해도 종료 전 풀이 도움을 주지 않는다. 환경 준비·기록 위치 같은 중립적 지원은 가능하다. | 현행 스킬이 종료 전 해법을 제공하는 실패가 재현될 때만 측정용 virtual 경계를 맞춘다. |

실행 단계에서는 `writing-skills`에 따라 격리된 응답 비교를 한다. 무지침 통제·현행 지침으로 원인을 확인하고, 필요한 후보만 비교한다. 각 표현 조건의 반복 응답과 예외를 직접 읽는다. 합성 상황은 학습 이력으로 저장하지 않는다. 기존 수업 개선 때의 응답 표본을 이 두 위험의 새 검증 결과로 재사용하지 않는다.

## 유지할 내용과 삭제하지 않을 자료

- 현행 `study-algorithms`, 대회 복기 스킬과 UI 4개는 역할·진입 요청·도움 경계가 채택 설계와 맞는다. 문구를 바꾸기 위한 전면 개고는 하지 않는다.
- 세 기록 템플릿은 이미 선택 항목과 미확인 값을 허용한다. 새 필수 추적 필드·정답 재시험·진도 DB를 추가하지 않는다.
- ROADMAP의 목표·주제 관계·시간 예산, STATE의 중단과 재개 선택은 유지한다. 이번 문서 정리를 새 학습 회차로 기록하지 않는다.
- 개념 노트 7개와 나머지 문제 복기는 확인한 설명·도움·실행 범위가 구분돼 있다. 과거 AC·미확인을 새 결과로 덮어쓰지 않는다.
- `CLAUDE.md`는 `@AGENTS.md` 한 줄의 연결 파일이다. 중복 지침 본문이 없으므로 유지한다. Claude 계열 클라이언트에서 실제로 불러오는지는 이번 점검으로 확인하지 않았다.
- `.specify/README.md`는 실행기 종료와 원래 경로 기준의 보관 원칙을 이미 설명한다. 퇴역 스킬 10개·템플릿 5개와 미비준 헌법은 보존한다. 옛 훅·설정·명령을 실행하거나 템플릿을 현행 규칙으로 채우지 않는다.
- 외부 자료의 연구 한계와 날짜가 있는 계정 수치를 보존한다. 최신 rating·개인 학습 효과를 새로 조사하거나 추정한 작업이 아니다.

## AGENTS 점검

`agents-md`의 빠른 점검 기준으로 **10/12**다. 7번 중복 최소화와 10번 필요한 경우에만 불러올 세부 정보 배치가 개선 대상이다. 기본 실행·검증·설정, 저장소 고유 주의점과 대안, 구현 선택을 바꾸는 계약, 유효한 로컬 참조, 보존 경계는 갖춰져 있다. 명령·설정은 실제 소스와 대조했고 아래 Python 검사는 실행했다. 웹 명령은 `web/package.json`과 대조했으며 이번 점검에서 웹 전체 검사를 새로 실행하지 않았다.

95줄이라는 길이 자체를 결함으로 보지 않는다. 짧게 만들기 위해 사용자 파일 보호, LeetCode API 보존, Git·Pages 경계, 라우터의 덮어쓰기 방지 규칙을 제거하지 않는다. `CLAUDE.md` 연결 방식도 실제 로더 확인 없이 교체하지 않는다.

## 점검 당시 확인 결과와 한계

| 검사 | 이번 점검의 결과 | 해석의 범위 |
| --- | --- | --- |
| 전체 문서 읽기·해시 대조 | 78/78, 기존 대상의 내용 변경 0개 | 새 보고서·계획 작성 전 기준 스냅샷을 유지했다. |
| Markdown 로컬 링크·제목 조각 점검 | 로컬 참조 332개 중 누락 파일 1개(F08) | 코드 예시의 경로 문자열은 실제 Markdown 링크와 구분했다. 외부 URL 151개는 개수만 확인했고 접속 상태를 검사하지 않았다. |
| 현행·퇴역 스킬 frontmatter | 14개 이름·설명 구조 확인 | 스킬 행동이 적절하다는 실증 검사는 아니다. |
| UI YAML | 4개 구조·스킬 호출명 확인 | 실제 클라이언트 로딩·선택 성공은 별도다. |
| 개념 예제 | 7개 문서의 완전한 Python 블록 9개 실행 성공 | 정렬 키의 문맥 의존 한 줄은 독립 실행 대상으로 삼지 않았다. 세그먼트 트리 두 블록은 함께 실행해 조회·수정도 확인했다. 학습자 숙달 증거로 쓰지 않는다. |
| `uv run --frozen python -m unittest discover -s tests -v` | 49개 통과 | 저장소 도구·반복 구현의 기존 회귀 검사다. |
| `uv run --frozen python scripts/validate_notes.py` | 실제 노트 24개 통과 | 기본 탐색은 README·템플릿·docs·스킬을 검사하지 않는다. 전체 문서 점검을 대신하지 않는다. |
| `uv lock --check` | 성공 | 의존성 변경은 없다. |

로컬 링크 점검에는 Markdown 구문 해석과 대상 파일·제목 대조를 사용했다. GitHub/웹에서 생성하는 모든 anchor의 런타임 호환, 외부 링크의 최신 내용, VS Code·CPH·온라인 제출·Pages의 현재 상태를 모두 검증했다는 뜻은 아니다. 이 전수 점검 단계에서는 새 스킬 응답 실험과 실제 수업 효과 관찰을 하지 않았다. 이후 실행 단계의 응답 비교는 아래 반영 결과에 구분하며 실제 수업 효과는 계속 미관찰이다.

문서만 고치는 범위이므로 새 검사기·CI·형식 규약을 만들지 않는다. 아래 명령으로 기존 링크 검사 함수를 전체 추적 Markdown에 다시 적용할 수 있으며, 제목 조각은 별도 대조한다. 앞선 전수 점검의 제목 조각 확인 범위를 파일 존재 검사로 축소해 완료를 보고하지 않는다.

```bash
uv run --frozen python - <<'PY'
from pathlib import Path
import subprocess
from scripts.validate_notes import MARKDOWN, split_frontmatter, validate_links

root = Path.cwd().resolve()
tracked = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"]).decode().split("\0")
paths = set(filter(None, tracked)) | {
    "docs/DOCUMENTATION_AUDIT.md",
    "docs/superpowers/plans/2026-10-23-documentation-consistency.md",
}
errors = []
count = 0
for name in sorted(paths):
    if name.startswith(".specify/retired/"):
        continue  # 보관본 내부 경로는 원래 위치 기준이다.
    path = root / name
    text = path.read_text(encoding="utf-8")
    body, start = text, 1
    if text.startswith("---\n"):
        _, body, closing, front_errors = split_frontmatter(path, text)
        errors.extend(front_errors)
        start = closing + 1
    env = {}
    tokens = MARKDOWN.parse(body, env)
    errors.extend(validate_links(path, root, tokens, env.get("references", {}), start))
    count += 1
print("\n".join(errors) if errors else f"OK: local file links in {count} Markdown files")
raise SystemExit(bool(errors))
PY
```

기준 스냅샷에서 위 파일 존재 검사는 F08을 보고하며, 수정 후에는 성공해야 한다. 새 보고서·계획은 명시 목록에 포함해 추적 전에도 검사한다. 구현 시 구체적인 순서와 기대 결과는 후속 계획에 둔다.

작성한 보고서와 계획을 포함한 80개 파일도 다시 대조했다. 로컬 참조 433개의 파일·제목 조각에서 기존 F08 외 새 오류는 없었다. 보고서의 명시 경로 메타데이터 검사는 통과했고 전수 목록 78행은 기준 목록과 일치했다. 수정 18개·조건부 2개·유지 58개 집계와 기존 대상 내용 변경 0개도 재확인했다.

## 전수 목록

다음은 기준 스냅샷에서 내린 판정이다. 조건부 2개를 유지한 실행 결과는 아래에 별도로 둔다. `수정`은 확정된 문서 정리, `조건부`는 응답 비교 후 필요할 때만 바꿀 스킬, `유지`는 보존한다는 판단이다. 행 번호는 점검 누락을 확인하기 위한 목록이며 새 진도 체계가 아니다.

| 번호 | 파일 | 판정·근거 |
| --- | --- | --- |
| 01 | [record-algorithm-knowledge/SKILL.md](../.agents/skills/record-algorithm-knowledge/SKILL.md) | 조건부 R01 · 명시적 과거 근거 조회와 추정 금지 구분 |
| 02 | [record-algorithm-knowledge/openai.yaml](../.agents/skills/record-algorithm-knowledge/agents/openai.yaml) | 유지 · 요청형 기록 진입 |
| 03 | [review-algorithm-contest/SKILL.md](../.agents/skills/review-algorithm-contest/SKILL.md) | 유지 · 종료 후 복기·측정 구분 |
| 04 | [review-algorithm-contest/openai.yaml](../.agents/skills/review-algorithm-contest/agents/openai.yaml) | 유지 · 대회 복기 호출 |
| 05 | [review-algorithm-problem/SKILL.md](../.agents/skills/review-algorithm-problem/SKILL.md) | 조건부 R02 · 측정용 virtual 경계 |
| 06 | [review-algorithm-problem/openai.yaml](../.agents/skills/review-algorithm-problem/agents/openai.yaml) | 유지 · 요청형 문제 복기 |
| 07 | [study-algorithms/SKILL.md](../.agents/skills/study-algorithms/SKILL.md) | 유지 · 개선된 회차 운영 기준 |
| 08 | [study-algorithms/openai.yaml](../.agents/skills/study-algorithms/agents/openai.yaml) | 유지 · 현재 위치 기반 학습 호출 |
| 09 | [.specify/README.md](../.specify/README.md) | 유지 · 퇴역 범위와 보관 원칙 명시 |
| 10 | [.specify/memory/constitution.md](../.specify/memory/constitution.md) | 유지 · 미비준 자리표시자를 채택 정책으로 만들지 않음 |
| 11 | [퇴역 speckit-analyze](../.specify/retired/.agents/skills/speckit-analyze/SKILL.md) | 유지 · 당시 교차 검토·승인 절차 |
| 12 | [퇴역 speckit-checklist](../.specify/retired/.agents/skills/speckit-checklist/SKILL.md) | 유지 · 당시 요구사항 검토 양식 |
| 13 | [퇴역 speckit-clarify](../.specify/retired/.agents/skills/speckit-clarify/SKILL.md) | 유지 · 당시 명세 질의 절차 |
| 14 | [퇴역 speckit-constitution](../.specify/retired/.agents/skills/speckit-constitution/SKILL.md) | 유지 · 당시 헌법 생성 절차, 실행하지 않음 |
| 15 | [퇴역 speckit-converge](../.specify/retired/.agents/skills/speckit-converge/SKILL.md) | 유지 · 당시 감사·수렴 절차 |
| 16 | [퇴역 speckit-implement](../.specify/retired/.agents/skills/speckit-implement/SKILL.md) | 유지 · 당시 구현·승인 게이트 |
| 17 | [퇴역 speckit-plan](../.specify/retired/.agents/skills/speckit-plan/SKILL.md) | 유지 · F08에서 연결할 역사적 근거 |
| 18 | [퇴역 speckit-specify](../.specify/retired/.agents/skills/speckit-specify/SKILL.md) | 유지 · 당시 명세 생성·승인 절차 |
| 19 | [퇴역 speckit-tasks](../.specify/retired/.agents/skills/speckit-tasks/SKILL.md) | 유지 · 당시 작업 분해 절차 |
| 20 | [퇴역 speckit-taskstoissues](../.specify/retired/.agents/skills/speckit-taskstoissues/SKILL.md) | 유지 · 당시 외부 이슈 생성 절차, 실행하지 않음 |
| 21 | [퇴역 checklist-template](../.specify/retired/.specify/templates/checklist-template.md) | 유지 · 과거 템플릿 원문 |
| 22 | [퇴역 constitution-template](../.specify/retired/.specify/templates/constitution-template.md) | 유지 · 과거 템플릿 원문 |
| 23 | [퇴역 plan-template](../.specify/retired/.specify/templates/plan-template.md) | 유지 · 과거 템플릿 원문 |
| 24 | [퇴역 spec-template](../.specify/retired/.specify/templates/spec-template.md) | 유지 · 과거 템플릿 원문 |
| 25 | [퇴역 tasks-template](../.specify/retired/.specify/templates/tasks-template.md) | 유지 · 과거 템플릿 원문 |
| 26 | [AGENTS.md](../AGENTS.md) | 수정 F01 · 중복과 호환 도구 전용 검사 배치 |
| 27 | [CLAUDE.md](../CLAUDE.md) | 유지 · 단일 연결, 실제 로더 동작 미검증 |
| 28 | [README.md](../README.md) | 수정 F04 · 과거 검증 링크 설명 |
| 29 | [ROADMAP.md](../ROADMAP.md) | 유지 · 목표·선수·예산·선택 기준 정합 |
| 30 | [STATE.md](../STATE.md) | 유지 · 학습 중단과 재개 선택 보존 |
| 31 | [abc192e.md](../atcoder/abc192e.md) | 유지 · 대기 간선·로컬 결과와 AC 구분 |
| 32 | [abc212d.md](../atcoder/abc212d.md) | 유지 · 보정 불변식과 핵심 도움 구분 |
| 33 | [abc214e.md](../atcoder/abc214e.md) | 유지 · 모범 코드 도움과 독립 근거 구분 |
| 34 | [abc221d.md](../atcoder/abc221d.md) | 유지 · 스위핑 경계·확인 범위 |
| 35 | [abc229d.md](../atcoder/abc229d.md) | 유지 · 윈도 모델·사용자 AC와 로컬 실행 구분 |
| 36 | [abc233d.md](../atcoder/abc233d.md) | 유지 · prefix 빈도와 도움·AC 범위 |
| 37 | [abc246d.md](../atcoder/abc246d.md) | 유지 · 탐색 범위·실행과 독립 해결 구분 |
| 38 | [abc277e.md](../atcoder/abc277e.md) | 유지 · 재현은 선택지, 최신 STATE 연결 |
| 39 | [abc325d.md](../atcoder/abc325d.md) | 수정 F09 · 정의되지 않은 실패 개수 |
| 40 | [abc340d.md](../atcoder/abc340d.md) | 유지 · Dijkstra 리뷰·확인 범위 |
| 41 | [abc395e.md](../atcoder/abc395e.md) | 유지 · 상태 그래프 교정·확인 범위 |
| 42 | [dpf.md](../atcoder/dpf.md) | 유지 · LCS 모범 코드·역추적 도움 구분 |
| 43 | [typical90a.md](../atcoder/typical90a.md) | 유지 · 경계 갱신·사용자 AC 근거 |
| 44 | [contests/README.md](../contests/README.md) | 유지 · 실제 참가·종료 후 요청 범위 |
| 45 | [contests/template.md](../contests/template.md) | 유지 · 선택 항목·미확인·측정 구분 |
| 46 | [Array_Division.md](../cses/Array_Division.md) | 유지 · greedy 조건·이분 탐색·근거 구분 |
| 47 | [cses/README.md](../cses/README.md) | 수정 F03 · 저장소 전체 상태의 부정확한 소개 |
| 48 | [LEARNING_REVIEW.md](LEARNING_REVIEW.md) | 수정 F05 · 개선 전 제안의 시점 표시 |
| 49 | [REFERENCES.md](REFERENCES.md) | 유지 · 자료의 역할·연구 한계·조회 시점 |
| 50 | [TEACHING_DESIGN.md](TEACHING_DESIGN.md) | 유지 · 채택 설계, 효과 미관찰 구분 |
| 51 | [TEACHING_IMPLEMENTATION_PLAN.md](TEACHING_IMPLEMENTATION_PLAN.md) | 유지 · 지난 구현 완료와 범위 기록 |
| 52 | [USAGE.md](USAGE.md) | 수정 F01·F02·F04 · 진단 조건·호환 절·당시 확인 |
| 53 | [VALIDATION.md](VALIDATION.md) | 수정 F04 · 과거 미확인 절차와 현행 진입 분리 |
| 54 | [WEB.md](WEB.md) | 유지 · package 명령·하위 경로·공개 범위 정합 |
| 55 | [knowledge/README.md](../knowledge/README.md) | 수정 F06 · 현재 목록을 작성 예시로 변경 |
| 56 | [prefix-aggregates.md](../knowledge/basics/prefix-aggregates.md) | 유지 · 경계·예제 실행 확인 |
| 57 | [sort-keys.md](../knowledge/basics/sort-keys.md) | 유지 · 정렬 키·도움·경험 시점 구분 |
| 58 | [two-pointers.md](../knowledge/basics/two-pointers.md) | 유지 · 음수 조건·예제 실행 확인 |
| 59 | [segment-tree.md](../knowledge/data-structures/segment-tree.md) | 유지 · 실제 경험·모범 코드·별도 실행 구분 |
| 60 | [bfs.md](../knowledge/graphs/bfs.md) | 유지 · 큐 레벨 경계·예제 실행 확인 |
| 61 | [dfs.md](../knowledge/graphs/dfs.md) | 유지 · 재귀 흐름·스택 범위·예제 실행 확인 |
| 62 | [binary-search.md](../knowledge/search/binary-search.md) | 유지 · 단조성·mid 갱신·예제 실행 확인 |
| 63 | [knowledge/template.md](../knowledge/template.md) | 유지 · 참고 예제와 실제 경험 분리 |
| 64 | [1422 복기](../leetcode/easy/1422.maximum-score-after-splitting-a-string.md) | 유지 · 저장 코드·추가 메모리 설명 대조 |
| 65 | [1302 복기](../leetcode/medium/1302.deepest-leaves-sum.md) | 유지 · 저장 코드·BFS 레벨 처리 대조 |
| 66 | [2226 복기](../leetcode/medium/2226.maximum-candies-allocated-to-k-children.md) | 유지 · 저장 코드·상단 mid·복잡도 대조 |
| 67 | [과거 requirements](../specs/001-redesign-learning-system/checklists/requirements.md) | 수정 F07 · 표시 의미·체크 상태는 보존 |
| 68 | [과거 document-records](../specs/001-redesign-learning-system/contracts/document-records.md) | 수정 F07 · 계약 본문은 보존 |
| 69 | [과거 learning-session](../specs/001-redesign-learning-system/contracts/learning-session.md) | 수정 F07 · 옛 재개 과제·계약 본문은 보존 |
| 70 | [과거 data-model](../specs/001-redesign-learning-system/data-model.md) | 수정 F07 · 개념 모델 본문은 보존 |
| 71 | [과거 plan](../specs/001-redesign-learning-system/plan.md) | 수정 F07 · 당시 승인·완료 기록은 보존 |
| 72 | [과거 quickstart](../specs/001-redesign-learning-system/quickstart.md) | 수정 F07 · 당시 절차·결과는 보존 |
| 73 | [과거 research-evidence](../specs/001-redesign-learning-system/research-evidence.md) | 수정 F07 · 당시 조회 근거는 보존 |
| 74 | [과거 research](../specs/001-redesign-learning-system/research.md) | 수정 F07·F08 · 퇴역 자료 안내와 깨진 참조 |
| 75 | [과거 spec](../specs/001-redesign-learning-system/spec.md) | 수정 F07 · FR·시나리오·당시 승인 보존 |
| 76 | [과거 tasks](../specs/001-redesign-learning-system/tasks.md) | 수정 F07 · 과거 작업·체크 상태 보존 |
| 77 | [problem-note 템플릿](../templates/problem-note.md) | 유지 · 선택 항목·미확인·근거 분리 |
| 78 | [web/README.md](../web/README.md) | 유지 · 상세 WEB 안내로 연결 |

## 반영 결과

2026-10-23 사용자의 “모두 구현하자” 요청 범위에서 반영했다. 기존 78개 중 문서 18개를 수정하고 스킬 2개를 포함한 60개를 유지했다. 보고서·계획 2개를 추가했다.

| 항목 | 실제 반영·판단 | 확인 근거 |
| --- | --- | --- |
| F01 | AGENTS의 회차 중복 설명을 줄이고 호환 생성기 집중 검사를 USAGE로 이동 | 기본 검사·소유권·저장·게시·파일 보존 경계를 유지했다. 정적 빠른 점검은 10/12에서 11/12, 95줄에서 94줄이다. 7번의 일부 중첩은 보수적으로 미충족으로 두었다. 이 점수는 실제 수업 행동 개선이나 Claude 로딩 검증이 아니다. |
| F02 | 충분한 현재 증거를 먼저 쓰고 부족할 때만 대표 과제로 확인 | 새 기법 설명·충분한 직접 구현을 유지하고 혼합 연습에서도 원문을 보존한다. RF1·RF5는 안내 의미로 대조했다. |
| F03·F06 | CSES 소개는 환경 안내, 개념 노트 연결 목록은 작성 예시로 정리 | 파일 존재·표·예시를 AC나 현재 진도 목록으로 확대하지 않았다. |
| F04·F05 | 예전 워크스페이스 절차·클라우드 확인·개선 전 다음 행동에 시점 표시 | 과거 날짜·표·결과는 보존하고 현재 단일 루트 사용법·STATE·학습 스킬로 연결했다. |
| F07·F08 | 과거 명세 10개에 시점·현행 기준 링크를 붙이고 퇴역 스킬 참조 복구 | 새 안내와 research의 한 링크를 제외한 원문이 바이트 단위로 같음을 확인했다. F08 파일 누락 실패(exit 1)를 확인한 뒤 링크 검사 성공(exit 0)을 확인했다. |
| F09 | Printing Machine 복기에서 정의되지 않은 과거 실패 개수만 제거 | 현재 코드의 반례 출력은 4다. 빌드된 페이지에도 기대값·인쇄 시간표가 남고 근거 없는 실패 개수는 없다. |
| R01·R02 | 두 기록 스킬 모두 유지 | K1·V1 각각 통제 5회·현행 5회, 총 20개 새 문맥의 실제 응답을 직접 읽었다. 과거 근거 조회 거부와 진행 중 측정용 virtual의 해법 제공은 통제·현행 모두 재현되지 않아 후보 문구를 작성하지 않았다. |

응답 비교는 두 위험만 확인했다. K1 현행 응답 1개는 설명받은 오름차순 키를 직접 작성한 경험처럼 귀속했고, 다른 1개는 `lambda(x):`의 괄호·콜론 위치를 부정확하게 서술했다. 따라서 20개 응답의 모든 사실이 정확했다고 보고하지 않는다. 원래 노트는 수정하지 않았으며 이 두 오류를 실제 사용자 경험으로 저장하지 않았다. 후보가 없으므로 K2·N1의 후보 비교와 후보 압박 시험은 수행하지 않았다. 원본 응답·수동 판독 결과는 Git 제외 로컬 증거에 남긴다.

| 실행 검증 | 실제 결과 |
| --- | --- |
| Python 기존 회귀 검사 | 격리 작업 위치의 기준 커밋에서 49개 통과. 소스·도구·의존성이 같으므로 문서 수정 뒤 중복 실행하지 않았다. |
| 노트 검사 | 기본 실제 노트 24개, 변경 문제 노트·보고서의 명시 검사 2개 통과 |
| 웹 | Astro 진단 오류·경고·힌트 0, Vitest 5개, 하위 경로 빌드·검색 색인 24페이지, 브라우저 검사 10개 통과 |
| 보존·문서 정합성 | 전체 로컬 파일·Markdown 제목 조각·메타데이터 검사와 허용 경로 대조. ROADMAP·STATE·원래 수업 설계·퇴역 자산·코드·설정·CPH·scratch는 보존한다. |

웹 검증은 Node 22.22.1과 임시 npm 10.9.2로 수행했다. 기존 시스템 npm 9.2.0은 명시된 최소 버전보다 낮아 사용하지 않았으며 전역 설정·lockfile은 바꾸지 않았다. 빈 contests 컬렉션 안내와 색상 환경변수 경고가 있었고, `npm ci`의 기존 잠금 의존성 감사 경고는 12개(낮음 5·보통 3·높음 4)였다. 이 문서 정리에서 의존성 업그레이드는 수행하지 않았다.

현재 결과는 로컬 변경·검증이다. 외부 URL 최신 내용·Claude 로더·사용자 PC의 CPH 연결·온라인 제출·실제 학습 효과·원격 CI·Pages 반영을 새로 확인한 결과로 해석하지 않는다.

별도 전체 변경 검토에서 Critical·Important·Minor 지적은 없었다. 동시 변경을 대조한 뒤 검토된 20개 파일을 공유 작업 폴더에 반영하고 저장된 내용을 다시 확인했다. Git 인덱스와 HEAD, 사용자 풀이·로컬 반례·중단 상태는 그대로이며 커밋·원격 반영은 수행하지 않았다. 검토에서 판단을 보류한 실제 학습 효과·일반 응답 정확성, 부수 오류의 회귀 여부, 미실행 조건부 시험, 외부 상태, 기존 감사 경고, 공유 반영 검증은 실행 담당자가 각각 범위·근거를 확인해 처리했다.
