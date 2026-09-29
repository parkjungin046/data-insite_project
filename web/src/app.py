"""
의사결정 대시보드 (Streamlit)
담당: C

실행 방법:
    pip install -r requirements.txt
    streamlit run web/src/app.py
"""

import streamlit as st

st.set_page_config(
    page_title="물순환 중심 토지이용계획 대시보드",
    page_icon="💧",
    layout="wide",
)

st.title("💧 물순환 중심 토지이용계획 의사결정 대시보드")
st.caption("복개하천 · 불투수면 · 열환경 분석을 기반으로 한 토지이용계획 지원 도구")

# ---------------------------------------------------------------------------
# TODO: B가 analysis/ 폴더에 분석 스크립트를 완성하면, 여기서 결과 데이터를 불러와
# 지도(예: st.map, pydeck, folium)와 차트(예: st.line_chart, plotly)로 시각화한다.
# 지금은 목업(더미) 데이터로 레이아웃만 먼저 잡아둔다.
# ---------------------------------------------------------------------------

col1, col2, col3 = st.columns(3)
col1.metric("불투수면 비율 (목업)", "47.7%")
col2.metric("침수 위험 저감률 (목업)", "-")
col3.metric("열 저감 효과 (목업)", "-")

st.divider()

tab_map, tab_analysis, tab_plan = st.tabs(["🗺️ 지도", "📊 분석 결과", "📋 계획안"])

with tab_map:
    st.info("지도 영역 — B의 GIS 분석 결과(복개하천 위치, 저지대, 옛 물길 등) 연동 예정")

with tab_analysis:
    st.info("분석 결과 영역 — 침수·열 저감 성능 분석 차트 연동 예정")

with tab_plan:
    st.info("계획안 영역 — A의 물순환 중심 토지이용계획도 연동 예정")
