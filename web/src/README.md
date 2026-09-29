# web/src/

실제 웹사이트(의사결정 대시보드) 코드가 들어가는 폴더입니다. (담당: C)

**기술 스택: Streamlit (Python)**

## 로컬에서 실행하기

```bash
pip install -r requirements.txt
streamlit run web/src/app.py
```

브라우저가 자동으로 열리며 `http://localhost:8501`에서 확인할 수 있습니다.

## 배포

완성 후 [Streamlit Community Cloud](https://streamlit.io/cloud)에 GitHub 저장소를 연결하면 무료로 공개 URL을 받을 수 있습니다.

## 데이터 연동

- B의 `analysis/` 폴더 분석 결과(CSV, GeoJSON 등)를 불러와 지도·차트로 시각화
- A의 `outputs/` 폴더 최종 계획도를 계획안 탭에 표시
